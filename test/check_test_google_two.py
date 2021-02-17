from pytest import mark
from pages.google_home_page import GoogleHomePage
from config.config import Config
import logging
import utilities.custom_logger as cl


class GoogleSecondTests:
    log = cl.customLogger(logging.DEBUG)

    @mark.GoogleSecondTest
    @mark.Google
    def test_two(self, driver, config: Config):
        google_page = GoogleHomePage(driver, domain=config.url)
        google_page.google_search_text.highlight()
        google_page.google_search_text.is_displayed()
        google_page.search.set_value(config.google_search_text)
        google_page.search_result.is_displayed()
        google_page.search_result.click()
        google_page.google_search_one.is_displayed()
        google_page.google_search_one.scroll_to()
        if google_page.google_search_one.get_attribute('href') is None:
            elements = google_page.find_elements("div#rso > div")
            for ls in elements:
                miw_link = ls.find_element("link[rel='prerender']").get_attribute('href')
                print(miw_link)
                assert miw_link == 'https://miwtech.com/'
                self.log.info("Second test case pass")
                break
        else:
            self.log.info("Test case Failed, MIW link is not first in the google search")



