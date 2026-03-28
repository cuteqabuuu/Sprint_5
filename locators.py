from selenium.webdriver.common.by import By


class MainPage:
    profile_link_text = (By.XPATH, './/p[text()="Личный Кабинет"]')
    login_button = (By.XPATH, './/button[text()="Войти в аккаунт"]')
    order_button = (By.XPATH, './/button[text()="Оформить заказ"]')
    constructor_link_text = (By.XPATH, './/p[text()="Конструктор"]')
    buns_tab = (By.XPATH, './/span[text()="Булки"]/parent::*')
    sauces_tab = (By.XPATH, './/span[text()="Соусы"]/parent::*')
    fillings_tab = (By.XPATH, './/span[text()="Начинки"]/parent::*')
    active_tab_class = 'tab_tab_type_current__2BEPc'


class RegistrationPage:
    name_input = (By.XPATH, './/label[text()="Имя"]//parent::*/input')
    email_input = (By.XPATH, './/label[text()="Email"]//parent::*/input')
    password_input = (By.XPATH, './/input[@type="password"]')
    registrate_button = (By.XPATH, './/button[text()="Зарегистрироваться"]')
    login_text_with_href = (By.CLASS_NAME, 'Auth_link__1fOlj')
    input_error_text = (By.XPATH, './/p[contains(@class, "input__error")]')


class LoginPage:
    title_text = (By.XPATH, './/h2[text()="Вход"]')
    login_button = (By.XPATH, './/button[text()="Войти"]')
    email_field = (By.XPATH, './/label[text()="Email"]//parent::*/input')
    password_field = (By.XPATH, './/input[@type="password"]')


class ForgotPasswordPage:
    login_text_with_href = (By.CLASS_NAME, 'Auth_link__1fOlj')


class ProfilePage:
    info_text = (By.XPATH, './/p[contains(text(),"персональные данные")]')
    history_link_text = (By.XPATH, './/a[text()="История заказов"]')
    constructor_link_text = (By.XPATH, './/p[text()="Конструктор"]')
    main_logo = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')
    logout_button = (By.XPATH, './/button[text()="Выход"]')
