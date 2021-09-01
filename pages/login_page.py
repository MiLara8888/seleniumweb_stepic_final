from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators  # импорт класса с локаторами


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert 'login' in str(url), f'login not in url {str(url)}'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):           #регистрация юзера
        self.browser.find_element(*LoginPageLocators.USER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.USER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.USER_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()
