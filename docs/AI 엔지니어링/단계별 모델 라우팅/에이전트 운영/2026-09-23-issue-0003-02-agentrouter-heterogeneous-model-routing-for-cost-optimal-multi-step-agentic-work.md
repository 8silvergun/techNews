---
generated_by: "technews-issue-archive-v1"
source_issue: 3
source_issue_url: "https://github.com/8silvergun/techNews/issues/3"
source_date: "2026-09-23"
category_major: "AI 엔지니어링"
category_middle: "에이전트 운영"
category_minor: "단계별 모델 라우팅"
article_url: "https://arxiv.org/abs/2609.22951"
---

# AgentRouter: Heterogeneous Model Routing for Cost-Optimal Multi-Step Agentic Workflows

> 원문: [https://arxiv.org/abs/2609.22951](https://arxiv.org/abs/2609.22951) · [GitHub Issue #3](https://github.com/8silvergun/techNews/issues/3)

- **한줄 요약:** 한 에이전트 궤적 안에서도 계획·코딩·포맷팅의 난도가 다르다는 점을 이용해, 각 단계마다 4개 모델 티어 중 하나를 선택하는 12M 파라미터 라우터를 제안합니다.
- **기술 자료인 이유:** 5만 개의 주석된 에이전트 단계로 훈련하고 A100에서 단계당 5ms 미만 오버헤드로 frontier-only 대비 비용을 72% 줄이면서 품질의 97.3%를 유지한 결과를 RouteLLM·FrugalGPT와 비교합니다.
