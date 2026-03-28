from time import sleep

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls, User
from locators import LoginPage, RegistrationPage


class TestRegistrationPage:

    def test_input_correct_creds_successful_registration(self, driver: WebDriver) -> None:
        driver.get(Urls.registration_page)
        driver.find_element(*RegistrationPage.name_input).send_keys(User.generate().name)
        driver.find_element(*RegistrationPage.email_input).send_keys(User.generate().login)
        driver.find_element(*RegistrationPage.password_input).send_keys(User.generate().password)
        driver.find_element(*RegistrationPage.registrate_button).click()

        WebDriverWait(driver, 5).until_not(
            EC.presence_of_element_located(RegistrationPage.registrate_button))

        assert driver.current_url == Urls.login_page and driver.find_element(*LoginPage.title_text)

    def test_input_empty_name_nothing_happens(self, driver: WebDriver) -> None:
        driver.get(Urls.registration_page)
        driver.find_element(*RegistrationPage.email_input).send_keys('test@ya.ru')
        driver.find_element(*RegistrationPage.password_input).send_keys('123456')
        driver.find_element(*RegistrationPage.registrate_button).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationPage.registrate_button))
        errors = driver.find_elements(*RegistrationPage.input_error_text)

        assert driver.current_url == Urls.registration_page and len(errors) == 0

    @pytest.mark.parametrize('email', ['test1@ya.ru', 'test2ya.ru', 'test3@ya.ru'])
    def test_input_incorrect_email_user_exists_error(self, driver: WebDriver, email: str) -> None:
        driver.get(Urls.registration_page)
        driver.find_element(*RegistrationPage.name_input).send_keys('test')
        driver.find_element(*RegistrationPage.email_input).send_keys(email)
        driver.find_element(*RegistrationPage.password_input).send_keys('123456')
        driver.find_element(*RegistrationPage.registrate_button).click()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegistrationPage.input_error_text))
        error_message = driver.find_element(*RegistrationPage.input_error_text)

        assert error_message.text == 'Такой пользователь уже существует'

    @pytest.mark.parametrize('password', ['1', '12345'])
    def test_input_incorrect_password_less_six_symbols_password_error(self, driver: WebDriver,
                                                                      password: str) -> None:
        driver.get(Urls.registration_page)
        driver.find_element(*RegistrationPage.name_input).send_keys('test')
        driver.find_element(*RegistrationPage.email_input).send_keys('test@ya.ru')
        driver.find_element(*RegistrationPage.password_input).send_keys(password)
        driver.find_element(*RegistrationPage.registrate_button).click()

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegistrationPage.input_error_text))
        error_message = driver.find_element(*RegistrationPage.input_error_text)

        assert error_message.text == 'Некорректный пароль'
