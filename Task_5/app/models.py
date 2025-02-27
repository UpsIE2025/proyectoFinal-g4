from sqlalchemy import Column, Integer, String, DateTime, Date

from app.database import Base


class Students(Base):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=False)
    fecha_nacimiento = Column(Date)
    carrera = Column(String(100))
    semestre = Column(Integer)
