from psylenium.page import Page


class BasePage(Page):
    def __init__(self, driver, *, href, title_tag, default_timeout=5, waits_enabled=True):
        super().__init__(driver, default_timeout=default_timeout, waits_enabled=waits_enabled)
        self.href = href
        self.title_tag = title_tag

    def go_to_href(self, domain: str):
        self.driver.get(f"{domain}{self.href}")
