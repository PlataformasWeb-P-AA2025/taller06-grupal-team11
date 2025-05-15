from sqlalchemy import create_engine

engine = create_engine('sqlite:///country-codes.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'paises'

    id = Column(Integer, primary_key=True)
    nombre_pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname_id = Column(String)
    itu = Column(String)
    lenguajes = Column(String)
    es_independiente = Column(String)


Base.metadata.create_all(engine)

