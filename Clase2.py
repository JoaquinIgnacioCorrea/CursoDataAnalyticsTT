# SECCION 1:
# CONSIGNA: Crear una lista llamada numeros que contenga los números del 1 al 10.

numeros = [1,2,3,4,5,6,7,8,9,10]

# CONSIGNA: Crear una tupla llamada meses que contenga los nombres de los 12 meses del año.
meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")

# CONSIGNA: Crear un diccionario llamado notas con el nombre de tres estudiantes como claves y sus respectivas notas como valores.
notas = {"Julian":6,"Camila":9,"Bruno":2}

# CONSIGNA: Crear un conjunto llamado numeros_unicos con algunos números, asegurándose de que no haya duplicados.
numeros_unicos = {1,2,14,54,32,1098,430,1240,453}

# SECCION 2:
# CONSIGNA: Modificar uno de los valores del diccionario notas (cambiar la nota de uno de los estudiantes).
notas["Bruno"] = 4

# CONSIGNA: Acceder a los elementos de la lista numeros y mostrar todos los números pares utilizando un bucle.
for numero in numeros:
    if(numero % 2 == 0):
        print(numero)

# CONSIGNA: Acceder al primer mes de la tupla meses y al último mes. Mostrar ambos.
primer_mes, ultimo_mes = meses[0], meses[len(meses)-1]
print(f"Primer mes:{primer_mes} \nUltimo mes: {ultimo_mes}")

# SECCION 3:
# CONSINGA: Definir una función normal llamada multiplicar_por_dos que tome un número y lo multiplique por 2. 
# Utilizar esta función para crear una nueva lista llamada dobles, que contenga los dobles de los números en la lista numeros.

def multiplicar_por_dos(numero):
    return numero * 2

dobles = []
for doble in numeros:
    dobles.append(multiplicar_por_dos(doble))

print(dobles)

# CONSIGNA: Definir una función lambda que haga lo mismo y utilizarla para crear una nueva lista llamada dobles_lambda, 
# que contenga los dobles de los números en la lista numeros.
dobles_lambda_def = lambda numero: numero * 2

dobles_lambda = []
for doble in numeros:
    dobles_lambda.append(dobles_lambda_def(doble))

print(f"Func lambda: \n{dobles_lambda}")

# SECCION 4:
# CONSIGNA: Utilizar list comprehensions para crear una lista llamada cuadrados que contenga los cuadrados de los números 
# en la lista numeros.
cuadrados = [cuadrado ** 2 for cuadrado in numeros]
print(f"Cuadrados: \n{cuadrados}")

# CONSIGNA: Utilizar dict comprehensions para crear un diccionario llamado cubos que contenga los números de la lista numeros 
# como claves y sus cubos como valores.
cubos = {cubo: cubo **3 for cubo in numeros}
print(f"Diccionario de cubos: \n{cubos}")

# SECCION 5
# CONSIGNA: Mostrar las listas dobles, dobles_lambda y cuadrados. Comparar sus resultados y argumentar cuál es el mejor método.
print(f"\nLista Dobles: {dobles}\nLista Doble Lambda: {dobles_lambda}\nLista Cuadrados: {cuadrados}")

# CONSIGNA: Imprimir el diccionario cubos y comparar con la creación de un diccionario usando un método convencional.
print(f"\nDiccionario Cubos: {cubos}\nDiccionario Notas: {notas}")