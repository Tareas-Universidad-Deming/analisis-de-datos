# Proyecto de la materia Programación en Python - Orientado a la analítica de datos.

## Descripción
Este proyecto está diseñado para ofrecer una experiencia interactiva de análisis de datos y visualización gráfica usando Python.
### Componentes del Proyecto:
1. Generador de Datos (generate_data.py): <br />
Este archivo es responsable de crear y guardar datos de ejemplo en archivos CSV.

2. Interfaz de Usuario (main.py): <br />
Este archivo permite al usuario seleccionar los datos a analizar y el tipo de gráfico a generar. 
La interfaz solicita al usuario que elija los datos y el tipo de gráfico deseado (por ejemplo, gráficos de dispersión). 
<br/>
El archivo gestiona la carga de los datos, la generación de gráficos y su visualización, así como la opción de guardar los gráficos en la carpeta de descargas del usuario.
<br/>
<br/>
Este enfoque modular facilita la separación de la generación de datos y la interacción del usuario, proporcionando una plataforma flexible para análisis de datos y visualización gráfica en Python.

## Requisitos
- Tener instalado Python 3.10
- Tener instalado pip
- Tener instalado git
- Tener instalado virtualenv (opcional - recomendado) `pip install virtualenv`

## Ejecución
1. Clonar el repositorio: `git clone https://github.com/Tareas-Universidad-Deming/analisis-de-datos.git`
2. Acceder a la carpeta del proyecto: `cd analisis-de-datos`
3. Crear un entorno virtual (opcional - recomendado) `virtualenv venv --python=python3.10`
   - Activar el entorno virtual: <br />
    `source venv/bin/activate` (Linux y MacOS) <br />
    `venv\Scripts\activate` (Windows)
4. Instalar las librerías necesarias: `pip install -r requirements.txt`
5. Ejecutar el archivo que genera los datos: `python generate_data.py`
6. Ejecutar el archivo principal: `python main.py`
7. Seleccionar los datos y el tipo de gráfico deseado.
8. Visualizar y guardar los gráficos generados.

## Integrantes
- Ruiz Navas Wilfred Junior 

## Entrega
- 13 de septiembre de 2024
- Instituto Superior Tecnológico Universitario Corporativo Edwards Deming
- Programación en Python - Orientado a la analítica de datos
- Profesor: Ing. Gallardo Arias, Italo Gualberto
- Quito, Ecuador
- 2024

## Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](https://github.com/Tareas-Universidad-Deming/analisis-de-datos/blob/main/LICENSE.txt) para más detalles.

![Licencia MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)
![Versión 1.0](https://img.shields.io/badge/Versión-1.0-blue.svg)