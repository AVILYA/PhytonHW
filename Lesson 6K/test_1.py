import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_form_validation(driver):
    """Тест проверяет заполнение и валидацию формы."""
   
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    
    input_data = {
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

    for field_id, value in input_data.items():
        input_field = driver.find_element(By.ID, field_id)
        input_field.send_keys(value)

    
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    
    wait = WebDriverWait(driver, 10)
    zip_code_field = wait.until(
        EC.presence_of_element_located((By.ID, "zipCode"))
    )
    assert "is-invalid" in zip_code_field.get_attribute("class"), "Zip code is not red."

   
    for field_id in input_data.keys():
        field = wait.until(
          EC.presence_of_element_located((By.ID, field_id))
          )
        assert "is-valid" in field.get_attribute("class"), f"{field_id} is not green."