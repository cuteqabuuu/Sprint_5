import random
import string

SERVICE_BASE_URL = 'https://stellarburgers.education-services.ru'


class Urls:
    main_page = f'{SERVICE_BASE_URL}/'
    registration_page = f'{SERVICE_BASE_URL}/register'
    login_page = f'{SERVICE_BASE_URL}/login'
    profile_page = f'{SERVICE_BASE_URL}/account/profile'
    order_history_page = f'{SERVICE_BASE_URL}/account/order-history'
    forgot_password_page = f'{SERVICE_BASE_URL}/forgot-password'


class User:
    login = 'ivanivanov2025@ya.ru'
    password = 'ivanpassword'

    def __init__(self, name: str, login: str, password: str) -> None:
        self.name = name
        self.login = login
        self.password = password

    @classmethod
    def generate(cls):
        return cls(name='Random User',
                   login=f'randomuser{random.randint(100, 999)}@ya.ru',
                   password=''.join(random.choices(string.ascii_letters + string.digits, k=6)))


class RegistrationTestData:
    def __init__(self):
        pass

    default_name = 'test'
    default_email = 'test@ya.ru'
    existing_user_email = 'existing_user@ya.ru'
    valid_password = '123456'
    short_passwords = ['1', '12345']
