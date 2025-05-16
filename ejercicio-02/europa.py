import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from generar_base import Pais, engine

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consultar países de Europa ordenados por capital
paises_europa = session.query(Pais).filter(Pais.continente == "EU").order_by(Pais.capital).all()

st.title("Países de Europa Ordenados por Capital")

# Mostrar en texto
for pais in paises_europa:
    st.write("País:", pais.nombre_pais, "-----------","Capital:", pais.capital)
    st.markdown("---")


st.title("Tabla de Países Europeos Ordenados por Capital")
lista_europa = []

for p in paises_europa:
    diccionario = {
        "ID": p.id,
        "País": p.nombre_pais,
        "Capital": p.capital,
        "Continente": p.continente,
        "Dial": p.dial,
        "Lenguajes": p.lenguajes,
        "Independiente": p.es_independiente
    }
    lista_europa.append(diccionario)

st.dataframe(lista_europa)
