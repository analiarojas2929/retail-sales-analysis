import pandas as pd
import numpy as np

def calcular_total_ventas_por_categoria(df):
    """
    Calcula el total de ventas por categoría.
    """
    # Usamos los nombres correctos de las columnas
    return df.groupby('Product Category')['Total Amount'].sum()

def calcular_promedio_ventas_diarias(df):
    """
    Calcula el promedio de ventas diarias.
    """
    # Aseguramos que la fecha sea datetime
    df['Date'] = pd.to_datetime(df['Date'])
    return df.groupby('Date')['Total Amount'].mean()

def identificar_categorias_extremas(total_ventas):
    categorias_ordenadas = sorted(total_ventas.items(), key=lambda x: x[1])
    menor_categoria = categorias_ordenadas[0]
    mayor_categoria = categorias_ordenadas[-1]
    
    return menor_categoria, mayor_categoria

if __name__ == "__main__":
    ruta = 'data/retail_sales_dataset.csv'
    datos = pd.read_csv(ruta)
    
    total_ventas = calcular_total_ventas_por_categoria(datos)
    promedio_ventas_diarias = calcular_promedio_ventas_diarias(datos)
    menor_categoria, mayor_categoria = identificar_categorias_extremas(total_ventas)
    
    print("Total de ventas por categoría:", total_ventas)
    print("Promedio de ventas diarias:", promedio_ventas_diarias)
    print("Categoría con menor venta:", menor_categoria)
    print("Categoría con mayor venta:", mayor_categoria)