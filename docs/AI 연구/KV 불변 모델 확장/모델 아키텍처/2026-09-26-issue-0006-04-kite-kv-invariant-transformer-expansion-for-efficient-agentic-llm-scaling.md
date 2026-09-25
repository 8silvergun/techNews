---
generated_by: "technews-issue-archive-v1"
source_issue: 6
source_issue_url: "https://github.com/8silvergun/techNews/issues/6"
source_date: "2026-09-26"
category_major: "AI 연구"
category_middle: "모델 아키텍처"
category_minor: "KV 불변 모델 확장"
article_url: "https://arxiv.org/abs/2609.27294"
---

# KITE: KV-Invariant Transformer Expansion for Efficient Agentic LLM Scaling

> 원문: [https://arxiv.org/abs/2609.27294](https://arxiv.org/abs/2609.27294) · [GitHub Issue #6](https://github.com/8silvergun/techNews/issues/6)

- **한줄 요약:** KV를 만드는 부분은 작게 유지하고 KV를 읽는 부분에 나중에 용량을 더하는 두 타워 구조로, 모델 확장 중 훈련과 추론의 계산비를 함께 낮추려 합니다.
- **기술 자료인 이유:** Step Scale Transformer의 KV 생성/읽기 경계와 업사이클링 경로를 설명하고, 같은 누적 훈련 계산에서 67B MoE와 47B·63B 기준 모델의 손실 및 추정 추론 비용(각각 6.7%·31.6% 감소)을 비교합니다. 비용 수치는 실측 운영비가 아닌 추정치입니다.
