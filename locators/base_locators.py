from selenium.webdriver.common.by import By

class BaseLocators:
    # Кнопка принятия кук (она может появиться на любой странице)
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")