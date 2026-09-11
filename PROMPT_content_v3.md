# THE HEADLINE 콘텐츠 제작 프롬프트 v3
(v2 + 저장률 기획 반영. 변경 지점만 표시 — 나머지는 v2 그대로)

────────────────────────────────
0. 브랜드 브리프  (v2 동일)
────────────────────────────────

────────────────────────────────
1. 저장 이유 설계 (신설)
────────────────────────────────
저장은 "나중에 다시 볼 이유"가 있을 때 일어난다. 모든 편은 아래 세 유형 중 최소 하나를 갖는다.
① 목록형 — 한 장에 여러 개 (6장 표, 7장 THE OTHER THREE, WEEKLY FIVE, MONTHLY INDEX)
② 규칙형 — 한 번 알면 계속 쓰는 원리 (HEADLINE GRAMMAR)
③ 테스트형 — 나중에 나를 다시 시험 (5장 퀴즈, WEEKLY QUIZ)

NEWS IDIOM 한 편의 저장 카드는 이제 두 장이다: 6장(표) + 7장(오답 이디엄 3개).

────────────────────────────────
2. 스토리라인 (7장으로 확장)
────────────────────────────────
1 WHY · 2 HOW · 3 HOW · 4 WHAT · 5 TEST · 6 POINT BRIEF · **7 FOOTNOTE(THE OTHER THREE)**
7장은 각주다. 메인 표현은 여전히 하나이며, 7장은 5장 오답 보기 셋을 한 줄씩 정리한다.

────────────────────────────────
3. 에이전트별 추가 지시
────────────────────────────────
에이전트1(설계자) 추가:
- 5장 오답 보기 3개는 처음부터 **"묶어서 외울 가치가 있는 실제 이디엄"** 으로 고른다. 말장난·비실재 표현 금지. 세 개 모두 외신 재등장 빈도가 있어야 한다.
- collection 필드에 이전 편 3~5개를 `#번호 표현` 형식으로 채운다.
- exam_source에 환언이 나오는 시험·유형을 적는다 (예: 편입 어휘 환언 · 토익 Part 5).

에이전트3(민쌤) 추가:
- 3장에 EXAM 한 줄: "편입·토익에서는 ___로 환언되어 나옵니다" 형식, 40자 이내.
- 7장: 오답 이디엄 각각 뜻 15자 이내 + 영어 예문 60자 이내. 뜻 확장 금지 규칙은 7장에도 적용.

에이전트2(마케터) 추가:
- 6장 하단 해시태그는 이미지에 넣지 않는다(검색에 안 잡힘). 그 자리는 COLLECTION 줄.
- 캡션 마지막 줄은 "전체 목록은 프로필 고정 게시물" 로 고정.

────────────────────────────────
4. 검수 항목 (v2 ⑩ + 3개)
────────────────────────────────
⑪ 7장 오답 이디엄 3개 모두 실제 표현이며 뜻 범위 안 ⑫ 3장 EXAM 한 줄 포함 ⑬ 6장 COLLECTION 줄 포함(해시태그 없음)

────────────────────────────────
5. JSON 스키마 추가 필드
────────────────────────────────
"kind": "idiom" | "grammar"
"distractor_meanings": [{"expr": "", "ko": "", "en": ""}, ×3]
"exam_line": ""            // 3장 한 줄
"exam_source": ""          // 시험·유형
"collection": ["#001 ...", "#002 ..."]

HEADLINE GRAMMAR 스키마 (kind: grammar)
"rule", "rule_en", "rule_ko", "hook_ko",
"demo": {"headline": "Fed [to hold] rates", "normal": "Fed [will hold] rates"}   // [ ]가 밑줄
"examples": [{"src","hl","full"}, ×3],
"quiz_hl", "quiz_options"[4], "quiz_answer",
"summary"[3], "collection"

────────────────────────────────
6. 시리즈별 출력 형태
────────────────────────────────
NEWS IDIOM / KOREA IN ENGLISH / NEWS COLLOCATION / HEADLINE TRAP → 7장 (build_v6_idiom.py)
HEADLINE GRAMMAR → 5장 (build_v6_grammar.py): 규칙 → 헤드라인 3 + 복원 → 퀴즈 → 요약+COLLECTION
WEEKLY FIVE → 2장 (build_v6_weekly.py): 그 주 JSON 5건에서 자동. 정답은 캡션.
HEADLINE VERB BANK / ONE STORY THREE HEADLINES / SEEN IN THE EXAM / MONTHLY INDEX → 수동 제작 후 반응 보고 템플릿화

────────────────────────────────
7. 주간 편성 (자동화 스케줄 기준)
────────────────────────────────
월 NEWS IDIOM (7장)          07:30
화 HEADLINE VERB BANK        07:30  (초기 수동)
수 NEWS IDIOM / KOREA IN ENGLISH 교대
목 NEWS COLLOCATION / HEADLINE TRAP 교대
금 ONE STORY THREE HEADLINES(격주) / SEEN IN THE EXAM
토 WEEKLY FIVE (2장)         — 월~금 JSON에서 자동
일 HEADLINE GRAMMAR (5장)
매월 1일 MONTHLY INDEX 갱신 → 프로필 고정

처음 4주는 그대로 돌리고, 인사이트의 저장/도달 비율로 시리즈 2개를 남기고 나머지를 줄인다.

────────────────────────────────
8. 보조 장치 (캐러셀 밖)
────────────────────────────────
- 매일 스토리: 전날 5장 퀴즈를 투표 스티커로. 결과 화면 "정답은 어제 6장".
- 주 1회 릴스: 7장을 2.5초씩 → 17초 세로 영상. 도달용. (릴스 렌더러는 파이프라인 2단계)
