import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_locators import OrderLocators


class OrderPage(BasePage):
    @allure.step("Заполнение первой формы 'Для кого самокат'")
    def fill_first_form(self, name, surname, address, metro, phone):
        self.find_element(OrderLocators.INPUT_NAME).send_keys(name)
        self.find_element(OrderLocators.INPUT_SURNAME).send_keys(surname)
        self.find_element(OrderLocators.INPUT_ADDRESS).send_keys(address)
        self.click_element(OrderLocators.INPUT_METRO)
        metro_locator = self.format_locator(OrderLocators.DROPDOWN_METRO_ITEM, metro)
        self.click_element(metro_locator)
        self.find_element(OrderLocators.INPUT_PHONE).send_keys(phone)
        self.click_element(OrderLocators.BUTTON_NEXT)

    @allure.step("Заполнение второй формы 'Про аренду'")
    def fill_second_form(self, date, period, color, comment):
        date_input = self.find_element(OrderLocators.INPUT_DATE)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)
        self.click_element(OrderLocators.DROPDOWN_PERIOD)
        period_option_locator = OrderLocators.get_period_option_locator(period)
        self.click_element(period_option_locator)
        color_locator = self.format_locator(OrderLocators.CHECKBOX_COLOR, color)
        self.click_element(color_locator)
        if comment:
            comment_input = self.find_element(OrderLocators.INPUT_COMMENT)
            comment_input.send_keys(comment)
        self.click_element(OrderLocators.BUTTON_ORDER)
        self.click_element(OrderLocators.BUTTON_CONFIRM)
    @allure.step("Проверка успешного оформления заказа")
    def is_success_modal_displayed(self):
        return self.wait_for_visibility(OrderLocators.MODAL_SUCCESS).is_displayed()