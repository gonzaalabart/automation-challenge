import requests
import pytest
from pytest_bdd import scenarios, when, then

scenarios('../features/api_departments.feature')

@when('Cuando Usuario hace una solicitud GET a https://www.mercadolibre.com.ar/menu/departments')
def get_departments(api_response):
    pass

@then("Entonces la respuesta tiene un código de estado 200")
def validar_codigo_estado(api_response):
    assert api_response.status_code == 200, f"Se esperaba código 200, pero se recibió {api_response.status_code}"


@then("Y la respuesta contiene la lista de departamentos")
def validar_departamentos(api_response):
    data = api_response.json()
    assert "departments" in data, "La respuesta no contiene la lista de departamentos"
    assert len(data["departments"]) > 0, "La lista de departamentos está vacía"