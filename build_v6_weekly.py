#!/usr/bin/env python3
"""WEEKLY FIVE: 이디엄 JSON 5건 → 2장 (v7 테마, 민트). 사용: python3 build_v6_weekly.py W37 data/NEWS_IDIOM_00[1-5].json"""
import json, sys, pathlib
from theme import shell, e
a = sys.argv[1] if len(sys.argv) > 1 else "W37"
if a.endswith(".json"):   # 주간 JSON 1건: {"week": "W38", "items": [...]}
    W = json.loads(pathlib.Path(a).read_text(encoding="utf-8")); week = W["week"]; files = W["items"]
else:
    week = a; files = sys.argv[2:] or sorted(pathlib.Path("data").glob("NEWS_WORD_00*.json"))[1:6]
items = [json.loads(pathlib.Path(f).read_text(encoding="utf-8")) for f in files]
OUT = pathlib.Path("cards"); OUT.mkdir(exist_ok=True)
def ans(d): return d['quiz_options']['ABCD'.index(d['quiz_answer'])]

rows = "".join(f"""<div class="box" style="display:grid;grid-template-columns:100px 1fr 1fr;gap:20px;align-items:center;padding:{12 if len(items)>5 else 14}px 26px">
  <div style="font-size:24px;color:var(--w60);font-weight:700">{e(d['number'])}</div>
  <div><div class="gw acc" style="font-size:38px">{e(d['expression'])}</div><div style="font-size:28px;color:var(--w95);margin-top:4px">{e(d['meaning_ko'])}</div></div>
  <div style="font-size:26px;color:var(--w95);line-height:1.4"><span class="lbl goldc" style="font-size:20px">EXAM</span><br>{e(d['bridge_exam'])}</div>
</div>""" for d in items)
c1 = f"""
<div class="si" style="padding-top:100px;padding-bottom:64px">
  <div class="chip">WEEKLY · {e(week)}</div>
  <div class="gw" style="font-size:56px;line-height:1.25;margin-bottom:8px">이번 주 표현 {len(items)}개, 한 장으로</div>
  <div style="font-size:28px;color:var(--w60);margin-bottom:22px">놓친 편이 있어도 이 장만 저장하면 따라잡습니다.</div>
  <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:22px">{rows}</div>
  <div class="cta"><p>다음 장에서 {len(items)}문항 복습<small>정답은 캡션에</small></p></div>
</div>
"""
qs = "".join(f"""<div class="box" style="padding:14px 26px;display:flex;gap:18px;align-items:flex-start">
  <span class="circ" style="width:54px;height:54px;font-size:24px">{i+1}</span>
  <div><div class="gw" style="font-size:32px;line-height:1.3">“{e(d['quiz_ko'])}”</div>
    <div class="ex-en" style="font-size:29px;font-style:normal;color:var(--w70);margin-top:8px">{e(d['quiz_en_blank']).replace('________', "<span style='display:inline-block;width:7ch;border-bottom:3px solid var(--acc);vertical-align:-.1em'></span>")}</div></div></div>""" for i, d in enumerate(items))
hints = " · ".join(e(d['meaning_ko']) for d in items)
c2 = f"""
<div class="si" style="padding-top:100px;padding-bottom:64px">
  <div class="chip">WEEKLY QUIZ · {e(week)}</div>
  <div class="gw" style="font-size:52px;line-height:1.25;margin-bottom:22px">빈칸 {len(items)}개, 60초 안에</div>
  <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:22px">{qs}</div>
  <div class="memo" style="font-size:26px;color:var(--w70)"><span class="lbl">HINT · 뜻만</span><br>{hints}</div>
</div>
"""
alts = {1: f"주간 치트시트 {week}. 표현과 뜻, 시험 환언", 2: f"주간 복습 퀴즈 {week}. 빈칸 문항"}
for n, body, glow in [(1, c1, (300,260)), (2, c2, (540,300))]:
    p = OUT / f"WEEKLY_{week}_card_0{n}.html"
    p.write_text(shell(n, 2, body, alts[n], "weekly", f"WEEKLY_{week}", glow), encoding="utf-8"); print("wrote", p)
print("CAPTION ANSWERS:", " / ".join(f"{i+1}. {ans(d)}" for i, d in enumerate(items)))
