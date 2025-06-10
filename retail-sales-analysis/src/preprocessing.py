def manejar_valores_faltantes(datos):
    # Reemplazar valores faltantes con la media de cada columna
    for i in range(datos.shape[1]):
        media = np.nanmean(datos[:, i])
        datos[np.isnan(datos[:, i]), i] = media
    return datos

def normalizar_datos(datos):
    # Normalizar los datos a un rango de 0 a 1
    min_valores = np.min(datos, axis=0)
    max_valores = np.max(datos, axis=0)
    datos_normalizados = (datos - min_valores) / (max_valores - min_valores)
    return datos_normalizados

def preprocesar_datos(ruta_archivo):
    datos = cargar_datos(ruta_archivo)
    datos_limpios = manejar_valores_faltantes(datos)
    datos_normalizados = normalizar_datos(datos_limpios)
    return datos_normalizados

if __name__ == "__main__":
    ruta = 'data/retail_sales_dataset.csv'
    datos_preprocesados = preprocesar_datos(ruta)
    print("Datos preprocesados:")
    print(datos_preprocesados[:5])  # Mostrar las primeras 5 filas de los datos preprocesados