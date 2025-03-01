from sqlalchemy import Column, Integer, String, DateTime, Date

from app.database import Base


class Students(Base):
    """
    Represents a student in the database.

    Attributes:
        id (int): The unique identifier for the student.
        nombre (str): The first name of the student.
        apellido (str): The last name of the student.
        correo (str): The email address of the student.
        fecha_nacimiento (datetime.date): The date of birth of the student.
        carrera (str): The major or course of study of the student.
        semestre (int): The current semester of the student.
    """

    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=False)
    fecha_nacimiento = Column(Date)
    carrera = Column(String(100))
    semestre = Column(Integer)
