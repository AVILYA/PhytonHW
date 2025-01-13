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

def test_slow_calculator(driver):
    """Тест проверяет работу калькулятора с задержкой."""
    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.send_keys("45")

    
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    
    wait = WebDriverWait(driver, 50)
    result_element = wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    assert result_element, "Result '15' is not displayed."