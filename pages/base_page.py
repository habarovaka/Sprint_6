import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента в DOM")
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент не найден: {locator}"
        )

    @allure.step("Клик по элементу")
    def click_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не кликабелен: {locator}"
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Получение текста элемента")
    def get_text(self, locator, time=10):
        return self.find_element(locator, time).text

    @allure.step("Форматирование локатора")
    def format_locator(self, locator, num):
        method, search_string = locator
        return (method, search_string.format(num))

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Принятие кук")
    def accept_cookies(self):
        try:
            self.click_element(BaseLocators.COOKIE_BUTTON, 3)
        except:
            pass

    @allure.step("Ожидание видимости элемента")
    def wait_for_visibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент не стал видимым: {locator}"
        )

    @allure.step("Получение текста из видимого элемента")
    def get_text_from_visible_element(self, locator, time=10):
        return self.wait_for_visibility(locator, time).text