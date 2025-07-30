#Importamos librerías necesarias para la aplicación
import streamlit as st
import pandas as pd
import plotly.express as px

#Importamos nuestro set de datos
car_data = pd.read_csv('C:/Users/ralf_/Documents/Proyectos/proyectos/proyecto_7/proyecto_7/vehicles_us.csv')

#Creamos un encavezado que describa el proyecto
st.header('Análisis del inventario actual de autos seminuevos a la venta')

#Creamos un botón para realizar un histograma interactivo
hist_button = st.button('Crea un histograma')

if hist_button:
    st.write('Creación de un histograma para visualizar los datos de los autos a la venta ')
    fig= px.histogram(car_data, x="odometer")

    st.plotyl_chart(fig, use_container_width=True)

#Creamos un checkBox para crear un gráfico de dispersión interactivo
scatter_box = st.checkbox('Crea un gráfico de dispersión')
if scatter_box:
    st.write('Costruir un gráfico para mostrar la relación entre el kolometrage y el precio del vehículo')
    fig= px.scatter(car_data, x= 'odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)

#Creamos un CheckBox para crear un gráfico de barras interactivo
bar_box = st.checkbox('Crea un gráfico de barras')
if bar_box:
    st.write('Construir un gráfico de barras para analizar los precios por los diferentes tipos de vehículos')
    fig= px.bar(car_data, x='type', y='price')
    st.plotyl_chart(fig, use_container_width=True)