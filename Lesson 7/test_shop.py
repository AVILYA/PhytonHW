import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages_shop import LoginPage, InventoryPage, CartPage, CheckoutPage, OverviewPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_purchase_flow(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    
    for item_name in items_to_add:
        inventory_page.add_item_to_cart(item_name)
    
    inventory_page.go_to_cart()
    
    cart_page = CartPage(driver)
    cart_page.go_to_checkout()
    
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("Test", "User", "12345")
    
    overview_page = OverviewPage(driver)
    total = overview_page.get_total()
    
    total_value = total.split(': ')[1]
    
    assert total_value == "$58.29", f"Total is {total_value}, but expected $58.29"