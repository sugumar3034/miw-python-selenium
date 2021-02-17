from pytest import fixture, yield_fixture
from config.config import Config
from base.driver import generate_driver


# Handle command line args
def pytest_addoption(parser):

    parser.addoption("--environment", action="store", type="string", default="",
                     help="Environment against which tests will be run")

    parser.addoption("--browser", action="store", type="string", default="chrome",
                     help="Browser to use with Selenium tests; default is Google Chrome headless")


@fixture(scope="session")
def environment(request):
    return request.config.option.environment


@fixture(scope='session')
def browser(request):
    return request.config.option.browser


@fixture(scope="session")
def config(environment):
    return Config(environment)


@yield_fixture(scope='session')
def driver(browser, config: Config):
    driver = generate_driver(browser=browser, config=config)

    yield driver
    driver.quit()
