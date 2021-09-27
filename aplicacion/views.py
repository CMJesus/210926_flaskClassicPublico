from aplicacion import app
from flask import render_template, request, redirect, url_for
from aplicacion.models import DBManager
from aplicacion.forms import MovimientoFormulario

ruta_basedatos = app.config.get("RUTA_BASE_DE_DATOS")
dbManager = DBManager(ruta_basedatos)

#Rutas

@app.route("/")
def inicio():

    consulta = """
        SELECT * 
            FROM movimientos 
            ORDER BY fecha;
    """
    movimientos = dbManager.consultaSQL(consulta)
    
    return render_template("index.html", items=movimientos)

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    formulario = MovimientoFormulario()

    if request.method == 'GET':
        return render_template("nuevo_mov.html", form=formulario)
    else:
        if formulario.validate():
            consulta = """INSERT INTO movimientos (fecha, concepto, ingreso_gasto, cantidad)
                            VALUES (:fecha, :concepto, :ingreso_gasto, :cantidad)"""

            dbManager.insertaSQL(consulta, formulario.data)

            return redirect(url_for("inicio"))
        else:
            return render_template("nuevo_mov.html", form = formulario)

        # Validar formulario
        # si la validación es Ok, insertar registro en Tabla y redireccionar a /
        # si la validación no es Ok, devolver formulario y render_template
        #         preparar plantilla para gestionar errores


@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def borrar(id):
    return f"Página de borrado de {id}"