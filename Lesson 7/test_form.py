import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages_form import DataTypesPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_form_validation(driver):
    """Тест проверяет заполнение и валидацию формы."""
    # 1. Создание объекта страницы
    data_types_page = DataTypesPage(driver)
    
    # 2. Открыть страницу
    data_types_page.open()
    
    # 3. Заполнить форму
    data_types_page.fill_form()
    
    # 4. Отправить форму
    data_types_page.submit_form()

    # 5. Проверить, что поле Zip code подсвечено красным
    zip_code_field = data_types_page.get_zip_code_field()
    assert "is-invalid" in zip_code_field.get_attribute("class"), "Zip code is not red."

    # 6. Проверить, что остальные поля подсвечены зеленым
    other_fields = data_types_page.get_other_fields()
    for field_id, field in other_fields.items():
       assert "is-valid" in field.get_attribute("class"), f"{field_id} is not green."