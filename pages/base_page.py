from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step('Ожидание загрузки выбранного элемента')
    def wait_for_load_element(self, element):
        WebDriverWait(self.browser, 3).until(expected_conditions.visibility_of_element_located(element))

    @allure.step('Клик по выбранному элементу')
    def click_element(self, find_element):
        self.browser.find_element(*find_element).click()

    @allure.step('Ввод выбранных значений в поле')
    def set_input_data(self, element, data):
        self.browser.find_element(*element).send_keys(str(data))

    @allure.step('Получаем значение элемента')
    def get_find_element_on_page(self, element):
        return self.browser.find_element(*element)

    @allure.step('Проверяем что элемент есть на странице')
    def check_visibility_element(self, element):
        data = self.get_find_element_on_page(element)
        if data.is_displayed():
            return True
        else:
            return False

    @allure.step('Ищем и получаем текст элемента по тексту ссылки')
    def get_element_by_link_text(self, text):
        return self.browser.find_element(By.LINK_TEXT, text).text
