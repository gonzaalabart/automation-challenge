
Feature: Agregado de productos al carrito de compra

    Background:
        Given Usuario inicio sesion en www.saucedemo.com

    @mi_marcador
    Scenario: Agregar producto a carrito desde pagina Inventory incrementa el contador
        When Cuando click en boton Add to cart de Sauce Labs Backpack
        Then Entonces el número del contador incrementa a 1


    Scenario: Eliminar multiples productos desde pagina Inventory decrece el contador
        Given E hizo click en boton Add to cart de Sauce Labs Backpack
        And E hizo click en boton Add to cart de Sauce Labs Bike Light
        When Cuando hace click en boton Remove de ambos productos agregados
        Then Entonces el numero del contador vuelve a 0