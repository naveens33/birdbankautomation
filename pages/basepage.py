from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def _click(self, locator):
        self._driver.find_element(*locator).click()

    def _enter_text(self, locator, text):
        self._driver.find_element(*locator).send_keys(text)

    def _wait_for_element(self, locator, timeout=30, condition="visibility"):
        wait = WebDriverWait(self._driver, timeout)
        if condition == "visibility":
            return wait.until(EC.visibility_of_element_located(locator))
        elif condition == "invisibility":
            return wait.until(EC.invisibility_of_element_located(locator))

    def _get_text(self, locator):
        return self._driver.find_element(*locator).text