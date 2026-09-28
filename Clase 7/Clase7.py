import pandas as pd

# SECCION 1
# CONSIGNA: Cargar el conjunto de datos , que contiene información sobre las ventas de diferentes productos en distintos meses.
data = {  
'producto': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],  
'mes': ['Enero', 'Enero', 'Febrero', 'Febrero', 'Marzo', 'Marzo', 'Marzo', 'Enero', 'Febrero'],  
'ventas': [150, 200, 250, 300, 100, 400, 350, 200, 300]  
}
df_data = pd.DataFrame(data)

# CONSIGNA: Agrupar las ventas por producto y sumar las ventas totales para cada uno.
ventas_agrupadas = df_data.groupby("producto")["ventas"].sum()
# print(f"Ventas agrupadas por productos:\n{ventas_agrupadas}")

# CONSIGNA: Generar un nuevo DataFrame que contenga el total de ventas por producto y lo mostrarlo en pantalla.
ventas_total = df_data.groupby("producto")["ventas"].count()
# print(f"Total de ventas por producto:\n{ventas_total}")

# SECCION 2
# CONSIGNA: Cargar el conjunto de datos ventas.csv de la actividad anterior.
df_ventas = pd.read_csv("Proyecto Final/Fuentes/ventas.csv")

# print (df_ventas)

# CONSIGNA: Utilizar la función pivot_table() para crear una tabla dinámica que muestre las ventas mensuales por producto.
df_ventas["fecha_venta"] = pd.to_datetime(df_ventas["fecha_venta"],dayfirst=True)
df_ventas["mes_venta"] = df_ventas["fecha_venta"].dt.strftime('%B')

ventas_dinamicas = df_ventas.pivot_table(index="mes_venta",columns="producto",values="cantidad",aggfunc="sum")

# CONSIGNA: Asegurarse de que la tabla muestre los productos en las filas y los meses en las columnas, con las ventas 
# totales como valores dentro de la tabla.
df_ventas["total_venta"] = df_ventas["precio"].str.replace('$','').astype(float)*df_ventas["cantidad"]

ventas_dinamicas2 = df_ventas.pivot_table(index="producto",columns="mes_venta",values="total_venta",aggfunc="sum")

# CONSIGNA: Mostrar la tabla dinámica en pantalla.
print(ventas_dinamicas)
print(ventas_dinamicas2)