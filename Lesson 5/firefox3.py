from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    
    driver.get("http://the-internet.herokuapp.com/login")

    
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    print("Введено значение в поле username: tomsmith")
    sleep(0.5)

    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("Введено значение в поле password: SuperSecretPassword!")
    sleep(0.5)

    
    login_button = driver.find_element(By.XPATH, "//button[@class='radius']")
    login_button.click()
    print("Нажата кнопка Login")

    sleep(3)  

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    
    driver.quit()