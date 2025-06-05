import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import data
from utils import Utils


@pytest.fixture
def browser():
    options = ChromeOptions()
    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        options=options)
    driver.maximize_window()
    driver.get(data.MAIN_PAGE)
    yield driver
    driver.quit()

@pytest.fixture
def user_data():
    utils = Utils()
    user_data = utils.generate_random_data_user_json()
    return user_data

@pytest.fixture
def recipe():
    utils = Utils()
    recipe = utils.generate_random_data_recipe()
    return recipe