from  pages.base_page import BasePage
import allure
import locators.create_recipe_page


class CreateRecipePage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Вводим название рецепта')
    def input_name_recipe(self, name):
        self.set_input_data(locators.create_recipe_page.FIELD_NAME_RECIPE, name)

    @allure.step('Вводим название ингредиента')
    def input_ingredient(self, ingredient):
        self.set_input_data(locators.create_recipe_page.FIELD_INGREDIENT, ingredient)

    @allure.step('Кликаем по найденому ингредиенту в списке')
    def click_ingredient(self):
        self.wait_for_load_element(locators.create_recipe_page.INGREDIENT_NAME)
        self.click_element(locators.create_recipe_page.INGREDIENT_NAME)

    @allure.step('Вводим количество ингредиентов')
    def input_ingredient_quantity(self, quantity):
        self.set_input_data(locators.create_recipe_page.FIELD_INGREDIENT_QUANTITY, quantity)

    @allure.step('Кликаем по ссылке добавить ингредиент')
    def click_add_ingredient(self):
        self.click_element(locators.create_recipe_page.HREF_ADD_INGREDIENT)

    @allure.step('Вводим время приготовления')
    def input_time_cooking(self, time):
        self.set_input_data(locators.create_recipe_page.FIELD_TIME_COOKING, time)

    @allure.step('Вводим описание рецепта')
    def input_discription(self, discription):
        self.set_input_data(locators.create_recipe_page.FIELD_DESCRIPTION, discription)

    @allure.step('Загружаем фото рецепта')
    def upload_file(self, photo):
        self.set_input_data(locators.create_recipe_page.SELECT_FILE, photo)

    @allure.step('Клик по кнопке "Создать рецепт"')
    def click_button_create_recipe(self):
        self.click_element(locators.create_recipe_page.BUTTON_CREATE_RECIPE)

    @allure.step('Создаем новый рецепт')
    def create_new_recipe(self, recipe):
        self.input_name_recipe(recipe["name"])
        self.input_ingredient(recipe["ingredient"])
        self.click_ingredient()
        self.input_ingredient_quantity(recipe["quantity_ingredient"])
        self.click_add_ingredient()
        self.input_time_cooking(recipe["time_cooking"])
        self.input_discription(recipe["discription"])
        self.upload_file(recipe["img"])
        self.click_button_create_recipe()

    @allure.step('Клик по ссылке рецепты')
    def click_recipe_page(self):
        self.wait_for_load_element(locators.create_recipe_page.IMG_NEW_RECIPE)
        self.click_element(locators.create_recipe_page.HREF_RECIPES)









