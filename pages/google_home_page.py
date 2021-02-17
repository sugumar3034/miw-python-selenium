from psylenium.element import Element
from pages import BasePage


class GoogleHomePage(BasePage):

    def __init__(self, driver, domain: str = None):
        super().__init__(driver=driver, href="", title_tag="TBU")

        if domain:
            self.go_to_href(domain=domain)

    @property
    def google_search_text(self) -> Element:
        return self.element(".FPdoLc [value='Google Search']")

    @property
    def search(self) -> Element:
        return self.element(".a4bIc > input[role='combobox']")

    @property
    def search_result(self) -> Element:
        return self.element("li:nth-of-type(1)  div[role='option']")

    @property
    def google_search_one(self) -> Element:
        return self.element(".YyVfkd")
