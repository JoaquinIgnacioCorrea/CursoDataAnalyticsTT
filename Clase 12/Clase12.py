import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so

# SECCION 1
# CONSGINA: Cargá los conjuntos de datos que contienen la información sobre las ventas, 
# productos y clientes.

clientes = pd.read_csv("Clase 12/clientes.csv")
productos = pd.read_csv("Clase 12/productos.csv")
ventas = pd.read_csv("Clase 12/ventas.csv")

# CONSGINA: Explorá cada DataFrame.

# a. Exploracion clientes
print(f"Primeras 3 filas:\n{clientes.head(3)}\nInfo del dataset:\n{clientes.info()}\n \
Descripcion del dataset:\n{clientes.describe()}")

# b. Exploracion productos
print(f"Primeras 3 filas:\n{productos.head(3)}\nInfo del dataset:\n{productos.info()}\n \
Descripcion del dataset:\n{productos.describe()}")

#c. Exploracion ventas
print(f"Primeras 3 filas:\n{ventas.head(3)}\nInfo del dataset:\n{ventas.info()}\n \
Descripcion del dataset:\n{ventas.describe()}")

# CONSGINA: Limpiá los datos, eliminando duplicados y manejando valores nulos.
# Asegurate de que las columnas de fecha estén en el formato adecuado.

# a. Limpieza clientes
clientes.drop_duplicates(inplace=True)
clientes.ffill(inplace=True)

# b. Limpieza productos
productos.drop_duplicates(inplace=True)
productos.ffill(inplace=True)

# c. Limpieza ventas
ventas.drop_duplicates(inplace=True)
ventas.ffill(inplace=True)

# COSNGINA: Ideá una manera de calcular el total gastado por cada cliente.
# CONSIGNA: En cada paso, documentá tus hallazgos y las modificaciones que vas aplicando.

# a. Mergeamos el dataset clientes y ventas mediante columna "ID_Cliente" (Consolidacion)
clientes_ventas = pd.merge(clientes,ventas, on="ID_Cliente", how="inner")
clientes_ventas_productos = pd.merge(clientes_ventas, productos, on="ID_Producto", how="inner")

# b. Agrupamos el total gastado por cada cliente (Agrupacion y Agregacion)

total_venta_cliente = clientes_ventas_productos.groupby("ID_Cliente").apply(
    lambda x: (x['Precio_Unitario'] * x['Cantidad']).sum()
).reset_index(name="Total_Gasto_Cliente")

# Comentario sobre funcion: Buscamos agrupar el nuevo dataset por cliente y aplicar una funcion lambda
# En la misma recorremos las sig columnas -> "Precio_Unitario" y "Cantidad"
# La operacion recorre cada venta realizada por el cliente, donde, mediante el merge con el dataset productos
# Recuperamos el precio del producto y lo multiplicamos por la cantidad de veces que se compro el mismo
# que se aclara en el dataset ventas
print(total_venta_cliente)

# CONSGINA: Realizá un análisis de las ventas por categoría de producto y visualiza los 
# resultados utilizando gráficos de barras.
total_ventas_categoria = clientes_ventas_productos.groupby("Categoría").apply(
    lambda x: (x["Cantidad"]).sum()
).reset_index(name="Total_Ventas_Categoria")

print(total_ventas_categoria)

sns.barplot(data=total_ventas_categoria,x="Categoría",y="Total_Ventas_Categoria", width=0.4)
plt.title("Cantidad de ventas por categoria")
plt.xlabel("Categorias")
plt.xticks(rotation=90, fontsize="10")
plt.tight_layout()
plt.ylabel("Cant Ventas")
plt.show()

# Analisis: Podemos apreciar un valor aproximado entre 150 a 400 ventas en la mayoria de las categorias
# Teniendo ese rango de promedio aproximado, por otro lado podemos ver que hay categorias con menor flujo de ventas
# Comprendido entre 150 a 100 ventas, despues tenemos datos anomalos donde se presenta un minimo de ventas en
# Seguridad y Vigilancia (8 ventas) y un mGrafico_Asistenciaimo en Electrodomesticos (997 ventas)
# Con esto entendemos que una estrategia de marketing factible seria para la categoria electrodomesticos que produce un buen flujo de ventas
# Mientras que la categoria de seguridad y vigilancia podria contemplarse el corto de importacion o establecer una campaña de marketing para
# Fortalecer el caudal de ventas y observar su potencial bajo una exposicion intencional por parte del cliente

# SECCION 2
# CONSIGNA: Cargá los conjuntos de datos.

talleres = pd.read_csv("Clase 12/talleres.csv")
participantes = pd.read_csv("Clase 12/participantes.csv")
resultados = pd.read_csv("Clase 12/resultados_taller.csv")

# CONSIGNA: Explorá cada DataFrame para familiarizarte con los datos.

# a. Exploramos talleres
print(f"Primeras 3 filas:\n{talleres.head()}\nInformacion del dataset:\n{talleres.info()}\nDescripcion del dataset:\n{talleres.describe()}")

# b. Exploramos participantes
print(f"Primeras 3 filas:\n{participantes.head()}\nInformacion del dataset:\n{participantes.info()}\nDescripcion del dataset:\n{participantes.describe()}")

# c. Exploramos resultados
print(f"Primeras 3 filas:\n{resultados.head()}\nInformacion del dataset:\n{resultados.info()}\nDescripcion del dataset:\n{resultados.describe()}")

# CONSGINA: Limpiá los datos.

# a. Limpieza talleres
talleres.drop_duplicates(inplace=True)
talleres.ffill(inplace=True)

# b. Limpieza participantes
participantes.drop_duplicates(inplace=True)
participantes.ffill(inplace=True)

# c. Limpieza resultados
resultados.drop_duplicates(inplace=True)
resultados.ffill(inplace=True)

# CONSGINA: Combiná los tres conjuntos de datos en un único DataFrame utilizando las claves apropiadas.

Participantes_Talleres_Result = resultados.merge(talleres, on="ID_Taller",how="inner").merge(participantes,on="ID_Participante",how="inner")


# CONSIGNA: Realizá un análisis para calcular la asistencia promedio a los talleres y el puntaje promedio obtenido por los participantes, 
# visualizando los resultados en gráficos.

# En este codigo se establece la cantidad de asistidos, no asistidos y total con sus correspondientes porcentajes por taller
Asistencia_Taller= Participantes_Talleres_Result.groupby("Nombre_Taller").apply(
    lambda x: pd.Series({
    "total_asistidos": (asistieron:=(x["Asistió"] == True).sum()), 
    "total_no_asistidos": (no_asistieron:=(x["Asistió"] == False).sum()), 
    "total_participantes": (total:=len(x)),
    "porcentaje_asistencia": (porcentaje_asistencia:=(((asistieron) / total) * 100)),
    "porcentaje_inasistencia": (porcentaje_no_asistencia:= (100 - porcentaje_asistencia)),
    })
).reset_index()
print(Asistencia_Taller)

# Generamos un grafico de barras horizontal en el cual establecemos los talleres,
# cantidad de asistidos y no asistidos junto apartado visual de barras por discriminacion de asistencia
Grafico_Asistencia = Asistencia_Taller.set_index('Nombre_Taller')[
    ['total_asistidos', 'total_no_asistidos']
].plot(kind='barh', stacked=True, color=['#2b5c8f', '#d95f02'], figsize=(10, 5))

# Generamos un recorrido for en las barras del grafico para
# ubicar la cantidad de asistidos y no asistidos dentro de las mismas
# logrando una mayor claridad a la hora de visualizar la ilustracion
for p in Grafico_Asistencia.patches:
    width = p.get_width()
    if width > 0:
        Grafico_Asistencia.annotate(
            f'{int(width)}',
            (p.get_x() + width / 2, p.get_y() + p.get_height() / 2),
            ha='center',
            va='center',
            color='white',
            fontweight='bold',
            fontsize=9,
        )

# Establecemos ultimos detalles que se dibujaran en la ventana a mostrar del grafico
plt.title('Asistencias en Tlleres')
plt.xlabel('Cantidad de Participantes')
plt.ylabel('')
plt.tight_layout()
plt.show()

Puntaje_Participantes = Participantes_Talleres_Result.groupby("Nombre_Taller")["Puntaje"].describe()
print(Puntaje_Participantes)

# Repetimos el mismo proceso pero para el promedio de notas de cada taller
Grafico_Promedio_Notas = (
    Puntaje_Participantes['mean']
    .sort_values()
    .plot(kind='barh', color='#2b5c8f', figsize=(9, 5))
)

for p in Grafico_Promedio_Notas.patches:
    width = p.get_width()
    Grafico_Promedio_Notas.annotate(
        f'{width:.2f}',
        (width + 0.1, p.get_y() + p.get_height() / 2),
        va='center',
        fontweight='bold',
        fontsize=9,
    )

plt.title('Promedio de Puntaje por Taller')
plt.xlabel('Puntaje Promedio')
plt.ylabel('')
plt.xlim(0, 7)
plt.tight_layout()
plt.show()