def cargar_datos(ruta_archivo):
    datos = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1, dtype=float)
    return datos

def guardar_datos(ruta_archivo, datos):
    np.savetxt(ruta_archivo, datos, delimiter=',', header='Header1,Header2,...', comments='')

def imprimir_datos(datos):
    for fila in datos:
        print(fila)