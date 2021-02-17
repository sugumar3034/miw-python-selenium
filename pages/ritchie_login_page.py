from psylenium.element import Element
from pages import BasePage


class RitchieLoginPage(BasePage):

    def __init__(self, driver, domain: str = None):
        super().__init__(driver=driver, href="", title_tag="TBU")

        if domain:
            self.go_to_href(domain=domain)

    @property
    def login_page_text(self) -> Element:
        return self.element("//span[contains(text(),'Hello QA')]")

    @property
    def username(self) -> Element:
        return self.element("[name='_58_login']")

    @property
    def password(self) -> Element:
        return self.element("[name='_58_password']")

    @property
    def sign_in_button(self) -> Element:
        return self.element("[value='Sign In']")

    @property
    def login_user(self) -> Element:
        return self.element(".user p > span:nth-of-type(1)")

    @property
    def advance_search(self) -> Element:
        return self.element("#adv-toggle-down")

    @property
    def watchlist(self) -> Element:
        return self.element("//div[@class='circle']/a[@href='/myaccount/my-equipment?tab=watchlist']")

    @property
    def watchlist_page_text(self) -> Element:
        return self.element("// hgroup[ @ id = 'page-title'] / h1[. = 'Watchlist']")

    @property
    def watchlist_lot_number(self) -> Element:
        return self.element("strong")

    @property
    def watchlist_remove(self) -> Element:
        return self.element(".btn-remove-upcoming-watchlist.faux-a.no-print")

    @property
    def watchlist_remove_confirmation(self) -> Element:
        return self.element(".bp2-no-left-margin .removed-item-alert")

    @property
    def user_home(self) -> Element:
        return self.element("//ol[@id='breadcrumbs']//a[@href='/home/auth']")

    @property
    def user_dropdown(self) -> Element:
        return self.element(".user .icon-chevron-down")

    @property
    def sign_out(self) -> Element:
        return self.element("#signOut")
