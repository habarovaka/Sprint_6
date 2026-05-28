from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_locators import OrderLocators


class OrderPage(BasePage):
    def fill_first_form(self, name, surname, address, metro, phone):
        self.find_element(OrderLocators.INPUT_NAME).send_keys(name)
        self.find_element(OrderLocators.INPUT_SURNAME).send_keys(surname)
        self.find_element(OrderLocators.INPUT_ADDRESS).send_keys(address)

        # Выбираем метро через клик и подстановку значения
        self.find_element(OrderLocators.INPUT_METRO).click()
        metro_locator = self.format_locator(OrderLocators.DROPDOWN_METRO_ITEM, metro)
        self.click_element(metro_locator)

        self.find_element(OrderLocators.INPUT_PHONE).send_keys(phone)
        self.click_element(OrderLocators.BUTTON_NEXT)

    def fill_second_form(self, date, period, color, comment):
        # 1. Заполняем дату и закрываем календарь нажатием Enter
        date_input = self.find_element(OrderLocators.INPUT_DATE)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        # 2. Кликаем по выпадающему списку "Срок аренды"
        self.find_element(OrderLocators.DROPDOWN_PERIOD).click()

        # 3. Кликаем по конкретному варианту срока (например, "сутки" или "двое суток")
        period_option_locator = OrderLocators.get_period_option_locator(period)
        self.find_element(period_option_locator).click()

        # 4. Выбираем цвет самоката (динамический локатор по id чекбокса)
        color_locator = (By.ID, color)  # 'black' или 'grey' из ваших параметров pytest
        self.find_element(color_locator).click()

        # 5. Пишем комментарий курьеру, если он передан
        if comment:
            # Замените на ваш реальный локатор для поля комментария, если он отличается
            comment_input = self.find_element((By.XPATH, "//input[@placeholder='Комментарий для курьера']"))
            comment_input.send_keys(comment)

        # 6. КЛИКАЕМ НА КНОПКУ "ЗАКАЗАТЬ" (этого шага не хватало)
        self.find_element(OrderLocators.BUTTON_ORDER_FINAL).click()

        # 7. КЛИКАЕМ НА КНОПКУ "ДА" В ОКНЕ ПОДТВЕРЖДЕНИЯ
        self.find_element(OrderLocators.BUTTON_CONFIRM).click()

    def is_success_modal_displayed(self):
        return self.find_element(OrderLocators.MODAL_SUCCESS).is_displayed()