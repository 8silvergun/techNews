---
generated_by: "technews-issue-archive-v1"
source_issue: 10
source_issue_url: "https://github.com/8silvergun/techNews/issues/10"
source_date: "2026-09-29"
category_major: "AI 시스템"
category_middle: "추론/서빙"
category_minor: "행동 중심 KV 캐시 압축"
article_url: "https://arxiv.org/abs/2609.31395"
---

# ActKV: Efficient LLM Agents through Action-Guided KV Cache Management

> 원문: [https://arxiv.org/abs/2609.31395](https://arxiv.org/abs/2609.31395) · [GitHub Issue #10](https://github.com/8silvergun/techNews/issues/10)

- **한줄 요약:** 에이전트의 모든 과거 토큰을 똑같이 보존하는 대신 다음 행동 생성에 중요한 KV 항목을 우선 남기고, 현재 단계의 확신에 따라 캐시 예산을 조절합니다.
- **기술 자료인 이유:** 행동 지향 교체 정책, 확신 기반 예산 배분, 페이지형 KV 관리용 커널을 구현하고 긴 궤적 과제에서 FullKV 정확도의 평균 98.53%를 유지하며 최대 KV 메모리는 25.98%만 사용했다고 보고합니다. 논문 조건에서 토큰·과제 처리량도 각각 3.97배·3.58배입니다.
