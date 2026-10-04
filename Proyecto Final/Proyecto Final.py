import pandas as pd
import numpy as np

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
            

print(f"Se genero el diccionario correctamente llamado 'Ventas Clasificadas' que tiene la sig \
cantidad de registros:\nDecoración: {len(ventas_clasificadas['Decoración'])}\nElectrodomésticos:\
 {len(ventas_clasificadas["Electrodomésticos"])}\nElectrónica: {len(ventas_clasificadas['Electrónica'])}")

# CONSIGNA: Introducción a Pandas: realizar un análisis exploratorio inicial de los DataFrames.
print(f"Analisis de la fuente ventas:\nPrimeros 3 registros:\n{ventas.head(3)}\nDimensiones de la fuente(filas,columnas): {ventas.shape}\
\nColumnas: {ventas.columns}\nTipo datos:\n{ventas.dtypes}\nDescripcion general mediante metodo:\n{ventas.describe()}")

# CONSIGNA: Calidad de datos: Identificar valores nulos y duplicados en los conjuntos de datos. 
# Documentar el estado inicial de los datos.
# a.Verificar cantidad de duplicados
ventas_duplicadas = ventas[ventas["id_venta"].duplicated()]
cantidad_duplicados = len(ventas_duplicadas)

print(f"Cantidad de duplicados: {cantidad_duplicados}\nRegistros duplicados:\n{ventas_duplicadas}")

# b.Verificar cantidad de registros con datos faltantes
ventas_con_datos_nulos = ventas[ventas.isna().any(axis=1)]
cantidad_registros_con_nulos = len(ventas_con_datos_nulos)
nulos_por_columna = ventas.isna().sum()

print(f"Cantidad de registros con datos nulos: {cantidad_registros_con_nulos}\nColumnas con datos nulos:\n{nulos_por_columna}\n\
Registros nulos:\n{ventas_con_datos_nulos}")

# Comentario -> Podemos observar que el dataset de ventas presenta 35 registros duplicados y 2 registros con datos nulos en precio y cantidad

# SECCION 2
# CONSIGNA: Limpieza de datos: Limpiar el conjunto de datos eliminando duplicados y caracteres no deseados. 
# Documentar el proceso y los resultados.
# a.Limpiamos datos duplicados
ventas_sin_duplicados = ventas.drop_duplicates(subset="id_venta")

print(f"Tamaño ventas sin duplicados: {len(ventas_sin_duplicados)}\nTamaño ventas con duplicados: {len(ventas)}")

# b.Limpiamos datos nulos
ventas_sin_nulos = ventas_sin_duplicados.dropna()

print(f"Ventas sin valores nulos: {len(ventas_sin_nulos)}\nVentas con valores nulos: {len(ventas_sin_duplicados)}")

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

print(f"Productos que superaron el 75% de recaudacion:\n{productos_alto_rendimiento}\
\nTotal de recaudacion de cada producto:\n{ventas_totales_por_producto}")

# CONSIGNA: Agregación: Resumir las ventas por categoría de producto y analizar los ingresos generados.
# a.Generamos un dataframe que filtra la suma total de ventas por categoria
ventas_totales_por_categoria = pd.DataFrame(ventas_limpias.groupby(["categoria"])["total_venta"].sum().sort_values(ascending=False))
print(f"Total de recaudacion por categoria:\n{ventas_totales_por_categoria}")

# CONSIGNA: Integración de datos: Combinar los sets de datos de ventas y marketing para obtener una visión más amplia de las tendencias.
marketing = pd.read_csv("Proyecto Final/Fuentes/marketing.csv")

# a.1.Hacemos analisis inicial de datos
print(f"Primeros 3 registros:\n{marketing.head(3)}\nDimensiones del dataframe:{marketing.shape}\nColumnas del dataframe:\
\n{marketing.columns}\nTipo de datos:\n{marketing.dtypes}\nBreve analisis del dataframe:\n{marketing.describe()}")

# a.2.Hacemos calidad de datos con el dataframe marketing
registros_marketing_duplicados = marketing[marketing["id_campanha"].duplicated()]
cantidad_duplicados_marketing = len(registros_marketing_duplicados)

registros_marketing_con_nulos = marketing[marketing.isna().any(axis=1)]
cantidad_registros_con_nulos_marketing = len(registros_marketing_con_nulos)

print(f"Cantidad de registros sin limpieza de duplicados o nulos: {len(marketing)}")
# a.2.1.Eliminamos datos duplicados
marketing_sin_duplicados = marketing.drop_duplicates(subset="id_campanha")
print(f"Cantidad de registros con datos duplicados del dataframe marketing: {cantidad_duplicados_marketing}\
\nCantidad de registros sin duplicados: {len(marketing_sin_duplicados)}")

marketing_limpio = marketing_sin_duplicados.dropna()

print(f"Cantidad registros con datos nulos:{cantidad_registros_con_nulos_marketing}\nCantidad registros sin datos nulos: {len(marketing_limpio)}")

# a.2.2 Formateamos datos para asegurar consistencia de formato
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

print(f"Combinacion de total de ventas y marketing por producto:\n{ventas_marketing_integradas}")