from selenium.webdriver.common.by import By
from .base_page import BasePage
from assets.products import PRODUCTS
from selenium.common.exceptions import TimeoutException

class InventoryPage(BasePage):
    CART_COUNTER = (By.XPATH, "//span[@class='shopping_cart_badge']")

    def navigate_to_inventory(self):
        self.navigate_to("https://www.saucedemo.com/inventory.html")
    
    def add_to_cart(self, product_name):
        product_locator = PRODUCTS[product_name]["add"]
        self.click(product_locator)
    
    def remove_from_cart(self, product_name):
        product_locator = PRODUCTS[product_name]["remove"]
        self.click(product_locator)
    
    def check_cart_counter(self):
        return int(self.wait_for_element(self.CART_COUNTER).text)

    def is_cart_counter_visible(self):
        try:
            self.wait_for_element(self.CART_COUNTER)
            return True  
        except TimeoutException:
            return False 
        