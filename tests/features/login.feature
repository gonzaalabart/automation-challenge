Feature: Login en e-commerce Sauce Demo

    Scenario: Inicio de sesion con credenciales correctas
        Given Dado que usuario accede a www.saucedemo.com
        When Cuando ingresa credenciales validas
        And Y hace click en boton Login
        Then Entonces accede al e-commerce, siendo rediriguido a la pagina Inventory

    Scenario: Intento de inicio de sesion sin ingresar credenciales
        Given Dado que usuario accede a www.saucedemo.com
        When Cuando hace click en boton Login
        Then Entonces el sistema despliega mensaje de error acorde