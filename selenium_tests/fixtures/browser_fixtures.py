import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()   # Selenium сам скачает драйвер (нужен установленный Chrome)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()