from typing import Any, Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls, User
from locators import LoginPage, MainPage


@pytest.fixture
def driver() -> Generator[WebDriver, Any, None]:
    driver = webdriver.Chrome()
    driver.get(Urls.main_page)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver: WebDriver) -> WebDriver:
    driver.get(Urls.login_page)
    driver.find_element(*LoginPage.email_field).send_keys(User.login)
    driver.find_element(*LoginPage.password_field).send_keys(User.password)
    driver.find_element(*LoginPage.login_button).click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(MainPage.order_button))
    return driver
