from pages.signin_page import SigninPage
from pages.signup_page import SignupPage
from  pages.recipes_page import RecipesPage
from  pages.create_recipe_page import CreateRecipePage
import allure


class TestAuthorizationUser:

    @allure.title('Проверка создания нового рецепта под авторизованным пользователем')
    @allure.description('Авторизуемся под новым пользователем, вводим данныеем рецепта и кликаем по кнопке Создать')
    def test_create_recipe_one_recipe_recipe_created(self, browser, user_data, recipe):
        signin_page = SigninPage(browser)
        signup_page = SignupPage(browser)
        recipes_page = RecipesPage(browser)
        create_recipe = CreateRecipePage(browser)
        signin_page.click_button_create_account()
        signup_page.create_random_account(user_data)
        signin_page.authorization_user(user_data["email"],user_data["password"])
        recipes_page.click_create_recipe()
        create_recipe.create_new_recipe(recipe)
        create_recipe.click_recipe_page()

        assert recipes_page.checking_display_new_recipe_card() == True
        assert recipes_page.get_new_title_recipe_card(recipe["name"]) == recipe["name"]







