import numpy as np
import pandas as pd
import os


# Directorio donde se guardarán los archivos
output_dir = os.path.join(os.getcwd())


# Generar datos de ventas
def generate_sales_data():
    products = ['Producto A', 'Producto B', 'Producto C', 'Producto D']
    sales = np.random.randint(50, 200, size=(10, len(products)))
    df_sales = pd.DataFrame(sales, columns=products)
    df_sales['Mes'] = [f'Mes {i}' for i in range(1, 11)]
    df_sales.to_csv(os.path.join(output_dir, 'datos_ventas.csv'), index=False, encoding='utf-8')
    print("Archivo 'datos_ventas.csv' generado.")


# Generar datos de temperaturas
def generate_temp_data():
    cities = ['Ciudad A', 'Ciudad B', 'Ciudad C', 'Ciudad D']
    temps = np.random.uniform(15, 40, size=(12, len(cities)))
    df_temps = pd.DataFrame(temps, columns=cities)
    df_temps['Mes'] = [f'Mes {i}' for i in range(1, 13)]
    df_temps.to_csv(os.path.join(output_dir, 'datos_temperaturas.csv'), index=False, encoding='utf-8')
    print("Archivo 'datos_temperaturas.csv' generado.")


# Generar datos de calificaciones
def generate_ratings_data():
    students = [f'Estudiante {i}' for i in range(1, 21)]
    courses = ['Matemáticas', 'Ciencias', 'Historia', 'Arte']
    ratings = np.random.randint(50, 100, size=(len(students), len(courses)))
    df_ratings = pd.DataFrame(ratings, columns=courses)
    df_ratings['Estudiante'] = students
    df_ratings.to_csv(os.path.join(output_dir, 'datos_calificaciones.csv'), index=False, encoding='utf-8')
    print("Archivo 'datos_calificaciones.csv' generado.")


# Ejecutar las funciones para generar los archivos
if __name__ == "__main__":
    generate_sales_data()
    generate_temp_data()
    generate_ratings_data()
