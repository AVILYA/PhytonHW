from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    
    driver.get("http://uitestingplayground.com/ajax")

   
    trigger_button = driver.find_element(By.ID, "ajaxButton")
    trigger_button.click()
    print("Нажата синяя кнопка.")

    
    wait = WebDriverWait(driver, 15)
    success_message = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class='bg-success']"))
    )

    
    message_text = success_message.text
    print(f"Полученный текст: {message_text}")

    assert message_text == "Data loaded with AJAX get request."
    print("Текст сообщения соответствует ожидаемому.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    
    driver.quit()