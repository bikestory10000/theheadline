#!/usr/bin/env python3
"""JSON 1건 → card_01~07.html (v7: 커버 상단 사진/하단 패널 · 색 역할 3개 · 글로우 · 폰트 상향)"""
import json, sys, pathlib, re
from theme import shell as _shell, e

SRC = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "data/NEWS_IDIOM_001.json")
OUT = pathlib.Path("cards"); OUT.mkdir(exist_ok=True)
D = json.loads(SRC.read_text(encoding="utf-8"))
TOTAL = 7
def sh(n, body, glow=None): return _shell(n, TOTAL, body, D["alt"][str(n)], "idiom", D["id"], glow)
def u(en): return re.sub(re.escape(D['expression']), f"<u>{e(D['expression'])}</u>", e(en), flags=re.I)
def acc_in(text, part): return e(text).replace(e(part), f'<span class="acc">{e(part)}</span>')
L = len(D['expression'])
COVER_PX = 190 if L <= 10 else 150 if L <= 14 else 122   # 표현 길이별 자동 축소
WORD_PX  = 122 if L <= 12 else 100 if L <= 16 else 84
MEAN_PX  = 54 if len(D['meaning_ko']) <= 18 else 46

# ---------------- 01 COVER : 사진 있으면 58/42, 없으면 타이포 전용 ----------------
if D.get('cover_photo'):
    c1 = f"""
<div style="position:absolute;left:0;top:0;width:1080px;height:783px;background:url('{D['cover_photo']}') center/cover"></div>
<div style="position:absolute;left:0;top:560px;width:1080px;height:223px;background:linear-gradient(to bottom,transparent,#0F1117)"></div>
<div style="position:absolute;left:0;top:783px;width:1080px;height:567px;padding:36px 63px 60px;display:flex;flex-direction:column;justify-content:center">
  <div style="display:flex;align-items:center;gap:18px;margin-bottom:26px">
    <span class="chip" style="margin:0">{e(D['series'])} {e(D['number'])}</span>
    <span style="font-size:26px;color:var(--w70);letter-spacing:.06em">{e(D['source'])} · {e(D['section'])}</span></div>
  <div class="gw" style="font-size:84px;line-height:1.2;margin-bottom:22px">{acc_in(D['headline'], D['expression'])}</div>
  <div class="gw" style="font-size:48px;line-height:1.35;color:var(--w95);margin-bottom:30px">{acc_in(D['hook_ko'], D['hook_hl'])}</div>
  <div style="display:flex;flex-wrap:wrap;gap:12px">{''.join(f'<span class="htag">{e(t)}</span>' for t in D['tags'])}</div>
</div>
"""
    glow1 = None
else:
    c1 = f"""
<div class="si" style="padding:150px 63px 110px;justify-content:space-between">
  <div>
    <div style="display:flex;align-items:center;gap:18px;margin-bottom:34px">
      <span class="chip" style="margin:0">{e(D['series'])} {e(D['number'])}</span>
      <span style="font-size:26px;color:var(--w70);letter-spacing:.06em">{e(D['source'])} · {e(D['section'])}</span></div>
    <div class="gw" style="font-size:62px;line-height:1.3;color:var(--w70)">{acc_in(D['headline'], D['expression'])}</div>
  </div>
  <div style="text-align:center">
    <div style="font-size:150px;line-height:1;margin-bottom:10px">{D['emoji']}</div>
    <div class="gw acc" style="font-size:{COVER_PX}px;line-height:1.02;letter-spacing:-.01em">{e(D['expression'])}</div>
  </div>
  <div>
    <div class="gw" style="font-size:52px;line-height:1.35;color:var(--w95);margin-bottom:26px">{acc_in(D['hook_ko'], D['hook_hl'])}</div>
    <div style="display:flex;flex-wrap:wrap;gap:12px">{''.join(f'<span class="htag">{e(t)}</span>' for t in D['tags'])}</div>
  </div>
</div>
"""
    glow1 = (540, 620)

# ---------------- 02 CONTEXT : 세로 3단 체인 ----------------
steps = ""
for i, k in enumerate(D['chain']):
    last = i == len(D['chain'])-1
    steps += f"""<div class="box gw" style="height:96px;display:flex;align-items:center;justify-content:center;font-size:38px;letter-spacing:.02em;
      {'background:var(--acc);color:#0F1117;border-color:var(--acc);font-weight:700' if last else ''}">{e(k)}</div>"""
    if not last: steps += '<div style="text-align:center;font-size:40px;line-height:1;color:var(--w70);margin:10px 0">↓</div>'
c2 = f"""
<div class="si">
  <div class="chip">WHAT HAPPENED?</div>
  <div class="gw" style="font-size:60px;line-height:1.3;margin-bottom:30px">{e(D['headline']).replace(e(D['expression']), f'<u style="text-decoration-color:var(--acc);text-underline-offset:10px;text-decoration-thickness:4px">{e(D["expression"])}</u>')}</div>
  <div style="font-size:33px;color:var(--w95);line-height:1.7;margin-bottom:40px">{e(D['news_summary_ko'])}</div>
  <div style="margin-bottom:34px">{steps}</div>
  <div class="memo" style="font-size:30px;color:var(--w70)">한 줄로 = <b style="color:var(--w95)">{e(D['metaphor_ko'])}</b></div>
</div>
"""

# ---------------- 03 EXPRESSION : 로프 이중선 + 이모지 + EXAM 골드 ----------------
rope = 'height:0;border-top:3px solid var(--acc);border-bottom:3px solid var(--acc);padding-top:12px'
c3 = f"""
<div class="si">
  <div class="chip">THE EXPRESSION</div>
  <div style="{rope};margin-bottom:26px"></div>
  <div style="display:flex;align-items:center;justify-content:space-between">
    <div class="gw acc" style="font-size:{WORD_PX}px;line-height:1">{e(D['expression'])}</div>
    <div style="font-size:96px;line-height:1">{D['emoji']}</div></div>
  <div style="{rope};margin-top:26px;margin-bottom:26px"></div>
  <div style="display:flex;gap:18px;font-size:28px;color:var(--w60);margin-bottom:22px"><span style="font-family:var(--ni)">{e(D['ipa'])}</span><span>·</span><span>{e(D['pron_kr'])}</span></div>
  <div class="gw" style="font-size:{MEAN_PX}px;margin-bottom:14px;line-height:1.3">{e(D['meaning_ko'])}</div>
  <div style="font-size:28px;color:var(--w60);margin-bottom:30px"><b style="color:var(--w70)">직역</b> {e(D['formula'])} → {e(D['literal_ko'])}</div>
  <div class="memo" style="margin-bottom:26px"><div style="color:var(--w95)">{e(D['nuance_ko'])}</div>
    <div style="font-size:28px;color:var(--w60);font-style:italic;margin-top:12px"><span class="lbl" style="font-style:normal;font-size:20px;color:var(--w60)">ORIGIN</span> &nbsp;{e(D['origin_ko'])}</div></div>
  <div class="box" style="padding:22px 30px;border-color:var(--gold);background:rgba(255,215,100,.08);font-size:30px;line-height:1.55"><b class="goldc" style="letter-spacing:.08em">EXAM</b> &nbsp;{e(D['exam_line'])}</div>
</div>
"""

# ---------------- 04 USE IT ----------------
def pc(tag, en, ko):
    return f"""<div class="box" style="padding:30px 36px"><div class="lbl" style="margin-bottom:12px">{tag}</div>
      <div class="ex-en">{u(en)}</div><div class="ex-ko">{e(ko)}</div></div>"""
c4 = f"""
<div class="si">
  <div class="chip">SPEAK IT · NEWS → REAL LIFE</div>
  <div style="display:flex;flex-direction:column;gap:22px;margin-bottom:40px">
    {pc('01 · WORK', D['example_work_en'], D['example_work_ko'])}
    {pc('02 · REAL LIFE', D['example_daily_en'], D['example_daily_ko'])}
  </div>
  <div class="lbl" style="margin-bottom:14px">BRIDGE · 뉴스 → 회화 → 시험</div>
  <div style="display:grid;grid-template-columns:230px 1fr;font-size:30px;line-height:1.5;border-top:1px solid var(--w30)">
    <span class="lbl" style="font-size:24px;padding:16px 0;border-bottom:1px solid var(--w30)">NEWS</span><span style="padding:16px 0;border-bottom:1px solid var(--w30);font-family:var(--ni)">{e(D['bridge_news'])}</span>
    <span class="lbl" style="font-size:24px;padding:16px 0;border-bottom:1px solid var(--w30)">TALK</span><span style="padding:16px 0;border-bottom:1px solid var(--w30);font-family:var(--ni)">{e(D['bridge_conversation'])}</span>
    <span class="lbl goldc" style="font-size:24px;padding:16px 12px;background:rgba(255,215,100,.12)">EXAM</span><span class="goldc" style="padding:16px 12px;background:rgba(255,215,100,.12);font-weight:700;font-family:var(--ni)">{e(D['bridge_exam'])}</span>
  </div>
</div>
"""

# ---------------- 05 QUIZ ----------------
blank = e(D['quiz_en_blank']).replace("________", "<span style='display:inline-block;width:8ch;border-bottom:4px solid var(--acc);vertical-align:-.1em'></span>")
opts = "".join(f"""<div class="box" style="height:100px;display:flex;align-items:center;gap:26px;padding:0 30px">
  <span class="circ">{'ABCD'[i]}</span><span class="gw" style="font-size:36px">{e(o)}</span></div>""" for i, o in enumerate(D['quiz_options']))
c5 = f"""
<div class="si">
  <div class="chip">CAN YOU USE IT?</div>
  <div class="gw" style="font-size:52px;line-height:1.35;margin-bottom:10px">“{e(D['quiz_ko'])}”</div>
  <div style="font-size:26px;color:var(--w60);margin-bottom:22px">영어로 하면?</div>
  <div class="ex-en" style="font-size:56px;font-style:normal;line-height:1.3;margin-bottom:40px">{blank}</div>
  <div style="display:flex;flex-direction:column;gap:16px;margin-bottom:36px">{opts}</div>
  <div class="acc" style="font-size:30px;font-weight:700;letter-spacing:.08em;text-align:center">ANSWER → NEXT ⟶</div>
</div>
"""

# ---------------- 06 SAVE ----------------
cells = [("WHAT", D['meaning_ko'], "acc"), ("REMEMBER", D['remember_ko'], ""), ("SIMILAR", D['synonym'], ""),
         ("OPPOSITE", D['antonym'], ""), ("NEWS USE", " · ".join(D['common_subjects']), ""), ("EXAM", D['bridge_exam'], "goldc")]
grid = "".join(f"""<div class="box" style="height:150px;padding:20px 26px;display:flex;flex-direction:column;justify-content:center;{'border-color:var(--gold)' if c=='goldc' else ''}">
  <div class="lbl" style="font-size:20px;margin-bottom:8px;{'color:var(--gold)' if c=='goldc' else ''}">{k}</div>
  <div class="gw {c}" style="font-size:34px;line-height:1.25">{e(v)}</div></div>""" for k, v, c in cells)
coll = "".join(f'<span class="htag {"on" if c.startswith(D["number"]) else ""}">{e(c)}</span>' for c in D['collection'])
c6 = f"""
<div class="si" style="padding-top:110px;padding-bottom:80px">
  <div style="font-size:24px;color:var(--w70);letter-spacing:.08em;margin-bottom:12px">TODAY'S EXPRESSION · ANSWER <b class="goldc">{e(D['quiz_answer'])}</b></div>
  <div class="gw acc" style="font-size:78px;line-height:1.1;margin-bottom:28px">{e(D['expression'])}<span style="font-family:var(--ns);font-size:56px;margin-left:16px">{D['emoji']}</span></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:28px">{grid}</div>
  <div class="cta" style="margin-bottom:24px"><p>저장해두면 다음 외신에서 바로 보입니다<small>전체 목록은 프로필 고정 게시물</small></p></div>
  <div class="lbl" style="margin-bottom:12px">COLLECTION · 모아두면 단어장</div>
  <div style="display:flex;flex-wrap:wrap;gap:10px">{coll}</div>
</div>
"""

# ---------------- 07 THE OTHER THREE ----------------
drows = "".join(f"""<div class="box" style="min-height:200px;padding:26px 34px 26px 40px;position:relative;display:flex;flex-direction:column;justify-content:center">
   <div style="position:absolute;left:0;top:26px;bottom:26px;width:4px;background:var(--w40);border-radius:2px"></div>
   <div class="gw" style="font-size:42px;margin-bottom:6px">{e(x['expr'])}</div>
   <div class="gw" style="font-size:34px;color:var(--w70);margin-bottom:10px">{e(x['ko'])}</div>
   <div class="ex-en" style="font-size:30px;color:var(--w70)">{e(x['en'])}</div></div>""" for x in D['distractor_meanings'])
c7 = f"""
<div class="si" style="padding-top:110px;padding-bottom:90px">
  <div class="chip" style="background:var(--w06);color:var(--w70)">THE OTHER THREE · 오답도 이디엄</div>
  <div class="gw" style="font-size:52px;line-height:1.3;margin-bottom:8px">퀴즈 보기 셋, 버리지 마세요</div>
  <div style="font-size:28px;color:var(--w60);margin-bottom:30px">전부 외신에 자주 나오는 표현. 오늘 한 번에 4개.</div>
  <div style="display:flex;flex-direction:column;gap:16px;margin-bottom:30px">{drows}</div>
  <div class="memo" style="font-size:30px;color:var(--w70)">메인은 <b class="acc">{e(D['expression'])}</b> 하나. 나머지 셋은 각주로만.</div>
</div>
"""

pages = [(1,c1,glow1),(2,c2,(540,900)),(3,c3,(400,420)),(4,c4,None),(5,c5,(540,420)),(6,c6,(300,260)),(7,c7,None)]
tag = f"{D['series'].replace(' ','_')}_{D['number'].strip('#')}"
for n, body, glow in pages:
    p = OUT / f"{tag}_card_0{n}.html"; p.write_text(sh(n, body, glow), encoding="utf-8"); print("wrote", p)
