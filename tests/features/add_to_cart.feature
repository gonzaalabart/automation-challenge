Feature: Agregado de productos al carrito de compra

    Background: Usuario inicio sesion en www.saucedemo.com

    Scenario: Agregar producto a carrito desde pagina Inventory
        When Cuando hace click en boton Add to cart de un producto
        Then Entonces el producto es agregado al carrito del usuario
        And Y el número del contador incrementa a 1

    Scenario Outline: Eliminar multiples productos desde pagina Inventory
        And E hizo click en boton Add to cart de <producto1>
        And E hizo click en boton Add to cart de <producto2>
        When Cuando hace click en boton Remove de ambos productos agregados
        Then Entonces se vacia el carrito del usuario
        And Y el numero del contador vuelve a 0

        Examples:
            | producto1           | producto2             |
            | Sauce Labs Backpack | Sauce Labs Bike Light |