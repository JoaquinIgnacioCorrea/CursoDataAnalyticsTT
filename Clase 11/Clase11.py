import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("diamonds")

# SECCION 1
# CONSGINA: Calcular la correlación entre precio y quilates de los diamantes color “F” y corte Premium.

# a. Analizamos formato del dataframe

print(f"Primeras 5 filas:\n{df.head(3)}") 

# b. Filtramos los diamantes con color f
diamantes_f = df[(df["color"] == "F") & (df["cut"] == "Premium")]

print(f"Dataframe con filtrado de diamantes color 'F' y calidad 'Premium':\n{diamantes_f.head(3)}")
print(f"Infor del nuevo dataframe:\n{diamantes_f.info()}")

# c. Eliminamos columnas que fueron filtros (sabemos que su valores se van a repetir)
diamantes_f.drop(["color","cut"],axis='columns',inplace=True)

# d. Generamos la correlacion entre precio y kilates de los diamantes color f calidad premium
correlacion_price_carat = diamantes_f["price"].corr(diamantes_f["carat"], method="pearson")
print(f"Correlacion entre precio/kilates en diamantes f calidad premium:\n{correlacion_price_carat}")
# Comentario: Vemos que la correlacion tiene una tendencia a una correlacion positiva fuerte

# CONSIGNA: Visualizar los resultados mediante gráfico de dispersión.

# a. Generamos el grafico estableciendo los ejes(eje x -> kilates / eje y -> precio)
sns.scatterplot(x="carat",y="price",data=diamantes_f)
plt.title("Distribucin precio y kilates en diamantes J calidad premium")
plt.xlabel("Kilates")
plt.ylabel("Precio")
plt.show()

# Observacion: Apreciamos que la correlacion es positiva debil, mientras los kilates 
# aumentan el precio lo hace pero de manera inconsistente

# SECCION 2
# CONSGINA: Observar cómo se distribuyen los pesos de los pingüinos según su especie.

# a. Importamos el dataset de pinguinos

penguins = sns.load_dataset("penguins")

# b. Revisamos que no tenga datos nulos y vemos estructura del dataset

print(f"Informacion de nulos:\n{penguins.info()}\nPrimeras 3 filas del dataset:\n{penguins.head(3)}")

# c. Creamos el grafico de distribuccion de los pinguinos de especie/peso 
sns.scatterplot(x="species",y="body_mass_g",data=penguins)
plt.title("Distribucion peso por especie en pinguinos")
plt.xlabel("Especies")
plt.ylabel("Peso")
plt.show()

# CONSGINA: Visualizar la distribución de características clave:
# Longitud del pìco
# Longitud de la aleta

# a. Generamos el diagrama de distribucion, en el mismo discriminamos por especies las longitud de aleta y pico
sns.scatterplot(x="bill_length_mm",y="flipper_length_mm",data=penguins,hue="species",style="species")
plt.title("Distribucion longitud de aleta y pico por especies")
plt.legend(title="Especies")
plt.xlabel("Pico")
plt.ylabel("Aleta")
plt.show()

# Observacion: Con esto vemos que la especie Adelie presenta una longitud de pico y aleta menor al resto
# la especie Chinstrap tiene una mayor tendencia de longitud de pico mas largos y tiene una longitud de aletas promedio
# por otro lado, la especie Gento presenta una longitud de aleta mayor a las otras especies y una longitud de pico tendiendo a la mas larga

# CONSGINA:Desglosar por ubicación geográfica: Mostrar para cada ubicación, analítica y gráficamente la distribución de:
# 1.Ejemplares por sexo
# 2.Ejemplares por especie
# 3.Desafio: por especie y sexo

# 1.a. Generamos descripcion de distribucion de sexo por islas, cantidades y porcentajes
penguins2 = penguins.dropna(ignore_index=True)

dist_sex = penguins2.groupby(["island"])["sex"]
describe_dist_sex = dist_sex.describe()
count_dist_sex = dist_sex.value_counts()
por_dist_sex = round(dist_sex.value_counts(normalize=True) * 100, 2)

print(f"Distribucion del sexo de los pinguinos por isla:\n{describe_dist_sex}\n\
Cantidad pinguinos por isla discriminado por sexo:\n{count_dist_sex}\n\
Porcentaje por cantidad de pinguinos por isla discriminado por sexo:\n{por_dist_sex}")

# b. Generamos distribucion grafica

sns.countplot(data=penguins,x="island",hue="sex")
plt.title("Distribucion del sexo de los pinguinos por isla")
plt.legend(title="Sexo")
plt.xlabel("Islas")
plt.ylabel("Cantidad de pinguinos")
plt.show()

# 2.a. Generamos distribucion analitica

dist_specie = penguins.groupby(["island"])["species"]
describe_dist_specie = dist_specie.describe()
count_dist_specie = dist_specie.value_counts()
por_dist_specie = round(dist_specie.value_counts(normalize=True) * 100,2)

print(f"Descripcion de distribucion por especie por isla:\n{describe_dist_specie}\n\
Cantidad de pinguinos por especie por isla:\n{count_dist_specie}\n\
Porcentaje de pinguinos por especie por isla:\n{por_dist_specie}")

# b. Generamos distribucion grafica

sns.countplot(penguins,x="island",hue="species")
plt.title("Distribucion de especies de pinguinos por islas")
plt.legend(title="Especie")
plt.xlabel("Islas")
plt.ylabel("Especies")
plt.show()

# 3.a. Generamos distribucion analitica

describe_dist_specie_sex = penguins2.groupby(["island","species","sex"],as_index=False).describe()
count_dist_specie_sex = penguins2.groupby(["island","species","sex"]).size()
por_dist_specie_sex = round(penguins2.groupby(["island","species"])["sex"].value_counts(normalize=True) * 100,2)

print(f"Distribucion de pinguinos por isla, sexo y especie:\n{describe_dist_specie_sex}\n\
Distribucion con su cantidad:\n{count_dist_specie_sex}\n\
Distribucion en porcentajes:\n{por_dist_specie_sex}")

# b. Generamos distribucion grafica
grafico_dist_sex_specie = por_dist_specie_sex.rename("porcentaje").reset_index()
sns.catplot(data=grafico_dist_sex_specie,x="species",y="porcentaje",hue="sex",col="island",kind="bar")
plt.ylabel("Porcentaje por sexo")
plt.show()

# CONSIGNA: Calcular la matriz de correlación y visualizarla
penguins.drop(["species","island","sex"],axis="columns",inplace=True)

matrix_pinguinos = penguins.corr()
sns.heatmap(matrix_pinguinos, annot=True, cmap="coolwarm")
plt.title("Correlacion entre profundidad de pico, masa del cuerpo, largo de aleta y pico")
plt.show()

# CONSGINA: Explorar, interpretar y mostrar gráficamente las variables que tienen
# Mayor correlación.
# Menor correlación.

# Observaciones: podemos apreciar que hay una correlacion alta entre largo de aleta e pico y el peso del pinguino
# como en el largo de la aleta y pico
# De esta forma deducimos que parte del peso del pinguino esta fuertemente asociado a la longitud de su pico y extremidades, 
# mientras que le largo de estas tiene una correlacion positiva relativamente fuerte.