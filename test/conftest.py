
import pytest as pytest
from selenium import webdriver
import warnings
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="function")
def setup(request, browser):
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1440")
        options.add_argument("--height=1000")
        driver = webdriver.Firefox()
    else:
        raise AssertionError("Invalid browser name:" + browser)
    driverWait = WebDriverWait(driver, 3)
    request.cls.driver = driver
    request.cls.wait = driverWait
    yield request.cls.driver
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="specify the browser you want to use (chrome, firefox)")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "Globant Tests Reports"