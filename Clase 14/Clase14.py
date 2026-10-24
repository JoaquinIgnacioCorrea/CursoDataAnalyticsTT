import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# SECCION 1
# CONSGINA: Cargá el dataset y visualizá los primeros registros.

# a. Traemos el dataframe que nos proporciona la practica
# Dataset
data = pd.DataFrame({
'cliente': ['Cliente 1', 'Cliente 2', 'Cliente 3', 'Cliente 4', 'Cliente 5'],
'importe_compra': [200, 450, 120, 700, 30],
'mes': ['Enero', 'Enero', 'Febrero', 'Febrero', 'Febrero']
})

# b. Imprimimos el dataframe para visualizar el mismo
print(data)

# CONSIGNA: Creá un boxplot que muestre la distribución de las compras por mes.
# Asegurate de personalizar el gráfico con títulos y etiquetas adecuadas.

sns.boxplot(x="mes",y="importe_compra",data=data, palette="Set2")
plt.title("Distribucion de compras por mes")
plt.xlabel("Mes")
plt.ylabel("Importe de compra")
plt.show()

# SECCION 2
# CONSIGNA: Cargá el dataset y visualiza los primeros registros.

# a. Cargamos el dataset
# Dataset  
data = pd.DataFrame({  
    'categoría': ['Electrónica', 'Electrónica', 'Ropa', 'Ropa', 'Alimentos', 'Alimentos'],  
    'producto': ['Televisor', 'Radio', 'Camisa', 'Pantalón', 'Pan', 'Leche'],  
    'precio': [300, 150, 20, 40, 2, 1.5]  
})

# b. Visualizamos el dataset para comprender estructura

print(data)

# CONSGINA: Creá un subplot que contenga un violin plot mostrando la distribución de precios por categoría, 
# junto con un gráfico de barras que represente el precio promedio por categoría.

fig, axs = plt.subplots(2,1)

sns.violinplot(x="categoría",y="precio",data=data,palette="muted",ax=axs[0])
axs[0].set_title("Distribucion de precios por categoria")
axs[0].set_xlabel("Categorias")
axs[0].set_ylabel("Precios")

promedio_precio = data["precio"].mean()

barplot =sns.barplot(x="categoría",y="precio",data=data,ax=axs[1], color="teal")
axs[1].axhline(y=promedio_precio,color="brown")
axs[1].set_title("Grafico de barras con promedio de ventas por categoria")
axs[1].set_xlabel("Categorias")
axs[1].set_ylabel("Precios")
axs[1]

plt.tight_layout()
plt.show()