import json
import tempfile
import unittest
from pathlib import Path

from scripts.archive_issue import (
    build_index,
    parse_issue_body,
    remove_previous_documents,
    write_documents,
)


SAMPLE_BODY = """# 2026-09-22 LLM/AI 기술 아티클

## AI 연구 > 에이전트 > 하네스 최적화

### [SoL-Pi: Efficient Agent Harness](https://example.com/sol-pi)

- **한줄 요약:** 테스트 요약
- **기술 자료인 이유:** 테스트 근거

## 시스템 엔지니어링 > 대규모 분산 시스템 > 온라인 스토리지

### [Scaling Storage](https://example.com/storage)

- **한줄 요약:** 스토리지 요약

## 선정 기준

- 단순 홍보 제외
"""


class ArchiveIssueTest(unittest.TestCase):
    def test_parse_structured_issue(self):
        articles = parse_issue_body(SAMPLE_BODY)

        self.assertEqual(2, len(articles))
        self.assertEqual("AI 연구", articles[0].major)
        self.assertEqual("에이전트", articles[0].middle)
        self.assertEqual("하네스 최적화", articles[0].minor)
        self.assertEqual("https://example.com/sol-pi", articles[0].url)
        self.assertIn("테스트 요약", articles[0].content)
        self.assertNotIn("선정 기준", articles[-1].content)

    def test_write_uses_major_minor_middle_path_order(self):
        issue = {
            "number": 2,
            "title": "2026-09-22 LLM/AI 기술 추천",
            "html_url": "https://github.com/8silvergun/techNews/issues/2",
            "body": SAMPLE_BODY,
        }
        articles = parse_issue_body(SAMPLE_BODY)

        with tempfile.TemporaryDirectory() as tmp:
            docs_root = Path(tmp) / "docs"
            written = write_documents(docs_root, issue, articles)

            expected_parent = docs_root / "AI 연구" / "하네스 최적화" / "에이전트"
            self.assertEqual(expected_parent, written[0].parent)

            text = written[0].read_text(encoding="utf-8")
            self.assertIn("source_issue: 2", text)
            self.assertIn('category_major: "AI 연구"', text)
            self.assertIn('category_middle: "에이전트"', text)
            self.assertIn('category_minor: "하네스 최적화"', text)

    def test_rearchive_removes_old_documents_and_builds_index(self):
        issue = {
            "number": 2,
            "title": "2026-09-22 LLM/AI 기술 추천",
            "html_url": "https://github.com/8silvergun/techNews/issues/2",
            "body": SAMPLE_BODY,
        }
        articles = parse_issue_body(SAMPLE_BODY)

        with tempfile.TemporaryDirectory() as tmp:
            docs_root = Path(tmp) / "docs"
            written = write_documents(docs_root, issue, articles)
            self.assertEqual(2, len(written))

            removed = remove_previous_documents(docs_root, 2)
            self.assertEqual(2, len(removed))

            rewritten = write_documents(docs_root, issue, articles)
            build_index(docs_root)
            index = (docs_root / "README.md").read_text(encoding="utf-8")

            self.assertEqual(2, len(rewritten))
            self.assertIn("## AI 연구", index)
            self.assertIn("### 하네스 최적화", index)
            self.assertIn("#### 에이전트", index)


if __name__ == "__main__":
    unittest.main()
