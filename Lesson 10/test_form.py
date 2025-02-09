import allure
from selenium import webdriver
from form_page import Autom_data
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@allure.title("Тест заполнения и проверки формы")
def test_auth_form():
    """
    Тест, проверяющий успешность заполнения формы данными о человеке и отображение результатов.
    Использует Selenium WebDriver для взаимодействия с веб-страницей.
    """
    with allure.step("Инициализация драйвера Chrome"):
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))

    with allure.step("Создание экземпляра класса Autom_data"):
        auth_page = Autom_data(driver)

    with allure.step("Заполнение формы данными"):
        auth_page.person_data(
            "Иван",
            "Петров",
            "Ленина, 55-3",
            "",
            "Москва",
            "Россия",
            "test@skypro.com",
            "+7985899998787",
            "QA",
            "SkyPro",
        )

    with allure.step("Поиск элементов результатов"):
        auth_page.check_person_data()

    with allure.step("Получение результатов проверки"):
        success_results, danger_results = auth_page.get_result()

    with allure.step("Проверка успешных результатов"):
        success_class = "alert-success"
        for i in success_results:
            assert success_class in i, f"Ожидаемый класс '{success_class}' не найден в '{i}'"

    with allure.step("Проверка результатов с ошибками"):
        danger_class = "alert-danger"
        for k in danger_results:
            assert danger_class in k, f"Ожидаемый класс '{danger_class}' не найден в '{k}'"

    with allure.step("Закрытие драйвера"):
        auth_page.driver.quit()