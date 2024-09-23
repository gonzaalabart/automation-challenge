# Proyecto de Automatización de Pruebas

## Objetivo del Proyecto

El objetivo de este proyecto fue automatizar pruebas para la plataforma **SauceDemo** y verificar la API de **Mercado Libre**. Las pruebas incluyen:

- **2 pruebas de UI** para el proceso de **login** en [www.saucedemo.com](https://www.saucedemo.com).
- **2 pruebas de UI** para la funcionalidad de **agregar productos al carrito**.
- **1 prueba a la API** de **Mercado Libre** para verificar que devuelve la lista de **departamentos**.

## Tecnologías Utilizadas

- **Selenium**: Para la automatización de pruebas de UI.
- **Requests**: Para realizar peticiones a la API.
- **Pytest**: Para la ejecución de pruebas.
- **Pytest-BDD**: Para estructurar las pruebas utilizando el enfoque de **Behavior-Driven Development** (BDD).

## Instrucciones para Levantar el Proyecto


1. Clonar el repositorio utilizando el siguiente comando:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

2. Instalar dependencias
Instala las dependencias necesarias desde el archivo requirements.txt:
```bash
pip install -r requirements.txt
```

3. Correr todas las pruebas
Para ejecutar todas las pruebas, utiliza el siguiente comando:

```bash
pytest tests
```

Para generar un reporte en formato HTML, utilizar:
```bash
pytest tests --html=report.html
```

4. Correr solo las pruebas de UI
Para ejecutar únicamente las pruebas de UI, utilizar la marca @UI-testing:
```bash
pytest -m "UI-testing"
```

5. Correr solo las pruebas de API
Para ejecutar únicamente las pruebas de API, utilizar la marca @API-testing:
```bash
pytest -m "API-testing"
```

6. Configuración del navegador
Por defecto, las pruebas se ejecutan en Chrome. Para ejecutar las pruebas en Edge, puedes hacerlo utilizando el siguiente comando:
```bash
pytest --browser=edge
```
