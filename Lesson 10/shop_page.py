from selenium.webdriver.common.by import By


class User_shop:
    """
    Класс, представляющий пользовательский интерфейс магазина на веб-сайте saucedemo.com.
    Использует Selenium WebDriver для автоматизации взаимодействия с веб-сайтом.
    """

    def __init__(self, driver):
        """
        Конструктор класса User_shop.

        Инициализирует экземпляр класса, открывает веб-сайт saucedemo.com,
        устанавливает неявное ожидание и максимизирует окно браузера.

        Args:
            driver: Экземпляр WebDriver (например, Chrome, Firefox),
                    который будет использоваться для взаимодействия с веб-сайтом.
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)  # Устанавливаем неявное ожидание в 4 секунды
        self._driver.maximize_window()

    def user_auth(self, username: str, password: str):
        """
        Выполняет аутентификацию пользователя на веб-сайте.

        Находит поля имени пользователя и пароля, вводит предоставленные учетные данные
        и нажимает кнопку входа.

        Args:
            username (str): Имя пользователя для входа.
            password (str): Пароль для входа.
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(username)
        self._driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def get_info(self):
        """
        Получает информацию о доступных товарах на странице магазина.

        Находит все элементы, представляющие кнопки "Add to Cart", названия товаров и цены товаров.
        Сохраняет найденные элементы в атрибуты экземпляра класса.

        Атрибуты:
            add_to_cart: Список элементов, представляющих кнопки "Add to Cart".
            item_names: Список элементов, представляющих названия товаров.
            prices: Список элементов, представляющих цены товаров.
        """
        self.add_to_cart = self._driver.find_elements(
            By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory"
        )
        self.item_names = self._driver.find_elements(
            By.CSS_SELECTOR, "div.inventory_item_name"
        )
        self.prices = self._driver.find_elements(
            By.CSS_SELECTOR, "div.inventory_item_price"
        )

    def add_data_card(self, name_item1: str, name_item2: str, name_item3: str):
        """
        Добавляет указанные товары в корзину.

        Находит кнопки "Add to Cart" для товаров с указанными именами и нажимает их.
        Если один из товаров не найден, он игнорируется.

        Args:
            name_item1 (str): Название первого товара для добавления в корзину.
            name_item2 (str): Название второго товара для добавления в корзину.
            name_item3 (str): Название третьего товара для добавления в корзину.
        """
        item1_button = None
        item2_button = None
        item3_button = None

        for i in range(len(self.item_names)):
            item = self.item_names[i]
            if item.text == name_item1 and not item1_button:
                item1_button = self.add_to_cart[i]
            elif item.text == name_item2 and not item2_button:
                item2_button = self.add_to_cart[i]
            elif item.text == name_item3 and not item3_button:
                item3_button = self.add_to_cart[i]

        if item1_button and item2_button and item3_button:
            item1_button.click()
            item2_button.click()
            item3_button.click()

    def place_order(self, first_name: str, last_name: str, zip_code: str):
        """
        Размещает заказ, вводя информацию о доставке.

        Переходит в корзину, затем на страницу оформления заказа, вводит имя, фамилию и почтовый индекс
        и нажимает кнопку "Continue".

        Args:
            first_name (str): Имя для доставки.
            last_name (str): Фамилия для доставки.
            zip_code (str): Почтовый индекс для доставки.
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link").click()
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        self._driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self._driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self._driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys(zip_code)
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def get_result_price(self):
        """
        Получает и возвращает итоговую цену заказа.

        Находит элемент, содержащий итоговую цену, и возвращает его текст.

        Returns:
            str: Текст элемента, содержащего итоговую цену заказа.
        """
        total = self._driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label"
        ).text
        return total