from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_locators import MainLocators

class MainPage(BasePage):
    def click_top_order_button(self):
        self.click_element(MainLocators.TOP_ORDER_BUTTON)

    def click_bottom_order_button(self):
        self.click_element(MainLocators.BOTTOM_ORDER_BUTTON)

    def click_scooter_logo(self):
        self.click_element(MainLocators.LOGO_SCOOTER)

    def click_yandex_logo(self):
        self.click_element(MainLocators.LOGO_YANDEX)

    def click_faq_question(self, index):
        formatted_locator = self.format_locator(MainLocators.FAQ_QUESTION, index)
        self.click_element(formatted_locator)

    def get_faq_answer_text(self, index):
        formatted_locator = self.format_locator(MainLocators.FAQ_ANSWER, index)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(formatted_locator))
        return self.get_text(formatted_locator)