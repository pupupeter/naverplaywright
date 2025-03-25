from playwright.sync_api import sync_playwright
import os
import time
import random
from dotenv import load_dotenv

# 讀取 .env 檔案
load_dotenv()
LINE_EMAIL = os.getenv("LINE_EMAIL")
LINE_PASSWORD = os.getenv("LINE_PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)  # 降低速度模仿真人
    context = browser.new_context()
    page = context.new_page()

    print("啟動瀏覽器，開始登入 Naver...")

    # 進入 Naver 登入頁面
    page.goto("https://nid.naver.com/nidlogin.login")
    page.wait_for_timeout(3000)

    # 點擊「使用 Line 登入」按鈕
    line_login_button = page.locator("a.sns_item:has-text('Line')")
    line_login_button.click()
    print("點擊 Line 登入")

    # 等待跳轉到 Line 登入頁面
    page.wait_for_url("https://access.line.me/oauth2/v2.1/login*", timeout=10000)
    print("進入 Line 登入頁面")

    # 模仿人類輸入帳號
    email_input = page.locator("input[name='tid']")
    email_input.click()
    page.wait_for_timeout(random.randint(500, 1500))  # 隨機等待 0.5~1.5 秒
    page.keyboard.type(LINE_EMAIL, delay=random.randint(50, 150))  # 模仿手打
    print("填入 Line 帳號")

    # 模仿人類輸入密碼
    password_input = page.locator("input[name='tpasswd']")
    password_input.click()
    page.wait_for_timeout(random.randint(500, 1500))
    page.keyboard.type(LINE_PASSWORD, delay=random.randint(50, 150))
    print("填入 Line 密碼")

    # 隨機移動滑鼠後，點擊登入按鈕
    login_button = page.locator("button:has-text('登入')")
    page.mouse.move(random.randint(100, 500), random.randint(200, 600))
    page.wait_for_timeout(random.randint(500, 1500))
    login_button.click()
    print("點擊登入")

    # 等待登入完成
    page.wait_for_timeout(5000)

    # 檢查是否需要額外驗證
    if "access.line.me/oauth2" in page.url:
        input("請手動完成驗證，然後按 Enter 繼續...")

    # 確保回到 Naver
    page.wait_for_url("https://nid.naver.com/*", timeout=10000)
    print("Line 登入成功，跳轉回 Naver")

    # 進入 Naver Blog
    page.goto("https://blog.naver.com/")
    page.wait_for_timeout(3000)
    print("進入 Naver Blog 首頁")

    # 在搜尋框中輸入 "peter-0512"
    search_input = page.locator('input[name="sectionBlogQuery"]')
    search_input.click()
    page.keyboard.type("peter-0512", delay=random.randint(100, 200))
    print("在搜尋框中輸入 'peter-0512'")

    # 按下 Enter 鍵進行搜尋
    page.keyboard.press("Enter")
    print("按下 Enter 鍵進行搜尋")

    # 等待搜尋結果加載
    page.wait_for_timeout(3000)

    # 點擊 "블로그" 類別
    blog_category = page.locator('span.category_name:has-text("블로그")')
    blog_category.click()
    print("點擊 '블로그' 類別")

    # 等待分類頁面加載
    page.wait_for_timeout(3000)

    # 點擊 <em class="name_author">peter-0512</em> 元素
    search_keyword = page.locator('em.name_author:has-text("peter-0512")')
    search_keyword.wait_for(state='visible', timeout=5000)  # 等待元素可見
    print("等待 'peter-0512' 元素可點擊")

    search_keyword.click()
    print("點擊 'peter-0512'")

    # 等待頁面加載完成
    page.wait_for_load_state('load')  # 等待頁面加載完成

    # 確認頁面是否已加載
    print("進入 'peter-0512' 的頁面")

    # 在這裡等待 50 秒
    print("等待 50 秒後關閉瀏覽器...")
    page.wait_for_timeout(50000)  # 等待 50 秒

    page.screenshot(path="naver_blog_category.png")

    # 關閉瀏覽器
    browser.close()
    print("瀏覽器已關閉")
