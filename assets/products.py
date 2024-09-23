from selenium.webdriver.common.by import By

PRODUCTS = {
    "Sauce Labs Backpack": {
        "add": (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"),
        "remove": (By.XPATH, "//button[@data-test='remove-sauce-labs-backpack']")
    },
    "Sauce Labs Bike Light": {
        "add": (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"),
        "remove": (By.XPATH, "//button[@data-test='remove-sauce-labs-bike-light']")
    }
}