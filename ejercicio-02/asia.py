import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, cast, Integer
from generar_base import Pais, engine

Session = sessionmaker(bind=engine)
session = Session()

paises_asia = session.query(Pais).filter(Pais.continente == "AS").order_by(cast(Pais.dial, Integer)).all()

st.title("Países del Continente Asiático (Ordenados por Dial)")

# Mostrar en texto
for pais in paises_asia:
    st.write("País:", pais.nombre_pais, "-----------", "Dial:", pais.dial)
    st.markdown("---")

# Mostrar en tabla
st.title("Tabla de Países de Asia Ordenados por Dial")
lista_asia = []

for p in paises_asia:
    diccionario = {
        "ID": p.id,
        "Nombre": p.nombre_pais,
        "Capital": p.capital,
        "Continente": p.continente,
        "Dial": p.dial,
        "Lenguajes": p.lenguajes,
        "Independiente": p.es_independiente
    }
    lista_asia.append(diccionario)

st.dataframe(lista_asia)
