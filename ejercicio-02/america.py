import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from generar_base import Pais, engine

Session = sessionmaker(bind=engine)
session = Session()


paises_america = session.query(Pais).filter(Pais.continente == "NA").all() + session.query(Pais).filter(Pais.continente == "SA").all()

# Mostrar con Streamlit
st.title("Países del Continente Americano")

# Mostrar en texto
for pais in paises_america:
    st.write("País:", pais.nombre_pais,"-----------", "Capital:", pais.capital)
    st.markdown("---")

# Mostrar en tabla
st.title("Tabla de Países del Continente Americano")
lista_paises = []

for p in paises_america:
    diccionario = {
        "ID": p.id,
        "Nombre": p.nombre_pais,
        "Capital": p.capital,
        "Continente": p.continente,
        "Dial": p.dial,
        "Lenguajes": p.lenguajes,
        "Independiente": p.es_independiente
    }
    lista_paises.append(diccionario)

st.dataframe(lista_paises)
