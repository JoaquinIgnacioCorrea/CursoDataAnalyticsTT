import pandas as pd
import seaborn as sns

df_titanic = sns.load_dataset('titanic')

# SECCION 1
# CONSIGNA: Filtrar pasajeros sobrevivientes: Tu primer paso será identificar y extraer a los pasajeros que lograron sobrevivir al desastre.

df_pasajeros_sobrevivientes = df_titanic[df_titanic['alive'] =='yes']

print(df_pasajeros_sobrevivientes)

# CONSIGNA: Seleccionar columnas relevantes: De los sobrevivientes, deberás extraer únicamente las columnas que te interesan para el análisis: 
# 'sex', 'age' y 'fare'.

df_columnas_interes = df_pasajeros_sobrevivientes[['sex','age','fare']]

print(df_columnas_interes)

# CONSIGNA: Crear una nueva columna: Vas a agregar una nueva columna al DataFrame que clasifique a cada pasajero según la clase en la que 
# viajaban, etiquetándola como una categoría

categorias = {"First":"Categoria A","Second":"Categoria B","Third":"Categoria C"}

df_columnas_interes['categoria'] = df_pasajeros_sobrevivientes['class'].astype(str).map(categorias)

print(df_columnas_interes.head())

# SECCION 2
# CONSGINA: Obtener los nombres de las columnas del DataFrame.

columnas = df_titanic.columns
print(f"Nombres de columnas:\n{columnas}")

# CONSIGNA: Eliminar la columna 'deck'. (tener en cuenta que puede contener valores nulos y la función puede dar advertencias).
df_titanic_copy = df_titanic.copy()
df_titanic_copy = df_titanic_copy.drop(columns=['deck'])
print(f"Columnas de dataframe sin columna 'deck':\n{df_titanic_copy.columns}")

# CONSIGNA: Reindexar el DataFrame después de eliminar la columna.

df_titanic_copy = df_titanic_copy.reset_index(drop=True)
print(f'Reindexación de dataframe tras eliminacion de columna:\n{df_titanic_copy}')