from playwright.sync_api import sync_playwright
import time

def test_page_title():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        page.goto("https://playwright.dev/")
        
        time.sleep(2)
        
        title = page.title()
                
        assert title == "Fast and reliable end-to-end testing for modern web apps | Playwright"

        browser.close()

if __name__ == "__main__":
    test_page_title()
