import asyncio
import pandas as pd
from playwright.async_api import async_playwright

BASE_URL = "https://xn--pckua2a7gp15o89zb.com"
SEARCH_PATH = "/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9E%E3%83%BC%E3%81%AE%E4%BB%95%E4%BA%8B-%E6%9D%B1%E4%BA%AC%E9%83%BD?e=1"

all_job_data = []


async def extract_job_details(page, url):
    try:
        await page.goto(url, timeout=60000)

        async def get_text(selector):
            locator = page.locator(selector)
            try:
                if await locator.count() > 0:
                    content = await locator.text_content()
                    return content.strip() if content else ""
                else:
                    return ""
            except Exception:
                return ""

        return {
            "求人タイトル": await get_text("p.p-detail_head_title"),
            "企業名": await get_text("p.p-detail_head_company"),
            "所在地": await get_text("li.p-detail_summary.p-detail_summary-area.c-icon--U2"),
            "給与": await get_text("li.p-detail_summary.p-detail_summary-pay.c-icon--V2"),
            "雇用形態": await get_text("li.p-detail_tag.p-detail_tag-employType"),
        }

    except Exception as e:
        print(f"エラー: {e}（URL: {url}）")
        return None


async def scrape_page(page, url):
    await page.goto(url)
    await page.wait_for_selector('[data-target-focus]')

    job_ids = await page.locator('[data-target-focus]').evaluate_all(
        """(elements) => {
            return elements
                .map(el => el.getAttribute('data-target-focus'))
                .filter(id => id);
        }"""
    )

    detail_urls = [f"{BASE_URL}/jb/{job_id}" for job_id in job_ids]
    print(f"✅ スクレイピング対象URL: {url} - 求人数: {len(detail_urls)}")

    for detail_url in detail_urls:
        job_info = await extract_job_details(page, detail_url)
        if job_info:
            all_job_data.append(job_info)


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for page_num in range(1, 3):  # 1ページ目と2ページ目
            full_url = f"{BASE_URL}{SEARCH_PATH}&pg={page_num}"
            await scrape_page(page, full_url)

        await browser.close()

    df = pd.DataFrame(all_job_data)
    df.to_excel("求人情報一覧.xlsx", index=False)
    print("📁 Excelに保存完了: 求人情報一覧.xlsx")

if __name__ == "__main__":
    asyncio.run(main())
