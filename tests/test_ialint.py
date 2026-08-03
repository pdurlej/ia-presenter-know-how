"""Unit tests for tools/ialint.py.

The linter encodes rules that were established by live testing in iA Presenter,
and it is what CI uses to gate the corpus. That makes it load-bearing, so it
gets tests of its own. Standard library only: `python3 -m unittest discover tests`
"""
import importlib.util
import os
import sys
import tempfile
import unittest

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location("ialint", os.path.join(_ROOT, "tools", "ialint.py"))
ialint = importlib.util.module_from_spec(_spec)
sys.modules["ialint"] = ialint
_spec.loader.exec_module(ialint)

TAB = "\t"


def codes(md, bundled=None):
    return [f.code for f in ialint.lint_text(md, bundled=bundled)]


class TestRenderBreakingRules(unittest.TestCase):
    """Errors: the deck renders wrong in iA Presenter."""

    def test_tab_indented_table_is_an_error(self):
        md = f"## T\n\n{TAB}| a | b |\n{TAB}|---|---|\n{TAB}| 1 | 2 |\n"
        self.assertEqual(codes(md).count("E001"), 3)

    def test_flush_left_table_is_clean(self):
        md = "## T\n\n| a | b |\n|---|---|\n| 1 | 2 |\n"
        self.assertNotIn("E001", codes(md))

    def test_tab_indented_code_fence_is_an_error(self):
        md = f"## C\n\n{TAB}```python\n{TAB}x = 1\n{TAB}```\n"
        self.assertIn("E002", codes(md))

    def test_flush_left_code_fence_is_clean(self):
        md = "## C\n\n```python\nx = 1\n```\n"
        self.assertNotIn("E002", codes(md))

    def test_image_without_leading_slash_is_an_error(self):
        self.assertIn("E003", codes("![Alt](photo.png)\n"))
        self.assertIn("E003", codes("![Alt](assets/photo.png)\n"))

    def test_root_relative_image_is_accepted(self):
        self.assertNotIn("E003", codes("![Alt](/assets/photo.png)\n"))

    def test_remote_image_url_is_an_error(self):
        self.assertIn("E004", codes("![Alt](https://example.com/p.jpg)\n"))
        self.assertIn("E004", codes("![Alt](http://example.com/p.jpg)\n"))

    def test_unbundled_image_is_an_error_when_package_contents_known(self):
        md = "![Alt](/assets/missing.png)\n"
        self.assertIn("E005", codes(md, bundled={"/assets/other.png"}))
        self.assertNotIn("E005", codes(md, bundled={"/assets/missing.png"}))

    def test_bundled_check_skipped_for_bare_markdown_files(self):
        self.assertNotIn("E005", codes("![Alt](/assets/anything.png)\n", bundled=None))

    def test_content_block_bare_path_is_checked_too(self):
        self.assertIn("E003", codes('photo.png "A caption"\n'))
        self.assertNotIn("E003", codes('/assets/photo.png "A caption"\n'))


class TestQualityWarnings(unittest.TestCase):
    """Warnings: it renders, but the deck is weaker."""

    def test_empty_alt_text_warns(self):
        self.assertIn("W101", codes("![](/assets/p.png)\n"))
        self.assertNotIn("W101", codes("![Something](/assets/p.png)\n"))

    def test_tab_indented_image_warns(self):
        self.assertIn("W102", codes(f"{TAB}![Alt](/assets/p.png)\n"))

    def test_space_indentation_warns(self):
        self.assertIn("W103", codes("## T\n\n   slide text indented with spaces\n"))

    def test_thank_you_close_warns(self):
        self.assertIn("W104", codes("## Start\n\n---\n\n## Thank You\n"))
        self.assertNotIn("W104", codes("## Start\n\n---\n\n# Cancel one meeting this week.\n"))

    def test_generic_title_warns(self):
        self.assertIn("W105", codes("## Overview\n"))
        self.assertIn("W105", codes("## Agenda\n"))
        self.assertNotIn("W105", codes("## The queue is not the problem\n"))

    def test_bullet_overload_warns(self):
        md = "## L\n\n" + "".join(f"{TAB}- item {i}\n" for i in range(10))
        self.assertIn("W106", codes(md))
        few = "## L\n\n" + "".join(f"{TAB}- item {i}\n" for i in range(4))
        self.assertNotIn("W106", codes(few))


class TestFencedContentIsIgnored(unittest.TestCase):
    def test_examples_inside_a_fence_do_not_trigger_rules(self):
        md = f"# Doc\n\n```markdown\n{TAB}| a | b |\n{TAB}|---|---|\n```\n"
        self.assertNotIn("E001", codes(md))


class TestDisableDirectives(unittest.TestCase):
    def test_bare_file_directive_disables_everything(self):
        md = f"<!-- ialint-disable -->\n\n{TAB}| a | b |\n![](x.png)\n"
        self.assertEqual(codes(md), [])

    def test_scoped_file_directive_disables_only_named_codes(self):
        md = f"<!-- ialint-disable E001 -->\n\n{TAB}| a | b |\n\n![Alt](x.png)\n"
        found = codes(md)
        self.assertNotIn("E001", found)
        self.assertIn("E003", found)

    def test_next_line_directive_is_scoped_to_one_line(self):
        md = (
            "<!-- ialint-disable-next-line E003 -->\n"
            "![Alt](first.png)\n"
            "![Alt](second.png)\n"
        )
        self.assertEqual(codes(md).count("E003"), 1)


class TestPackageLinting(unittest.TestCase):
    def _pkg(self, tmp, text="# Deck\n", info='{"net.ia.presenter":{"template":"basel"}}'):
        d = os.path.join(tmp, "deck.iapresenter")
        os.makedirs(os.path.join(d, "assets"), exist_ok=True)
        with open(os.path.join(d, "text.md"), "w", encoding="utf-8") as f:
            f.write(text)
        if info is not None:
            with open(os.path.join(d, "info.json"), "w", encoding="utf-8") as f:
                f.write(info)
        return d

    def test_missing_text_md_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = os.path.join(tmp, "empty.iapresenter")
            os.makedirs(d)
            found, _ = ialint.lint_package(d)
            self.assertIn("E010", [f.code for f in found])

    def test_invalid_info_json_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = self._pkg(tmp, info="{not json")
            found, _ = ialint.lint_package(d)
            self.assertIn("E011", [f.code for f in found])

    def test_missing_theme_warns(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = self._pkg(tmp, info='{"net.ia.presenter":{}}')
            found, _ = ialint.lint_package(d)
            self.assertIn("W110", [f.code for f in found])

    def test_bundled_image_resolves_against_package_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = self._pkg(tmp, text="# Deck\n\n![Mood](/assets/bg.png)\n")
            open(os.path.join(d, "assets", "bg.png"), "wb").write(b"\x89PNG\r\n\x1a\n")
            found, _ = ialint.lint_package(d)
            self.assertNotIn("E005", [f.code for f in found])


if __name__ == "__main__":
    unittest.main()
