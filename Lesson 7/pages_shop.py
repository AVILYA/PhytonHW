from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        username_field.send_keys(username)
        password_field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys(password)
        login_button = self.wait.until(EC.presence_of_element_located((By.ID, "login-button")))
        login_button.click()

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_item_to_cart(self, item_name):
          add_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"))
                )
          add_button.click()
    def go_to_cart(self):
        cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']")))
        cart_button.click()


class CartPage:
      def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 10)

      def go_to_checkout(self):
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_checkout_form(self, first_name, last_name, zip_code):
        first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        first_name_field.send_keys(first_name)
        last_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "last-name")))
        last_name_field.send_keys(last_name)
        zip_code_field = self.wait.until(EC.presence_of_element_located((By.ID, "postal-code")))
        zip_code_field.send_keys(zip_code)
        continue_button = self.wait.until(EC.element_to_be_clickable((By.ID, "continue")))
        continue_button.click()
    
class OverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_total(self):
       total_element = self.wait.until(
           EC.presence_of_element_located((By.XPATH, "//div[@class='summary_info_label summary_total_label']"))
       )
       return total_element.text