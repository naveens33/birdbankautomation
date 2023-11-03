from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class PayBillsPage(BasePage):
    __add_new_biller_button = By.ID, "add_payee"
    __biller_name_textfield = By.XPATH, "//input[contains(@placeholder,'Name')]"
    __reg_number_textfield = By.XPATH, "//input[contains(@placeholder,'Number')]"
    __no_radiobutton = By.XPATH, "//label[text()='No']"
    __save_button = By.ID, "save"
    __confirmation_text = By.ID, "confirmationMessage"

    def click_add_new_biller_button(self):
        self._click(self.__add_new_biller_button)

    def do_add_new_payee(self, name, reg_num):
        self._wait_for_element(self.__biller_name_textfield).send_keys(name)
        self._enter_text(self.__reg_number_textfield, reg_num)
        self._click(self.__no_radiobutton)
        self._click(self.__save_button)

    def get_confirmation_text(self):
        return self._get_text(self.__confirmation_text)
