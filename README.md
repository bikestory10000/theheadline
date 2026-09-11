# THE HEADLINE 카드 파이프라인 (v7)

## 구조
data/            JSON 1건 = 게시물 1편 (kind: idiom | grammar)
theme.py         공통 디자인 토큰 (dict_v1 다크 시스템) — 여기만 바꾸면 전 시리즈 반영
build_v6_idiom.py    JSON → 7장  (NEWS IDIOM · KOREA IN ENGLISH · COLLOCATION · TRAP)
build_v6_grammar.py  JSON → 5장  (HEADLINE GRAMMAR)
build_v6_weekly.py   JSON 5건 → 2장 (WEEKLY FIVE + QUIZ)
render.py        cards/*.html → png/*.png + 넘침 검사 + 시리즈별 미리보기
cards/, png/     산출물

## 실행
python3 build_v6_idiom.py data/NEWS_IDIOM_001.json
python3 build_v6_grammar.py data/HEADLINE_GRAMMAR_001.json
python3 build_v6_weekly.py W37 data/NEWS_IDIOM_00[1-5].json   # 정답은 stdout(캡션용)
python3 render.py

## 주간 편성
월~토  NEWS WORD (이디엄, 7장)
일     WEEKLY (그 주 월~토 6건 정리 + 복습 퀴즈, 2장)
GRAMMAR/VERB BANK 등은 보류 — data/HEADLINE_GRAMMAR_001.json은 큐에서 제외된 채 보관

## 주의
- 발행 전 헤드라인은 실제 기사로 교체 (지금 값은 샘플). #002~#005는 WEEKLY 시연용 스텁.
- cover_photo는 무료 라이선스 이미지로 교체. 언론사 사진·로고 금지.
- 6장에 해시태그 넣지 않음(COLLECTION 줄). 해시태그는 캡션에만.

## v7 디자인 규칙 (theme.py)
- 배경 #0F1117 통일 + 핵심 요소 뒤 시리즈색 글로우 9%
- 투명도: w40 헤더 전용 / w60 보조 / w70 라벨·칩 / w95 본문
- 박스: border w30 + bg w06, radius 24
- 색 역할: --acc(시리즈색) = 오늘의 주인공 / --gold = EXAM·정답 / 나머지 흰색
- 시리즈색: IDIOM 라임 · GRAMMAR 골드 · WEEKLY 민트 · VERB 블루 · TRAP 코랄
- 커버: 사진 상단 58% + 하단 패널 42%. 사진은 visual_metaphor 기반(cover_photo)
- 폰트 최소: 영어 예문 34 / 번역 28 / 라벨 22 / 칩 26 / 표 값 34 / 보기 36
