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
    st.write('El gráfico muestra la distrubución del kilometraje de los vehículos en stock ')
    fig= px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

#Creamos un checkBox para crear un gráfico de dispersión interactivo
scatter_box = st.checkbox('Crea un gráfico de dispersión')
if scatter_box:
    st.write('El gráfico muestra la relación entre el kilometraje y el precio de los vehículos')
    fig= px.scatter(car_data, x= 'odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)

#Creamos un CheckBox para crear un gráfico de barras interactivo
bar_box = st.checkbox('Crea un gráfico de barras')
if bar_box:
    st.write('El gráfico muestra la diferencia de precio según el tipo de vehículo')
    fig= px.bar(car_data, x='type', y='price')
    st.plotly_chart(fig, use_container_width=True)