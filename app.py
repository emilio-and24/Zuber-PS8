import pandas as pd
import streamlit as st
import plotly.express as px
#
car_data = pd.read_csv('../vehicles_us.csv')
#
st.header("Analisis sobre anuncios de ventas de coches")
#
# box histo
hist_button = st.checkbox('Construir histograma')
if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
#
# box disp
scat_button = st.checkbox("Contriuir grafico de dispersion")
if scat_button:
    st.write("Creacion de un grafico de dispersion para el conjunto de datos anuncios de venta de coches")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
