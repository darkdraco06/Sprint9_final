from  pages.base_page import BasePage
import allure
import locators.signin_page
import time


class SigninPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Кликаем по кнопке "Создать аккаунт"')
    def click_button_create_account(self):
        self.click_element(locators.signin_page.BUTTON_CREATE_ACCOUNT)

    @allure.step('Проверка отображения формы авторизации')
    def checking_display_authorization_form(self):
        self.wait_for_load_element(locators.signin_page.AUTHORIZATION_FORM)
        return self.check_visibility_element(locators.signin_page.AUTHORIZATION_FORM)

    @allure.step('Вводим email зарегистрированного пользователя в поле Электронная почта')
    def input_email(self, email):
        self.set_input_data(locators.signin_page.FIELD_EMAIL, email)

    @allure.step('Вводим пароль зарегистрированного пользователя в поле Пароль')
    def input_password(self, password):
        self.set_input_data(locators.signin_page.FIELD_PASSWORD, password)

    @allure.step('Клик по кнопке Войти')
    def click_signin_button(self):
        self.click_element(locators.signin_page.BUTTON_SIGNIN)

    @allure.step('Авторизация зарегистрированного пользвоателя')
    def authorization_user(self, email, password):
        self.wait_for_load_element(locators.signin_page.BUTTON_SIGNIN)
        self.input_email(email)
        self.input_password(password)
        self.click_signin_button()



