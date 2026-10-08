import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# SECCION 1
# CONSIGNA: Importar las bibliotecas necesarias y cargar el conjunto de datos “diamonds” de Seaborn. 

diamonds = sns.load_dataset("diamonds")

# CONSGINA: Visualizar las primeras filas del DataFrame para comprender la estructura de los datos.

print(f"Primeras 3 filas del dataframe 'Diamonds':\n{diamonds.head(3)}")
print(f"Tipo datos:\n{diamonds.dtypes}\nColumnas:\n{diamonds.columns}")

# CONSIGNA: Realizar un resumen estadístico de los datos y observar las características de las variables numéricas.

print(diamonds.describe())

# CONSIGNA: Crear un gráfico de distribución de los precios con Seaborn.

sns.histplot(diamonds["price"],bins=20,kde=True)
plt.title("Distribucion de precios en diamantes")
plt.xlabel("Precio")
plt.ylabel("Frecuencia del precio")
plt.show()

# CONSGINA: Crear un gráfico de distribución por color.

sns.countplot(data=diamonds, x="color")
plt.title("Distribucion de colores en diamantes")
plt.xlabel("Color")
plt.ylabel("Frecuencia de colores")
plt.show()

# CONSGINA: Interpretá los resultados e intentá justificar la elección de los gráficos.

# Se puede observar que se frecuenta una mayor cantidad de diamantes a precios accesibles ante los diamantes costosos
# Por otro lado veo que los colores mas solicitados son G,E y F teniendo una solicitud por encima de las 9000 unidades

# SECCION 2
# CONSGINA: Cargá la base de datos “titanic” y visualizá las primeras filas.

titanic = sns.load_dataset("titanic")
print(titanic.head())

# CONSGINA: Realizá un análisis estadístico básico de la tasa de supervivencia por clase de pasajero.

titanic1 = titanic.groupby("class")["alive"]
titanic2 = titanic1.value_counts()
titanic1 = round(titanic1.value_counts(normalize=True) * 100,2)
print(titanic1, titanic2)

# CONSGINA: Creá un gráfico de barras que muestre la tasa de supervivencia por clase.

titanic1 = titanic1.reset_index()
supervivientes = titanic1[titanic1["alive"] == "yes"]

plt.bar(supervivientes["class"], supervivientes["proportion"])
plt.title("Tasa de supervivencia por clase")
plt.xlabel("Clases")
plt.ylabel("Tasa de supervivencia (procentaje)")
plt.show()

# CONSGINA: Analizá si existe alguna correlación entre la edad de los pasajeros y su tasa de supervivencia, 
# utilizando un diagrama de caja (box plot).

sns.boxplot(data=titanic, x="alive", y="age")
plt.show()