from pages.signin_page import SigninPage
from pages.signup_page import SignupPage
from  pages.recipes_page import RecipesPage
import allure
import data

class TestAuthorizationUser:

    @allure.title('Проверка авторизации под существующим пользователем')
    @allure.description('Регистрируем пользователя со случайными данными. Вводим валидный email и password и кликаем по кнопке Войти')
    def test_authorization_user_one_user_user_authorizated(self, browser, user_data):
        signin_page = SigninPage(browser)
        signup_page = SignupPage(browser)
        recipes_page = RecipesPage(browser)
        signin_page.click_button_create_account()
        signup_page.create_random_account(user_data)
        signin_page.authorization_user(user_data["email"],user_data["password"])


        assert recipes_page.checking_display_button_exit() == True
        assert browser.current_url == data.RECIPES_PAGE



