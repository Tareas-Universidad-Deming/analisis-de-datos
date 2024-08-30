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
- Crear un entorno virtual (opcional) `virtualenv venv --python=python3.10`
- Instalar las librerías necesarias: `pip install -r requirements.txt`

## Ejecución
1. Clonar el repositorio: `git clone`
2. Acceder a la carpeta del proyecto: `cd analisis de datos universidad`
3. Ejecutar el archivo que genera los datos: `python generate_data.py`
4. Ejecutar el archivo principal: `python main.py`
5. Seleccionar los datos y el tipo de gráfico deseado.
6. Visualizar y guardar los gráficos generados.