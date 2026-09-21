---
generated_by: "technews-issue-archive-v1"
source_issue: 1
source_issue_url: "https://github.com/8silvergun/techNews/issues/1"
source_date: "2026-09-21"
category_major: "AI 엔지니어링"
category_middle: "추론/서빙"
category_minor: "커널·스케줄링"
article_url: "https://vllm.ai/blog/2026-09-13-kimi-k3-performance-optimization"
---

# Kimi K3 Performance Optimizations in vLLM: The Road to 2.8× Throughput

> 원문: [https://vllm.ai/blog/2026-09-13-kimi-k3-performance-optimization](https://vllm.ai/blog/2026-09-13-kimi-k3-performance-optimization) · [GitHub Issue #1](https://github.com/8silvergun/techNews/issues/1)

- **한줄 요약:** 스케줄 토큰 예산, MoE latent-tail 커널, ReplaySSM, prefill/decode 분리, decode context parallelism을 손봐 처리량을 2.2~2.8배 높이고 TTFT를 72~85% 낮췄습니다.
- **기술 자료인 이유:** 변경 사항을 실제 vLLM PR 번호, 벤치마크 명령, 워크로드 조건, 커널 통신 방식과 함께 설명해 구현 수준으로 추적할 수 있습니다.
