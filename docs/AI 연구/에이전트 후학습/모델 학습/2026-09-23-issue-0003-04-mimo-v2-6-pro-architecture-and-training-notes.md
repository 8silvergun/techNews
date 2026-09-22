---
generated_by: "technews-issue-archive-v1"
source_issue: 3
source_issue_url: "https://github.com/8silvergun/techNews/issues/3"
source_date: "2026-09-23"
category_major: "AI 연구"
category_middle: "모델 학습"
category_minor: "에이전트 후학습"
article_url: "https://sebastianraschka.com/blog/2026/mimo-v2-6-pro-architecture-training-notes.html"
---

# MiMo-V2.6 Pro Architecture and Training Notes

> 원문: [https://sebastianraschka.com/blog/2026/mimo-v2-6-pro-architecture-training-notes.html](https://sebastianraschka.com/blog/2026/mimo-v2-6-pro-architecture-training-notes.html) · [GitHub Issue #3](https://github.com/8silvergun/techNews/issues/3)

- **한줄 요약:** 복잡한 새 attention보다 에이전트 과제 비중, 여러 하네스에 걸친 훈련, 실행 궤적을 보는 grader, 대규모 RL 배치가 성능 향상의 핵심이었다는 기술 보고서의 포인트를 정리합니다.
- **기술 자료인 이유:** 128-token sliding window를 포함한 GQA/SWA 구조와 함께, 홀드아웃 하네스의 DeepSWE pass@1이 약 50%에서 66%로 오른 점, 업데이트당 25,088개 궤적과 27~37억 학습 토큰 규모를 구체적으로 분석합니다.
