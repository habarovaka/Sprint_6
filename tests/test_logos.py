import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from data import Urls

class TestLogos:
    @allure.title("Проверка перехода на главную страницу Самоката")
    @allure.description("Кликаем по логотипу 'Самокат' в хедере и проверяем, что возвращаемся на стартовую страницу.")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_top_order_button()
        main_page.click_scooter_logo()
        assert driver.current_url == Urls.SCOOTER_MAIN_PAGE

    @allure.title("Проверка перехода на страницу Дзена")
    @allure.description("Кликаем по логотипу 'Яндекс', переключаемся на новую вкладку и проверяем, что открылся Дзен.")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        WebDriverWait(driver, 10).until(EC.url_contains(Urls.DZEN_URL))
        assert Urls.DZEN_URL in driver.current_url, "Редирект на страницу Дзена не произошел"