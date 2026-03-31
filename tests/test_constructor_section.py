from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPage


class TestConstructorSection:
    def test_click_buns_scroll_to_buns(self, login: WebDriver) -> None:
        driver = login
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(MainPage.constructor_link_text)).click()
        wait.until(EC.element_to_be_clickable(MainPage.fillings_tab)).click()
        wait.until(EC.element_to_be_clickable(MainPage.buns_tab)).click()

        wait.until(
            lambda d: MainPage.active_tab_class in d.find_element(*MainPage.buns_tab).get_attribute('class')
        )
        buns_tab_class = driver.find_element(*MainPage.buns_tab).get_attribute('class')

        assert buns_tab_class is not None and MainPage.active_tab_class in buns_tab_class

    def test_click_sauces_scroll_to_sauces(self, login: WebDriver) -> None:
        driver = login
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(MainPage.constructor_link_text)).click()
        wait.until(EC.element_to_be_clickable(MainPage.sauces_tab)).click()

        wait.until(
            lambda d: MainPage.active_tab_class in d.find_element(*MainPage.sauces_tab).get_attribute('class')
        )
        sauces_tab_class = driver.find_element(*MainPage.sauces_tab).get_attribute('class')

        assert sauces_tab_class is not None and MainPage.active_tab_class in sauces_tab_class

    def test_click_fillings_scroll_to_fillings(self, login: WebDriver) -> None:
        driver = login
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(MainPage.constructor_link_text)).click()
        wait.until(EC.element_to_be_clickable(MainPage.fillings_tab)).click()

        wait.until(
            lambda d: MainPage.active_tab_class in d.find_element(*MainPage.fillings_tab).get_attribute('class')
        )
        fillings_tab_class = driver.find_element(*MainPage.fillings_tab).get_attribute('class')

        assert fillings_tab_class is not None and MainPage.active_tab_class in fillings_tab_class
