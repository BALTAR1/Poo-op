from flask import Flask, request, render_template, redirect, url_for, session, json
from flask_session import Session
from datetime import datetime, date
from borrar import obtener_fechas_mes
import calendar
from flask_sqlalchemy import SQLAlchemy
import hashlib

# <br><br><a href="{{ url_for('login') }}"> Inicio </a><br><br>
app = Flask(__name__)
app.config.from_pyfile("config.py")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

from models import db
from models import Preceptor, Padre, Estudiante, Curso, Asistencia


@app.route("/", methods=["GET", "POST"])
def index():
    if not session.get("user"):
        return redirect(url_for("login"))
    else:
        return redirect(url_for("preceptor"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if not request.form.get("email") or not request.form.get("clave"):
            return render_template("error.html", error="Ingrese email y contraseña")
        else:
            if request.form["rol"] == "preceptor":
                ususario_actual = Preceptor.query.filter_by(
                    correo=request.form["email"]
                ).first()
                if ususario_actual:
                    clave = hashlib.md5(
                        bytes(request.form["clave"], encoding="utf-8")
                    ).hexdigest()
                    if clave == ususario_actual.clave:
                        serialized_preceptor = ususario_actual.to_dict()
                        session["user"] = ususario_actual.id
                        session["rol"] = "preceptor"
                        session["preceptor"] = json.dumps(serialized_preceptor)
                        cursos = Curso.query.filter(
                            Curso.idpreceptor == ususario_actual.id
                        ).all()
                        serialized_cursos = [curso.to_dict() for curso in cursos]
                        session["cursos"] = json.dumps(serialized_cursos)
                        return render_template(
                            "preceptor.html", usuario=json.loads(session["preceptor"])
                        )
                    else:
                        return render_template(
                            "error.html", error="Contraseña incorrecta"
                        )
                else:
                    return render_template("error.html", error="Email incorrecto")
            else:
                ususario_actual = Padre.query.filter_by(
                    correo=request.form["email"]
                ).first()
                if ususario_actual:
                    clave = hashlib.md5(
                        bytes(request.form["clave"], encoding="utf-8")
                    ).hexdigest()
                    if clave == ususario_actual.clave:
                        return render_template(
                            "error.html", error="No es un trabajo grupal"
                        )
                    else:
                        return render_template(
                            "error.html", error="Contraseña incorrecta"
                        )
                else:
                    return render_template("error.html", error="Email incorrecto")
    else:
        return render_template("/login.html")


@app.route("/preceptor", methods=["GET", "POST"])
def preceptor():
    return render_template("/preceptor.html")


@app.route("/cursospreceptor", methods=["GET", "POST"])
def cursos():
    if session["rol"] == "preceptor":
        if request.method == "POST":
            año = datetime.today().year
            mes = datetime.today().month
            fechas = obtener_fechas_mes(año, mes)
            curso = request.form["curso"]
            clase = request.form["clase"]
            estudiantes = Estudiante.query.filter(Estudiante.idcurso == curso).all()
            today = date.today()
            return render_template(
                "/registro_asistencia.html",
                curso=curso,
                clase=clase,
                estudiantes=estudiantes,
                fechas=fechas,
                date=today,
            )
        else:
            return render_template(
                "cursospreceptor.html",
                cursos=json.loads(session["cursos"]),
                usuario=json.loads(session["preceptor"]),
            )
    else:
        return render_template("error.html", error="No tiene acceso.")


@app.route("/registro_asistencias", methods=["GET", "POST"])
def registro_asistencia():
    if request.method == "POST":
        fecha = request.form["fecha"]
        idestudiante = request.form["idestudiante"]
        asisistenciacarga = Asistencia.query.filter(
            Asistencia.idestudiante == idestudiante, Asistencia.fecha == fecha
        ).first()
        if asisistenciacarga is None:
            codigoclase = request.form["clase"]
            asistio = request.form["asistio"]
            justificacion = request.form["justificacion"]
            asistencia = Asistencia(
                fecha, codigoclase, asistio, justificacion, idestudiante
            )
            db.session.add(asistencia)
            db.session.commit()
            print("En teoria se guardó")
            return redirect(url_for("cursos"))
        else:
            return render_template(
                "error.html", error="Ya hay una asistencia en ese día."
            )
    else:
        return render_template("/registro_asistencia.html")


@app.route("/elegircurso", methods=["GET", "POST"])
def elegircurso():
    if session["rol"] == "preceptor":
        if request.method == "POST":
            curso = request.form["curso"]
            estudiantes = (
                Estudiante.query.filter(Estudiante.idcurso == curso)
                .order_by(Estudiante.nombre)
                .all()
            )
            aulaP = []
            aulaJ = []
            aulaIn = []
            fisP = []
            fisJ = []
            fisIn = []
            for estudiante in estudiantes:
                aulaPCont = 0
                aulaJCont = 0
                aulaInCont = 0
                fisPCont = 0
                fisJCont = 0
                fisInCont = 0
                asistencias = Asistencia.query.filter(
                    Asistencia.idestudiante == estudiante.id
                ).all()
                for asistencia in asistencias:
                    if int(asistencia.codigoclase) == 1:
                        if asistencia.asistio == "s":
                            aulaPCont += 1
                        else:
                            if asistencia.justificacion == "":
                                aulaInCont += 1
                            else:
                                aulaJCont += 1
                    else:
                        if asistencia.asistio == "s":
                            fisPCont += 0.5
                        else:
                            if asistencia.justificacion == "":
                                fisInCont += 0.5
                            else:
                                fisJCont += 0.5
                aulaP.append(aulaPCont)
                aulaJ.append(aulaJCont)
                aulaIn.append(aulaInCont)
                fisP.append(fisPCont)
                fisJ.append(fisJCont)
                fisIn.append(fisInCont)

            return render_template(
                "/obtener_informe.html",
                todo=zip(estudiantes, aulaP, aulaJ, aulaIn, fisP, fisJ, fisIn),
            )
        else:
            return render_template(
                "/elegircurso.html",
                cursos=json.loads(session["cursos"]),
                usuario=json.loads(session["preceptor"]),
            )
    else:
        return render_template("error.html", error="No tiene acceso")


@app.route("/obtener_informe", methods=["GET", "POST"])
def obtener_informe():
    if session["rol"] == "preceptor":
        if request.method == "POST":
            return redirect(url_for("elegircurso"))
        else:
            return render_template("/obtener_informe.html")
    else:
        return render_template("error.html", error="No tiene permiso para esta acción")


@app.route("/informe_detallado/<idestudiante>", methods=["GET", "POST"])
def informe_detallado(idestudiante):
    estudiante = Estudiante.query.filter(Estudiante.id == idestudiante).first()
    asistencias = Asistencia.query.filter(Asistencia.idestudiante == idestudiante).all()
    return render_template(
        "informe_detallado.html", estudiante=estudiante, asistencias=asistencias
    )


@app.route("/pagina_anterior")
def pagina_anterior():
    return redirect(request.referrer or url_for("preceptor"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)
