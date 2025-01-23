from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60) # Увеличено время ожидания

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay_value):
        delay_input = self.wait.until(EC.presence_of_element_located((By.ID, "delay")))
        delay_input.send_keys(delay_value)

    def click_button(self, button_text):
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button_text}']")))
        button.click()

    def get_result(self):
        result_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "screen")))
        return result_element.text