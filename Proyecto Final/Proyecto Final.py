import pandas as pd
import numpy as np

# SECCION 1
# CONSIGNA: Realizar un script básico que calcule las ventas mensuales utilizando variables y operadores.

ventas = pd.read_csv("Proyecto Final/Fuentes/ventas.csv")

Ventas_mensuales_total = {
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

for venta in ventas.iterrows():
    mes = venta[1]["fecha_venta"].split("/")[1]
    if(venta[1]["precio"] != "" and venta[1]["cantidad"] != ""):
        try:    
            precio_producto = float(venta[1]["precio"].replace("$",""))
            cantidad_producto = float(venta[1]["cantidad"])
        except:
            print(f"Datos faltantes en la venta con id: {venta[1]["id_venta"]}")
    total_venta = precio_producto * cantidad_producto
    Ventas_mensuales_total[mes] += total_venta

# print(Ventas_mensuales_total)

# CONSIGNA: Estructuras de datos: Desarrollar un programa que almacene los datos de ventas (producto, precio, cantidad). 
# Decidir si conviene utilizar diccionarios o listas.

ventas_clasificadas = {
    "Decoración":[],
    "Electrodomésticos":[],
    "Electrónica":[]
}

venta_caracteristicas = {
    "id":0,
    "producto":"",
    "precio":"",
    "cantidad":""
}

for venta in ventas.iterrows():
    if(venta[1]["producto"] != None and venta[1]["precio"] != None and venta[1]["cantidad"] != None ):
        nueva_venta = venta_caracteristicas.copy()
        try:
            nueva_venta["id"] = venta[1]["id_venta"]
            nueva_venta["producto"] = venta[1]["producto"]
            nueva_venta["precio"] = venta[1]["precio"]
            nueva_venta["cantidad"] = venta[1]["cantidad"]
            if(venta[1]["categoria"] == "Decoración"):
                ventas_clasificadas["Decoración"].append(nueva_venta)
            elif(venta[1]["categoria"] == "Electrodomésticos"):
                ventas_clasificadas["Electrodomésticos"].append(nueva_venta)
            elif(venta[1]["categoria"] == "Electrónica"):
                ventas_clasificadas["Electrónica"].append(nueva_venta)
        except:
            print(f"Error con la venta: {venta[1]["id_venta"]}")

print(f"Se genero el diccionario correctamente llamado 'Ventas Clasificadas' que tiene la sig \
cantidad de registros:\nDecoración: {len(ventas_clasificadas['Decoración'])}\nElectrodomésticos:\
 {len(ventas_clasificadas["Electrodomésticos"])}\nElectrónica: {len(ventas_clasificadas['Electrónica'])}")

# CONSIGNA: Introducción a Pandas: realizar un análisis exploratorio inicial de los DataFrames.

print(f"Analisis de la fuente ventas:\nPrimeros 3 registros:\n{ventas.head(3)}\nDimensiones de la fuente(filas,columnas): {ventas.shape}\
\nColumnas: {ventas.columns}\nTipo datos:\n{ventas.dtypes}\nDescripcion general mediante metodo:\n{ventas.describe()}")

# CONSIGNA: Integración de datos: Combinar los sets de datos de ventas y marketing para obtener una visión más amplia de las tendencias.
