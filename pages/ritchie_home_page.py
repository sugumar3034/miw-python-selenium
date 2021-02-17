from psylenium.element import Element
from pages import BasePage


class RitchieHomePage(BasePage):

    def __init__(self, driver, domain: str = None):
        super().__init__(driver=driver, href="", title_tag="TBU")

        if domain:
            self.go_to_href(domain=domain)

    @property
    def logo(self) -> Element:
        return self.element(".desktop > img")

    @property
    def sign_in(self) -> Element:
        return self.element("#signInBtn")
