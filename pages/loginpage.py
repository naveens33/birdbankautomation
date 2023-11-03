from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class LoginPage(BasePage):
    __username_textfield = By.ID, "id_username"
    __password_textfield = By.ID, "id_password"
    __login_button = By.ID, "signin"

    def do_login(self, username, password):
        self._enter_text(self.__username_textfield, username)
        self._enter_text(self.__password_textfield, password)
        self._click(self.__login_button)
