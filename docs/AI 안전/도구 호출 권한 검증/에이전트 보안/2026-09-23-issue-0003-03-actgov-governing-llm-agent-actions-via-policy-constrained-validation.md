---
generated_by: "technews-issue-archive-v1"
source_issue: 3
source_issue_url: "https://github.com/8silvergun/techNews/issues/3"
source_date: "2026-09-23"
category_major: "AI 안전"
category_middle: "에이전트 보안"
category_minor: "도구 호출 권한 검증"
article_url: "https://arxiv.org/abs/2609.24446"
---

# ActGov: Governing LLM Agent Actions via Policy-Constrained Validation

> 원문: [https://arxiv.org/abs/2609.24446](https://arxiv.org/abs/2609.24446) · [GitHub Issue #3](https://github.com/8silvergun/techNews/issues/3)

- **한줄 요약:** 장기 실행 에이전트가 제안한 각 도구 호출을 외부 효과 전에 유한한 정책 레코드로 변환하고, 사용자의 작업 범위와 검증된 정책을 만족할 때만 허용합니다.
- **기술 자료인 이유:** 도구 명세·정상 과제·공격 실패 로그에서 정책을 만들고 Z3 반례 검사로 배포 전에 검증하며, 런타임에서는 동결된 정책을 결정적으로 집행하는 구조를 AgentDojo·AgentDyn에서 평가합니다.
