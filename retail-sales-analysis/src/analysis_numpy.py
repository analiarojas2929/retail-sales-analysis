import numpy as np

def cargar_datos(ruta_archivo):
    datos = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1, dtype=float)
    return datos

if __name__ == "__main__":
    ruta = '../data/retail_sales_dataset.csv'
    datos = cargar_datos(ruta)
    print("Datos cargados:")
    print(datos[:5])  # Mostrar las primeras 5 filas