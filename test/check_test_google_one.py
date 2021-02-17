from pytest import mark
from pages.google_home_page import GoogleHomePage
from config.config import Config
import logging
import utilities.custom_logger as cl


class GoogleFirstTests:
    log = cl.customLogger(logging.DEBUG)

    @mark.GoogleFirstTest
    @mark.Google
    def test_one(self, driver, config: Config):
        google_page = GoogleHomePage(driver, domain=config.url)
        if google_page.google_search_text.is_displayed() is True:
            google_page.google_search_text.highlight()
            self.log.info("Google page loaded - Test Case Pass")
        else:
            self.log.info("Google page is not loading - Test Case Fail")
