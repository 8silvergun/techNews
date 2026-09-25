---
generated_by: "technews-issue-archive-v1"
source_issue: 6
source_issue_url: "https://github.com/8silvergun/techNews/issues/6"
source_date: "2026-09-26"
category_major: "AI 엔지니어링"
category_middle: "추론/서빙"
category_minor: "지속 실행 GPU 커널"
article_url: "https://www.tilert.ai/blog/tilert-amd-agentx.html"
---

# 469 tok/s/user on Million-Token Agent Sessions: TileRT Takes the Top Spot on AgentX with AMD Instinct MI355X GPUs

> 원문: [https://www.tilert.ai/blog/tilert-amd-agentx.html](https://www.tilert.ai/blog/tilert-amd-agentx.html) · [GitHub Issue #6](https://github.com/8silvergun/techNews/issues/6)

- **한줄 요약:** 모델 전체를 지속 실행 GPU 커널로 펼쳐 커널 실행·전역 장벽을 줄이고, 스트리밍 동기화와 선반입 및 통신-계산 겹치기로 긴 에이전트 세션의 디코드 지연을 낮춥니다.
- **기술 자료인 이유:** FP8 가중치·BF16 KV·TP8·MTP K=3 구성과 AgentX 기준 MI355X 8장 단일 사용자 469 tok/s 결과, 별도 MI350X 8장의 1K~1M 컨텍스트 속도(648→425 tok/s)를 구분해 밝힙니다. 공급사 공동 작성 자료이므로 경쟁사 대비 우열은 자체 제출 벤치마크 맥락에서 읽어야 합니다.
