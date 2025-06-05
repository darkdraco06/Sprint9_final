import data
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage
import allure


class TestCreateAccount:

    @allure.title('Проверка создания нового Аккаунта')
    @allure.description('Открываем главную страницу сайта, скликам на кнопку создать аккаунт. Вводим валидные данные и кликаем на кнопку создать аккаунт')
    def test_create_user_one_user_user_created(self, browser, user_data):
        signin_page = SigninPage(browser)
        signup_page = SignupPage(browser)
        signin_page.click_button_create_account()
        signup_page.create_random_account(user_data)

        assert signin_page.checking_display_authorization_form() == True
        assert browser.current_url == data.SIGNIN_PAGE

