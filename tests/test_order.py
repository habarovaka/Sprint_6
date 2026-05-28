from selenium.webdriver.common.by import By
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.common.by import By  # 👈 ВОТ ЭТОТ ИМПОРТ ИСПРАВИТ ОШИБКУ
from selenium.webdriver.common.keys import Keys  # Нужен для работы Keys.ENTER
from pages.base_page import BasePage
from locators.order_locators import OrderLocators  # Проверьте, что путь к локаторам у вас такой


class OrderPage(BasePage):
    # ... ваши остальные методы (__init__, fill_first_form и т.д.) ...

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

        # 4. Выбираем цвет самоката (теперь By.ID сработает без ошибок!)
        color_locator = (By.ID, color)
        self.find_element(color_locator).click()

        # 5. Пишем комментарий
        if comment:
            comment_input = self.find_element((By.XPATH, "//input[@placeholder='Комментарий для курьера']"))
            comment_input.send_keys(comment)

        # 6. Кликаем на кнопку "Заказать" внизу формы
        self.find_element(OrderLocators.BUTTON_ORDER_FINAL).click()

        # 7. Кликаем на кнопку "Да" в окне подтверждения
        self.find_element(OrderLocators.BUTTON_CONFIRM).click()