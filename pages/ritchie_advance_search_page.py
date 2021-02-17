from psylenium.element import Element
from pages import BasePage


class RitchieAdvanceSearchPage(BasePage):

    def __init__(self, driver, domain: str = None):
        super().__init__(driver=driver, href="", title_tag="TBU")

        if domain:
            self.go_to_href(domain=domain)

    @property
    def keyword(self) -> Element:
        return self.element("input#adv-keyword")

    @property
    def industry_dropdown(self) -> Element:
        return self.element("//li[@id='adv-industry']/div/div[@class='Select-control']/"
                            "span[@class='Select-arrow-zone']")

    @property
    def industry(self) -> Element:
        return self.element("input#adv-keyword")


    @property
    def make(self) -> Element:
        return self.element("#adv-make")

    @property
    def min_year(self) -> Element:
        return self.element("input#adv-year-min")

    @property
    def max_year(self) -> Element:
        return self.element("input#adv-year-max")

    @property
    def search_button(self) -> Element:
        return self.element("button#adv-submit-button")
