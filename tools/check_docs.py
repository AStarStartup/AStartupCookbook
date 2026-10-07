# Copyright AStarship <https://astarship.net>.
"""Check local Markdown links without network access."""

import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt
import yaml


UtilityFiles = frozenset(("README.md", "AGENTS.md", "BacklogTriagePlan.md", "RepoSyncPlan.md", "license.md"))


class TUniqueLoader(yaml.SafeLoader):
  pass


def TUniqueMapping(loader, node):
  loader.flatten_mapping(node)
  mapping = {}
  for key_node, value_node in node.value:
    key = loader.construct_object(key_node)
    try:
      if key in mapping:
        raise yaml.YAMLError(f"Duplicate YAML key: {key}")
      mapping[key] = loader.construct_object(value_node)
    except TypeError as error:
      raise yaml.YAMLError("YAML mapping key must be hashable") from error
  return mapping


TUniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, TUniqueMapping)


def THeadingIds(parser, text):
  text = re.sub(r"^---\n.*?\n---(?:\n|$)", "", text, count=1, flags=re.S)
  tokens = parser.parse(text)
  ids = set()
  for index, token in enumerate(tokens):
    if token.type != "heading_open":
      continue
    children = tokens[index + 1].children or []
    label = "".join(child.content for child in children if child.type in ("text", "code_inline", "image"))
    base = "".join(char for char in label.lower() if not unicodedata.category(char).startswith(("P", "S")) or char in "-_")
    base = re.sub(r"\s", "-", base.strip())
    slug = base
    suffix = 0
    while slug in ids:
      suffix += 1
      slug = f"{base}-{suffix}"
    ids.add(slug)
  ids.update(match.group(1) for match in re.finditer(r'\b(?:id|name)=["\']([^"\']+)["\']', text))
  return ids


def TDocsCheck(root, strict_content=False):
  report = {"files": 0, "local_links": 0, "draft_files": [], "errors": [], "warnings": []}
  errors = report["errors"]
  if not root.is_dir():
    errors.append("root: invalid-root: Expected an existing directory")
    return report
  parser = MarkdownIt("commonmark").enable("table")
  ignored = {".git", ".venv", "venv", "node_modules", "_site", "__pycache__"}
  for path in sorted(root.rglob("*.md")):
    relative = path.relative_to(root)
    if any(part in ignored for part in relative.parts):
      continue
    report["files"] += 1
    if not path.resolve().is_relative_to(root.resolve()):
      errors.append(f"{relative}: outside-root: Markdown source is outside repository")
      continue
    try:
      text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
      errors.append(f"{relative}: read-error: {error}")
      continue
    body = text
    metadata = {}
    content_page = relative.as_posix() not in UtilityFiles and ".github" not in relative.parts
    if text.startswith("---\n"):
      try:
        closing = re.search(r"(?m)^---[ \t]*$", text[4:])
        if not closing:
          raise ValueError("Missing exact closing delimiter")
        metadata = yaml.load(text[4:][:closing.start()], Loader=TUniqueLoader)
        if not isinstance(metadata, dict):
          raise ValueError("Expected a YAML mapping")
        if content_page:
          if metadata.get("layout") != "page" or not isinstance(metadata.get("title"), str) or not metadata["title"].strip():
            raise ValueError("Expected layout: page and a nonempty title")
        body = text[4:][closing.end():].lstrip("\n")
      except (ValueError, yaml.YAMLError) as error:
        metadata = {}
        errors.append(f"{relative}: front-matter: {error}")
    elif content_page:
      errors.append(f"{relative}: front-matter: Missing YAML front matter")
    tokens = parser.parse(body)
    lines = body.splitlines()
    for token in tokens:
      if token.type == "fence" and token.map:
        start, end = token.map
        last = lines[end - 1].strip().lstrip("> ") if end else ""
        closing_pattern = re.escape(token.markup[0]) + "{" + str(len(token.markup)) + r",}\s*"
        if end <= start + 1 or not re.fullmatch(closing_pattern, last):
          errors.append(f"{relative}: fence: Unterminated code fence")
    prose = "\n".join(token.content for token in tokens if token.type == "inline")
    placeholder = bool(re.search(r"\[(?:Insert|Note:\s*Insert|@todo)[^\]]*\]|\(Insert\s|@todo\s+Fix|#WorkInProgress|Some random paragraph|_{3,}", prose, re.I))
    empty = not any(token.type in ("paragraph_open", "table_open", "fence", "code_block", "html_block") for token in tokens)
    declared_draft = metadata.get("status") == "draft"
    if content_page and (declared_draft or placeholder or empty):
      report["draft_files"].append(relative.as_posix())
      report["warnings"].append(f"{relative}: draft: incomplete or declared draft content")
      if not declared_draft:
        errors.append(f"{relative}: unmarked-draft: Mark incomplete material status: draft")
    for token in tokens:
      for child in token.children or []:
        if child.type not in ("link_open", "image"):
          continue
        destination = str(child.attrGet("href" if child.type == "link_open" else "src") or "")
        split = urlsplit(destination)
        if split.scheme or split.netloc:
          continue
        report["local_links"] += 1
        if split.path.startswith("/"):
          target = root / unquote(split.path).lstrip("/")
        elif split.path:
          target = path.parent / unquote(split.path)
        else:
          target = path
        if not target.resolve().is_relative_to(root.resolve()):
          errors.append(f"{relative}: outside-root: {destination}")
          continue
        if not target.exists():
          errors.append(f"{relative}: missing-target: {destination}")
          continue
        if target.is_dir():
          target = next((target / name for name in ("README.md", "index.md") if (target / name).is_file()), target)
        if not target.resolve().is_relative_to(root.resolve()):
          errors.append(f"{relative}: outside-root: {destination}")
          continue
        if split.fragment and child.type == "link_open" and target.suffix.lower() == ".md":
          try:
            ids = THeadingIds(parser, target.read_text(encoding="utf-8"))
          except (OSError, UnicodeError) as error:
            errors.append(f"{relative}: read-error: {destination}: {error}")
            continue
          if unquote(split.fragment) not in ids:
            errors.append(f"{relative}: missing-fragment: {destination}")
  if strict_content and report["draft_files"]:
    errors.append(f"strict-content: {len(report['draft_files'])} draft/incomplete pages remain")
  return report


def TMain():
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument("root", nargs="?", default=".")
  parser.add_argument("--json", action="store_true", help="Print machine-readable counts and findings")
  parser.add_argument("--strict-content", action="store_true", help="Fail if any draft/incomplete pages remain")
  args = parser.parse_args()
  report = TDocsCheck(Path(args.root).resolve(), args.strict_content)
  if args.json:
    print(json.dumps(report, indent=2))
  else:
    for error in report["errors"]:
      print(error)
    verdict = "FAIL" if report["errors"] else "PASS"
    print(f"{verdict}: {report['files']} Markdown files; {report['local_links']} local links; {len(report['errors'])} errors; {len(report['draft_files'])} draft/incomplete files")
  return 1 if report["errors"] else 0


if __name__ == "__main__":
  sys.exit(TMain())
