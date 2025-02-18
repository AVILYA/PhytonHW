import allure
from selenium import webdriver
from calculator_page import Calculator
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@allure.severity("critical")
@allure.title("Тест калькулятора: сложение")
@allure.feature("Калькулятор")
@allure.description("Тест вводит секунды ожидания ответа от калькулятора и выполняет математические операции")
@pytest.mark.parametrize("keys_press, result, delay", [("7+8=", 15, 45)])
def test_calculator(keys_press, result, delay):
    with allure.step("Инициализация драйвера Chrome"):
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))

    with allure.step(f"Инициализация страницы калькулятора с драйвером: {driver}"):
        calc = Calculator(driver)

    with allure.step(f"Установка задержки: {delay}"):
        calc.set_delay(delay)

    with allure.step(f"Ввод текста в калькулятор: {keys_press}"):
        calc.input_text(keys_press)

    with allure.step(f"Ожидание результата: {result} в течение {delay} секунд"):
        calc.wait_result(delay, result)

    with allure.step(f"Проверка результата: ожидаем {result}, получили {calc.result_text()}"):
        actual_result = calc.result_text()
        assert actual_result == str(result), f"Ожидался результат {result}, а получен {actual_result}"

    with allure.step("Закрытие драйвера"):
        driver.quit()