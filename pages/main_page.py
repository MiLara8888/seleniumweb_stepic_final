from .base_page import BasePage  # импорт базового класса
from .locators import MainPageLocators  # импорт класса с локаторами
from .login_page import LoginPage


class MainPage(BasePage):  # класс главной страницы сайта наследник класса basepage имеет все атрибуты родителя
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
