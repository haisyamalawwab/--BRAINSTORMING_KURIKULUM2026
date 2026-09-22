import asyncio
from playwright.async_api import async_playwright

USER_DATA_DIR = r"C:\Users\admin\AppData\Local\Google\Chrome\User Data"

async def test():
    print("Launching Playwright with Chrome channel and Profile 2...")
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            channel="chrome",
            headless=False,
            args=["--profile-directory=Profile 2"],
            no_viewport=True
        )
        print("Playwright launched persistent context successfully!")
        page = context.pages[0] if context.pages else await context.new_page()
        await page.goto("https://siakad.widyagama.ac.id/siakad/list_mkkurikulum/MjAyNi81OTIwMQ")
        print("Current URL:", page.url)
        print("Page Title:", await page.title())
        await asyncio.sleep(5)
        await context.close()
        print("Closed context cleanly.")

if __name__ == "__main__":
    asyncio.run(test())
