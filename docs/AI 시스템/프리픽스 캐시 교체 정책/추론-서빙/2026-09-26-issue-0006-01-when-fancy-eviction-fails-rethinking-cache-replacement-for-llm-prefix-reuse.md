---
generated_by: "technews-issue-archive-v1"
source_issue: 6
source_issue_url: "https://github.com/8silvergun/techNews/issues/6"
source_date: "2026-09-26"
category_major: "AI 시스템"
category_middle: "추론/서빙"
category_minor: "프리픽스 캐시 교체 정책"
article_url: "https://arxiv.org/abs/2609.28870"
---

# When Fancy Eviction Fails: Rethinking Cache Replacement For LLM Prefix Reuse

> 원문: [https://arxiv.org/abs/2609.28870](https://arxiv.org/abs/2609.28870) · [GitHub Issue #6](https://github.com/8silvergun/techNews/issues/6)

- **한줄 요약:** 두 서비스의 실제 요청 트레이스에서 14가지 캐시 교체 정책을 비교하니 복잡한 방식 대부분이 LRU보다 낫지 않았고, 세션의 짧고 규칙적인 재사용 간격이 그 이유였습니다.
- **기술 자료인 이유:** 32.75만·51.58만 요청의 프로덕션 트레이스, HBM과 대형 메모리 풀 범위, 요청 단위 상주 제약을 반영한 C++ 시뮬레이터, 블록 적중률과 계산 절약률을 비교합니다. 트레이스·시뮬레이터는 향후 공개 예정이라고 적혀 있으므로 현재 재현 가능하다고 보지는 않습니다.
