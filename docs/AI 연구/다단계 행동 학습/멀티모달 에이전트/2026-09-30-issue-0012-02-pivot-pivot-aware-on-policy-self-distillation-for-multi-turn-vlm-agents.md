---
generated_by: "technews-issue-archive-v1"
source_issue: 12
source_issue_url: "https://github.com/8silvergun/techNews/issues/12"
source_date: "2026-09-30"
category_major: "AI 연구"
category_middle: "멀티모달 에이전트"
category_minor: "다단계 행동 학습"
article_url: "https://arxiv.org/abs/2609.35303"
---

# PIVOT: Pivot-Aware On-Policy Self-Distillation for Multi-Turn VLM Agents

> 원문: [https://arxiv.org/abs/2609.35303](https://arxiv.org/abs/2609.35303) · [GitHub Issue #12](https://github.com/8silvergun/techNews/issues/12)

- **한줄 요약:** 다단계 시각 에이전트가 돌이킬 수 없는 첫 실패 행동을 찾아 토큰별 학습 신호로 바꾸어, 환경을 실제로 되돌리는 비용 없이 행동 정책을 개선합니다.
- **기술 자료인 이유:** 실패 분석기·분리된 교사·학생 모델을 이용해 GRPO와 확신 기반 증류를 결합합니다. 5개 VLM 에이전트 과제에서 Qwen2.5-VL-3B 전체 정확도 0.90을 보고하며 SFT+GRPO 대비 8% 향상이라고 명시합니다. 시험 시 분석기와 교사는 제거됩니다.
