import pytest
from playwright.sync_api import Page
from pytest_performancetotal.performance import Performance

@pytest.mark.parametrize("iteration", [1, 2, 3])
def test_has_title(page: Page, performancetotal: Performance, iteration):
    print(f"iteration: {iteration}")
    page.goto("https://saucelabs.com/")
    
    performancetotal.sample_start("Playwright")
    page.goto("https://playwright.dev/")
    performancetotal.sample_end("Playwright")
    
    performancetotal.sample_start("Webdriverio")
    page.goto("https://webdriver.io/")
    performancetotal.sample_end("Webdriverio")

   