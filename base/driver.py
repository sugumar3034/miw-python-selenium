from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config.config import Config


def generate_driver(*, browser: str, config: Config):
    browser = browser.lower()

    if browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--kiosk")
        options.add_argument("--disable-infobars")
        options.add_experimental_option("prefs", {"credentials_enable_service": False})
        driver = webdriver.Chrome(options=options)

    elif browser == 'headless':
        options = ChromeOptions()
        options.add_argument("headless")
        options.add_argument("no-sandbox")
        options.add_argument('window-size=1024,768')
        options.add_experimental_option("prefs", {"credentials_enable_service": False})
        driver = webdriver.Chrome(options=options)

    else:
        raise ValueError('Browser %s not recognized.' % browser)

    driver.implicitly_wait(5)
    driver.get(config.url)
    return driver
