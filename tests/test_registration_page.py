import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls, User, RegistrationTestData
from locators import LoginPage, RegistrationPage


class TestRegistrationPage:

    def test_input_correct_creds_successful_registration(self, driver: WebDriver):
        user = User.generate()

        driver.get(Urls.registration_page)
        driver.find_element(*RegistrationPage.name_input).send_keys(user.name)
        driver.find_element(*RegistrationPage.email_input).send_keys(user.login)
        driver.find_element(*RegistrationPage.password_input).send_keys(user.password)
        driver.find_element(*RegistrationPage.registrate_button).click()

        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(LoginPage.title_text)
        )

        assert driver.current_url == Urls.login_page
        assert driver.find_element(*LoginPage.title_text).is_displayed()

    def test_input_empty_name_nothing_happens(self, driver: WebDriver):
        driver.get(Urls.registration_page)
        driver.find_element(*RegistrationPage.email_input).send_keys(
            RegistrationTestData.default_email
        )
        driver.find_element(*RegistrationPage.password_input).send_keys(
            RegistrationTestData.valid_password
        )
        driver.find_element(*RegistrationPage.registrate_button).click()

        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(RegistrationPage.registrate_button)
        )

        assert driver.current_url == Urls.registration_page
        assert driver.find_element(*RegistrationPage.registrate_button).is_displayed()

    def test_input_existing_email_show_user_exists_error(self, driver: WebDriver):
        driver.get(Urls.registration_page)
        driver.find_element(*RegistrationPage.name_input).send_keys(
            RegistrationTestData.default_name
        )
        driver.find_element(*RegistrationPage.email_input).send_keys(
            RegistrationTestData.existing_user_email
        )
        driver.find_element(*RegistrationPage.password_input).send_keys(
            RegistrationTestData.valid_password
        )
        driver.find_element(*RegistrationPage.registrate_button).click()

        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(RegistrationPage.user_exists_error_text)
        )

        assert driver.find_element(*RegistrationPage.user_exists_error_text).is_displayed()

    @pytest.mark.parametrize('password', RegistrationTestData.short_passwords)
    def test_input_short_password_show_password_error(
        self, driver: WebDriver, password: str
    ):
        driver.get(Urls.registration_page)
        driver.find_element(*RegistrationPage.name_input).send_keys(
            RegistrationTestData.default_name
        )
        driver.find_element(*RegistrationPage.email_input).send_keys(
            RegistrationTestData.default_email
        )
        driver.find_element(*RegistrationPage.password_input).send_keys(password)
        driver.find_element(*RegistrationPage.registrate_button).click()

        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(RegistrationPage.invalid_password_error_text)
        )

        assert driver.find_element(*RegistrationPage.invalid_password_error_text).is_displayed()
