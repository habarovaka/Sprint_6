from selenium.webdriver.common.by import By

class MainLocators:
    # Логотипы
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    # Кнопки заказа
    TOP_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    # Локаторы для "Вопросы о важном" (с фигурными скобками для форматирования)
    FAQ_QUESTION = (By.XPATH, "//div[@id='accordion__heading-{}']")
    FAQ_ANSWER = (By.XPATH, "//div[@id='accordion__panel-{}']")