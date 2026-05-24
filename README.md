# Pre-Entrega de Proyecto: Automatización de Pruebas con Selenium y Python

Este proyecto implementa una suite de pruebas automatizadas para la plataforma web demo SauceDemo utilizando Python, Selenium WebDriver y Pytest. El objetivo de este proyecto es validar flujos básicos de navegación web como inicio de sesión, verificación del catálogo de productos y el comportamiento del carrito de compras.

---

## Tecnologías Utilizadas

* Python 3.x - Lenguaje de programación principal.
* Pytest - Framework de testing estructurado para Python.
* Selenium WebDriver (v4+) - Herramienta para la automatización del navegador.
* Pytest-HTML - Plugin de pytest para generar reportes interactivos en HTML.
* Selenium Manager (Integrado en Selenium 4) - Administra la descarga y actualización de ChromeDriver.

---

## Estructura del Proyecto

```text
pre-entrega-automation-testing-mailen-barba/
│
├── utils/
│   ├── __init__.py
│   └── driver_factory.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_saucedemo.py
│
├── reports/
│   ├── reporte.html
│   └── screenshots/
│
├── requirements.txt
└── README.md
```

---

## Instrucciones de Instalación y Configuración

Sigue estos pasos para configurar el entorno de ejecución en tu máquina:

### 1. Clonar el repositorio u obtener los archivos
Asegúrate de estar dentro del directorio del proyecto.

### 2. Crear un entorno virtual
Es una buena práctica crear un entorno virtual para aislar las librerías del proyecto. Ejecuta en tu terminal:

En Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

En Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias
Instala los paquetes requeridos definidos en requirements.txt:
```bash
pip install -r requirements.txt
```

---

## Ejecución de las Pruebas

Para correr todas las pruebas y generar el reporte de ejecución HTML, ejecuta el siguiente comando en la raíz del proyecto:

```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html
```

* -v: Habilita el modo detallado (verbose) en la consola.
* --html=reports/reporte.html: Guarda el reporte final en la carpeta reports/ con el nombre reporte.html.

Si deseas que el archivo HTML sea autocontenido (con los estilos CSS incrustados), puedes agregar la bandera `--self-contained-html`:
```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html
```

Si deseas ver las impresiones de consola generadas por los tests (como el nombre y precio del primer producto encontrado), añade la bandera -s:
```bash
pytest tests/test_saucedemo.py -v -s --html=reports/reporte.html --self-contained-html
```

---

## Casos de Prueba Implementados

Los casos de prueba están definidos dentro de tests/test_saucedemo.py:

1. test_login_success:
   * Navega a la pantalla de login.
   * Completa el login usando credenciales válidas con esperas explícitas.
   * Valida la redirección a la página de inventario y comprueba que se visualicen los elementos "Products" y "Swag Labs".

2. test_inventory_navigation:
   * Realiza login automático.
   * Comprueba que el título de la pestaña del navegador sea "Swag Labs".
   * Verifica la presencia de productos en la UI.
   * Imprime en la consola el nombre y precio del primer producto del catálogo.
   * Valida la presencia de elementos del menú de hamburguesa y el menú desplegable de filtros.

3. test_add_to_cart_and_verify:
   * Realiza login automático.
   * Agrega el primer producto disponible al carrito de compras.
   * Comprueba que el contador de la bolsa de compras se actualice a "1".
   * Navega hacia la pantalla del carrito.
   * Valida que el producto agregado coincida en el carrito.