---
generated_by: "technews-issue-archive-v1"
source_issue: 2
source_issue_url: "https://github.com/8silvergun/techNews/issues/2"
source_date: "2026-09-22"
category_major: "AI 엔지니어링"
category_middle: "추론/서빙"
category_minor: "프리픽스 캐시 운영"
article_url: "https://huggingface.co/blog/pavle-scalably/qwen3-8-27b-nvfp4-production-agents-rtx-5090"
---

# Prefix cache, not throughput: 14 days serving Qwen3.8-27B NVFP4 to production agents on two RTX 5090s

> 원문: [https://huggingface.co/blog/pavle-scalably/qwen3-8-27b-nvfp4-production-agents-rtx-5090](https://huggingface.co/blog/pavle-scalably/qwen3-8-27b-nvfp4-production-agents-rtx-5090) · [GitHub Issue #2](https://github.com/8silvergun/techNews/issues/2)

- **한줄 요약:** RTX 5090 두 장으로 27B 모델을 14일간 실제 에이전트 트래픽에 서빙한 결과, 프리픽스 캐시가 prefill 토큰의 82.6%를 처리했고 캐시 여유·스케줄 설정이 커널 속도보다 운영 안정성에 더 큰 영향을 줬습니다.
- **기술 자료인 이유:** vLLM 실행 플래그, 모델·양자화 구성, GPU별 메모리, 프롬프트 분포, TTFT/ITL, 캐시·preemption 카운터와 재현 명령을 공개하며 벤치마크 생성기가 아닌 실제 `/metrics` 값을 사용합니다.
