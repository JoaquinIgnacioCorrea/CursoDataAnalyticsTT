import numpy as np
from scipy import stats

# SECCION 1
# CONSIGA: Calcular la media de las ventas.

ventas = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Ventas (millones)': [1.2, 2.5, 3.1, 18.3, 40.5, 52.1, 54.8, 46.2,
                          25.5, 13.8, 11.9, 9.2]
}

media = round(np.mean(ventas["Ventas (millones)"]),2)
print(f"Media de ventas: {media}")

# COSIGNA: Calcular la mediana de las ventas.

mediana = np.median(ventas["Ventas (millones)"])
print(f"Mediana de ventas: {mediana:.2f}")

# CONSIGNA: Calcular la moda de las ventas.

moda = stats.mode(ventas["Ventas (millones)"])[0]
print(f"Moda de ventas : {moda}")

# SECCION 2
# CONSGINA: Calcular el rango de las ventas.

max_ventas = np.max(ventas["Ventas (millones)"])
min_ventas = np.min(ventas["Ventas (millones)"])
rango = max_ventas - min_ventas
print(f"Rango de ventas: {rango:.2f}")

# CONSGINA: Calcular la varianza de las ventas.

varianza = np.var(ventas["Ventas (millones)"])
print(f"Varianza de ventas: {varianza:.2f}")

# CONSGINA: Calcular la desviación standard de las ventas.

desvio_estandar = np.std(ventas["Ventas (millones)"])
print(f"Desvio estandar de ventas: {desvio_estandar:.2f}")

print("El mes de mayor ventas es en julio, se teoriza que se ajusta a un aumento considerable de bufandas")