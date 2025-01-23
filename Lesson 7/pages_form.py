from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataTypesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.input_data = {
            "firstName": "Иван",
            "lastName": "Петров",
            "address": "Ленина, 55-3",
            "email": "test@skypro.com",
            "phoneNumber": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "jobPosition": "QA",
            "company": "SkyPro",
        }
    def open(self):
         self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    def fill_form(self):
        for field_id, value in self.input_data.items():
             input_field = self.wait.until(
                 EC.presence_of_element_located((By.ID, field_id))
            )
             input_field.send_keys(value)

    def submit_form(self):
         submit_button = self.wait.until(
              EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
         )
         submit_button.click()
    
    def get_zip_code_field(self):
       zip_code_field = self.wait.until(
              EC.presence_of_element_located((By.ID, "zipCode"))
       )
       return zip_code_field

    def get_other_fields(self):
         other_fields = {}
         for field_id in self.input_data.keys():
            field = self.wait.until(
            EC.presence_of_element_located((By.ID, field_id))
             )
            other_fields[field_id] = field
         return other_fields