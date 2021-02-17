from pytest import mark
from pages.ritchie_home_page import RitchieHomePage
from pages.ritchie_login_page import RitchieLoginPage
from pages.ritchie_advance_search_page import RitchieAdvanceSearchPage
from pages.ritchie_search_result_page import RitchieSearchResultPage
from config.config import Config
import logging
import utilities.custom_logger as cl


class RitchieSecondTests:
    log = cl.customLogger(logging.DEBUG)

    @mark.RitchieSecondTest
    @mark.Ritchie
    def test_ritchie_two(self, driver, config: Config):
        ritchie_home_page = RitchieHomePage(driver, domain=config.url)
        # Navigate to home page and click on sign in link
        ritchie_home_page.logo.is_displayed()
        ritchie_home_page.logo.highlight()
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
        # pick the 2nd listing and click
        ritchie_result_page = RitchieSearchResultPage(driver)
        ritchie_result_page.search_page_text.is_displayed()
        ritchie_result_page.search_page_text.highlight()
        ritchie_result_page.second_listing.scroll_to()
        ritchie_result_page.second_listing.is_displayed()
        ritchie_result_page.second_listing.highlight()
        ritchie_result_page.second_listing_lot.is_displayed()
        ritchie_result_page.second_listing_lot.highlight()
        second_listing_lot = ritchie_result_page.second_listing_lot.get_attribute('innerText')
        ritchie_result_page.second_listing.click()
        ritchie_result_page.second_listing_lot_check.is_displayed()
        ritchie_result_page.second_listing_lot_check.highlight()
        second_listing_lot_check = ritchie_result_page.second_listing_lot_check.get_attribute('innerText')
        assert second_listing_lot[-4:] == second_listing_lot_check[-4:]
        ritchie_result_page.second_listing_ad_watchlist.is_displayed()
        ritchie_result_page.second_listing_ad_watchlist.highlight()
        ritchie_result_page.second_listing_ad_watchlist.click()
        ritchie_result_page.second_listing_added_watchlist.is_displayed()
        ritchie_result_page.second_listing_added_watchlist.highlight()
        # Check more items and check all upcoming auctions section and select the first listing
        ritchie_result_page.more_item_like_this.is_displayed()
        ritchie_result_page.more_item_like_this.scroll_to()
        ritchie_result_page.more_item_like_this.highlight()
        ritchie_result_page.more_item_like_this.click()
        ritchie_result_page.at_all_upcoming_auctions.scroll_to()
        ritchie_result_page.at_all_upcoming_auctions.is_displayed()
        ritchie_result_page.at_all_upcoming_auctions.highlight()
        ritchie_result_page.at_all_upcoming_auctions.is_displayed()
        ritchie_result_page.first_at_all_upcoming_auctions.is_displayed()
        ritchie_result_page.first_at_all_upcoming_auctions.highlight()
        ritchie_result_page.first_at_all_upcoming_auctions.click()
        ritchie_result_page.vin_number.is_displayed()
        ritchie_result_page.vin_number.highlight()
        vin_number = ritchie_result_page.vin_number.get_attribute('innerText')
        self.log.info(vin_number)
        print(vin_number)
        # Cross check the watchlist
        ritchie_home_page.logo.is_displayed()
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
        assert watchlist_lot_number == second_listing_lot
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
