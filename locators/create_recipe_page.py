from selenium.webdriver.common.by import By


BUTTON_EXIT = [By.XPATH, '//a[text()="Выход"]']
BUTTON_SIGNIN = [By.XPATH, '//button[text()="Создать рецепт"]']
BUTTON_CREATE_RECIPE = [By.XPATH, '//button[text()="Создать рецепт"]']
HREF_RECIPES = [By.XPATH, '//a[text()="Рецепты"]']
IMG_NEW_RECIPE = [By.XPATH, '//img[@class="styles_single-card__image__O135K"]']

FIELD_NAME_RECIPE = [By.XPATH, '//div[text()="Название рецепта"]/following-sibling::input']
FIELD_INGREDIENT = [By.XPATH, '//div[text()="Ингредиенты"]/following-sibling::input']
FIELD_TIME_COOKING  = [By.XPATH, '//div[text()="Время приготовления"]/following-sibling::input']

INGREDIENT_NAME = [By.XPATH, '//div[@class="styles_container__3ukwm"]/child::div']
FIELD_INGREDIENT_QUANTITY= [By.XPATH, '//input[@class="styles_inputField__3eqTj styles_ingredientsAmountValue__2matT"]']
HREF_ADD_INGREDIENT = [By.XPATH, '//div[text()="Добавить ингредиент"]']

FIELD_DESCRIPTION = [By.XPATH, '//div[text()="Описание рецепта"]/following-sibling::textarea[@class="styles_textareaField__1wfhC"]']
SELECT_FILE = [By.XPATH, '//input[@class="styles_fileInput__3HjP3"]']


