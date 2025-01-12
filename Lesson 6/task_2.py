from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    
    driver.get("http://uitestingplayground.com/textinput")

   
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")
    print("Введено значение в поле ввода: SkyPro")

    
    change_button = driver.find_element(By.ID, "updatingButton")
    change_button.click()
    print("Нажата синяя кнопка")

    
    wait = WebDriverWait(driver, 15)
    changed_button = wait.until(
    	EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    	)
    
    button_text = driver.find_element(By.ID, "updatingButton").text
    
    
    print(f"Текст кнопки: {button_text}")
    
    assert button_text == "SkyPro"
    print("Текст кнопки соответствует ожидаемому")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    
    driver.quit()