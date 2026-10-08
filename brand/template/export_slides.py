import asyncio,sys
from pathlib import Path
from playwright.async_api import async_playwright
out=Path(sys.argv[2]);out.mkdir(exist_ok=True,parents=True)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":420,"height":525},device_scale_factor=float(sys.argv[3]))
        await pg.set_content(Path(sys.argv[1]).read_text(encoding="utf-8"),wait_until="networkidle")
        await pg.wait_for_timeout(3000)
        await pg.evaluate("""()=>{document.querySelectorAll('.ig-header,.ig-dots,.ig-actions,.ig-caption').forEach(e=>e.style.display='none');
        document.querySelector('.ig-frame').style.cssText='width:420px;height:525px;max-width:none;border-radius:0;box-shadow:none;overflow:hidden;margin:0;';
        document.querySelector('.carousel-viewport').style.cssText='width:420px;height:525px;aspect-ratio:unset;overflow:hidden;';
        document.body.style.cssText='padding:0;margin:0;display:block;overflow:hidden;';}""")
        for i in range(int(sys.argv[4]) if len(sys.argv)>4 else 7):
            await pg.evaluate("(i)=>{const t=document.querySelector('.carousel-track');t.style.transition='none';t.style.transform='translateX('+(-i*420)+'px)';}",i)
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=str(out/f"slide_{i+1}.png"),clip={"x":0,"y":0,"width":420,"height":525})
        await b.close()
asyncio.run(main())
