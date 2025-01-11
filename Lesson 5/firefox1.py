from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    
    driver.get("http://the-internet.herokuapp.com/entry_ad")
    
    sleep(1)

   
    close_button = driver.find_element(By.XPATH, "//div[@class='modal']//p[text()='Close']")
    close_button.click()
    print("Кнопка 'Close' в модальном окне была нажата.")

    sleep(3) 

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    
    driver.quit()