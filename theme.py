"""공통 디자인 토큰 v7. 여기만 바꾸면 전 시리즈에 반영.
색 역할: --acc(시리즈 식별색) = 오늘의 주인공 / --gold = EXAM·정답 / 나머지 흰색.
IDIOM 라임 · GRAMMAR 골드 · WEEKLY 민트 · VERB 블루 · TRAP 코랄
"""
import html
def e(s): return html.escape(str(s))

SERIES_COLOR = {"idiom": "#C8E86A", "grammar": "#FFD764", "weekly": "#7FDFAA", "verb": "#82C4FF", "trap": "#FFB085"}
BG = "#0F1117"

def css(acc):
    return f"""
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Noto+Sans:ital,wght@0,400;0,700;1,400&family=Playfair+Display:ital,wght@0,500;0,700;0,900;1,700&display=swap" rel="stylesheet">
<style>
@font-face{{font-family:'GangwonEduPower';src:url('https://cdn.jsdelivr.net/gh/fonts-archive/GangwonEduPower/GangwonEduPower.woff2') format('woff2');font-display:swap}}
:root{{--acc:{acc};--gold:#FFD764;--lime:#C8E86A;
  --w95:rgba(255,255,255,.95);--w70:rgba(255,255,255,.70);--w60:rgba(255,255,255,.60);--w40:rgba(255,255,255,.40);--w30:rgba(255,255,255,.30);--w06:rgba(255,255,255,.06);
  --gw:'GangwonEduPower',cursive;--serif:'Playfair Display',Georgia,serif;--ns:'Noto Sans KR','Noto Sans',sans-serif;--ni:'Noto Sans',sans-serif;}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{background:{BG};color:var(--w95);font-family:var(--ns);position:relative;word-break:keep-all}}
.glow{{position:absolute;width:1000px;height:1000px;border-radius:50%;pointer-events:none;
  background:radial-gradient(circle,var(--acc) 0%,transparent 60%);opacity:.09;transform:translate(-50%,-50%)}}
.topbar{{position:absolute;top:40px;left:54px;right:54px;display:flex;justify-content:space-between;align-items:center;z-index:10}}
.snum,.br{{font-size:24px;font-weight:500;color:var(--w40);letter-spacing:.06em}}
.si{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:120px 63px 100px}}
.chip{{display:inline-block;align-self:flex-start;font-size:26px;font-weight:700;letter-spacing:.1em;padding:10px 30px;border-radius:40px;margin-bottom:34px;
  background:color-mix(in srgb,var(--acc) 14%,transparent);color:var(--acc)}}
 .gw{{font-family:var(--gw)}}
.serif{{font-family:var(--serif)}}
.mark{{background:var(--acc);color:#0F1117;padding:0 .1em;border-radius:3px;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
.lbl{{font-size:22px;font-weight:700;letter-spacing:.1em;color:var(--w70)}}
.box{{border:2px solid var(--w30);background:var(--w06);border-radius:24px}}
.acc{{color:var(--acc)}} .goldc{{color:var(--gold)}}
.ex-en{{font-size:34px;color:var(--w95);line-height:1.55;font-family:var(--ni);font-style:italic}}
.ex-en u{{font-style:normal;color:var(--acc);font-weight:700;text-decoration-color:var(--acc);text-underline-offset:7px;text-decoration-thickness:3px}}
.ex-ko{{font-size:28px;color:var(--w60);line-height:1.5;margin-top:10px}}
.memo{{font-size:32px;line-height:1.7;padding:26px 36px;border-left:4px solid var(--w30)}}
.htag{{font-size:23px;color:var(--w60);padding:8px 22px;border-radius:30px;border:1px solid var(--w30);background:var(--w06)}}
.htag.on{{color:var(--acc);border-color:var(--acc)}}
.circ{{width:64px;height:64px;border-radius:50%;border:2px solid var(--w70);color:var(--w95);display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700;flex:none}}
.cta{{background:color-mix(in srgb,var(--acc) 12%,transparent);border:2px solid color-mix(in srgb,var(--acc) 30%,transparent);border-radius:24px;padding:26px 40px;text-align:center}}
.cta p{{font-size:32px;font-weight:700;color:var(--acc);line-height:1.5}}
.cta small{{display:block;font-size:24px;color:var(--w70);font-weight:500;margin-top:6px}}
</style>
"""

def shell(n, total, body, alt, kind="idiom", title="", glow=None):
    g = f'<div class="glow" style="left:{glow[0]}px;top:{glow[1]}px"></div>' if glow else ""
    return f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><title>{e(title)} card {n}</title>{css(SERIES_COLOR[kind])}</head>
<body>{g}
<img alt="{e(alt)}" src="data:image/gif;base64,R0lGODlhAQABAAAAACw=" style="position:absolute;width:1px;height:1px;opacity:0">
{body}
<div class="topbar"><div class="snum">{n} / {total}</div><div class="br">THE HEADLINE · @theheadline.eng</div></div>
</body></html>"""
