from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)


class Preceptor(db.Model):
    __tablename__ = "preceptor"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    apellido = db.Column(db.String, nullable=False)
    correo = db.Column(db.String, unique=True, nullable=False)
    clave = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "clave": self.clave,
        }


class Padre(db.Model):
    __tablename__ = "padre"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    apellido = db.Column(db.String, nullable=False)
    correo = db.Column(db.String, unique=True, nullable=False)
    clave = db.Column(db.String, nullable=False)


class Estudiante(db.Model):
    __tablename__ = "estudiante"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    apellido = db.Column(db.String, nullable=False)
    dni = db.Column(db.String, nullable=False)
    idcurso = db.Column(db.Integer, nullable=False)
    idpadre = db.Column(db.Integer, nullable=False)


class Curso(db.Model):
    __tablename__ = "curso"
    id = db.Column(db.Integer, primary_key=True)
    anio = db.Column(db.String, nullable=False)
    division = db.Column(db.String, nullable=False)
    idpreceptor = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "anio": self.anio,
            "division": self.division,
            "idpreceptor": self.idpreceptor,
        }


class Asistencia(db.Model):
    __tablename__ = "asistencia"
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String, nullable=False)
    codigoclase = db.Column(db.String, nullable=False)
    asistio = db.Column(db.Text, nullable=False)
    justificacion = db.Column(db.String(100), nullable=False)
    idestudiante = db.Column(db.Integer, nullable=False)

    def __init__(self, fecha, codigoclase, asistio, justificacion, idestudiante):
        self.fecha = fecha
        self.codigoclase = codigoclase
        self.asistio = asistio
        self.justificacion = justificacion
        self.idestudiante = idestudiante
