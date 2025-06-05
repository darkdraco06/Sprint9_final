from  pages.base_page import BasePage
import allure
import locators.recipes_page


class RecipesPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Проверка отображения кнопки Выход')
    def checking_display_button_exit(self):
        self.wait_for_load_element(locators.recipes_page.BUTTON_EXIT_ACCOUNT)
        return self.check_visibility_element(locators.recipes_page.BUTTON_EXIT_ACCOUNT)

    @allure.step('Кликаем по ссылке "Создать рецепт"')
    def click_create_recipe(self):
        self.wait_for_load_element(locators.recipes_page.BUTTON_EXIT_ACCOUNT)
        self.click_element(locators.recipes_page.BUTTON_CREATE_RECIPE)

    @allure.step('Проверяем отображение названия последнего созданного рецепта')
    def get_new_title_recipe_card(self, text):
        return self.get_element_by_link_text(text)

    @allure.step('Проверяем отображение карточки последнего созданного рецепта')
    def checking_display_new_recipe_card(self):
        self.wait_for_load_element(locators.recipes_page.CARD_NEW_RECIPE)
        return self.check_visibility_element(locators.recipes_page.CARD_NEW_RECIPE)

