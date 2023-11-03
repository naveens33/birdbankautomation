import pytest
from ctreport_selenium.ctlistener import Session
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

from pages.homepage import HomePage
from pages.loginpage import LoginPage

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    LOGGER.info("in driver fixture")
    options = Options()
    options.add_experimental_option('detach', True)
    driver_ = webdriver.Chrome(options)
    Session.start(test_execution_name="Bird Bank Automation",
                  path=r"C:\Users\Me\PycharmProjects\birdbankautomation\reports",
                  driver=driver_,
                  config_file=r"C:\Users\Me\PycharmProjects\birdbankautomation\reportconfig.json")

    driver_.maximize_window()
    driver_.get('https://birdbank.pythonanywhere.com/')
    LOGGER.info("driver initialized and open https://birdbank.pythonanywhere.com/")

    def cleanup():
        Session.end()
        driver_.quit()
        LOGGER.info("driver session ended")
        pass

    request.addfinalizer(cleanup)

    return driver_


@pytest.fixture(scope="class")
def do_login(driver):
    home = HomePage(driver)
    home.click_login_button()
    login = LoginPage(driver)
    login.do_login("testuser1", "testpassword")

