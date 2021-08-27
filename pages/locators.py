from selenium.webdriver.common.by import By
#файл для вынесения констант селекторов во внешнююпеременную

class MainPageLocators():          #каждый класс соответствует объекту paje object
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")       #пара как искать и что искать

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')      #ищем форму логина
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')   #ищем ыорму регистрации
