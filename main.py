import pandas as pd
import matplotlib.pyplot as plt
import os


# Directorio donde se guardan los archivos
data_dir = os.getcwd()
# Ruta a la carpeta de descargas del usuario
if os.name == 'nt':  # Windows
    download_folder = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
else:  # macOS y Linux
    download_folder = os.path.join(os.getenv('HOME'), 'Downloads')


# Listar archivos de datos disponibles
def list_files():
    files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    print("Archivos disponibles:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")
    return files


# Cargar datos desde un archivo CSV seleccionado
def load_data(archivo):
    return pd.read_csv(os.path.join(data_dir, archivo))


# Mostrar opciones de gráficos
def show_menu_graphs():
    print("\nSeleccione el tipo de gráfico que desea generar:")
    print("1. Gráfico de Barras")
    print("2. Gráfico de Líneas")
    print("3. Gráfico de Pastel")
    print("4. Gráfico de Dispersión")
    print("5. Salir")
    option = input("Seleccione una opción: ")
    return option


# Generar gráfico según la elección del usuario
def generate_graph(df, graph_option):
    if graph_option == '1':
        df.plot(kind='bar', x=df.columns[-1])
        plt.title("Gráfico de Barras")
        plt.grid(True)
        file_path = os.path.join(download_folder, 'grafico_de_barras.png')
        plt.savefig(file_path)
    elif graph_option == '2':
        df.plot(kind='line', x=df.columns[-1])
        plt.title("Gráfico de Líneas")
        plt.grid(True)
        file_path = os.path.join(download_folder, 'grafico_de_lineas.png')
        plt.savefig(file_path)
    elif graph_option == '3':
        df.iloc[:, :-1].sum().plot(kind='pie', autopct='%1.1f%%')
        plt.title("Gráfico de Pastel")
        file_path = os.path.join(download_folder, 'grafico_de_pastel.png')
        plt.savefig(file_path)
    elif graph_option == '4':
        if df.shape[1] >= 3:
            file_path = os.path.join(download_folder, 'grafico_de_dispersion.png')
            plt.figure(figsize=(10, 6))
            x, y = df.iloc[:, -1], df.iloc[:, :-1]
            counter = 0
            colors = ['orange', 'blue', 'red', 'black']
            labels = y.columns.to_list()
            for col in y.columns:
                plt.scatter(x, y[col], color=colors[counter], label=labels[counter])
                counter += 1

            plt.grid(True)
            plt.ylabel(", ".join(labels))
            plt.xlabel("Estudiantes")
            plt.tight_layout(pad=3.0, rect=(0, 0, 0.9, 1))
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.xticks(rotation=90)
            plt.title("Gráfico de Dispersión")
            plt.savefig(file_path)
        else:
            print("El archivo seleccionado no tiene suficientes columnas para generar un gráfico de dispersión.")
            return
    else:
        print("Opción no válida.")
        return

    plt.show()
    print(fr"Gráfico guardado en: {file_path}")


# Función principal
def main():
    files = list_files()
    selection = int(input("\nSeleccione el archivo que desea analizar: ")) - 1
    if selection < 0 or selection >= len(files):
        print("Selección no válida.")
        return

    df = load_data(files[selection])
    print(f"\nDatos cargados del archivo: {files[selection]}")
    print(df.head())

    while True:
        graph_option = show_menu_graphs()
        if graph_option == '5':
            print("Saliendo...")
            break
        generate_graph(df, graph_option)


if __name__ == "__main__":
    main()
