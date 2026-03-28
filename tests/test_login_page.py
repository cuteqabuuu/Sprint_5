from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls, User
from locators import ForgotPasswordPage, LoginPage, MainPage, RegistrationPage


class TestLoginPage:
    def test_login_via_login_button_show_main_page(self, driver: WebDriver) -> None:
        driver.find_element(*MainPage.login_button).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPage.title_text))
        driver.find_element(*LoginPage.email_field).send_keys(User.login)
        driver.find_element(*LoginPage.password_field).send_keys(User.password)
        driver.find_element(*LoginPage.login_button).click()
        WebDriverWait(driver, 5).until_not(EC.presence_of_element_located(LoginPage.login_button))

        assert driver.current_url == Urls.main_page and driver.find_element(*MainPage.order_button)

    def test_login_via_profile_show_main_page(self, driver: WebDriver) -> None:
        driver.find_element(*MainPage.profile_link_text).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPage.title_text))
        driver.find_element(*LoginPage.email_field).send_keys(User.login)
        driver.find_element(*LoginPage.password_field).send_keys(User.password)
        driver.find_element(*LoginPage.login_button).click()
        WebDriverWait(driver, 5).until_not(EC.presence_of_element_located(LoginPage.login_button))

        assert driver.current_url == Urls.main_page and driver.find_element(*MainPage.order_button)

    def test_login_via_registration_page_show_main_page(self, driver: WebDriver) -> None:
        driver.get(Urls.registration_page)
        driver.find_element(*RegistrationPage.login_text_with_href).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPage.title_text))
        driver.find_element(*LoginPage.email_field).send_keys(User.login)
        driver.find_element(*LoginPage.password_field).send_keys(User.password)
        driver.find_element(*LoginPage.login_button).click()
        WebDriverWait(driver, 5).until_not(EC.presence_of_element_located(LoginPage.login_button))

        assert driver.current_url == Urls.main_page and driver.find_element(*MainPage.order_button)

    def test_login_via_forgot_password_page_show_main_page(self, driver: WebDriver) -> None:
        driver.get(Urls.forgot_password_page)
        driver.find_element(*ForgotPasswordPage.login_text_with_href).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPage.title_text))
        driver.find_element(*LoginPage.email_field).send_keys(User.login)
        driver.find_element(*LoginPage.password_field).send_keys(User.password)
        driver.find_element(*LoginPage.login_button).click()
        WebDriverWait(driver, 5).until_not(EC.presence_of_element_located(LoginPage.login_button))

        assert driver.current_url == Urls.main_page and driver.find_element(*MainPage.order_button)
