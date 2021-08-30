from selenium.webdriver.common.by import By
#файл для вынесения констант селекторов во внешнююпеременную

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    GO_TO_BASKET=(By.CSS_SELECTOR, ".btn-group .btn-default")


class MainPageLocators():          #каждый класс соответствует объекту paje object
    pass     #пара как искать и что искать

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')      #ищем форму логина
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')   #ищем ыорму регистрации

class ProductPageLocators(object):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE= (By.CSS_SELECTOR, ".alert-success")

class BasketPageLocators():
    MESSAGE_BASKET_EMPTY= (By.CSS_SELECTOR,"div#content_inner p")
    ITEMS_IN_BASKET= (By.CSS_SELECTOR, '.basket-title .row')


