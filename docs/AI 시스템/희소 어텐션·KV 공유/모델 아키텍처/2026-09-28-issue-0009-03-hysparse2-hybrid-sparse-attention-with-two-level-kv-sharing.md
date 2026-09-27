---
generated_by: "technews-issue-archive-v1"
source_issue: 9
source_issue_url: "https://github.com/8silvergun/techNews/issues/9"
source_date: "2026-09-28"
category_major: "AI 시스템"
category_middle: "모델 아키텍처"
category_minor: "희소 어텐션·KV 공유"
article_url: "https://arxiv.org/abs/2609.26368"
---

# HySparse2: Hybrid Sparse Attention with Two-Level KV Sharing

> 원문: [https://arxiv.org/abs/2609.26368](https://arxiv.org/abs/2609.26368) · [GitHub Issue #9](https://github.com/8silvergun/techNews/issues/9)

- **한줄 요약:** self-decoder의 KV를 cross-decoder와 공유하고 토큰 단위 희소 선택을 써서, 긴 도구 응답을 읽는 에이전트의 prefill 계산량과 KV 저장량을 줄입니다.
- **기술 자료인 이유:** 80B-A3B MoE를 동일 학습 조건의 HySparse·Hybrid SWA와 비교하고, 1M 토큰에서 prefill FLOPs가 각각 2.92배·5.02배 적다고 분석합니다. MRCR-v2·RULER-v2 장문 검색과 256K까지의 AgentPPL도 비교합니다. FLOPs 분석을 실측 서비스 속도로 오해해서는 안 됩니다.
