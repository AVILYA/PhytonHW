from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

   
    wait = WebDriverWait(driver, 15)
    images = wait.until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )

    
    third_image = images[2]
    src_value = third_image.get_attribute("src")
    
   
    print(f"Значение атрибута src у 3-й картинки: {src_value}")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    
    driver.quit()