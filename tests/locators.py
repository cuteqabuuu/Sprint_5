from selenium.webdriver.common.by import By


class MainPage:
    profile_link_text = (By.XPATH, "...")
    constructor_link_text = (By.XPATH, "...")

    constructor_title = (By.XPATH, "//h1[text()='Соберите бургер']")


class RegistrationPage:
    name_input = (By.XPATH, "...")
    email_input = (By.XPATH, "...")
    password_input = (By.XPATH, "...")
    registrate_button = (By.XPATH, "...")

    user_exists_error_text = (
        By.XPATH,
        "//p[text()='Такой пользователь уже существует']"
    )
    invalid_password_error_text = (
        By.XPATH,
        "//p[text()='Некорректный пароль']"
    )
