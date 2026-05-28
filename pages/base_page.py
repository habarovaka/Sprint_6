from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент не найден: {locator}"
        )

    def click_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не кликабелен: {locator}"
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def get_text(self, locator, time=10):
        return self.find_element(locator, time).text

    def format_locator(self, locator, num):
        method, search_string = locator
        return (method, search_string.format(num))

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def accept_cookies(self):
        try:
            self.click_element(BaseLocators.COOKIE_BUTTON, 3)
        except:
            pass