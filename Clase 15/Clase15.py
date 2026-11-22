import pandas as pd
import plotly.express as px
import ipywidgets as widgets
from dash import Dash, dcc, html, Input, Output

# SECCION 1
# CONSIGNA: Cargar el dataset de ventas ventas_por_region.csv
data = pd.read_csv('Clase 15/ventas_por_region.csv')

# CONSIGNA: Utilizar Plotly para crear un gráfico de líneas que muestre la evolución de las ventas a lo largo del tiempo para cada producto.
# CONSIGNA: Implementar interactividad: Permitir que los usuarios puedan pasar el cursor sobre las líneas para visualizar 
# los valores exactos de ventas en cada fecha.

data["ventas"] = data["ventas"].str.strip()
data["ventas"] = data["ventas"].str.replace("$","", regex=False)
data["ventas"] = data["ventas"].astype(float)

data["fecha"] = pd.to_datetime(data["fecha"], errors="coerce", format="%Y-%m-%d")
data = data.sort_values("fecha")
data = data.groupby("fecha")["ventas"].mean().reset_index()

fig = px.line(data, x="fecha", y="ventas",title="Evolucion ventas en el tiempo", 
              line_shape="spline", render_mode="svg", hover_data="ventas")
fig.show()

# CONSGINA: Crear un gráfico de barras que compare las ventas totales de cada producto.
# CONSGINA: Implementar filtros para que los usuarios puedan seleccionar una región específica y visualizar 
# las ventas únicamente para esa región.

data["año"] = data["fecha"].dt.year

data1 = data[data["año"] == 2024].groupby("producto")["ventas"].sum().reset_index()
data2 = data[data["año"] == 2025].groupby("producto")["ventas"].sum().reset_index()

selector = widgets.Dropdown(options=[2024,2025],value=2024,
                            description="Año:")

def grafico_bar_personalizado(año):
    dataframe = data1 if año == 2024 else data2
    fig2 = px.bar(dataframe, x="producto", y="ventas", color="producto", 
              hover_data=["ventas"], title=f'Ventas del año {año}'
              ,labels={"valor":"ventas totales", "categoria":"Productos"})
    fig2.show()

grafico_bar_personalizado(selector.value)
widgets.interact(grafico_bar_personalizado,año=selector)

# SECCION 2
# CONSGINA: Cargar el dataset de redes sociales rrss.csv, Utilizar Dash y Plotly para crear un 
# dashboard con los siguientes elementos

data = pd.read_csv("Clase 15/rrss.csv")
data["fecha"] = pd.to_datetime(data["fecha"], errors="coerce", format="%Y-%m-%d")

# CONSIGNA: Un gráfico de líneas que muestre la evolución de la cantidad de seguidores a 
# lo largo del tiempo para cada plataforma (Facebook, Twitter, Instagram, etc.).

selector1 = widgets.Dropdown(options=[2024,2025],value=2024,
                            description="Año:")

selector2 = widgets.Dropdown(options=['TikTok', 'YouTube', 'Facebook', 'X', 'Instagram'], value="X",
                              description="Plataforma:")

def lineas_rrss(plataforma, año):
    data_p = data[(data["plataforma"] == plataforma) & (data["fecha"].dt.year == año)].sort_values("fecha")
    data_p = data_p.groupby("fecha")["seguidores"].mean().reset_index()
    fig = px.line(data_p,x="fecha",y="seguidores",
                  title=f"Evolucion de seguidores de {plataforma} en {año}", hover_data="seguidores",
                  line_shape="spline", render_mode="svg")
    fig.show()

lineas_rrss(selector2.value,selector1.value)
widgets.interact(lineas_rrss,año=selector1, plataforma=selector2)

# CONSIGNA: Un gráfico de barras que compare la cantidad de "me gusta" y comentarios en cada plataforma.

def barras_rrss(plataforma, año):
    data_p = data[(data["plataforma"] == plataforma) & (data["fecha"].dt.year == año)].sort_values("fecha")
    data_p = data_p.groupby("fecha")[["likes","comentarios"]].mean().reset_index()
    fig = px.bar(data_p,x="fecha", y=["likes","comentarios"], barmode="group", 
                  title=f"Likes y comentarios en {año} de {plataforma}")
    fig.show()

barras_rrss(selector2.value, selector1.value)
widgets.interact(barras_rrss,año=selector1, plataforma=selector2)

# CONSGINA: Filtros que permitan a los usuarios seleccionar una o varias plataformas y 
# un período de tiempo específico.
# CONSGINA: Títulos claros y concisos para cada gráfico.

# Respuesta: se realizaron con la creacion del grafico en si.