import data
import random
import string
import allure


class Utils:

    @allure.step('Генерируем случаныйе данные пользователя: name, last_name, name_user, email, password')
    def generate_random_data_user_json(self):

        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        name = generate_random_string(10)
        last_name = generate_random_string(10)
        user_name= generate_random_string(10)
        email = generate_random_string(10) + "@yandex.ru"
        password = generate_random_string(10)


        payload = {
        "name": name,
        "last_name": last_name,
        "user_name": user_name,
        "email": email,
        "password": password
        }
        return payload

    @allure.step('Генерируем случаныйе данные для рецепта')
    def generate_random_data_recipe(self):

        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        name = generate_random_string(10)
        ingredient = "сосиски"
        quantity_ingredient = random.randint(1, 10)
        time_cooking = random.randint(10, 100)
        discription = generate_random_string(50)
        img = data.IMG


        payload = {
        "name": name,
        "ingredient": ingredient,
        "quantity_ingredient": quantity_ingredient,
        "time_cooking": time_cooking,
        "discription": discription,
        "img": img

        }
        return payload