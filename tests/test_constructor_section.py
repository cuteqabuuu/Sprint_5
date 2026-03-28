from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver

from locators import MainPage


class TestConstructorSection:
    def test_click_buns_scroll_to_buns(self, login: WebDriver) -> None:
        driver = login
        driver.find_element(*MainPage.constructor_link_text).click()
        driver.find_element(*MainPage.fillings_tab).click()
        driver.find_element(*MainPage.buns_tab).click()
        sleep(1)
        buns_tab_class = driver.find_element(*MainPage.buns_tab).get_attribute('class')

        assert buns_tab_class is not None and MainPage.active_tab_class in buns_tab_class

    def test_click_sauces_scroll_to_sauces(self, login: WebDriver) -> None:
        driver = login
        driver.find_element(*MainPage.constructor_link_text).click()
        driver.find_element(*MainPage.sauces_tab).click()
        sleep(1)
        sauses_tab_class = driver.find_element(*MainPage.sauces_tab).get_attribute('class')

        assert sauses_tab_class is not None and MainPage.active_tab_class in sauses_tab_class

    def test_click_fillings_scroll_to_fillings(self, login: WebDriver) -> None:
        driver = login
        driver.find_element(*MainPage.constructor_link_text).click()
        driver.find_element(*MainPage.fillings_tab).click()
        sleep(1)
        fillings_tab_class = driver.find_element(*MainPage.fillings_tab).get_attribute('class')

        assert fillings_tab_class is not None and MainPage.active_tab_class in fillings_tab_class
