---
generated_by: "technews-issue-archive-v1"
source_issue: 10
source_issue_url: "https://github.com/8silvergun/techNews/issues/10"
source_date: "2026-09-29"
category_major: "AI 시스템"
category_middle: "멀티모달 서빙"
category_minor: "인코딩·프리필·디코딩 분리"
article_url: "https://arxiv.org/abs/2609.31551"
---

# EAServe: Encode-Aware Disaggregated Serving for Multimodal Large Language Models

> 원문: [https://arxiv.org/abs/2609.31551](https://arxiv.org/abs/2609.31551) · [GitHub Issue #10](https://github.com/8silvergun/techNews/issues/10)

- **한줄 요약:** 이미지·영상·음성 모델의 Encode–Prefill–Decode 단계에서 인코딩 GPU의 유휴 용량을 활용하고, 인코딩에서 후속 단계로 넘어가는 속도를 조절합니다.
- **기술 자료인 이유:** 부하 적응형 마이크로배칭, 부분 프리필 오프로딩, SM 분할 및 GPU 배치 탐색을 함께 구현했습니다. 세 가지 멀티모달 구조에서 동일 SLO 조건의 NVIDIA Dynamo·vLLM 대비 goodput이 각각 최대 4.3배·1.7배였다고 보고합니다. '최대' 수치이며 모든 구성의 보장치가 아닙니다.
