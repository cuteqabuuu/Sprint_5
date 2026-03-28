from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls
from locators import LoginPage, MainPage, ProfilePage


class TestProfilePage:

    def test_click_profile_link_open_profile_page_with_order_history(self,
                                                                     login: WebDriver) -> None:
        driver = login
        driver.find_element(*MainPage.profile_link_text).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(ProfilePage.info_text))
        driver.find_element(*ProfilePage.history_link_text).click()

        assert Urls.order_history_page == driver.current_url

    def test_click_constructor_link_show_constructor(self, login: WebDriver) -> None:
        driver = login
        driver.find_element(*MainPage.profile_link_text).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(ProfilePage.info_text))
        driver.find_element(*ProfilePage.constructor_link_text).click()

        h1_elements = driver.find_elements(By.XPATH, './/h1')
        assert len(h1_elements) > 0 and h1_elements[0].text == 'Соберите бургер'

    def test_click_main_logo_show_constructor(self, login: WebDriver) -> None:
        driver = login
        driver.find_element(*MainPage.profile_link_text).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(ProfilePage.info_text))
        driver.find_element(*ProfilePage.main_logo).click()

        h1_elements = driver.find_elements(By.XPATH, './/h1')
        assert len(h1_elements) > 0 and h1_elements[0].text == 'Соберите бургер'

    def test_click_logout_button_show_login_page(self, login: WebDriver) -> None:
        driver = login
        driver.find_element(*MainPage.profile_link_text).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(ProfilePage.info_text))
        driver.find_element(*ProfilePage.logout_button).click()
        WebDriverWait(driver, 5).until_not(EC.presence_of_element_located(ProfilePage.logout_button))

        assert driver.current_url == Urls.login_page and driver.find_element(*LoginPage.title_text)
