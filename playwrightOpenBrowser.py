from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    firefox = playwright.firefox
    browser = firefox.launch(headless= False)
    page = browser.new_page()
    page.goto("https://google.com")
    print(page.title())
    print(page.url)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)