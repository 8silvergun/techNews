---
generated_by: "technews-issue-archive-v1"
source_issue: 3
source_issue_url: "https://github.com/8silvergun/techNews/issues/3"
source_date: "2026-09-23"
category_major: "AI 시스템"
category_middle: "추론/서빙"
category_minor: "다중 엔진 재현 벤치마크"
article_url: "https://rocm.blogs.amd.com/artificial-intelligence/kimi-k3-mad/README.html"
---

# Benchmarking Kimi-K3 Across vLLM, SGLang, and ATOM on MI350X

> 원문: [https://rocm.blogs.amd.com/artificial-intelligence/kimi-k3-mad/README.html](https://rocm.blogs.amd.com/artificial-intelligence/kimi-k3-mad/README.html) · [GitHub Issue #3](https://github.com/8silvergun/techNews/issues/3)

- **한줄 요약:** 8× MI350X에서 2.8T 파라미터 Kimi-K3를 vLLM·SGLang·ATOM으로 서빙하고, 공통 하네스로 8,192 입력/1,024 출력 토큰과 동시성 1~128 구간을 측정합니다.
- **기술 자료인 이유:** 컨테이너 digest, 서버 플래그, 환경 변수, 클라이언트 명령, metric 정의를 공개하고 MAD의 선언형 YAML로 세 엔진을 같은 CSV 형식에 맞춥니다. 동시성 32에서 세 엔진이 0.5% 이내였지만 보조 설정이 달라 순수 엔진 우열 비교로 해석하면 안 된다는 한계도 명시합니다.
