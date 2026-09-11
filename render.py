#!/usr/bin/env python3
import asyncio, pathlib, sys, glob
from playwright.async_api import async_playwright
from PIL import Image

CARDS = sorted(glob.glob("cards/*_card_0?.html"))
OUT = pathlib.Path("png"); OUT.mkdir(exist_ok=True)

OVERFLOW_JS = """
() => {
  const bad = [];
  document.querySelectorAll('.si *, .cover *').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0 || el.classList.contains('bleed') || el.classList.contains('tape')) return;
    if (r.right > 1080 - 60 || r.bottom > 1350 - 110)
      bad.push(el.tagName + ' "' + (el.innerText||'').slice(0,30) + '" r=' + Math.round(r.right) + ' b=' + Math.round(r.bottom));
    if (el.scrollWidth > el.clientWidth + 2 && getComputedStyle(el).overflow !== 'visible')
      bad.push('SCROLL ' + el.tagName + ' "' + (el.innerText||'').slice(0,30) + '"');
  });
  const si = document.querySelector('.si');
  if (si && si.scrollHeight > si.clientHeight + 2) bad.push('SI overflow by ' + (si.scrollHeight - si.clientHeight) + 'px');
  return bad;
}
"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(viewport={"width":1080,"height":1350}, device_scale_factor=1, ignore_https_errors=True)
        pg = await ctx.new_page()
        pngs = []
        for f in CARDS:
            await pg.goto("file://" + str(pathlib.Path(f).resolve()))
            await pg.wait_for_timeout(300)
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(1500)
            issues = await pg.evaluate(OVERFLOW_JS)
            out = OUT / (pathlib.Path(f).stem + ".png")
            await pg.screenshot(path=str(out), clip={"x":0,"y":0,"width":1080,"height":1350})
            pngs.append(out)
            print(f"{out.name}: {'OK' if not issues else 'OVERFLOW ' + '; '.join(issues)}")
        await b.close()
    # 시리즈별 미리보기 스트립
    from itertools import groupby
    key = lambda p: p.stem.rsplit("_card_",1)[0]
    for k, grp in groupby(sorted(pngs, key=lambda p: p.stem), key):
        ims = [Image.open(p) for p in grp]
        if len(ims) > 10: print(f"⚠ {k}: {len(ims)}장 — API 캐러셀 상한 10장 초과")
        w = 360; h = 450; gap = 16
        strip = Image.new("RGB", (len(ims)*w + (len(ims)-1)*gap, h), "#1A1A1A")
        for i, im in enumerate(ims):
            strip.paste(im.resize((w,h), Image.LANCZOS), (i*(w+gap), 0))
        strip.save(OUT / f"preview_{k}.png"); print("preview:", OUT / f"preview_{k}.png")

asyncio.run(main())
