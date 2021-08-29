from .pages.main_page import MainPage
from .pages.product_page import PageObject

def test_check_registration_forms(browser):
    link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019.'
    page=PageObject(browser,link)
    page.open()
    page.correct_addition_to_cart()