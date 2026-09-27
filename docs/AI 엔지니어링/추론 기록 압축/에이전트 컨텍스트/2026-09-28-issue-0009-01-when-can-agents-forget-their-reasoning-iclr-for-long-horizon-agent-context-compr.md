---
generated_by: "technews-issue-archive-v1"
source_issue: 9
source_issue_url: "https://github.com/8silvergun/techNews/issues/9"
source_date: "2026-09-28"
category_major: "AI 엔지니어링"
category_middle: "에이전트 컨텍스트"
category_minor: "추론 기록 압축"
article_url: "https://arxiv.org/abs/2609.29875"
---

# When Can Agents Forget Their Reasoning? ICLR for Long-Horizon Agent Context Compression

> 원문: [https://arxiv.org/abs/2609.29875](https://arxiv.org/abs/2609.29875) · [GitHub Issue #9](https://github.com/8silvergun/techNews/issues/9)

- **한줄 요약:** 오래된 추론 기록의 중요도를 상태에 따라 매겨 지우되 행동·도구 호출·관찰은 보존하는 온라인 압축으로, 에이전트가 필요할 때만 과거 생각을 다시 참조하게 합니다.
- **기술 자료인 이유:** 동결된 프록시 모델의 엔트로피로 추론 블록을 순위화하며 WorkBuddyBench 260개 과제에서 평균 보상이 0.699→0.718, 입력 토큰이 25.5%, 캐시 읽기 토큰이 33.3% 감소했다고 보고합니다. 삭제가 이후 행동 경로를 바꿀 수 있다는 한계도 분석합니다.
