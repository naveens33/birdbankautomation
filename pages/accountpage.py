from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class AccountPage(BasePage):
    __pay_bills_link = By.LINK_TEXT, "PAY BILLS"

    def click_pay_bills_link(self):
        self._click(self.__pay_bills_link)
