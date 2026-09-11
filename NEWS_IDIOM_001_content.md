# NEWS IDIOM #001 · on the ropes — 제작 기록

입력
- 시리즈 NEWS IDIOM / 번호 #001 / 출처 BBC NEWS / 섹션 ECONOMY / 날짜 2026-09-11
- 원문 헤드라인(샘플): UK economy on the ropes as inflation bites

---

## 에이전트1 · 설계

타깃 표현: **on the ropes** — 외신 재등장 빈도 높음(경제·기업·스포츠), 직역하면 "로프에 걸렸다"로 오해 발생, 회화·시험 전이 가능(in serious trouble / in jeopardy). 헤드라인의 inflation, bite는 다루지 않는다.

장별 구조: 1 STOP → 2 KNOW(3키워드 체인) → 3 LEARN(직역/실제 뜻/뉘앙스/유래/주어) → 4 USE(예문 2 + 3단 브리지) → 5 TEST(한→영 4지선다) → 6 SAVE(정답 + 6칸 표)

## 에이전트2 · 마케터

- 1장 훅: **영국 경제가 로프에 걸렸다?** (직역 오해형, 13자)
- 캡션 1행: 동일
- 5장 퀴즈: "그 회사는 지금 벼랑 끝이야." → The company is ____ right now. / A on the ropes · B on the fence · C in the loop · D off the hook
- 6장 CTA: SAVE THIS CARD 📌 다음 외신에서 다시 만나게 됩니다.

## 에이전트3 · 민쌤

- 2장: INFLATION ↑ → ECONOMIC PRESSURE → ON THE ROPES / 물가 상승이 이어지며 영국 경제가 성장 둔화와 소비 위축을 동시에 겪고 있다는 기사 / 비유: 링 위에서 로프에 기대 겨우 서 있는 복서
- 3장: 직역 로프 위에 있는 / 실제 궁지에 몰린, 거의 무너지기 직전인 / 뉘앙스: 이미 큰 타격을 입고 겨우 버티는 상태. 아직 쓰러진 건 아니라서 회복 여지를 남김 / 유래: 복싱에서 온 표현으로 알려져 있음(단정 안 함) / 주어: the economy · the company · the champion
- 4장: WORK "After losing two big clients, the agency is on the ropes." / REAL LIFE "Three straight losses — our team is on the ropes." / 브리지 NEWS The economy is on the ropes. · CONVERSATION We're on the ropes here. · EXAM in serious trouble / in jeopardy
- 6장 표: WHAT 궁지에 몰린, 거의 무너지기 직전인 / REMEMBER 로프에 기대 버티는 복서 / SIMILAR in serious trouble / OPPOSITE going strong / NEWS USE economy · company · champion / EXAM in serious trouble / in jeopardy

---

## A. 카드 텍스트 → `cards/NEWS_IDIOM_001_card_0n.html` (JSON에서 자동 주입)
배경 이미지 검색어(3장 일러스트용): boxer leaning on ring ropes / empty boxing ring dark / boxing ropes close up
대체텍스트: JSON `alt` 필드, 장마다 `<img alt>`로 삽입됨

## B. 캡션

영국 경제가 로프에 걸렸다?

BBC가 영국 경제를 "on the ropes"라고 썼습니다. 물가 상승이 이어지면서 성장은 둔화하고 소비는 위축되는 상황. 기자는 이걸 한 방 맞고 로프에 기댄 복서에 비유했습니다. (BBC NEWS · Economy)

on the ropes = 궁지에 몰린, 거의 무너지기 직전인
After losing two big clients, the agency is on the ropes.

퀴즈 정답은 A. 몇 번 골랐는지 댓글로 남겨주세요.

#외신영어 #헤드라인영어 #뉴스영어 #영어이디엄 #편입영어 #BBC영어 #영어표현 #영어공부 #뉴스로영어 #ontheropes

## C. 발행 메모
- 권장: 월·수·금 NEWS IDIOM / 07:30 KST
- 시리즈 표기: 우상단 NEWS IDIOM · #001 (색 구분 없음, 4색 고정)
- 2주 모음집: 편입 O (첫 편이므로 #001~#005 묶음의 1번)

## D. DB 레코드 → `data/NEWS_IDIOM_001.json`

## E. 검수 (에이전트1)
① 1장 뜻 미노출 O ② 표현 1개만 O ③ 4장 뉴스 문장 없음 O ④ 예문 뜻 범위 안 O ⑤ 정답 6장에만 O ⑥ 글자 수(1장 13자·2장 41자·3장 뉘앙스 42자·4장 예문 각 60자 이내·5장 14자) O ⑦ Exam 환언 포함 O

---

## 디자인 QA (자체, 렌더링 검증 완료)
① 여백·헤더·푸터 6장 동일 O ② 커버에 뜻 없음 O ③ 5장 정답 없음 O ④ red 카드당 1회 이하 O(3장 편집자 마크 1회) ⑤ 이모지 카드당 1개 이하 O(1·6장) ⑥ 최소 글자 크기 O(본문 한국어 최소 36px — 3장 뉘앙스·6장 표는 규격 42px 미달, 아래 보고) ⑦ 넘침 없음 O(자동 검사 통과) ⑧ 6장 표 각 칸 2줄 이내 O

## 넘침·미확정 보고
- 3장 NUANCE 36px, 유래 31px, 6장 표 36px — 규격(한국어 42px)보다 작음. 42px로 올리면 3장·6장 세로 넘침. 규격 유지하려면 3장 유래를 캡션으로 내리거나 6장 표를 4칸(WHAT·SIMILAR·OPPOSITE·EXAM)으로 줄여야 함. 결정 필요.
- 3장 일러스트 슬롯: 파일 없음 → 사전 박스 전폭 폴백 적용. 박스 아래 빈 영역이 일러스트 자리.
- 헤드라인은 샘플. 실제 발행 시 실제 기사 헤드라인으로 교체.
