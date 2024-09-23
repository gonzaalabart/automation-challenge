import pytest
from pytest_bdd import scenarios, scenario, given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

scenarios("../features/add_to_cart.feature")


# Background
@given("Usuario inicio sesion en www.saucedemo.com")
def user_logged_in(login_page):
    login_page.login("standard_user", "secret_sauce")

@when("Cuando hace click en boton Add to cart de un producto")
def add_to_cart_inventory(inventory_page):
    inventory_page

@then("Entonces el producto es agregado al carrito del usuario")
def c2():
    pass

@then("Y el número del contador incrementa a 1")
def e2():
    pass

@when("E hizo click en boton Add to cart de otro producto")
def f2():
    pass

@given("E hizo click en boton Add to cart de un producto")
def g2():
    pass

@given("E hizo click en boton Add to cart de otro producto")
def h2():
    pass

@when("Cuando hace click en boton Remove de ambos productos agregados")
def i2():
    pass

@then("Entonces se vacia el carrito del usuario")
def j2():
    pass

@then("Y el numero del contador vuelve a 0")
def k2():
    pass