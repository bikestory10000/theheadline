#!/usr/bin/env python3
"""HEADLINE GRAMMAR: 규칙 JSON 1건 → 5장 (v7 테마)"""
import json, sys, pathlib
from theme import shell, e
SRC = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "data/HEADLINE_GRAMMAR_001.json")
D = json.loads(SRC.read_text(encoding="utf-8")); OUT = pathlib.Path("cards"); OUT.mkdir(exist_ok=True)
TOTAL = 5
def br(t, col): return e(t).replace("[", f'<u style="text-decoration-color:{col};text-underline-offset:10px;text-decoration-thickness:4px">').replace("]", "</u>")
def sh(n, body, glow=None): return shell(n, TOTAL, body, D['alt'][str(n)], "grammar", D['id'], glow)

c1 = f"""
<div class="si" style="justify-content:flex-end;padding-bottom:130px">
  <div class="chip">{e(D['series'])} {e(D['number'])} · 규칙 하나로 모든 외신</div>
  <div class="gw" style="font-size:60px;line-height:1.3;margin-bottom:30px">{e(D['hook_ko'])}</div>
  <div class="gw acc" style="font-size:118px;line-height:1.05;margin-bottom:14px">{e(D['rule'])}</div>
  <div style="font-size:34px;color:var(--w60);font-family:var(--ni)">{e(D['rule_en'])}</div>
</div>
"""
c2 = f"""
<div class="si">
  <div class="chip">THE RULE</div>
  <div class="gw acc" style="font-size:72px;line-height:1.15;margin-bottom:26px">{e(D['rule'])}</div>
  <div class="memo" style="margin-bottom:34px">{e(D['rule_ko'])}</div>
  <div class="box" style="padding:44px 40px;display:grid;grid-template-columns:1fr 70px 1fr;align-items:center;text-align:center;gap:10px">
    <div><div class="lbl" style="margin-bottom:16px">HEADLINE</div><div class="gw" style="font-size:42px;line-height:1.3">{br(D['demo']['headline'],'var(--acc)')}</div></div>
    <div style="font-size:44px;color:var(--w70)">→</div>
    <div><div class="lbl" style="margin-bottom:16px">NORMAL</div><div class="gw" style="font-size:42px;line-height:1.3">{br(D['demo']['normal'],'var(--acc)')}</div></div>
  </div>
</div>
"""
exs = "".join(f"""<div class="box" style="padding:26px 34px"><div class="lbl" style="color:var(--w60);margin-bottom:10px">{e(x['src'])}</div>
  <div class="gw acc" style="font-size:38px;line-height:1.3">{e(x['hl'])}</div>
  <div class="ex-en" style="font-size:29px;font-style:normal;color:var(--w70);margin-top:10px">= {e(x['full'])}</div></div>""" for x in D['examples'])
c3 = f"""<div class="si"><div class="chip">SEEN IN HEADLINES · 복원해 보기</div><div style="display:flex;flex-direction:column;gap:20px">{exs}</div></div>"""
opts = "".join(f"""<div class="box" style="min-height:100px;display:flex;align-items:center;gap:26px;padding:16px 30px">
  <span class="circ">{'ABCD'[i]}</span><span style="font-size:33px;line-height:1.4">{e(o)}</span></div>""" for i, o in enumerate(D['quiz_options']))
c4 = f"""
<div class="si">
  <div class="chip">CAN YOU READ IT?</div>
  <div class="gw acc" style="font-size:54px;line-height:1.3;margin-bottom:12px">{e(D['quiz_hl'])}</div>
  <div style="font-size:28px;color:var(--w60);margin-bottom:30px">이 헤드라인의 뜻은?</div>
  <div style="display:flex;flex-direction:column;gap:16px;margin-bottom:36px">{opts}</div>
  <div class="acc" style="font-size:30px;font-weight:700;letter-spacing:.08em;text-align:center">ANSWER → NEXT ⟶</div>
</div>
"""
summ = "".join(f'<div class="box" style="display:flex;gap:20px;align-items:center;padding:22px 30px"><span class="acc" style="font-size:32px">✓</span><span class="gw" style="font-size:36px">{e(s)}</span></div>' for s in D['summary'])
coll = "".join(f'<span class="htag {"on" if c.startswith(D["number"]) else ""}">{e(c)}</span>' for c in D['collection'])
c5 = f"""
<div class="si">
  <div style="font-size:24px;color:var(--w70);letter-spacing:.08em;margin-bottom:12px">TODAY'S RULE · ANSWER <b class="goldc">{e(D['quiz_answer'])}</b></div>
  <div class="gw acc" style="font-size:78px;line-height:1.1;margin-bottom:30px">{e(D['rule'])}</div>
  <div style="display:flex;flex-direction:column;gap:14px;margin-bottom:34px">{summ}</div>
  <div class="cta" style="margin-bottom:24px"><p>규칙은 한 번 저장하면 모든 외신에 적용됩니다<small>매주 일요일 · HEADLINE GRAMMAR</small></p></div>
  <div class="lbl" style="margin-bottom:12px">COLLECTION</div><div style="display:flex;flex-wrap:wrap;gap:10px">{coll}</div>
</div>
"""
for n, body, glow in [(1,c1,(540,780)),(2,c2,(540,380)),(3,c3,None),(4,c4,(540,380)),(5,c5,(300,280))]:
    p = OUT / f"{D['id']}_card_0{n}.html"; p.write_text(sh(n, body, glow), encoding="utf-8"); print("wrote", p)
