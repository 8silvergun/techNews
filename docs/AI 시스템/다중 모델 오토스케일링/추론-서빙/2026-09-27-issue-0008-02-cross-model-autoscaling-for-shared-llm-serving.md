---
generated_by: "technews-issue-archive-v1"
source_issue: 8
source_issue_url: "https://github.com/8silvergun/techNews/issues/8"
source_date: "2026-09-27"
category_major: "AI 시스템"
category_middle: "추론/서빙"
category_minor: "다중 모델 오토스케일링"
article_url: "https://arxiv.org/abs/2609.29160"
---

# Cross-Model Autoscaling for Shared LLM Serving

> 원문: [https://arxiv.org/abs/2609.29160](https://arxiv.org/abs/2609.29160) · [GitHub Issue #8](https://github.com/8silvergun/techNews/issues/8)

- **한줄 요약:** 여러 모델이 고정된 GPU 풀을 공유할 때 모델별 수요·지연 목표를 비교할 공통 서비스 지표를 만들고, 여유가 부족한 모델에 GPU 용량을 재배분합니다.
- **기술 자료인 이유:** Token Service Share 지표와 빠른 구제·느린 재균형 제어를 Kubernetes 핫스위치 서빙 스택에 구현하고, 7개 트레이스에서 비교 기준 대비 P95 지연 11.9~79.0%, P99 지연 12.5~72.6% 감소를 보고합니다. 같은 핫스위치 런타임에서 수행한 비교입니다.
