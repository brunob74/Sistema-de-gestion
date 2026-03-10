# 📦 Sistema de Gestión de Inventario y Ventas (POS)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey.svg)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-darkgreen.svg)

## 📖 Descripción del Proyecto
Una aplicación de escritorio robusta y escalable desarrollada en Python para automatizar la administración operativa de pequeñas y medianas empresas (PyMEs). El sistema está diseñado para reemplazar los registros manuales, ofreciendo un Punto de Venta (POS) eficiente, control de stock en tiempo real y persistencia segura de datos sin necesidad de servidores externos.

## Funcionalidades Principales
* **Punto de Venta (POS) Dinámico:** Registro de transacciones multiproducto con cálculo automático de subtotales y totales.
* **Control de Stock en Tiempo Real:** Verificación inmediata de disponibilidad de artículos y actualización automática del inventario post-venta.
* **Lógica de Compensación y Anulación:** Sistema de seguridad que reintegra automáticamente los artículos al inventario general al modificar o anular una venta, garantizando la consistencia matemática de los datos ($S'_{i}=S_{i}-\sum_{j=1}^{n}V_{ij}$).
* **Reportes y Trazabilidad:** Generación de listados de ventas diarias e históricas filtrables por cliente, permitiendo auditorías rápidas.
* **Arquitectura Local Segura:** Utilización de SQLite para garantizar la persistencia e integridad de la información comercial ante cortes de energía o cierres inesperados.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.10+
* **Base de Datos Racional:** SQLite3 (Librería nativa)
* **Interfaz Gráfica (GUI):** CustomTkinter / Tkinter
* **Procesamiento de Datos:** Pandas

## Instalación y Uso

1. Clonar el repositorio:
    ```bash
    git clone [https://github.com/brunob74/Sistema-de-gestion.git](https://github.com/brunob74/Sistema-de-gestion.git)

2. Instalar dependencias:
    ```bash
    pip install customtkinter pandas

3. Inicializar la base de datos (creará las tablas estructurales y un set de datos de prueba):
    ```bash
    python inicializador_db.py

4. Ejecutar la aplicación principal:
    ```bash
    python main.py


👨‍💻 Autor
Bruno Santiago Mangini
Técnico Electromecánico | Estudiante de Ing. en Sistemas de Información
