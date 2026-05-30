import allure
from pages.base_page import BasePage
from locators.main_locators import MainLocators

class MainPage(BasePage):
    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_top_order_button(self):
        self.click_element(MainLocators.TOP_ORDER_BUTTON)

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_bottom_order_button(self):
        self.click_element(MainLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Клик по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.click_element(MainLocators.LOGO_SCOOTER)

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        self.click_element(MainLocators.LOGO_YANDEX)

    @allure.step("Клик по вопросу в FAQ под номером {index}")
    def click_faq_question(self, index):
        formatted_locator = self.format_locator(MainLocators.FAQ_QUESTION, index)
        self.click_element(formatted_locator)

    @allure.step("Получение текста ответа в FAQ под номером {index}")
    def get_faq_answer_text(self, index):
        formatted_locator = self.format_locator(MainLocators.FAQ_ANSWER, index)
        return self.get_text_from_visible_element(formatted_locator)