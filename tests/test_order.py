import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrder:
    @allure.title("Проверка успешного оформления заказа самоката")
    @allure.description(
        "Позитивный сценарий: проверяем весь цикл оформления заказа через две разные кнопки "
        "(в хедере и внизу страницы). Заполняем обе формы валидными данными и проверяем "
        "появление модального окна об успешном создании заказа."
    )
    @pytest.mark.parametrize(
        "button_type, name, surname, address, metro, phone, date, period, color, comment",
        [
            # Тест-кейс 1: заказ через верхнюю кнопку, черный самокат
            ("top", "Иван", "Иванов", "ул. Ленина, д. 10", "Черкизовская", "79991112233", "15.06.2026", "сутки",
             "black", "Позвонить за час"),
            # Тест-кейс 2: заказ через нижнюю кнопку, серый самокат
            ("bottom", "Анна", "Петрова", "Сиреневый бульвар, д. 5", "Сокольники", "89994445566", "16.06.2026",
             "двое суток", "grey", "")
        ]
    )
    def test_order_flow_success(self, driver, button_type, name, surname, address, metro, phone, date, period, color,
                                comment):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        if button_type == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()
        order_page = OrderPage(driver)
        order_page.fill_first_form(name, surname, address, metro, phone)
        order_page.fill_second_form(date, period, color, comment)
        assert order_page.is_success_modal_displayed(), "Модальное окно успешного заказа не отобразилось!"