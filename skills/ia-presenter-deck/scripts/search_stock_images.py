#!/usr/bin/env python3
"""Search Unsplash and Pexels for presentation-safe stock images.

Uses official APIs when keys are available:
- UNSPLASH_ACCESS_KEY
- PEXELS_API_KEY

Falls back to official website search URLs when keys are missing.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request


def fetch_json(url: str, headers: dict[str, str]) -> dict:
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def unsplash_search(query: str, count: int, orientation: str) -> list[dict]:
    key = os.environ.get("UNSPLASH_ACCESS_KEY")
    if not key:
        q = urllib.parse.quote(query)
        return [
            {
                "provider": "unsplash",
                "mode": "browser",
                "search_url": f"https://unsplash.com/s/photos/{q}",
                "note": "Set UNSPLASH_ACCESS_KEY to use the official API.",
            }
        ]

    params = urllib.parse.urlencode(
        {
            "query": query,
            "per_page": count,
            "orientation": orientation,
            "content_filter": "high",
        }
    )
    data = fetch_json(
        f"https://api.unsplash.com/search/photos?{params}",
        {
            "Authorization": f"Client-ID {key}",
            "Accept-Version": "v1",
            "User-Agent": "ia-presenter-know-how/stock-search",
        },
    )
    results = []
    for item in data.get("results", []):
        user = item.get("user") or {}
        urls = item.get("urls") or {}
        links = item.get("links") or {}
        results.append(
            {
                "provider": "unsplash",
                "mode": "api",
                "id": item.get("id"),
                "description": item.get("description")
                or item.get("alt_description")
                or "(no description)",
                "photographer": user.get("name"),
                "profile_url": (user.get("links") or {}).get("html"),
                "page_url": links.get("html"),
                "hotlink_url": urls.get("regular") or urls.get("full"),
                "thumb_url": urls.get("small") or urls.get("thumb"),
                "note": "Use API image URLs as hotlinks when displaying the exact source image.",
            }
        )
    return results


def pexels_search(query: str, count: int, orientation: str) -> list[dict]:
    key = os.environ.get("PEXELS_API_KEY")
    if not key:
        q = urllib.parse.quote(query)
        return [
            {
                "provider": "pexels",
                "mode": "browser",
                "search_url": f"https://www.pexels.com/search/{q}/",
                "note": "Set PEXELS_API_KEY to use the official API.",
            }
        ]

    params = urllib.parse.urlencode(
        {
            "query": query,
            "per_page": count,
            "orientation": orientation,
        }
    )
    data = fetch_json(
        f"https://api.pexels.com/v1/search?{params}",
        {
            "Authorization": key,
            "User-Agent": "ia-presenter-know-how/stock-search",
        },
    )
    results = []
    for item in data.get("photos", []):
        src = item.get("src") or {}
        results.append(
            {
                "provider": "pexels",
                "mode": "api",
                "id": item.get("id"),
                "description": item.get("alt") or "(no description)",
                "photographer": item.get("photographer"),
                "profile_url": item.get("photographer_url"),
                "page_url": item.get("url"),
                "hotlink_url": src.get("landscape") or src.get("large"),
                "thumb_url": src.get("medium") or src.get("small"),
                "note": "Link back to Pexels and credit the photographer when possible.",
            }
        )
    return results


def print_text(results: list[dict]) -> None:
    for item in results:
        print(f"[{item['provider']}]")
        if item["mode"] == "browser":
            print(f"search: {item['search_url']}")
            print(f"note:   {item['note']}")
            print()
            continue
        print(f"id:          {item.get('id')}")
        print(f"description: {item.get('description')}")
        print(f"author:      {item.get('photographer')}")
        if item.get("page_url"):
            print(f"page:        {item['page_url']}")
        if item.get("profile_url"):
            print(f"profile:     {item['profile_url']}")
        if item.get("hotlink_url"):
            print(f"image:       {item['hotlink_url']}")
        if item.get("thumb_url"):
            print(f"thumb:       {item['thumb_url']}")
        print(f"note:        {item['note']}")
        print()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument(
        "--provider",
        choices=("all", "unsplash", "pexels"),
        default="all",
        help="Image provider to search",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=5,
        help="Number of results per provider when APIs are available",
    )
    parser.add_argument(
        "--orientation",
        choices=("landscape", "portrait", "squarish"),
        default="landscape",
        help="Preferred orientation",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON",
    )
    args = parser.parse_args()

    results: list[dict] = []
    if args.provider in ("all", "unsplash"):
        results.extend(unsplash_search(args.query, args.count, args.orientation))
    if args.provider in ("all", "pexels"):
        pexels_orientation = "landscape" if args.orientation == "landscape" else (
            "portrait" if args.orientation == "portrait" else "landscape"
        )
        results.extend(pexels_search(args.query, args.count, pexels_orientation))

    if args.json:
        json.dump(results, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        print_text(results)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
