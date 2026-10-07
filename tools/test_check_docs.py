# Copyright AStarship <https://astarship.net>.
"""Exercise the documentation checker against isolated Markdown fixtures."""

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class TDocumentationTests(unittest.TestCase):
  def test_missing_relative_target_fails(self):
    with tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR")) as directory:
      root = Path(directory)
      (root / "README.md").write_text("[Missing](./Missing.md)\n", encoding="utf-8")
      result = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("check_docs.py")), str(root)],
        capture_output=True, text=True, check=False,
      )
      self.assertEqual(result.returncode, 1, result.stderr)
      self.assertIn("missing-target", result.stdout)

  def test_content_page_without_front_matter_fails(self):
    with tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR")) as directory:
      root = Path(directory)
      (root / "Topic.md").write_text("# Topic\nA useful procedure.\n", encoding="utf-8")
      result = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("check_docs.py")), str(root)],
        capture_output=True, text=True, check=False,
      )
      self.assertEqual(result.returncode, 1, result.stderr)
      self.assertIn("front-matter", result.stdout)

  def test_missing_heading_fragment_fails(self):
    with tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR")) as directory:
      root = Path(directory)
      (root / "README.md").write_text("[Topic](./Topic.md#missing)\n", encoding="utf-8")
      (root / "Topic.md").write_text("---\nlayout: page\ntitle: Topic\n---\n# Topic\n", encoding="utf-8")
      result = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("check_docs.py")), str(root)],
        capture_output=True, text=True, check=False,
      )
      self.assertEqual(result.returncode, 1, result.stderr)
      self.assertIn("missing-fragment", result.stdout)

  def test_links_cannot_escape_repository(self):
    with tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR")) as directory:
      parent = Path(directory)
      root = parent / "Repo"
      root.mkdir()
      (parent / "Outside.md").write_text("# Outside\n", encoding="utf-8")
      (root / "README.md").write_text("[Outside](../Outside.md)\n", encoding="utf-8")
      result = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("check_docs.py")), str(root)],
        capture_output=True, text=True, check=False,
      )
      self.assertEqual(result.returncode, 1, result.stderr)
      self.assertIn("outside-root", result.stdout)

  def test_nonexistent_root_does_not_pass(self):
    with tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR")) as directory:
      root = Path(directory) / "Missing"
      result = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("check_docs.py")), str(root)],
        capture_output=True, text=True, check=False,
      )
      self.assertNotEqual(result.returncode, 0)

  def test_json_summary_counts_files(self):
    with tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR")) as directory:
      root = Path(directory)
      (root / "README.md").write_text("# Index\n", encoding="utf-8")
      result = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("check_docs.py")), str(root), "--json"],
        capture_output=True, text=True, check=False,
      )
      self.assertEqual(result.returncode, 0, result.stderr)
      self.assertIn('"files": 1', result.stdout)

  def test_draft_is_reported_and_strict_content_fails(self):
    with tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR")) as directory:
      root = Path(directory)
      (root / "Topic.md").write_text("---\nlayout: page\ntitle: Topic\nstatus: draft\n---\n# Topic\nDraft notes.\n", encoding="utf-8")
      command = [sys.executable, str(Path(__file__).with_name("check_docs.py")), str(root)]
      normal = subprocess.run(command, capture_output=True, text=True, check=False)
      strict = subprocess.run(command + ["--strict-content"], capture_output=True, text=True, check=False)
      self.assertEqual(normal.returncode, 0, normal.stderr)
      self.assertIn("draft", normal.stdout)
      self.assertEqual(strict.returncode, 1, strict.stderr)
      self.assertIn("strict-content", strict.stdout)

  def test_unclosed_fence_fails(self):
    with tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR")) as directory:
      root = Path(directory)
      (root / "README.md").write_text("# Example\n```python\nprint('hello')\n", encoding="utf-8")
      result = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("check_docs.py")), str(root)],
        capture_output=True, text=True, check=False,
      )
      self.assertEqual(result.returncode, 1, result.stderr)
      self.assertIn("fence", result.stdout)

  def test_invalid_front_matter_mapping_and_duplicate_keys_fail(self):
    cases = [
      "---\n- page\n---\n# Topic\nNotes.\n",
      "---\nlayout: page\ntitle: Topic\n---not-a-delimiter\n# Topic\nNotes.\n",
      "---\nlayout: page\ntitle: First\ntitle: Second\n---\n# Topic\nNotes.\n",
    ]
    for content in cases:
      with self.subTest(content=content), tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR")) as directory:
        root = Path(directory)
        (root / "Topic.md").write_text(content, encoding="utf-8")
        result = subprocess.run(
          [sys.executable, str(Path(__file__).with_name("check_docs.py")), str(root)],
          capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("front-matter", result.stdout)

  def test_valid_reference_image_duplicate_and_encoded_links_pass(self):
    import json
    with tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR")) as directory:
      root = Path(directory)
      (root / "A Topic.md").write_text("---\nlayout: page\ntitle: A Topic\n---\n# Repeat\nNotes.\n# Repeat\nMore notes.\n", encoding="utf-8")
      (root / "image.png").write_bytes(b"fixture: link target, not a decoded image")
      (root / "README.md").write_text(
        "# Index\n[Topic][topic]\n\n[topic]: ./A%20Topic.md#repeat-1\n\n![Image](image.png)\n\n```markdown\n[Ignored](Missing.md)\n```\n",
        encoding="utf-8",
      )
      result = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("check_docs.py")), str(root), "--json"],
        capture_output=True, text=True, check=False,
      )
      self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
      report = json.loads(result.stdout)
      self.assertEqual(report["files"], 2)
      self.assertEqual(report["local_links"], 2)

  def test_directory_index_symlink_cannot_bypass_boundary(self):
    with tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR")) as directory:
      parent = Path(directory)
      root = parent / "Repo"
      docs = root / "Docs"
      docs.mkdir(parents=True)
      outside = parent / "Outside.md"
      outside.write_text("# Outside\n", encoding="utf-8")
      (docs / "README.md").symlink_to(outside)
      (root / "README.md").write_text("[Outside](./Docs/#outside)\n", encoding="utf-8")
      result = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("check_docs.py")), str(root)],
        capture_output=True, text=True, check=False,
      )
      self.assertEqual(result.returncode, 1, result.stderr)
      self.assertIn("README.md: outside-root: ./Docs/#outside", result.stdout)


if __name__ == "__main__":
  unittest.main()
