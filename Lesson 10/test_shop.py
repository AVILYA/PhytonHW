import allure
from selenium import webdriver
from shop_page import User_shop
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@allure.feature("Магазин Saucedemo")
class TestShop:  # Переименовал класс для соответствия конвенции именования

    @allure.story("Успешное оформление заказа")
    def test_successful_order_placement(self): # Переименовал тест для лучшей читаемости и информативности
        """
        Тест проверяет успешное оформление заказа в магазине Saucedemo.

        Шаги:
        1. Авторизация пользователя.
        2. Получение информации о товарах.
        3. Добавление товаров в корзину.
        4. Заполнение информации о доставке.
        5. Проверка итоговой стоимости заказа.
        6. Закрытие браузера.
        """
        with allure.step("Инициализация драйвера и страницы магазина"):
            driver = webdriver.Chrome(service=ChromeService(
                ChromeDriverManager().install()))
            cl_shop = User_shop(driver)

        with allure.step("Авторизация пользователя"):
            cl_shop.user_auth("standard_user", "secret_sauce")

        with allure.step("Получение информации о товарах"):
            cl_shop.get_info()

        with allure.step("Добавление товаров в корзину"):
            cl_shop.add_data_card(
                "Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"
            )

        with allure.step("Заполнение информации о доставке"):
            cl_shop.place_order("Иван", "Иванов", "125319")

        with allure.step("Проверка итоговой стоимости заказа"):
            total = cl_shop.get_result_price()
            allure.attach(total, name="Итоговая стоимость",
                          attachment_type=allure.attachment_type.TEXT) # Более информативное прикрепление
            assert total == "Total: $58.29"

        with allure.step("Закрытие браузера"):
            cl_shop._driver.quit()