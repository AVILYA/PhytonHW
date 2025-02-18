from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Autom_data:
    """
    Класс для автоматизации заполнения и проверки данных на странице с формами.
    """

    def __init__(self, driver):
        """
        Инициализирует объект Autom_data, открывает страницу и настраивает драйвер.

        Args:
            driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        self.driver.implicitly_wait(4)  # Неявное ожидание для поиска элементов
        self.driver.maximize_window()  # Разворачиваем окно браузера на весь экран
        self.ch_first_name = None  # Инициализируем атрибуты, чтобы избежать ошибки NameError
        self.ch_last_name = None
        self.ch_address = None
        self.ch_e_mail = None
        self.ch_phone_number = None
        self.ch_zip_code = None
        self.ch_city = None
        self.ch_country = None
        self.ch_job_position = None
        self.ch_company = None

    def person_data(
        self,
        first_name,
        last_name,
        address,
        zip_code,
        city,
        country,
        e_mail,
        phone_number,
        job_position,
        company,
    ):
        """
        Заполняет поля формы данными о человеке и отправляет форму.

        Args:
            first_name (str): Имя.
            last_name (str): Фамилия.
            address (str): Адрес.
            zip_code (str): Почтовый индекс.
            city (str): Город.
            country (str): Страна.
            e_mail (str): Электронная почта.
            phone_number (str): Номер телефона.
            job_position (str): Должность.
            company (str): Компания.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="address"]').send_keys(address)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(e_mail)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone_number)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys(zip_code)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(job_position)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)
        self.driver.find_element(
            By.CSS_SELECTOR, 'button.btn-outline-primary[type="submit"]').click()

    def check_person_data(self):
        """
        Находит элементы для отображения введенных данных о человеке на странице после отправки формы.
        Сохраняет их в атрибуты объекта для дальнейшего использования.
        """
        self.ch_first_name = self.driver.find_element(
            By.CSS_SELECTOR, "#first-name")
        self.ch_last_name = self.driver.find_element(
            By.CSS_SELECTOR, "#last-name")
        self.ch_address = self.driver.find_element(
            By.CSS_SELECTOR, "#address")
        self.ch_e_mail = self.driver.find_element(By.CSS_SELECTOR, "#e-mail")
        self.ch_phone_number = self.driver.find_element(
            By.CSS_SELECTOR, "#phone")
        self.ch_zip_code = self.driver.find_element(
            By.CSS_SELECTOR, "#zip-code")
        self.ch_city = self.driver.find_element(By.CSS_SELECTOR, "#city")
        self.ch_country = self.driver.find_element(
            By.CSS_SELECTOR, "#country")
        self.ch_job_position = self.driver.find_element(
            By.CSS_SELECTOR, "#job-position"
        )
        self.ch_company = self.driver.find_element(
            By.CSS_SELECTOR, "#company")

    def get_result(self):
        """
        Получает результаты проверки данных на странице.

        Returns:
            tuple: Кортеж из двух списков. Первый список содержит результаты проверки для всех полей, кроме zip_code.
                   Второй список содержит результат проверки для поля zip_code.
        """
        success_results = []
        danger_results = []

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.alert-success"))
        )  # Ожидаем появления элемента div.alert-success

        fields = [
            self.ch_first_name,
            self.ch_last_name,
            self.ch_address,
            self.ch_e_mail,
            self.ch_phone_number,
            self.ch_city,
            self.ch_country,
            self.ch_job_position,
            self.ch_company,
        ]

        for element in fields:
            result = element.get_attribute("class")  # Получаем класс элемента
            success_results.append(result)

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.alert-danger"))
        )  # Ожидаем появления элемента div.alert-danger
        danger_element = self.ch_zip_code.get_attribute("class")  # Получаем класс элемента
        danger_results.append(danger_element)

        return success_results, danger_results