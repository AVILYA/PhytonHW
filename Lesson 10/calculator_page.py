from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    """
    Класс, представляющий страницу калькулятора и предоставляющий методы для взаимодействия с элементами на этой странице.

    Атрибуты:
        driver: Экземпляр веб-драйвера Selenium.
    """

    def __init__(self, driver):
        """
        Инициализирует объект Calculator.

        Args:
            driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        self.driver.implicitly_wait(4)  # Неявное ожидание для поиска элементов
        self.driver.maximize_window()  # Разворачиваем окно браузера на весь экран

    def set_delay(self, delay):
        """
        Устанавливает задержку калькулятора.

        Args:
            delay: Задержка в секундах (тип: str или int).
        """
        input_delay = self.driver.find_element(By.CSS_SELECTOR, "input#delay")
        input_delay.clear()  # Очищаем поле ввода задержки
        input_delay.send_keys(str(delay))  # Вводим новое значение задержки

    def input_text(self, keys_calculator):
        """
        Вводит последовательность клавиш в калькулятор.

        Args:
            keys_calculator: Список или кортеж строк, представляющих клавиши для ввода.
                             Например: ['1', '+', '2', '=']
        """
        for val in keys_calculator:
            self.driver.find_element(
                By.XPATH, f'//span[text()="{val}"]').click()  # Кликаем на элемент, содержащий текст клавиши

    def wait_result(self, delay, result):
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        Args:
            delay: Задержка в секундах (тип: int), используется для WebDriverWait.
            result: Ожидаемый результат (тип: int или str).
        """
        waiter = WebDriverWait(self.driver, delay + 1)  # Создаем объект WebDriverWait
        waiter.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '.screen'), str(result)))  # Ждем, пока текст результата не появится на экране

    def result_text(self):
        """
        Возвращает текст результата, отображаемого на экране калькулятора.

        Returns:
            str: Текст результата.
        """
        result = self.driver.find_element(By.CSS_SELECTOR, '.screen')  # Находим элемент экрана с результатом
        return result.text  # Возвращаем текст этого элемента