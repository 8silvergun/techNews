---
generated_by: "technews-issue-archive-v1"
source_issue: 1
source_issue_url: "https://github.com/8silvergun/techNews/issues/1"
source_date: "2026-09-21"
category_major: "시스템 엔지니어링"
category_middle: "대규모 분산 시스템"
category_minor: "온라인 스토리지"
article_url: "https://openai.com/index/scaling-storage-one-billion-users-part-one/"
---

# Rapidly scaling online storage to serve over 1 billion ChatGPT users

> 원문: [https://openai.com/index/scaling-storage-one-billion-users-part-one/](https://openai.com/index/scaling-storage-one-billion-users-part-one/) · [GitHub Issue #1](https://github.com/8silvergun/techNews/issues/1)

- **한줄 요약:** 온라인 스토리지 계층 Habitat를 확장하며 asyncio 스케줄링, NAT·커넥션 관리, LIFO 풀의 메타안정 실패를 해결하고 Python 서비스를 Rust로 옮긴 과정을 다룹니다.
- **기술 자료인 이유:** 초당 요청 수, 프로세스 수, 장애 메커니즘, 완화 실험을 제시하며 Rust 전환 후 CPU 6배·메모리 15배 효율 향상이라는 운영 측정값까지 공개합니다.
