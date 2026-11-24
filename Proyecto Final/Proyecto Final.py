import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import ipywidgets as widgets

# SECCION 1
# CONSIGNA: Realizar un script básico que calcule las ventas mensuales utilizando variables y operadores.
ventas = pd.read_csv("Proyecto Final/Fuentes/ventas.csv")

total_ventas_mensuales = {
    "01": 0,
    "02": 0,
    "03": 0,
    "04": 0,
    "05": 0,
    "06": 0,
    "07": 0,
    "08": 0,
    "09": 0,
    "10": 0,
    "11": 0,
    "12": 0
}

for registro_venta in ventas.iterrows():
    mes = registro_venta[1]["fecha_venta"].split("/")[1]
    if(registro_venta[1]["precio"] != "" and registro_venta[1]["cantidad"] != ""):
        try:    
            precio_producto = float(registro_venta[1]["precio"].replace("$",""))
            cantidad_producto = float(registro_venta[1]["cantidad"])
        except:
            print(f"Datos faltantes en la venta con id: {registro_venta[1]["id_venta"]}")
    total_venta = precio_producto * cantidad_producto
    total_ventas_mensuales[mes] += total_venta

print(total_ventas_mensuales)

# CONSIGNA: Estructuras de datos: Desarrollar un programa que almacene los datos de ventas (producto, precio, cantidad). 
# Decidir si conviene utilizar diccionarios o listas.
ventas_clasificadas = {
    "Decoración":[],
    "Electrodomésticos":[],
    "Electrónica":[]
}

plantilla_venta = {
    "id":0,
    "producto":"",
    "precio":"",
    "cantidad":""
}

for registro_venta in ventas.iterrows():
    if(registro_venta[1]["producto"] != None and registro_venta[1]["precio"] != None and registro_venta[1]["cantidad"] != None ):
        nueva_venta = plantilla_venta.copy()
        try:
            nueva_venta["id"] = registro_venta[1]["id_venta"]
            nueva_venta["producto"] = registro_venta[1]["producto"]
            nueva_venta["precio"] = registro_venta[1]["precio"]
            nueva_venta["cantidad"] = registro_venta[1]["cantidad"]
            if(registro_venta[1]["categoria"] == "Decoración"):
                ventas_clasificadas["Decoración"].append(nueva_venta)
            elif(registro_venta[1]["categoria"] == "Electrodomésticos"):
                ventas_clasificadas["Electrodomésticos"].append(nueva_venta)
            elif(registro_venta[1]["categoria"] == "Electrónica"):
                ventas_clasificadas["Electrónica"].append(nueva_venta)
        except:
            print(f"Error con la venta: {registro_venta[1]["id_venta"]}")
            

print(f"\nSe genero el diccionario correctamente llamado 'Ventas Clasificadas' que tiene la sig \
cantidad de registros:\nDecoración: {len(ventas_clasificadas['Decoración'])}\nElectrodomésticos:\
 {len(ventas_clasificadas["Electrodomésticos"])}\nElectrónica: {len(ventas_clasificadas['Electrónica'])}")

# CONSIGNA: Introducción a Pandas: realizar un análisis exploratorio inicial de los DataFrames.
print(f"\nAnalisis de la fuente ventas:\nPrimeros 3 registros:\n{ventas.head(3)}\nDimensiones de la fuente(filas,columnas): {ventas.shape}\
\nColumnas: {ventas.columns}\nTipo datos:\n{ventas.dtypes}\nDescripcion general mediante metodo:\n{ventas.describe()}")

# CONSIGNA: Calidad de datos: Identificar valores nulos y duplicados en los conjuntos de datos. 
# Documentar el estado inicial de los datos.
# a.Verificar cantidad de duplicados
ventas_duplicadas = ventas[ventas["id_venta"].duplicated()]
cantidad_duplicados = len(ventas_duplicadas)

print(f"\nCantidad de duplicados: {cantidad_duplicados}\nRegistros duplicados:\n{ventas_duplicadas}")

# b.Verificar cantidad de registros con datos faltantes
ventas_con_datos_nulos = ventas[ventas.isna().any(axis=1)]
cantidad_registros_con_nulos = len(ventas_con_datos_nulos)
nulos_por_columna = ventas.isna().sum()

print(f"\nCantidad de registros con datos nulos: {cantidad_registros_con_nulos}\nColumnas con datos nulos:\n{nulos_por_columna}\n\
Registros nulos:\n{ventas_con_datos_nulos}")

# Comentario -> Podemos observar que el dataset de ventas presenta 35 registros duplicados y 2 registros con datos nulos en precio y cantidad

# SECCION 2
# CONSIGNA: Limpieza de datos: Limpiar el conjunto de datos eliminando duplicados y caracteres no deseados. 
# Documentar el proceso y los resultados.
# a.Limpiamos datos duplicados
ventas_sin_duplicados = ventas.drop_duplicates(subset="id_venta")

print(f"\nTamaño ventas sin duplicados: {len(ventas_sin_duplicados)}\nTamaño ventas con duplicados: {len(ventas)}")

# b.Limpiamos datos nulos
ventas_sin_nulos = ventas_sin_duplicados.dropna()

print(f"\nVentas sin valores nulos: {len(ventas_sin_nulos)}\nVentas con valores nulos: {len(ventas_sin_duplicados)}")

ventas_limpias = ventas_sin_nulos

# CONSIGNA: Transformación de datos: Aplicar filtros y transformaciones para crear una tabla de ventas que muestre 
# solo los productos con alto rendimiento.

# a.Aplicamos formato en dataframe para trabajar con filtros
ventas_limpias["producto"] = ventas_limpias["producto"].str.strip()
ventas_limpias["producto"] = ventas_limpias["producto"].str.lower()
ventas_limpias["categoria"] = ventas_limpias["categoria"].str.strip()
ventas_limpias["categoria"] = ventas_limpias["categoria"].str.lower()

# a.1.Aplico formato a ventas para pasarlo a numero flotante
ventas_limpias["precio"] = ventas_limpias["precio"].str.strip()
ventas_limpias["precio"] = ventas_limpias["precio"].str.replace("$","")
ventas_limpias["precio"] = ventas_limpias["precio"].astype(float)

# a.2.Aplico formato fecha a la fecha de la venta
ventas_limpias["fecha_venta"] = pd.to_datetime(ventas_limpias["fecha_venta"], errors="coerce", format="%d/%m/%Y")

# a.3.Creo una columna que realiza el total de la venta para su filtrado
ventas_limpias["total_venta"] = ventas_limpias["precio"] * ventas_limpias["cantidad"]

# b.1.Creo un dataframe que recopila el total de todas la ventas por producto
ventas_totales_por_producto = pd.DataFrame(ventas_limpias.groupby(["producto"])["total_venta"].sum().sort_values(ascending=False))

# b.2.Se crea una tabla que recopila los productos de alto rendimiento (recaudacion mayor al percentil 75)
productos_alto_rendimiento = ventas_totales_por_producto[ventas_totales_por_producto["total_venta"] > ventas_totales_por_producto["total_venta"].quantile(0.75)]

print(f"\nProductos que superaron el 75% de recaudacion:\n{productos_alto_rendimiento}\
\nTotal de recaudacion de cada producto:\n{ventas_totales_por_producto}")

# CONSIGNA: Agregación: Resumir las ventas por categoría de producto y analizar los ingresos generados.
# a.Generamos un dataframe que filtra la suma total de ventas por categoria
ventas_totales_por_categoria = pd.DataFrame(ventas_limpias.groupby(["categoria"])["total_venta"].sum().sort_values(ascending=False))
print(f"\nTotal de recaudacion por categoria:\n{ventas_totales_por_categoria}")

# CONSIGNA: Integración de datos: Combinar los sets de datos de ventas y marketing para obtener una visión más amplia de las tendencias.
marketing = pd.read_csv("Proyecto Final/Fuentes/marketing.csv")

# a.1.Hacemos analisis inicial de datos
print(f"\nPrimeros 3 registros:\n{marketing.head(3)}\nDimensiones del dataframe:{marketing.shape}\nColumnas del dataframe:\
\n{marketing.columns}\nTipo de datos:\n{marketing.dtypes}\nBreve analisis del dataframe:\n{marketing.describe()}")

# a.2.Hacemos calidad de datos con el dataframe marketing
registros_marketing_duplicados = marketing[marketing["id_campanha"].duplicated()]
cantidad_duplicados_marketing = len(registros_marketing_duplicados)

registros_marketing_con_nulos = marketing[marketing.isna().any(axis=1)]
cantidad_registros_con_nulos_marketing = len(registros_marketing_con_nulos)

print(f"\nCantidad de registros sin limpieza de duplicados o nulos: {len(marketing)}")
# a.2.1.Eliminamos datos duplicados
marketing_sin_duplicados = marketing.drop_duplicates(subset="id_campanha")
print(f"\nCantidad de registros con datos duplicados del dataframe marketing: {cantidad_duplicados_marketing}\
\nCantidad de registros sin duplicados: {len(marketing_sin_duplicados)}")

marketing_limpio = marketing_sin_duplicados.dropna()

print(f"\nCantidad registros con datos nulos:{cantidad_registros_con_nulos_marketing}\nCantidad registros sin datos nulos: {len(marketing_limpio)}")

# a.2.2.Formateamos datos para asegurar consistencia de formato
marketing_limpio["producto"] = marketing_limpio["producto"].str.strip()
marketing_limpio["producto"] = marketing_limpio["producto"].str.lower()
marketing_limpio["canal"] = marketing_limpio["canal"].str.strip()
marketing_limpio["canal"] = marketing_limpio["canal"].str.lower()

marketing_limpio["fecha_inicio"] = marketing_limpio["fecha_inicio"].str.strip()
marketing_limpio["fecha_fin"] = marketing_limpio["fecha_fin"].str.strip()

marketing_limpio["fecha_inicio"] = pd.to_datetime(marketing_limpio["fecha_inicio"], errors="coerce", format="%d/%m/%Y")
marketing_limpio["fecha_fin"] = pd.to_datetime(marketing_limpio["fecha_fin"], errors="coerce", format="%d/%m/%Y")

# b.1.Integramos ambos dataframe

ventas_marketing_integradas = pd.merge(ventas_totales_por_producto,marketing_limpio, on="producto", how="outer")

print(f"\nCombinacion de total de ventas y marketing por producto:\n{ventas_marketing_integradas}")

# Correcciones Trabajo Final Data Analitycs
# 2. Dejar una conclusión final respecto al trabajo previo con las fuentes de datos 

# SECCION 3
# CONSGINA: Estadística descriptiva: Calcular medidas de tendencia central y dispersión sobre las ventas. 
# Presentar los resultados en un informe.
# a.1.1.Realizamos las medidas de tendencia central de todas la ventas en general
# utilizando la columna "total_venta" y el metodo describe.
medidas_central_ventas = ventas_limpias["total_venta"].describe()
medidas_central_categoria = ventas_limpias.groupby("categoria")["total_venta"].describe()

# a.1.2.Realizamos otras medidas de tendencia central que faltaron
moda_vetas = ventas_limpias["producto"].mode().iloc[0]
moda_categorias = ventas_limpias["categoria"].mode().iloc[0]

# a.1.3.Mostramos los resultados en consola
print(f"\nMedidas de tendencia central de todas las ventas(descritas en pesos $):\n{medidas_central_ventas} \
      \nModa en ventas (producto): {moda_vetas}\
      \nMedidas de tendencia central de las categorias(descritas en pesos $):\n{medidas_central_categoria}\
      \nModa en categoria: {moda_categorias}")

# a.2.1.Realizamos de dispersión que faltaron(rango, varianza, coeficiente de variacion)
rango_ventas = ventas_limpias["total_venta"].max() - ventas_limpias["total_venta"].min()
rango_categoria = ventas_limpias.groupby("categoria")["total_venta"].max() - ventas_limpias.groupby("categoria")["total_venta"].min()

varianza_ventas = ventas_limpias["total_venta"].var(ddof=0)
varianza_categoria = ventas_limpias.groupby("categoria")["total_venta"].var(ddof=0)

coeficientevariacion_ventas = (ventas_limpias["total_venta"].std()/ventas_limpias["total_venta"].mean()) * 100
coeficientevariacion_categoria = (ventas_limpias.groupby("categoria")["total_venta"].std()/ventas_limpias.groupby("categoria")["total_venta"].mean()) * 100

# a.2.2.Mostramos los resultados en consola
print(f"\nMedidas de dispersion de ventas y categoria:\nRango de ventas: {rango_ventas}\nRango de ventas por categoria:\n{rango_categoria}\
      \nVarianza de ventas: {varianza_ventas}\nVarianza de ventas por categoria:\n{varianza_categoria}\
      \nCoeficiente de variacion de ventas: {coeficientevariacion_ventas}\nCoeficiente de variacion de ventas por categoria:\n{coeficientevariacion_categoria}")

# CONSGINA: Análisis exploratorio de datos (EDA): Realizar un análisis exploratorio utilizando visualizaciones para identificar patrones y 
# tendencias en las ventas.

# a.1.Realizamos la visualizacion de datos correspondiente del EDA
# a.1.1.Realizamos graficos de barras que comparen monto total tanto en ventas por producto (tomamos los mejores 10) como por categoria
plt.bar(ventas_totales_por_producto.index,ventas_totales_por_producto["total_venta"])
plt.title("Comparacion de rendimiento por producto")
plt.xlabel("Productos")
plt.ylabel("Suma total de importe")
plt.xticks(rotation=65)
plt.show()

plt.bar(ventas_totales_por_categoria.index,ventas_totales_por_categoria["total_venta"])
plt.title("Comparacion de rendimiento por categoria")
plt.xlabel("categoria")
plt.ylabel("Suma total de importe")
plt.show()

# a.1.2.Realizamos graficos de lineas para ver evolucion de ventas en el tiempo de los productos como sus categorias
ventas_limpias["mes"] = ventas_limpias["fecha_venta"].dt.month

venta_mes_producto = ventas_limpias.groupby(["mes","producto"])["total_venta"].sum().reset_index().pivot(
    index="mes",columns="producto",values="total_venta")
ventas_mes_categoria = ventas_limpias.groupby(["mes","categoria"])["total_venta"].sum().reset_index().pivot(
    index="mes",columns="categoria",values="total_venta")

plt.plot(venta_mes_producto.index,venta_mes_producto.values)
plt.title("Evolucion mensual de ventas por producto")
plt.xlabel("Meses")
plt.ylabel("Suma total de importe")
plt.show()

plt.plot(ventas_mes_categoria.index,ventas_mes_categoria.values)
plt.title("Evolucion mensual de ventas por categoria")
plt.xlabel("Meses")
plt.ylabel("Suma total de importe")
plt.show()

# a.1.3.Realizamos grafico histograma para frecuencia en el total de ventas
sns.histplot(ventas_limpias["producto"],bins={ventas_limpias["producto"].nunique()},kde=True)
plt.title("Distribucion de ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Frecuencia de venta")
plt.xticks(rotation=65)
plt.show()

# a.2.Realizamos el resumen de datos del EDA
# a.2.1.Realizamos las descripciones de los datasets

print(f"\nDescripcion de ventas en general:\n{ventas_limpias.describe()}\nInformacion de ventas en general:\n{ventas_limpias.info()}\
      \nDescripcion de marketing en general:\n{marketing_limpio.describe()}\nInformacion de marketing en general\n{marketing_limpio.info()}")

# CONSGINA: Correlación: Evaluar la relación entre diferentes variables (por ejemplo, precio y cantidad vendida) y mostrar los resultados en 
# un gráfico.
# a.1.1.Realizamos graficos de relacion para verificar relaciones entre variables
sns.scatterplot(x="precio",y="total_venta",data=ventas_limpias)
plt.title("Distribucion entre precio y total de venta")
plt.xlabel("Precio")
plt.ylabel("Total Venta")
plt.show()

sns.scatterplot(x="cantidad",y="total_venta",data=ventas_limpias)
plt.title("Distribucion entre total de venta y cantidad")
plt.xlabel("Cantidad")
plt.ylabel("Total Venta")
plt.show()

sns.scatterplot(x="mes",y="total_venta",data=ventas_limpias)
plt.title("Distribucion entre total de venta y mes")
plt.xlabel("Mes")
plt.ylabel("Total Venta")
plt.show()

sns.scatterplot(x="precio",y="cantidad",data=ventas_limpias)
plt.title("Distribucion entre precio y cantidad")
plt.xlabel("Precio")
plt.ylabel("Cantidad")
plt.show()

# CONSGINA: Consolidación de datos: Consolidar todos los análisis previos y preparar un conjunto de datos final que resuma los hallazgos 
# clave para la presentación.

# a.1.1.Realizamos un dataframe final con los valores que nos interesan por categoria para saber el rendimiento de las mismas
# involucramos totales, cantidades, media, mediana, max, min y desvio estandar
analisis_final = ventas_totales_por_categoria.copy()
analisis_final["total_cantidad"] = ventas_limpias.groupby("categoria")["cantidad"].sum().astype(int)
analisis_final["promedio_total_venta"] = ventas_limpias.groupby("categoria")["total_venta"].mean()
analisis_final["mediana_total_venta"] = ventas_limpias.groupby("categoria")["total_venta"].median()
analisis_final["max_total_venta"] = ventas_limpias.groupby("categoria")["total_venta"].max()
analisis_final["min_total_venta"] = ventas_limpias.groupby("categoria")["total_venta"].min()
analisis_final["desv_estandar_total_venta"] = ventas_limpias.groupby("categoria")["total_venta"].std()

# a.1.2.Preparamos el dataset de marketing para discriminar el gasto del mismo por categoria
productos_categoria_marketing = ventas_limpias[["producto","categoria"]].drop_duplicates()
productos_categoria_marketing = pd.merge(marketing_limpio, productos_categoria_marketing,
                                         on="producto",how="left")

# a.1.3.Realizamos las columnas correspondientes a las categorias relacionadas a los gastos de marketing de las mismas
# involucramos totales, media, mediana, max, min y desvio estandar
analisis_final["total_gasto_marketing"] = productos_categoria_marketing.groupby("categoria")["costo"].sum()
analisis_final["promedio_gasto_marketing"] = productos_categoria_marketing.groupby("categoria")["costo"].mean()
analisis_final["mediana_gasto_marketing"] = productos_categoria_marketing.groupby("categoria")["costo"].median()
analisis_final["max_gasto_marketing"] = productos_categoria_marketing.groupby("categoria")["costo"].max()
analisis_final["min_gasto_marketing"] = productos_categoria_marketing.groupby("categoria")["costo"].min()
analisis_final["desv_estandar_gasto_marketing"] = productos_categoria_marketing.groupby("categoria")["costo"].std()

# a.1.4.Preparamos un dataset que discrime el total gastado de marketing por categoria y canal para integrarlo en el dataset del analisis final
costo_canal = productos_categoria_marketing.groupby(["categoria","canal"])["costo"].sum().reset_index().pivot(index="categoria",columns="canal",values="costo")
analisis_final = analisis_final.join(costo_canal[["tv","email","rrss"]])

print(analisis_final)
# Devolucion: de esta forma tenemos un dataset completo que nos indica toda la informacion necesaria para que se pueda estudiar que categoria
# es la mas rentable a la hora de vender, su frecuencia, el promedio de la misma y como influyo sus respectivas campañas de marketing en la misma
# contemplando el presupuesto que se permitio otorgar a la misma y como fue su impacto segun la distribucion de los distintos canales

# SECCION 4
# CONSGINA: Visualización con Matplotlib: Crear gráficos básicos (líneas, barras, dispersión) que representen las ventas con diferentes 
# periodos de tiempo.

# a.1.1.Realizamos graficos de lineas en diferentes tiempos (diario, mensual y trimestral)
ventas_diarias = ventas_limpias.groupby([
    "producto",
    "fecha_venta"])["total_venta"].sum().reset_index().pivot(
    index="fecha_venta",
    columns="producto",
    values="total_venta")

ventas_trimestrales = ventas_limpias.groupby(
    ["producto", 
     ventas_limpias["fecha_venta"].dt.to_period("Q").rename("trimestre")]
)["total_venta"].sum().reset_index().pivot(
    index="trimestre",
    columns="producto",
    values="total_venta"
)

for producto in ventas_diarias.columns:
    plt.plot(ventas_diarias.index, ventas_diarias[producto], label=producto)
plt.title("Evolucion diaria de ventas por producto")
plt.xlabel("Dias")
plt.ylabel("Suma total de importe")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

for producto in venta_mes_producto.columns:
    plt.plot(venta_mes_producto.index, venta_mes_producto[producto], label=producto)
plt.title("Evolucion mensual de ventas por producto")
plt.xlabel("Meses")
plt.ylabel("Suma total de importe")
plt.legend()
plt.tight_layout()
plt.show()

for producto in ventas_trimestrales.columns:
    plt.plot(ventas_trimestrales.index.astype(str), ventas_trimestrales[producto], label=producto)
plt.title("Evolucion trimestral de ventas por producto")
plt.xlabel("Trimestres")
plt.ylabel("Suma total de importe")
plt.legend()
plt.tight_layout()
plt.show()

# a.1.2.Realizamos graficos de barras
ventas_mes_categoria.plot(kind="bar")
plt.title("Ventas mensuales por categoría")
plt.xlabel("Meses")
plt.ylabel("Importe total de ventas")
plt.xticks(rotation=45)
plt.legend(title="Categorías")
plt.tight_layout()
plt.show()

ventas_categoria_trimestre = ventas_limpias.groupby([
    "categoria",
    ventas_limpias["fecha_venta"].dt.to_period("Q").rename("trimestre")]
    )["total_venta"].sum().reset_index().pivot(
        index="trimestre",
        columns="categoria",
        values="total_venta"
    )

ventas_categoria_trimestre.plot(kind="bar")
plt.title("Ventas trimestrales por categoría")
plt.xlabel("Trimestres")
plt.ylabel("Importe total de ventas")
plt.xticks(rotation=45)
plt.legend(title="Categorías")
plt.tight_layout()
plt.show()

# a.1.3.Realizamos graficos de dispersion
sns.scatterplot(
    data=ventas_limpias,
    x="precio",
    y="cantidad",
)
plt.title("Relación entre precio y cantidad vendida por categoría")
plt.xlabel("Precio del producto")
plt.ylabel("Cantidad vendida")
plt.tight_layout()
plt.show()

# CONSGINA: Visualización avanzada con Seaborn: Desarrollar visualizaciones estadísticas avanzadas, utilizando paletas y estilos para 
# mejorar la presentación.
# a.1.1.Generamos un subplot de seaborn con las diferentes ventas mensuales por producto personalizado
ventas_mes_deco = ventas_limpias[ventas_limpias["categoria"] == "decoración"].groupby(["producto","mes"])["total_venta"].sum().reset_index()
ventas_mes_electrodo = ventas_limpias[ventas_limpias["categoria"] == "electrodomésticos"].groupby(["producto","mes"])["total_venta"].sum().reset_index()
ventas_mes_electro = ventas_limpias[ventas_limpias["categoria"] == "electrónica"].groupby(["producto","mes"])["total_venta"].sum().reset_index()

fig, axs = plt.subplots(3,1)
sns.lineplot(x="mes",y="total_venta",hue="producto",data=ventas_mes_deco,ax=axs[0], marker="o")
axs[0].set_title("Distribucion de ventas por mes decoración")
axs[0].set_ylabel("Importe de venta")

sns.lineplot(x="mes",y="total_venta",hue="producto",data=ventas_mes_electrodo,ax=axs[1], marker="o")
axs[1].set_title("Distribucion de ventas por mes electrodomésticos")
axs[1].set_ylabel("Importe de venta")

sns.lineplot(x="mes",y="total_venta",hue="producto",data=ventas_mes_electro,ax=axs[2], marker="o")
axs[2].set_title("Distribucion de ventas por mes electrónica")
axs[2].set_ylabel("Importe de venta")

for ax in axs:
    ax.grid(True, linestyle="--", alpha=0.5)

plt.subplots_adjust(hspace=0.5)
plt.tight_layout()
plt.show()

# a.1.2.Generamos segundo subplot con graficos no contemplados anteriormente (heatmap y violin plot)
fig, axs = plt.subplots(1,2)
sns.boxplot(data=ventas_limpias,x="categoria",y="total_venta",hue="categoria",palette="Set2",ax=axs[0])
axs[0].set_title("Distribución de importes de venta por categoría")
axs[0].set_xlabel("Categoría")
axs[0].set_ylabel("Importe de venta")
axs[0].grid(axis="y", linestyle="--", alpha=0.4)

sns.violinplot(
    data=ventas_limpias,
    x="categoria",
    y="total_venta",
    hue="categoria",
    palette="Pastel1",
    inner="quart",
    legend=False,
    ax=axs[1]
)
axs[1].set_title("Densidad de importes de venta por categoría")
axs[1].set_xlabel("Categoría")
axs[1].set_ylabel("Importe de venta")
axs[1].grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.show()

correlacion = ventas_limpias[["precio","cantidad","total_venta"]].corr()

sns.heatmap(data=correlacion,annot=True,cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5)
plt.title("Matriz de correlación de variables de ventas")
plt.tight_layout()
plt.show()

# CONSGINA: Visualización interactiva con Plotly: Construir un dashboard interactivo que combine múltiples visualizaciones, permitiendo al 
# usuario explorar los datos dinámicamente.
# a.1.1.Preparamos selectores para los graficos interactivos

selector_categoria = widgets.Dropdown(options=['decoración', 'electrodomésticos', 'electrónica'],value="electrónica",
                            description="Categoria:")

# a.1.2.Realizamos funciones de graficos interactivos con sus respectivos llamados

def grafico_bar_categoria(categoria):
    data = ventas_limpias[ventas_limpias["categoria"] == categoria].groupby("producto")["total_venta"].sum().reset_index()
    fig = px.bar(data,x="producto", y="total_venta", 
                  title=f"Ventas anuales de productos de la categoria {categoria}")
    fig.show()

grafico_bar_categoria(selector_categoria.value)
widgets.interact(grafico_bar_categoria,categoria=selector_categoria)

def grafico_lineas_categoria(categoria):
        data = ventas_limpias[ventas_limpias["categoria"] == categoria].groupby(["producto","mes"])["total_venta"].sum().reset_index()
        fig = px.line(data,x="mes",y="total_venta",markers=True,color="producto",
                  title=f"Ventas anuales de productos de la categoria {categoria}")
        fig.show()

grafico_lineas_categoria(selector_categoria.value)
widgets.interact(grafico_lineas_categoria,categoria=selector_categoria)

def grafico_dispersion_categoria(categoria):
    data = ventas_limpias[ventas_limpias["categoria"] == categoria]
    fig = px.scatter(data,
        x="precio",
        y="cantidad",
        color="categoria",
        size="total_venta",
        hover_data=["producto", "fecha_venta", "total_venta"],
        color_discrete_sequence=px.colors.qualitative.Set2,
        title="Relación entre precio y cantidad vendida")
    fig.show()

grafico_dispersion_categoria(selector_categoria.value)
widgets.interact(grafico_dispersion_categoria,categoria=selector_categoria)


# CONSGINA: Presentación final: Preparar una presentación que resuma los hallazgos, insights y visualizaciones generadas a lo largo del 
# proyecto. Presentar ante un panel simulado de "expertos" en SynthData, recibiendo feedback sobre el trabajo realizado.


