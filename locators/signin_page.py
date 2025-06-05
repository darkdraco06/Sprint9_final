from selenium.webdriver.common.by import By

BUTTON_SIGNIN = [By.XPATH, '//button[text()="Войти"]']
BUTTON_CREATE_ACCOUNT = [By.XPATH, '//a[text()="Создать аккаунт"]']
AUTHORIZATION_FORM = [By.XPATH, '//form[@class="styles_form__2nwxz styles_form__2_42b"]']
FIELD_EMAIL = [By.XPATH, '//input[@name="email"]']
FIELD_PASSWORD = [By.XPATH, '//input[@name="password"]']