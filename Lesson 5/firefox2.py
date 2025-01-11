from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep



driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    
    driver.get("http://the-internet.herokuapp.com/inputs")

    
    input_field = driver.find_element(By.TAG_NAME, "input")

    
    input_field.send_keys("1000")
    print("Введено значение: 1000")
    sleep(0.5)

    
    input_field.clear()
    print("Поле ввода очищено")
    sleep(0.5)

    
    input_field.send_keys("999")
    print("Введено значение: 999")
    sleep(0.5)

    sleep(3)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    
    driver.quit()