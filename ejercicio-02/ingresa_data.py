from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_base import Pais
import requests

engine = create_engine('sqlite:///country-codes.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

archivo = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json')

datos_json = archivo.json()

for d in datos_json:
    print(d)
    print(len(d.keys()))
    p = Pais(nombre_pais=d['CLDR display name'], capital=d['Capital'], continente=d['Continent'], dial=d['Dial'], geoname_id=d['Geoname ID'] , itu=d['ITU'], lenguajes=d['Languages'], es_independiente=d['is_independent'])
    session.add(p)  
session.commit()
