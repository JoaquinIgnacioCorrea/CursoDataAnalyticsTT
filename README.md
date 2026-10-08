# Curso de Análisis de Datos

Repositorio con las actividades desarrolladas durante un curso de análisis de datos utilizando Python, archivos CSV y planillas Excel.

## Contenido del repositorio

### [Clase 1](./Clase%201/)

Introducción a Python y a los conceptos básicos de programación aplicados al análisis de datos. Se trabajan variables, tipos de datos, operadores, estructuras de control y funciones.

- `Clase1.py`

### [Clase 2](./Clase%202/)

Continuación de los fundamentos de Python. Se incorporan estructuras de datos, listas, diccionarios, recorridos, procesamiento de información y resolución de ejercicios prácticos.

- `Clase2.py`

### [Clase 3](./Clase%203/)

Se incorporan el alcance de variables (_scope_) y la lectura de archivos externos. Se analizan datos de ventas en formatos CSV y Excel.

- `Clase3.py`
- [`ventas.csv`](./Clase%203/ventas.csv)
- [`ventas.xlsx`](./Clase%203/ventas.xlsx)

### [Clase 4](./Clase%204/)

Se profundiza el análisis de datos utilizando información sobre satisfacción de clientes. Se aplican los conocimientos anteriores y se incorporan nuevas actividades con archivos CSV y Excel.

- `Clase4.py`
- [`satis_clientes.csv`](./Clase%204/satis_clientes.csv)
- [`Actividad 2.xlsx`](./Clase%204/Actividad%202.xlsx)

### [Clase 5](./Clase%205/)

Se continúa con el análisis de datos de clientes y productos mediante archivos CSV.

- `Clase5.py`
- [`data_clientes.csv`](./Clase%205/data_clientes.csv)
- [`productos.csv`](./Clase%205/productos.csv)

### [Clase 6](./Clase%206/)

Se introducen las operaciones de transformación en pandas, contemplando filtros y selecciones.
El archivo dispone de la importación de un módulo de seaborn con el archivo `titanic.csv` para realizar las prácticas.

- `Clase6.py`

### [Clase 7](./Clase%207/)

Se presentan funciones de agregación y agrupamiento de datos.
Se utiliza un recurso creado como diccionario y el archivo `ventas.csv`.

- `Clase7.py`

### [Clase 8](./Clase%208/)

Combinación de diferentes fuentes de datos.
Se realiza una introducción a la combinación de datos tanto en Python puro como en librerías tales como NumPy y pandas.
Se utilizan métodos como `merge`, `join` y `concat`.

- `Clase8.py`
- [`data_empleados.csv`](./Clase%208/data_empleados.csv)
- [`situacion_empleados.csv`](./Clase%208/situacion_empleados.csv)
- [`ventas - Norte.csv`](./Clase%208/ventas%20-%20Norte.csv)
- [`ventas - Sur.csv`](./Clase%208/ventas%20-%20Sur.csv)

### [Clase 9](./Clase%209/)

Se introducen medidas de estadística descriptiva para analizar las ventas mensuales.
Se calculan la media, la mediana, la moda, el rango, la varianza y la desviación estándar utilizando NumPy y SciPy.

- `Clase9.py`

### [Clase 10](./Clase%2010/)

Se profundiza el análisis exploratorio y la visualización de datos utilizando los conjuntos `diamonds` y `titanic` de Seaborn.
Se realizan resúmenes estadísticos y gráficos de distribución, conteo, barras y cajas para analizar precios, colores y tasas de supervivencia.

- `Clase10.py`

### [Prácticas de auditoría](./Practicas%20Auditoria/)

Prácticas de análisis y auditoría de datos de ventas utilizando Python y archivos CSV.

- `Practica.py`
- [`datos_ventas_para_auditoria.csv`](./Practicas%20Auditoria/datos_ventas_para_auditoria.csv)

### [Proyecto final](./Proyecto%20Final/)

Aplicación de los contenidos desarrollados durante el curso en un proyecto de análisis de datos sobre ventas y acciones de marketing.

La preentrega incluye el análisis exploratorio y el control de calidad de los datos de ventas, la limpieza y transformación de los registros, el cálculo de ventas por producto y categoría, y la integración de ventas con marketing mediante una combinación por producto.

- [`Proyecto Final.py`](./Proyecto%20Final/Proyecto%20Final.py)
- [`Fuentes/clientes.csv`](./Proyecto%20Final/Fuentes/clientes.csv)
- [`Fuentes/marketing.csv`](./Proyecto%20Final/Fuentes/marketing.csv)
- [`Fuentes/ventas.csv`](./Proyecto%20Final/Fuentes/ventas.csv)
- [`Consigna - Rubrica/Rúbrica de Evaluación - Preentrega Data Analytics - Rúbrica.pdf`](./Proyecto%20Final/Consigna%20-%20Rubrica/R%C3%BAbrica%20de%20Evaluaci%C3%B3n%20-%20Preentrega%20Data%20Analytics%20-%20R%C3%BAbrica.pdf)
- [`Consigna - Rubrica/Sets de datos.pdf`](./Proyecto%20Final/Consigna%20-%20Rubrica/Sets%20de%20datos.pdf)

## Cómo ejecutar

Los scripts utilizan Python y, según la clase, las librerías `pandas`, `numpy` y `seaborn`. Para ejecutar el proyecto final:

```powershell
python -m pip install pandas numpy seaborn openpyxl
python "Proyecto Final/Proyecto Final.py"
```

El comando debe ejecutarse desde la carpeta raíz del repositorio, porque el script utiliza rutas relativas para acceder a los archivos de `Proyecto Final/Fuentes/`.

## Progresión de contenidos

El repositorio refleja una incorporación progresiva de conceptos:

1. Fundamentos de Python y programación.
2. Estructuras de datos y procesamiento de información.
3. Scope de variables y lectura de archivos externos.
4. Análisis de archivos CSV y Excel.
5. Transformación y limpieza de datos con pandas.
6. Agregación y agrupamiento de información.
7. Combinación de fuentes de datos con `merge`, `join` y `concat`.
8. Aplicación de los contenidos en prácticas de auditoría y en el proyecto final.
9. Aplicación de medidas de estadística descriptiva sobre datos de ventas.
10. Análisis exploratorio y visualización de datos con Seaborn y Matplotlib.

## Estructura del repositorio

```text
Cursada Analisis de Datos/
├── Clase 1/
│   └── Clase1.py
├── Clase 2/
│   └── Clase2.py
├── Clase 3/
│   ├── Clase3.py
│   ├── ventas.csv
│   └── ventas.xlsx
├── Clase 4/
│   ├── Clase4.py
│   ├── satis_clientes.csv
│   └── Actividad 2.xlsx
├── Clase 5/
│   ├── Clase5.py
│   ├── data_clientes.csv
│   └── productos.csv
├── Clase 6/
│   └── Clase6.py
├── Clase 7/
│   └── Clase7.py
├── Clase 8/
│   ├── Clase8.py
│   ├── data_empleados.csv
│   ├── situacion_empleados.csv
│   ├── ventas - Norte.csv
│   ├── ventas - Sur.csv
├── Clase 9/
│   └── Clase9.py
├── Clase 10/
│   └── Clase10.py
├── Practicas Auditoria/
│   ├── Practica.py
│   └── datos_ventas_para_auditoria.csv
├── Proyecto Final/
│   ├── Consigna - Rubrica/
│   │   ├── Rúbrica de Evaluación - Preentrega Data Analytics - Rúbrica.pdf
│   │   └── Sets de datos.pdf
│   ├── Fuentes/
│   │   ├── clientes.csv
│   │   ├── marketing.csv
│   │   └── ventas.csv
│   └── Proyecto Final.py
└── README.md
```
