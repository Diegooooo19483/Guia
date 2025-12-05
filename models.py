from sqlalchemy import Column, Integer, String
from database import Base

# Tabla de jugadores
class Jugador(Base):
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)
    posicion = Column(String)
    goles = Column(Integer, default=0)
