# Categorias a tener en cuenta para la practica
# 1. Inconsistencia de formatos de fecha
# 2. Registros duplicados y claves unicas
# 3. Problemas de estandarizacion y espacios
# 4. Valores faltantes o nulos
# 5. Categorias no autorizadas

import pandas as pd
datos = pd.read_csv('Practicas Auditoria/datos_ventas_para_auditoria.csv')

# PARTE 1: Inconsistencia de formatos de fecha
# Modificacion de caracteres alternativos en columna fecha, se normaliza
datos['Fecha_Venta'] = datos['Fecha_Venta'].astype(str).str.replace(r'[.-]',"/",regex=True)

# Seteo de tipo de dato en la columna, transformamos el texto en formato fecha
datos['Fecha_Venta'] = pd.to_datetime(datos['Fecha_Venta'],format='mixed',dayfirst=True,errors='coerce')

# Modificamos orden de fecha a formato local ej: dd/mm/yyyy
datos['Fecha_Venta'] = datos['Fecha_Venta'].dt.strftime('%d/%m/%Y')

# Muestro 5 ejemplos para ver formateo de columna fechas en el dataframe
print(datos)

# PARTE 2: Registros duplicados y claves unicas
# Separo en un dataset las filas con datos duplicados mediante el id de transaccion
filas_duplicadas = datos[datos['ID_Transaccion'].duplicated()]

# Muestro filas duplicadas y su cantidad
print(f'Cantidad de filas duplicadas: {len(filas_duplicadas)}\nCantidad de filas: {len(datos)}\nFilas Duplicadas:\n{filas_duplicadas}')

# Elimino datos duplicados con filtro en la columna de id de transaccion
datos = datos.drop_duplicates(subset='ID_Transaccion')

# Muestro filas afectadas
print(f'Cantidad filas sin duplicados: {len(datos)}\n')

# PARTE 3: Problemas de estandarizacion y espacios
# Eliminamos espacios antes y despues de los valores de celda en las sig columnas
datos['Cliente_Nombre'] = datos['Cliente_Nombre'].str.strip()
datos['Categoria_Producto'] = datos['Categoria_Producto'].str.strip()
datos['Metodo_Pago'] = datos['Metodo_Pago'].str.strip()

# Seteamos todos los valores de las columnas en miniscula para evitar sensibilitecase
datos['Cliente_Nombre'] = datos['Cliente_Nombre'].str.lower()
datos['Categoria_Producto'] = datos['Categoria_Producto'].str.lower()
datos['Metodo_Pago'] = datos['Metodo_Pago'].str.lower()

# Seteamos valores en precio unitario respetando decimales con punto
datos['Precio_Unitario'] = datos['Precio_Unitario'].astype(str)
datos['Total_Calculado'] = datos['Total_Calculado'].astype(str)

datos['Precio_Unitario'] = datos['Precio_Unitario'].str.replace(',','.')
datos['Total_Calculado'] = datos['Total_Calculado'].str.replace(',','.')

datos['Precio_Unitario'] = datos['Precio_Unitario'].astype(float)
datos['Total_Calculado'] = datos['Total_Calculado'].astype(float)

# Modificamos datos en cantidad con error en su valor siendo negativo
datos['Cantidad'] = datos['Cantidad'].astype(str)
datos['Cantidad'] = datos['Cantidad'].str.replace('-','')
datos['Cantidad'] = datos['Cantidad'].astype(float)

print(datos)

# PARTE 4/5: Valores faltantes o nulos - Categorias no autorizadas
# Eliminamos filas con nulos en precio unitario, 
# eliminando a su vez las cat no autorizadas (la mayoria estaban relacionadas)
datos = datos.dropna(subset='Precio_Unitario')

# Definimos funcion para saber valores unicos en categorias que queramos buscar
def tipo_datos(columna_p):

    for columna in datos.columns:
        if columna in columna_p:
            print(columna)
            print(datos[columna].unique())

# Columnas a averiguar datos anomalos seteadas en str
columnas_interes = ['Categoria_Producto','Metodo_Pago','Estatus_Auditoria']
# Uso funcion para saber si quedan datos anomalos en columnas de interes
tipo_datos(columnas_interes)

# Modifico cantidad en celdas que tienen precio unitario y total calculado, evitando eliminacion de las mismas
datos.loc[datos['Cantidad'].isna(), 'Cantidad'] = (datos.loc[datos['Cantidad'].isna(), 
                                                             'Total_Calculado'] / datos.loc[datos['Cantidad'].isna(), 'Precio_Unitario'])

print(datos)