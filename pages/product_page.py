from .base_page import BasePage
from .locators import ProductPageLocators


class PageObject(BasePage):

    def correct_addition_to_cart(self):
        self.add_to_Basket()
        self.should_match_the_price_of_the_item()
        self.must_match_the_name_of_the_product()

    def add_to_Basket(self):  # метод добавления в корзину
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        link.click()
        self.solve_quiz_and_get_code()

    def should_match_the_price_of_the_item(self):  # цена вкорзине должна соответствоват цене товара
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == message_basket_total, f"{self.browser.current_url} - No product price in the message"

    def must_match_the_name_of_the_product(self):  # продукт в корзине сопадает с выбранным
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name == message, f"{self.browser.current_url} - No product name in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_is_disappeared(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "is_disappeared"
