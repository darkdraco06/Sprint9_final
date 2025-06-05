from  pages.base_page import BasePage
import allure
import locators.signup_page


class SignupPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Вводим имя в поле Имя')
    def input_name(self, name):
        self.set_input_data(locators.signup_page.FIELD_FIRST_NAME, name)

    @allure.step('Вводим фамилию в поле Фамилия')
    def input_last_name(self, last_name):
        self.set_input_data(locators.signup_page.FIELD_LAST_NAME, last_name)

    @allure.step('Вводим имя пользователя в поле Имя пользователя')
    def input_user_name(self, user_name):
        self.set_input_data(locators.signup_page.FIELD_USER_NAME, user_name)

    @allure.step('Вводим email в поле Адрес электроннной почты')
    def input_email(self, email):
        self.set_input_data(locators.signup_page.FIELD_EMAIL, email)

    @allure.step('Вводим пароль в поле Пароль')
    def input_password(self, password):
        self.set_input_data(locators.signup_page.FIELD_PASSWORD, password)

    @allure.step('Клик по кнопке "Создать аккаунт')
    def click_button_create_account(self):
        self.click_element(locators.signup_page.BUTTON_CREATE_ACCOUNT)

    @allure.step('Создание аккаунта со случайными данными')
    def create_random_account(self, user_data):
        self.input_name(user_data["name"])
        self.input_last_name(user_data["last_name"])
        self.input_user_name(user_data["user_name"])
        self.input_email(user_data["email"])
        self.input_password(user_data["password"])
        self.click_button_create_account()
