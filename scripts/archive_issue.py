#!/usr/bin/env python3
"""Archive a structured GitHub issue into categorized Markdown documents."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
import urllib.parse
from dataclasses import dataclass
from pathlib import Path
from typing import Any

GENERATED_BY = "technews-issue-archive-v1"
CATEGORY_RE = re.compile(r"^##\s+(.+?)\s*>\s*(.+?)\s*>\s*(.+?)\s*$")
ARTICLE_RE = re.compile(r"^###\s+\[(.+?)\]\((https?://[^)]+)\)\s*$")
DATE_RE = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b")
INVALID_PATH_CHARS_RE = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
SLUG_RE = re.compile(r"[^\w가-힣]+", re.UNICODE)


@dataclass(frozen=True)
class Article:
    index: int
    title: str
    url: str
    major: str
    middle: str
    minor: str
    content: str


def parse_issue_body(body: str) -> list[Article]:
    """Parse sections shaped as: ## major > middle > minor / ### [title](url)."""
    articles: list[Article] = []
    category: tuple[str, str, str] | None = None
    current: dict[str, Any] | None = None

    def flush() -> None:
        nonlocal current
        if current is None:
            return
        content = "\n".join(current["lines"]).strip()
        major, middle, minor = current["category"]
        articles.append(
            Article(
                index=len(articles) + 1,
                title=current["title"],
                url=current["url"],
                major=major,
                middle=middle,
                minor=minor,
                content=content,
            )
        )
        current = None

    for raw_line in body.splitlines():
        category_match = CATEGORY_RE.match(raw_line)
        if category_match:
            flush()
            category = tuple(part.strip() for part in category_match.groups())
            continue

        article_match = ARTICLE_RE.match(raw_line)
        if article_match and category:
            flush()
            current = {
                "title": article_match.group(1).strip(),
                "url": article_match.group(2).strip(),
                "category": category,
                "lines": [],
            }
            continue

        # Any other level-2 heading ends the current categorized section,
        # e.g. "## 선정 기준".
        if raw_line.startswith("## "):
            flush()
            category = None
            continue

        if current is not None:
            current["lines"].append(raw_line)

    flush()
    return articles


def safe_component(value: str) -> str:
    value = unicodedata.normalize("NFC", value).strip()
    value = INVALID_PATH_CHARS_RE.sub("-", value)
    value = re.sub(r"\s+", " ", value).strip(" .-")
    return value or "미분류"


def slugify(value: str, max_length: int = 80) -> str:
    value = unicodedata.normalize("NFC", value).strip().lower()
    value = SLUG_RE.sub("-", value).strip("-_")
    value = value[:max_length].rstrip("-_")
    return value or "article"


def yaml_scalar(value: str) -> str:
    # JSON double-quoted strings are valid YAML scalars and safely escape punctuation.
    return json.dumps(value, ensure_ascii=False)


def issue_date(issue: dict[str, Any]) -> str:
    title = str(issue.get("title") or "")
    body = str(issue.get("body") or "")
    for candidate in (title, body):
        match = DATE_RE.search(candidate)
        if match:
            return match.group(1)

    created_at = str(issue.get("created_at") or "")
    if len(created_at) >= 10:
        return created_at[:10]
    return "unknown-date"


def render_document(article: Article, issue: dict[str, Any], date: str) -> str:
    issue_number = int(issue["number"])
    issue_url = str(issue.get("html_url") or issue.get("url") or "")

    original_content = article.content
    if original_content:
        original_content = f"\n{original_content}\n"

    return f"""---
generated_by: {yaml_scalar(GENERATED_BY)}
source_issue: {issue_number}
source_issue_url: {yaml_scalar(issue_url)}
source_date: {yaml_scalar(date)}
category_major: {yaml_scalar(article.major)}
category_middle: {yaml_scalar(article.middle)}
category_minor: {yaml_scalar(article.minor)}
article_url: {yaml_scalar(article.url)}
---

# {article.title}

> 원문: [{article.url}]({article.url}) · [GitHub Issue #{issue_number}]({issue_url})
{original_content}"""


def generated_for_issue(text: str, issue_number: int) -> bool:
    return (
        f"generated_by: {yaml_scalar(GENERATED_BY)}" in text[:1500]
        and re.search(rf"(?m)^source_issue:\s*{issue_number}\s*$", text[:1500])
        is not None
    )


def remove_previous_documents(docs_root: Path, issue_number: int) -> list[Path]:
    removed: list[Path] = []
    if not docs_root.exists():
        return removed

    for path in docs_root.rglob("*.md"):
        if path == docs_root / "README.md":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        if generated_for_issue(text, issue_number):
            path.unlink()
            removed.append(path)

    # Remove empty category directories from deepest to shallowest.
    directories = sorted(
        (path for path in docs_root.rglob("*") if path.is_dir()),
        key=lambda p: len(p.parts),
        reverse=True,
    )
    for directory in directories:
        try:
            directory.rmdir()
        except OSError:
            pass
    return removed


def write_documents(
    docs_root: Path, issue: dict[str, Any], articles: list[Article]
) -> list[Path]:
    date = issue_date(issue)
    issue_number = int(issue["number"])
    written: list[Path] = []

    for article in articles:
        # Source headings are major > middle > minor.
        # Repository layout requested by the user is major / minor / middle.
        directory = (
            docs_root
            / safe_component(article.major)
            / safe_component(article.minor)
            / safe_component(article.middle)
        )
        directory.mkdir(parents=True, exist_ok=True)

        filename = (
            f"{date}-issue-{issue_number:04d}-{article.index:02d}-"
            f"{slugify(article.title)}.md"
        )
        path = directory / filename
        path.write_text(
            render_document(article, issue, date),
            encoding="utf-8",
            newline="\n",
        )
        written.append(path)

    return written


def parse_frontmatter(path: Path) -> dict[str, str] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    try:
        _, block, remainder = text.split("---\n", 2)
    except ValueError:
        return None

    metadata: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        raw_value = raw_value.strip()
        try:
            value = json.loads(raw_value)
        except (json.JSONDecodeError, TypeError):
            value = raw_value
        metadata[key.strip()] = str(value)

    title_match = re.search(r"(?m)^#\s+(.+)$", remainder)
    if title_match:
        metadata["title"] = title_match.group(1).strip()
    return metadata


def build_index(docs_root: Path) -> None:
    entries: list[tuple[str, str, str, str, str, Path]] = []
    if docs_root.exists():
        for path in docs_root.rglob("*.md"):
            if path == docs_root / "README.md":
                continue
            metadata = parse_frontmatter(path)
            if not metadata or metadata.get("generated_by") != GENERATED_BY:
                continue
            entries.append(
                (
                    metadata.get("category_major", "미분류"),
                    metadata.get("category_minor", "미분류"),
                    metadata.get("category_middle", "미분류"),
                    metadata.get("source_date", "unknown-date"),
                    metadata.get("title", path.stem),
                    path,
                )
            )

    entries.sort(key=lambda row: (row[0], row[1], row[2], row[3], row[4]))

    lines = [
        "# Tech News Archive",
        "",
        "> 이 파일은 이슈 아카이브 CI가 자동 생성합니다. 직접 수정하지 마세요.",
        "",
        "경로 순서: **대분류 / 소분류 / 중분류**",
        "",
    ]

    previous_major: str | None = None
    previous_minor: str | None = None
    previous_middle: str | None = None

    for major, minor, middle, date, title, path in entries:
        if major != previous_major:
            lines.extend([f"## {major}", ""])
            previous_major = major
            previous_minor = None
            previous_middle = None
        if minor != previous_minor:
            lines.extend([f"### {minor}", ""])
            previous_minor = minor
            previous_middle = None
        if middle != previous_middle:
            lines.extend([f"#### {middle}", ""])
            previous_middle = middle

        relative = path.relative_to(docs_root).as_posix()
        href = urllib.parse.quote(relative, safe="/")
        lines.append(f"- {date} · [{title}]({href})")

    if not entries:
        lines.append("_아직 아카이브된 문서가 없습니다._")

    lines.append("")
    docs_root.mkdir(parents=True, exist_ok=True)
    (docs_root / "README.md").write_text(
        "\n".join(lines), encoding="utf-8", newline="\n"
    )


def load_issue(args: argparse.Namespace) -> dict[str, Any]:
    if args.event:
        payload = json.loads(Path(args.event).read_text(encoding="utf-8"))
        issue = payload.get("issue")
        if not isinstance(issue, dict):
            raise ValueError("GitHub event payload does not contain an issue object")
        return issue

    if args.issue:
        issue = json.loads(Path(args.issue).read_text(encoding="utf-8"))
        if not isinstance(issue, dict):
            raise ValueError("Issue JSON must be an object")
        return issue

    raise ValueError("Either --event or --issue is required")


def main() -> int:
    parser = argparse.ArgumentParser()
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--event", help="GitHub event JSON path")
    source.add_argument("--issue", help="Raw GitHub issue JSON path")
    parser.add_argument("--docs-root", default="docs", help="Archive root directory")
    args = parser.parse_args()

    issue = load_issue(args)
    if "number" not in issue:
        raise ValueError("Issue JSON is missing 'number'")

    body = str(issue.get("body") or "")
    articles = parse_issue_body(body)
    if not articles:
        raise ValueError(
            "No articles found. Expected '## major > middle > minor' followed by "
            "'### [title](https://...)'."
        )

    docs_root = Path(args.docs_root)
    issue_number = int(issue["number"])
    removed = remove_previous_documents(docs_root, issue_number)
    written = write_documents(docs_root, issue, articles)
    build_index(docs_root)

    print(
        f"issue #{issue_number}: removed {len(removed)} old document(s), "
        f"wrote {len(written)} document(s)"
    )
    for path in written:
        print(path.as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
