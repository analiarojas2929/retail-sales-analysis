import numpy as np
import matplotlib.pyplot as plt

def graficar_ventas_por_categoria(categorias, ventas):
    plt.figure(figsize=(10, 6))
    plt.bar(categorias, ventas, color='skyblue')
    plt.title('Ventas por Categoría')
    plt.xlabel('Categorías')
    plt.ylabel('Total de Ventas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graficar_ventas_diarias(fecha, ventas_diarias):
    plt.figure(figsize=(12, 6))
    plt.plot(fecha, ventas_diarias, marker='o', linestyle='-', color='orange')
    plt.title('Ventas Diarias')
    plt.xlabel('Fecha')
    plt.ylabel('Ventas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()