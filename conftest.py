import pytest
from selenium import webdriver
from data import Urls

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.SCOOTER_MAIN_PAGE)
    yield driver
    driver.quit()