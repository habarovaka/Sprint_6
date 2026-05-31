import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:
    @allure.title("Проверка оформления заказа через верхнюю кнопку")
    @allure.description(
        "Позитивный сценарий: заполняем форму валидными данными и "
        "оформляем заказ через кнопку 'Заказать' в хедере."
    )
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, period, color, comment",
        [
            ("Иван", "Иванов", "ул. Ленина, д. 10", "Черкизовская", "79991112233", "15.06.2026", "сутки", "black",
             "Позвонить за час")
        ]
    )
    def test_order_flow_top_button_success(self, driver, name, surname, address, metro, phone, date, period, color,
                                           comment):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_top_order_button()
        order_page = OrderPage(driver)
        order_page.fill_first_form(name, surname, address, metro, phone)
        order_page.fill_second_form(date, period, color, comment)
        assert order_page.is_success_modal_displayed(), "Модальное окно успешного заказа не отобразилось!"

    @allure.title("Проверка оформления заказа через нижнюю кнопку")
    @allure.description(
        "Позитивный сценарий: заполняем форму валидными данными и "
        "оформляем заказ через кнопку 'Заказать' внизу страницы."
    )
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, period, color, comment",
        [
            ("Анна", "Петрова", "Сиреневый бульвар, д. 5", "Сокольники", "89994445566", "16.06.2026", "двое суток",
             "grey", "")
        ]
    )
    def test_order_flow_bottom_button_success(self, driver, name, surname, address, metro, phone, date, period, color,
                                              comment):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_bottom_order_button()
        order_page = OrderPage(driver)
        order_page.fill_first_form(name, surname, address, metro, phone)
        order_page.fill_second_form(date, period, color, comment)
        assert order_page.is_success_modal_displayed(), "Модальное окно успешного заказа не отобразилось!"