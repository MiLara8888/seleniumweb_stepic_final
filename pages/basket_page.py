from .base_page import BasePage  # импорт базового класса
from .locators import BasketPageLocators  # импорт класса с локаторами

class BasketPage(BasePage):
    def should_report_that_the_basket_is_empty(self):              #что есть сообщение о том, что коризна пуста
        text_empty=self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_EMPTY).text
        assert  'Your basket is empty' in text_empty, 'basket is not empty'

    def should_be_no_items_in_the_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), 'there are items in the cart'
