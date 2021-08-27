from selenium.common.exceptions import NoSuchElementException
class BasePage():          #основной класс
    def __init__(self, browser, url, timeout=10):
        self.browser = browser        #экземпляр драйвера
        self.url = url               #url экземпляр
        self.browser.implicitly_wait(timeout)     #команда для неявного ожидания

    def open(self):
        self.browser.get(self.url)               #метод открывающий нужную страницу

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
