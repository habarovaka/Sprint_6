from selenium.webdriver.common.by import By

class OrderLocators:
    # Экран "Для кого самокат"
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    DROPDOWN_METRO_ITEM = (By.XPATH, "//div[contains(@class, 'select-search__select')]//*[text()='{}']")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

    # Экран "Про аренду"
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DROPDOWN_PERIOD = (By.XPATH, "//div[@class='Dropdown-control']")
    OPTION_PERIOD = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")
    CHECKBOX_COLOR = (By.ID, "{}")
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    BUTTON_CONFIRM = (By.XPATH, "//button[text()='Да']")
    MODAL_SUCCESS = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")

    @staticmethod
    def get_period_option_locator(period_text):
        return (By.XPATH, f"//div[@class='Dropdown-menu']/div[text()='{period_text}']")