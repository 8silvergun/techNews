---
generated_by: "technews-issue-archive-v1"
source_issue: 2
source_issue_url: "https://github.com/8silvergun/techNews/issues/2"
source_date: "2026-09-22"
category_major: "AI 시스템"
category_middle: "메모리 계층"
category_minor: "DRAM·SSD 오프로딩"
article_url: "https://inferencex.semianalysis.com/blog/engrams-embedding-entendre-codesign"
---

# Engrams Embedding Entendre: Codesign for Efficient DRAM/SSD Offloading

> 원문: [https://inferencex.semianalysis.com/blog/engrams-embedding-entendre-codesign](https://inferencex.semianalysis.com/blog/engrams-embedding-entendre-codesign) · [GitHub Issue #2](https://github.com/8silvergun/techNews/issues/2)

- **한줄 요약:** 토큰 ID로 접근하는 희소 Engram 테이블을 HBM 밖으로 옮겨 DRAM·SSD 경로를 비교하고, DRAM 오프로딩으로 B300 구성을 TP4에서 TP2로 줄여 Pareto 성능을 최대 1.6배 개선했습니다.
- **기술 자료인 이유:** UVA 기반 GPU 직접 접근과 SSD mmap의 CPU 왕복 경로를 구현 수준으로 비교하고, B200에서 DRAM이 125 tok/s/user 부근에서 달러당 1.21억 토큰, SSD는 5,200만 토큰이라는 실측으로 SSD가 비용·지연 모두 열세임을 보여줍니다.
