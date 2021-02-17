from pytest import mark
from pages.ritchie_home_page import RitchieHomePage
from pages.ritchie_login_page import RitchieLoginPage
from pages.ritchie_advance_search_page import RitchieAdvanceSearchPage
from pages.ritchie_search_result_page import RitchieSearchResultPage
from config.config import Config
import logging
import utilities.custom_logger as cl


class RitchieOneTests:
    log = cl.customLogger(logging.DEBUG)

    @mark.RitchieFirstTest
    @mark.Ritche
    def test_ritchie_one(self, driver, config: Config):
        ritchie_home_page = RitchieHomePage(driver, domain=config.url)
        # Navigate to home page and click on sign in link
        ritchie_home_page.logo.highlight()
        ritchie_home_page.logo.is_displayed()
        ritchie_home_page.sign_in.highlight()
        ritchie_home_page.sign_in.click()
        # Sign in to the site and click on advance search option
        ritchie_login_page = RitchieLoginPage(driver)
        ritchie_login_page.username.is_displayed()
        ritchie_login_page.username.highlight()
        ritchie_login_page.username.set_value(config.username)
        ritchie_login_page.password.highlight()
        ritchie_login_page.password.set_value(config.password)
        ritchie_login_page.sign_in_button.highlight()
        ritchie_login_page.sign_in_button.click()
        ritchie_login_page.login_user.is_displayed()
        ritchie_login_page.login_user.highlight()
        user_id = ritchie_login_page.login_user.get_attribute('innerText')
        assert user_id == 'Hello QA'
        ritchie_login_page.advance_search.is_displayed()
        ritchie_login_page.advance_search.highlight()
        ritchie_login_page.advance_search.click()
        # Fill the search criteria and click on search equipment
        ritchie_search_page = RitchieAdvanceSearchPage(driver)
        ritchie_search_page.keyword.is_displayed()
        ritchie_search_page.keyword.highlight()
        ritchie_search_page.keyword.set_value(config.search_text)
        ritchie_search_page.make.is_displayed()
        ritchie_search_page.make.highlight()
        ritchie_search_page.make.set_value(config.make)
        ritchie_search_page.min_year.is_displayed()
        ritchie_search_page.min_year.highlight()
        ritchie_search_page.min_year.set_value(config.min_year)
        ritchie_search_page.max_year.is_displayed()
        ritchie_search_page.max_year.highlight()
        ritchie_search_page.max_year.set_value(config.max_year)
        ritchie_search_page.search_button.is_displayed()
        ritchie_search_page.search_button.highlight()
        ritchie_search_page.search_button.click()
        # pick the 3rd listing and capture the meter reads, third_listing_details and add to wishlist
        ritchie_result_page = RitchieSearchResultPage(driver)
        ritchie_result_page.search_page_text.is_displayed()
        ritchie_result_page.search_page_text.highlight()
        ritchie_result_page.third_listing.scroll_to()
        ritchie_result_page.third_listing.is_displayed()
        ritchie_result_page.third_listing.highlight()
        ritchie_result_page.third_listing_meter_read.is_displayed()
        ritchie_result_page.third_listing_meter_read.highlight()
        meter_read = ritchie_result_page.third_listing_meter_read.get_attribute('innerText')
        self.log.info(meter_read)
        print(meter_read)
        ritchie_result_page.third_listing_details.is_displayed()
        ritchie_result_page.third_listing_details.highlight()
        details = ritchie_result_page.third_listing_details.get_attribute('innerText')
        self.log.info(details)
        print(details)
        ritchie_result_page.third_listing_lot.is_displayed()
        ritchie_result_page.third_listing_lot.highlight()
        listing_lot_number = ritchie_result_page.third_listing_lot.get_attribute('innerText')
        ritchie_result_page.add_to_watchlist.is_displayed()
        ritchie_result_page.add_to_watchlist.highlight()
        ritchie_result_page.add_to_watchlist.click()
        ritchie_result_page.watching.is_displayed()
        ritchie_result_page.watching.highlight()
        # Cross check the watchlist
        ritchie_home_page.logo.highlight()
        ritchie_home_page.logo.click()
        ritchie_login_page.login_user.is_displayed()
        ritchie_login_page.login_user.highlight()
        user_id = ritchie_login_page.login_user.get_attribute('innerText')
        assert user_id == 'Hello QA'
        ritchie_login_page.watchlist.is_displayed()
        ritchie_login_page.watchlist.highlight()
        ritchie_login_page.watchlist.click()
        ritchie_login_page.watchlist_page_text.is_displayed()
        ritchie_login_page.watchlist_page_text.highlight()
        ritchie_login_page.watchlist_lot_number.is_displayed()
        ritchie_login_page.watchlist_lot_number.highlight()
        watchlist_lot_number = ritchie_login_page.watchlist_lot_number.get_attribute('innerText')
        assert listing_lot_number == watchlist_lot_number
        # Remove the watchlist and sign out
        ritchie_login_page.watchlist_remove.is_displayed()
        ritchie_login_page.watchlist_remove.highlight()
        ritchie_login_page.watchlist_remove.click()
        ritchie_login_page.watchlist_remove_confirmation.is_displayed()
        ritchie_login_page.watchlist_remove_confirmation.highlight()
        ritchie_login_page.user_home.highlight()
        ritchie_login_page.user_home.click()
        ritchie_login_page.user_dropdown.is_displayed()
        ritchie_login_page.user_dropdown.highlight()
        ritchie_login_page.user_dropdown.click()
        ritchie_login_page.sign_out.is_displayed()
        ritchie_login_page.sign_out.scroll_to()
        ritchie_login_page.sign_out.highlight()
        ritchie_login_page.sign_out.click()
        ritchie_home_page.sign_in.is_displayed()
