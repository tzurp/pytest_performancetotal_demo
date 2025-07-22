import pytest
from playwright.sync_api import Page
from pytest_performancetotal.performance import Performance
from pytest_cleanuptotal.cleanup import Cleanup

@pytest.mark.parametrize("iteration", [1, 2, 3])
def test_has_title(page: Page, performancetotal: Performance, cleanuptotal: Cleanup, iteration):
    print(f"iteration: {iteration}")
    page.goto("https://saucelabs.com/")
    cleanuptotal.add_cleanup(lambda: print("Cleanup after saucelabs"))
    
    performancetotal.sample_start("Playwright")
    page.goto("https://playwright.dev/")
    cleanuptotal.add_cleanup(lambda: print("Cleanup after playwright"))
    performancetotal.sample_end("Playwright")
        
    performancetotal.sample_start("Webdriverio")
    page.goto("https://webdriver.io/")
    cleanuptotal.add_cleanup(lambda: print("Cleanup after webdriverio"))
    performancetotal.sample_end("Webdriverio")

   