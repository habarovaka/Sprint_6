import pytest
from pages.main_page import MainPage

class TestFAQ:
    @pytest.mark.parametrize("index, expected_text", [
        (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1, "Пока что у нас так: один заказ — один самокат."),
        (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня."),
        (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток"),
        (6, "Да, пока самокат не привезли. Штрафа не будет"),
        (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")])

    def test_faq_dropdown_opens_correct_text(self, driver, index, expected_text):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_faq_question(index)
        answer_text = main_page.get_faq_answer_text(index)
        assert expected_text in answer_text, f"Ожидаемый текст '{expected_text}' не найден в ответе."