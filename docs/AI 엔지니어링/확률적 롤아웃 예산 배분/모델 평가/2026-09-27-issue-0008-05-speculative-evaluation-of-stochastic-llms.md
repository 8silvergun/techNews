---
generated_by: "technews-issue-archive-v1"
source_issue: 8
source_issue_url: "https://github.com/8silvergun/techNews/issues/8"
source_date: "2026-09-27"
category_major: "AI 엔지니어링"
category_middle: "모델 평가"
category_minor: "확률적 롤아웃 예산 배분"
article_url: "https://arxiv.org/abs/2609.28560"
---

# Speculative Evaluation of Stochastic LLMs

> 원문: [https://arxiv.org/abs/2609.28560](https://arxiv.org/abs/2609.28560) · [GitHub Issue #8](https://github.com/8silvergun/techNews/issues/8)

- **한줄 요약:** 각 평가 문제에 같은 횟수로 샘플을 돌리는 대신 짧은 예비 평가로 문제별 분산을 추정하고, 정해진 총 롤아웃 예산을 오차가 큰 문제에 더 배분합니다.
- **기술 자료인 이유:** 계층 베이지안 Neyman 배분과 파일럿 동기화 대기 중의 비동기 선행 실행을 설계하고, 6개 체크포인트·18개 벤치마크군의 107개 프로필에서 동일 예산의 균등 배분보다 평균 추정 분산을 12.8~33.6% 낮췄다고 보고합니다. 비동기 실행의 실시간 오버헤드도 따로 시험합니다.
