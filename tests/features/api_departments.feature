@API-testing
Feature: Validar la respuesta del servicio web de Mercado Libre

    Scenario: Verificar que el servicio de Mercado Libre contenga departamentos
        When Cuando Usuario hace una solicitud GET a https://www.mercadolibre.com.ar/menu/departments
        Then Entonces la respuesta tiene un código de estado 200
        And Y la respuesta contiene la lista de departamentos