#!/usr/bin/env python3
"""
Extract readable text from an EPUB.

Features:
- reads normal text-based EPUBs via the spine
- optionally OCRs image-only EPUB pages when `--ocr-images` is set and `tesseract` is installed
- prints plain text to stdout

This is intentionally lightweight and stdlib-first so it can run in constrained environments.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET
from zipfile import ZipFile


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        text = " ".join(data.split())
        if text:
            self.parts.append(text)

    def text(self) -> str:
        return "\n".join(self.parts)


def find_opf(zf: ZipFile) -> str:
    names = set(zf.namelist())
    if "META-INF/container.xml" in names:
        container = ET.fromstring(zf.read("META-INF/container.xml"))
        ns = {"c": "urn:oasis:names:tc:opendocument:xmlns:container"}
        rootfile = container.find(".//c:rootfile", ns)
        if rootfile is not None:
            return rootfile.attrib["full-path"]
    for candidate in ("content.opf", "OPS/content.opf"):
        if candidate in names:
            return candidate
    raise SystemExit("Could not locate OPF in EPUB")


def spine_docs(zf: ZipFile, opf_path: str) -> list[str]:
    opf = ET.fromstring(zf.read(opf_path))
    ns = {"opf": "http://www.idpf.org/2007/opf"}
    manifest = {
        item.attrib["id"]: item.attrib["href"]
        for item in opf.findall(".//opf:item", ns)
        if "href" in item.attrib
    }
    spine = [
        item.attrib["idref"]
        for item in opf.findall(".//opf:spine/opf:itemref", ns)
        if "idref" in item.attrib
    ]
    base = Path(opf_path).parent
    docs = []
    for sid in spine:
        href = manifest.get(sid)
        if not href:
            continue
        docs.append(str(base / href) if str(base) != "." else href)
    return docs


def html_to_text(html: str) -> str:
    parser = TextExtractor()
    parser.feed(html)
    return parser.text()


def ocr_image_bytes(image_bytes: bytes, tesseract: str) -> str:
    with tempfile.TemporaryDirectory() as td:
        img = Path(td) / "page.jpg"
        out = Path(td) / "out"
        img.write_bytes(image_bytes)
        subprocess.run(
            [tesseract, img.name, out.name],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            cwd=td,
        )
        txt = out.with_suffix(".txt")
        return txt.read_text(encoding="utf-8", errors="ignore")


def extract_from_doc(zf: ZipFile, name: str, ocr_images: bool, tesseract: str | None) -> str:
    raw = zf.read(name).decode("utf-8", "ignore")
    text = html_to_text(raw)
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return text if len(text.strip()) > 40 else ""

    image_sources = []
    for elem in root.iter():
        if elem.tag.endswith("img") and "src" in elem.attrib:
            image_sources.append(elem.attrib["src"])

    boilerplate_markers = [
        "The Pyramid Principle: Logic in Writing and Thinking",
        "@page {padding:",
    ]
    boilerplate_hits = sum(marker in text for marker in boilerplate_markers)
    should_ocr = bool(image_sources) and (
        len(text.strip()) < 300 or boilerplate_hits > 0
    )

    if not should_ocr:
        return text if len(text.strip()) > 40 else ""

    if not ocr_images or not tesseract:
        return ""

    if not image_sources:
        return ""

    base = Path(name).parent
    chunks = []
    for src in image_sources:
        image_name = str(base / src) if str(base) != "." else src
        if image_name not in zf.namelist():
            continue
        try:
            chunks.append(ocr_image_bytes(zf.read(image_name), tesseract).strip())
        except subprocess.CalledProcessError:
            continue
    return "\n".join(c for c in chunks if c)


def iter_text(zf: ZipFile, docs: Iterable[str], ocr_images: bool) -> Iterable[str]:
    tesseract = shutil.which("tesseract") if ocr_images else None
    for doc in docs:
        if not doc.endswith((".html", ".htm", ".xhtml")):
            continue
        chunk = extract_from_doc(zf, doc, ocr_images, tesseract)
        cleaned = "\n".join(line.strip() for line in chunk.splitlines() if line.strip())
        if cleaned:
            yield cleaned


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract text from an EPUB")
    parser.add_argument("epub", help="Path to EPUB file")
    parser.add_argument(
        "--ocr-images",
        action="store_true",
        help="OCR image-only EPUB pages with tesseract",
    )
    args = parser.parse_args()

    epub_path = Path(args.epub)
    if not epub_path.is_file():
        raise SystemExit(f"Missing EPUB: {epub_path}")

    with ZipFile(epub_path) as zf:
        opf_path = find_opf(zf)
        docs = spine_docs(zf, opf_path)
        out = "\n\n".join(iter_text(zf, docs, args.ocr_images))
        sys.stdout.write(out)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
