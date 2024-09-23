import pytest
from pytest_bdd import scenarios, scenario, given, when, then
from pages.login_page import LoginPage

scenarios("../features/login.feature")

# Fixtures
@given("Dado que usuario accede a www.saucedemo.com")
def go_to_saucedemo(login_page):
    login_page.navigate_login() 

@when("Cuando ingresa credenciales validas")
def enter_valid_credentials(login_page):
    login_page.enter_credentials("standard_user", "secret_sauce")

@when("Y hace click en boton Login")
@when("Cuando hace click en boton Login")
def click_login_button(login_page):
    login_page.click_login()

@then("Entonces accede al e-commerce, siendo rediriguido a la pagina Inventory")
def user_is_on_inventory_page(login_page):
    assert login_page.get_current_url() == "https://www.saucedemo.com/inventory.html"

@then("Entonces el sistema despliega mensaje de error acorde")
def username_required_error_pop_up(login_page):
    login_page.message_error_is_displayed(login_page.USERNAME_REQUIRED_ERROR_MESSAGE)
