---
generated_by: "technews-issue-archive-v1"
source_issue: 10
source_issue_url: "https://github.com/8silvergun/techNews/issues/10"
source_date: "2026-09-29"
category_major: "AI 시스템"
category_middle: "추론/서빙"
category_minor: "분기 추측 실행"
article_url: "https://arxiv.org/abs/2609.31047"
---

# DynBranch: Speculative Subgraph Reuse for Dynamic Agentic LLM Serving

> 원문: [https://arxiv.org/abs/2609.31047](https://arxiv.org/abs/2609.31047) · [GitHub Issue #10](https://github.com/8silvergun/techNews/issues/10)

- **한줄 요약:** 모델이나 사용자가 다음 분기를 고르기 전에 후보 하위 작업을 식별·실행하고 결과를 재사용해, 분기 결정이 후속 작업을 막는 대기 시간을 줄입니다.
- **기술 자료인 이유:** 안정된 분기 좌표와 예상 이득·시스템 부하를 따지는 2단계 제어기를 모델 API 경계에 구현했습니다. Qwen3-32B·H200 4장으로 수행한 네 에이전트 워크로드에서 각 워크로드의 가장 강한 비교군 대비 평균 지연을 최대 32% 줄였다고 보고하며, 8B·RTX 4090에서도 시험합니다.
