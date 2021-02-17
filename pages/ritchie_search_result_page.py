from psylenium.element import Element
from pages import BasePage


class RitchieSearchResultPage(BasePage):

    def __init__(self, driver, domain: str = None):
        super().__init__(driver=driver, href="", title_tag="TBU")

        if domain:
            self.go_to_href(domain=domain)

    @property
    def search_page_text(self) -> Element:
        return self.element(".sc-kgoBCf")

    @property
    def third_listing(self) -> Element:
        return self.element("div:nth-of-type(3) > .cCRZtc.sc-cHGsZl  h3 > a")

    @property
    def third_listing_meter_read(self) -> Element:
        return self.element("//div[@id='searchResultsList']/div[3]//main/p[1]")

    @property
    def third_listing_details(self) -> Element:
        return self.element("//div[@id='searchResultsList']/div[3]//main/p[2]")

    @property
    def third_listing_lot(self) -> Element:
        return self.element("#searchResultsList .domish:nth-of-type(3) figcaption")

    @property
    def make(self) -> Element:
        return self.element("#adv-make")

    @property
    def add_to_watchlist(self) -> Element:
        return self.element("#rba--category-page .domish:nth-child(4) .domish:nth-of-type(3) [type]")

    @property
    def watching(self) -> Element:
        return self.element("//div[@id='searchResultsList']/div[3]"
                            "/div[2]//button[@type='secondary']//span[.='Watching']")

    @property
    def search_button(self) -> Element:
        return self.element("button#adv-submit-button")

    @property
    def second_listing(self) -> Element:
        return self.element("div#searchResultsList > div:nth-of-type(2) .sc-kpOJdX.uYEbR > a")

    @property
    def second_listing_lot(self) -> Element:
        return self.element("#searchResultsList .domish:nth-of-type(2) figcaption")

    @property
    def second_listing_lot_check(self) -> Element:
        return self.element("#lblLotNo")

    @property
    def second_listing_ad_watchlist(self) -> Element:
        return self.element("button#btnAddToWatchlist")

    @property
    def second_listing_added_watchlist(self) -> Element:
        return self.element("#addedWatchlist")

    @property
    def more_item_like_this(self) -> Element:
        return self.element(".rba-tabset-inner [data-target-pane='similar-pane'] .rba-tab-inner")

    @property
    def at_all_upcoming_auctions(self) -> Element:
        return self.element("#similar-pane div:nth-child(5) h5")

    @property
    def first_at_all_upcoming_auctions(self) -> Element:
        return self.element("div:nth-of-type(5)  .rba-carousel-slides > div:nth-of-type(1) > a")

    @property
    def vin_number(self) -> Element:
        return self.element("#lblSerialOrVin .elwEdR")
