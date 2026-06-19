# Proyecto Delimitación FDP Ciclo 3

Sistema de consola (CLI) en Python diseñado para automatizar la gestión de inventario y estiba de la bodega "El Ahorro". Su objetivo principal es reducir las pérdidas por aplastamiento (mermas) mediante la asignación inteligente de zonas de almacenamiento según el tipo de empaque. El sistema procesa registros, valida entradas, calcula alertas de daño en tiempo real y asegura la persistencia del inventario en archivos de texto plano.

## 🚀 Comenzar

Para ejecutar este proyecto localmente, asegúrate de tener instalado Python y corre el archivo principal desde tu terminal:

```bash
python main.py

```

## 📂 Estructura del Proyecto

* **`main.py`**: Archivo principal que ejecuta la aplicación y controla el menú interactivo.
* **`modulos_bodega.py`**: Módulo que contiene las funciones matemáticas, validaciones y lógica de negocio de la bodega.
* **`reporte_inventario.txt`**: Archivo de texto autogenerado por el sistema donde se guarda físicamente el registro de la sesión.
