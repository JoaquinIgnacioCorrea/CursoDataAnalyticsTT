# SECCION 1
# CONSIGNA: Cargar el conjunto de datos.

import pandas as pd

datos = pd.read_csv('Clase 5/data_clientes.csv')

# CONSIGNA: Identificar y eliminar las filas duplicadas.
# Usarás técnicas específicas para encontrar y eliminar cualquier registro duplicado que pueda afectar la calidad de tu análisis. 
# No olvides escribir un reporte de los hallazgos y modificaciones.

duplicados = datos[datos.duplicated()]

cant_datos = len(datos)
cant_duplicados = len(duplicados)

print(f'Cantidad de filas: {cant_datos}\nCantidad de filas duplicadas: {cant_duplicados}\n')
print(duplicados)

# Identificamos cantidas de filas duplicadas y las eliminamos

datos_sin_duplicados = datos.drop_duplicates()
cant_datos = len(datos_sin_duplicados)

print(f'Cantidad de filas eliminando duplicados: {cant_datos}')
print(datos_sin_duplicados)

# CONSGINA: Manejar los datos faltantes en la columna de edad, evaluando cuál es la mejor decisión, 
# considerando que vamos a realizar un análisis enfocado en grupos etarios de los clientes. 
# Evaluar el impacto sobre el análisis si:
# Se eliminan las filas que no contienen la edad.
# Se completa el dato con la media de la columna.

datos_faltantes = datos_sin_duplicados[datos_sin_duplicados.isna().any(axis=1)]
cant_datos_faltantes_columnas = datos_sin_duplicados.isna().sum()
cant_datos_faltantes = cant_datos_faltantes_columnas.sum()

print(f'Cantidad de columnas con datos faltantes por columna: \n{cant_datos_faltantes_columnas}\n \
Cantidad de filas con datos faltantes: {cant_datos_faltantes}')
print(datos_faltantes)

datos_sin_nulos = datos_sin_duplicados.dropna(subset="Edad")

# Parseo de edad a entero
datos_sin_nulos['Edad'] = datos_sin_nulos['Edad'].astype(int)
cant_datos = len(datos_sin_nulos)

print(f'Cantidad de filas eliminando nulos: {cant_datos}\n')
print(datos_sin_nulos)

# SECCION 2
# CONSIGNA: Cargar el conjunto de datos.

datos2 = pd.read_csv('Clase 5/productos.csv')

# CONSIGNA: Corregir el tipo de datos de la columna de precio a un tipo numérico.
datos2_tipos_por_columna = datos2.dtypes

# Formateamos columna precio
datos2['Precio'] = datos2['Precio'].str.replace('$','')
datos2['Precio'] = datos2['Precio'].astype(float)

print(f'Tipo de datos por columna original:\n{datos2_tipos_por_columna}\n \
      Tipo de datos modificando precio:\n{datos2.dtypes}\n{datos2.head()}')

# CONSIGNA: Normalizar el nombre del producto para que todas las entradas estén en minúsculas y sin caracteres especiales.

datos2['Producto'] = datos2['Producto'].astype(str).str.strip().str.replace({'ñ':'n','á':'a','ó':'o'}).str.lower()
print(f'Datos normalizados en nombre y precio:\n{datos2.head()}')
