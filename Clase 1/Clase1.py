
# CONSIGNA: Escribí un programa que:
# Pida al usuario que ingrese un número entero usando input()
# Convierta ese valor a entero (int())
# Use una estructura if/else para verificar si el número es divisible por 2
# Imprima un mensaje indicando si el número es par o impar
# Ejecutá el bloque al menos dos veces, con un número par y uno impar.
entrada = int(input("Ingresa un numero entero: "))

if(entrada % 2 == 0):
  print('El numero es par')
else:
  print('El numero es impar')

# CONSIGNA: Crear una lista con varios tipos de datos y acceder a sus elementos.
lista = ['Joaquin Correa', 24, True]
print(lista)
print(lista[0])

# CONSIGNA: Crear un diccionario y acceder a sus valores por clave.
diccionario = {'nombre':'Joaquin','edad':24}
print(diccionario['nombre'])