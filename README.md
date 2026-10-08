# Proyecto Urban Grocers API Tests

Este proyecto contiene pruebas automatizadas para la creación de kits de productos utilizando Python, Pytest y Requests.

## Descripción del proyecto

Se automatizaron pruebas para verificar la funcionalidad de creación de kits dentro de un usuario utilizando la API de Urban Grocers.

Las pruebas incluyen validaciones positivas y negativas para el parámetro `name`.

## Tecnologías utilizadas

- Python
- Pytest
- Requests

## Estructura del proyecto

- `configuration.py`  
Contiene las rutas y URL de la API.

- `data.py`  
Contiene los datos de prueba y headers.

- `sender_stand_request.py`  
Contiene las solicitudes HTTP.

- `create_kit_name_kit_test.py`  
Contiene las pruebas automatizadas.

## Cómo ejecutar las pruebas

1. Clonar el repositorio.
2. Abrir el proyecto en PyCharm.
3. Instalar las dependencias:

```bash
pip install pytest
pip install requests