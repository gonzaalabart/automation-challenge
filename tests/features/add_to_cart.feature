Feature: Agregado de productos al carrito de compra

    Scenario: Agregar producto a carrito desde pagina Inventory
        Given Dado que usuario inicio sesion en www.saucedemo.com
        When Cuando hace click en boton Add to cart de un producto
        Then Entonces el producto es agregado al carrito del usuario
        And Y el número del contador incrementa a 1

    Scenario: Eliminar multiples productos desde pagina Inventory
        Given Dado que usuario inicio sesion en url www.saucedemo.com
        And E hizo click en boton Add to cart de un producto
        And E hizo click en boton Add to cart de otro producto
        When Cuando hace click en boton Remove de ambos productos agregados
        Then Entonces se vacia el carrito del usuario
        And el numero del contador vuelve a 0