from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:

    driver.get("http://uitestingplayground.com/classattr")

 
    blue_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary') and contains(@class, 'custom-class')]")
    blue_button.click()
    print("Клик по синей кнопке выполнен.")

    sleep(3)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
   
    driver.quit()