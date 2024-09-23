import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from assets.products import PRODUCTS

scenarios("../features/add_to_cart.feature")

# Background
@given("Usuario inicio sesion en www.saucedemo.com")
def user_logged_in(login_page):
    login_page.login()

@when("Cuando click en boton Add to cart de Sauce Labs Backpack")
def add_to_cart_inventory(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")

@then("Entonces el número del contador incrementa a 1")
def verify_cart_count(inventory_page):
    assert inventory_page.check_cart_counter() == 1  

@given("E hizo click en boton Add to cart de Sauce Labs Backpack")
def add_first_product_to_cart(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")

@given("E hizo click en boton Add to cart de Sauce Labs Bike Light")
def add_second_product_to_cart(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Bike Light")

@when("Cuando hace click en boton Remove de ambos productos agregados")
def remove_all_products(inventory_page):
    inventory_page.remove_from_cart("Sauce Labs Backpack")
    inventory_page.remove_from_cart("Sauce Labs Bike Light")

@then("Entonces el numero del contador no es visible")
def verify_cart_count_equals_zero(inventory_page):
    assert inventory_page.is_cart_counter_visible() # deberia ser assert not, pero queremos que falle para el screenshot