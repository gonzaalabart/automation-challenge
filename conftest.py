import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser: chrome, edge")

@pytest.fixture(scope="function")
def browser(request):
    browser_type = request.config.getoption("--browser").lower()
    if browser_type == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser_type == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError(f"Browser {browser_type} no disponible para estas pruebas")
    yield driver
    driver.quit()

@pytest.fixture
def login_page(browser):
    # Devuelve una instancia de LoginPage con el navegador configurado
    return LoginPage(browser)

@pytest.fixture
def inventory_page(browser):
    return InventoryPage(browser)