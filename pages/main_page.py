from .base_page import BasePage          #импорт базового класса
from selenium.webdriver.common.by import By
from .locators import MainPageLocators     #импорт класса с локаторами

class MainPage(BasePage):          #класс главной страницы сайта наследник класса basepage имеет все атрибуты родителя
    def go_to_login_page(self):       #проверяет кликабельность кнопки зарегестрироваться
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):  #что есть ссылка, которая ведет на логин
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

