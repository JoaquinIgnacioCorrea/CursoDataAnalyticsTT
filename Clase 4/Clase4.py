# SECCION 1
# CONSIGNA: Descargá los datos en formato CSV y cargalos en un DataFrame en Python usando Pandas. 
# Utilizá el método isnull() para identificar las filas con datos faltantes y contar el número de valores nulos por columna.

import pandas as pd
import numpy as np

datos = pd.read_csv('Clase 4/satis_clientes.csv')

# 1.1.Identificar datos faltantes por celdas
print(datos.isnull())

# # 1.2. Identificar datos faltantes por filas
print(datos.isnull().any(axis=1).head(5))

# # 2.Cantidad de datos faltantes por columna
print(datos.isnull().sum())

# CONSIGNA: Usá el método duplicated() para identificar las filas duplicadas y contar cuántas filas duplicadas hay en total

# 1.1. Muestra las filas con datos duplicados por celdas
print(datos[datos.duplicated()])

# 1.2. Identificar datos duplicados por filas
print(datos.duplicated())

# 2. Cantidad de filas repetidas
print(datos.duplicated().sum())

# CONSIGNA: Creá un informe que incluya: La cantidad total de registros en el DataFrame.
# La cantidad total de valores nulos por columna y La cantidad de filas duplicadas.
totalData = len(datos) #Cantidad de filas
totalNullValues = datos.isnull().sum().sum() #Cantidad de valores nulos
totalDuplicatedRows = datos.duplicated().sum() #Cantidad de filas repetidas

print(f"\nCantidad total de registros: {totalData}\nCantidad total de valores nulos: {totalNullValues}\n\
Cantidad de filas duplicadas: {totalDuplicatedRows}")

# CONSIGNA: Creá un dataframe de los registros duplicados para que se vea el contenido.
duplicatedData = datos[datos.duplicated()]
print(duplicatedData)

# SECCION 2
# CONSIGNA: Creá un dataframe a partir de la planilla de cálculo y efectuá un examen preliminar.
seguimiento_paciente = pd.read_excel('Clase 4/Actividad 2.xlsx')

spDatosNulos = seguimiento_paciente.isnull().sum()
spTotalDatosNulos = spDatosNulos.sum()
print(f'Cantidad de datos nulos por columna:\n{spDatosNulos[1:].to_string()}\nCantidad total de datos nulos: {spTotalDatosNulos}')

spFilasDuplicadas = seguimiento_paciente[seguimiento_paciente.duplicated()]
spCantidadFilasDuplicadas = seguimiento_paciente.duplicated().sum()

print(f'Cantidad de filas duplicadas: {spCantidadFilasDuplicadas}')

# CONSIGNA: Analizá cuál sería el mejor tratamiento para los datos anómalos (fuera de rango) y nulos en los siguientes contextos:
# Contextos: 1.Estudio estadistico 2.Seguimiento de un paciente 3.Deteccion de casos de contagio
# Tratamientos: 1.Ignorar 2.Eliminar 3.Reemplazar 4.Analizar

# Estudio estadistico: datos nulos -> Reemplazar-Eliminar / datos anomalos -> Reemplazar
# Seguimiento de un paciente: datos nulos -> Analizar / datos anomalos -> Analizar
# Deteccion de casos de contangio: datos nulos -> Reemplazar-Analizar / datos anomalos -> Reemplazar