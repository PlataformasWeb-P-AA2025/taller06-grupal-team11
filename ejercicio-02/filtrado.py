import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, or_
from generar_base import Pais, engine

Session = sessionmaker(bind=engine)
session = Session()

# Consulta: países con "uador" en el nombre o "ito" en la capital, ordenados por nombre del país
paises_filtrados = session.query(Pais).filter(or_(Pais.nombre_pais.ilike("%uador%"),Pais.capital.ilike("%ito%"))).order_by(Pais.nombre_pais).all()

#paises_filtrados = session.query(Pais).filter(or_(Pais.nombre_pais=="uador", Pais.capital=="ito")).order_by(Pais.nombre_pais).all()


# Mostrar resultados
st.title('Países con "uador" en el nombre o "ito" en la capital')

for pais in paises_filtrados:
    st.write("País:", pais.nombre_pais, "Capital:", pais.capital)
    st.markdown("---")

st.title("Tabla de Países Filtrados")
lista_paises = []

for p in paises_filtrados:
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
