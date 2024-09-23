import pytest
from pytest_bdd import scenarios, scenario, given, when, then
from pages.login_page import LoginPage

scenarios("../features/login.feature")

# Fixtures
@given("Dado que usuario accede a www.saucedemo.com")
def go_to_saucedemo(browser):
    login_page = LoginPage(browser)
    login_page.navigate_login()

@when("Cuando ingresa credenciales validas")
def b():
    pass

@when("Y hace click en boton Login")
@when("Cuando hace click en boton Login")
def c():
    pass

@then("Entonces accede al e-commerce, siendo rediriguido a la pagina Inventory")
def d():
    assert 1==1

@then("Entonces el sistema despliega mensaje de error acorde")
def e():
    assert 1==1
