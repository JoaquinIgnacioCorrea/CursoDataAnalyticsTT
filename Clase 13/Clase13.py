import matplotlib.pyplot as plt


# SECCION 1
# CONSIGNA: Crear un gráfico de líneas que muestra las ventas mensuales.

# a. Agregamos los datos que nos proveen para esta consigna (corresponden a dos listas)

## Datos de ventas mensuales (en unidades)  
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'] # Lista de los meses del año  
ventas = [100, 120, 130, 150, 180, 170, 200, 210, 250, 270, 300, 320] # Lista de las unidades vendidas correspondientes a cada mes 

# b. Generamos el grafico de lineas con sus respectivas modificaciones
plt.plot(meses,ventas,color="purple",marker="s")
plt.title("Progresion de ventas en el tiempo")
plt.ylabel("Cantidad de ventas")
plt.xlabel("Meses")
plt.grid(True)
plt.show()

# CONSGINA: Redactar un párrafo breve que explique la gráfica.

# Observación: Se puede apreciar que las ventas van en alza durante el transcurso del año
# presentando un maximo en diciembre y un minimo en enero, por otro lado vemos una leve
# reduccion de ventas entre el mes de mayo y junio

# SECCION 2
# CONSGINA: Crear un gráfico que muestre las ventas por artículo.
# CONSGINA: Agregar el contexto al gráfico y buscar una forma de resaltar el artículo más vendido

# a. Agregamos los datos que nos proveen para esta consigna (corresponden a dos listas)
# Datos de ventas por producto  
productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D']  # Lista de los nombres de los productos
ventas = [300, 250, 400, 350] # Lista de las unidades vendidas de cada producto en la campaña.  

# b. Generamos el grafico con un contexto apropiado enfocandonos en el articulo mas vendido

colores = ["orange"] * len(productos)
mejor_producto = ventas.index(max(ventas))
colores[mejor_producto] = "green"

plt.bar(productos, ventas, color=colores , width=0.5)
plt.title("Rendimiento del marketing en ventas por producto")
plt.ylabel("Cantidad de ventas")
plt.xlabel("Productos")
plt.show()