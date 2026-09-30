import pandas as pd
import numpy as np

# SECCION 1
# CONSIGNA: Obtener los dos DataFrames que contienen los datos de ventas.
ventas_norte = pd.read_csv("Clase 8/ventas - Norte.csv")
ventas_sur = pd.read_csv("Clase 8/ventas - Sur.csv")

# CONSIGNA: Concatenar los DataFrames (decidir si correponde hacerlo horizontal o verticalmente), verificar y describir el resultado. 
# Sugerir cómo manejar los datos faltantes, si los hubiera.

ventas = pd.concat([ventas_norte,ventas_sur], axis=0, ignore_index=True)

# print(ventas)
# Se decidio una concatenacion en vertical, para tener un recorrido mas sencillo en el dataframe, por otro lado, el reemplazo de datos faltantes
# Lo reemplazaria por una cadena de string que diga "Sin importe", si no se pudiera modificar esa problematica de columnas repetidas

# CONSIGNA: Asegurarse de realizar las operaciones previas necesarias para obtener la siguiente estructura de columnas: 
# Sucursal, Producto, Ventas, Mes
ventas["Ventas"] = ventas["Ventas"].combine_first(ventas["Ingresos"])
ventas["Sucursal"] = ventas["Sucursal"].combine_first(ventas["Sede"])
ventas = ventas.drop(columns=["Ingresos","Sede"])

# print(ventas)

# SECCION 2
# CONSIGNA: Utiliza pd.merge() para combinar ambos DataFrames basados en la columna que se considere más apropiada, 
# con el join que corresponda. Dejar documentada la justificación de ambas elecciones.

datos_empleados = pd.read_csv("Clase 8/data_empleados.csv")
situacion_empleados = pd.read_csv("Clase 8/situacion_empleados.csv")

datos_empleados_completos = pd.merge(datos_empleados,situacion_empleados,on="ID",how="outer")
datos_empleados_completos = datos_empleados_completos.fillna("Sin datos")
print(datos_empleados_completos)

# Utilize outer para conservar tanto los datos de los empleados como sus situaciones, de esta forma tenemos un solo recurso para realizar multiples
# analisis, por otro lado, reemplaze valores nulos para un manejo menos complejo del dataframe