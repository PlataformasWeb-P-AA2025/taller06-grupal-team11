import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from generar_base import Pais, engine

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los países
paises = session.query(Pais).all()

# Título principal
st.title("Lenguajes por País")

# Mostrar en texto
for pais in paises:
    st.write("País:", pais.nombre_pais, "-----------","Lenguajes:", pais.lenguajes)
    st.markdown("---")


st.title("Tabla de Lenguajes por País")
lista_lenguajes = []

for p in paises:
    diccionario = {
        "País": p.nombre_pais,
        "Lenguajes": p.lenguajes
    }
    lista_lenguajes.append(diccionario)

st.dataframe(lista_lenguajes)
