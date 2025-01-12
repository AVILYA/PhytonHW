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

def test_purchase_flow(driver):
    """Тест проверяет сценарий покупки товара."""
   
    driver.get("https://www.saucedemo.com/")

   
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item_name in items_to_add:
        add_button = driver.find_element(
            By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        )
        add_button.click()
    
   
    cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart_button.click()

    
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

   
    first_name_field = driver.find_element(By.ID, "first-name")
    first_name_field.send_keys("Test")
    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.send_keys("User")
    zip_code_field = driver.find_element(By.ID, "postal-code")
    zip_code_field.send_keys("12345")
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

   
    wait = WebDriverWait(driver, 10)
    total_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='summary_info_label summary_total_label']"))
    )
    total_text = total_element.text
    
   
    total_value = total_text.split(': ')[1]

  
    assert total_value == "$58.29", f"Total is {total_value}, but expected $58.29"