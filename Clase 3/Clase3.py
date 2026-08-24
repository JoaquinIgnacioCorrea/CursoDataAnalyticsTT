# SECCION 1
# CONSIGNA: Parámetros posicionales: Crear una función llamada multiplicar que reciba dos números y devuelva su producto. 
# Probar la función con diferentes pares de números.
def multtiplicar(a,b):
    return a * b

print(multtiplicar(2,3))
print(multtiplicar(4,2))
print(multtiplicar(6,8))

# CONSINGA: Parámetros por defecto: Crear una función llamada bienvenida que reciba un nombre y un mensaje de bienvenida.
# El mensaje debe tener un valor por defecto de "¡Bienvenido!". Si no se proporciona un mensaje, la función debe usar el valor 
# por defecto. Probar la función proporcionando solo el nombre y con el mensaje.
def bienvenida(nombre,mensaje="Bienvenido"):
    print(f"{mensaje} {nombre}")

bienvenida("Joaquin", "Que onda facha, como estas")

# CONSIGNA: Parámetros indefinidos (*args): Crear una función llamada calcular_promedio que acepte un número variable de notas 
# (posicionales) y devuelva el promedio de esas notas. Probar la función con diferentes cantidades de notas.
def calcular_promedio(*args):
    return sum(args)/len(args)

print(calcular_promedio(8,8))

# CONSIGNA: Parámetros de palabras clave indefinidas (**kwargs): Crear una función llamada concatena_info que reciba un nombre y 
# un número indefinido de palabras clave (por ejemplo, edad, ciudad, ocupación) y devuelva un string que combine todos los datos. 
# Probar la función pasando varios pares de clave-valor.
def concatena_info(nombre, **kwargs):
    message = f"{nombre}\n"
    for clave, valor in kwargs.items():
        message += f"{clave}: {valor}\n"
    return message

persona1 = {"edad":22,"profesion":"Ingeniero","ciudad":"La Plata"}
print(concatena_info("Julian", **persona1))

persona2 = {"edad":45,"profesion":"CEO","ciudad":"Tigre"}
print(concatena_info("Alejandro", **persona2))

# SECCION 2
# CONSIGNA: Cargá un csv en Google Colab y visualizá sus primeras filas usando Pandas.
import pandas as pd

data = pd.read_csv('Clase 3/ventas.csv')
print(data.head(3))

# CONSIGNA: Repetí el ejercicio anterior con una planilla de Google Sheets.
data2 = pd.read_excel('Clase 3/ventas.xlsx')
print(data2.head(3))

# CONSGINA: Investigá el método para cargar planillas de Excel en Google Colab, 
# utilizando Pandas, y repetí el ejercicio del punto 1.

