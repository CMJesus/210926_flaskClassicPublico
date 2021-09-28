from aplicacion import app
from flask import render_template, request, redirect, url_for
from aplicacion.models import DBManager
from aplicacion.forms import MovimientoFormulario
from datetime import date

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

            try:
                dbManager.insertaSQL(consulta, formulario.data)
            except Exception as es:
                print("Se ha producido un error de acceso a base de datos:", e)
                flash("Se ha producido un error en la base de datos. Consulte con su administrador")
                return render_template("nuevo_mov.html", el_formulario=formulario)

            return redirect(url_for("inicio"))
        else:
            return render_template("nuevo_mov.html", form = formulario)

        # Validar formulario
        # si la validación es Ok, insertar registro en Tabla y redireccionar a /
        # si la validación no es Ok, devolver formulario y render_template
        #         preparar plantilla para gestionar errores


@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def borrar(id):
    if request.method == 'GET':
        consulta = """
        SELECT id, fecha, concepto, ingreso_gasto, cantidad
        FROM movimientos
        WHERE id = ?;
        """

        movimientos = dbManager.consultaSQL(consulta, [id])
        if len(movimientos) == 0:
            flash(f"Movimiento {id} no encontrado")
            return redirect(url_for("inicio"))


        el_movimiento = movimientos[0]
        el_movimiento["fecha"] = date.fromisoformat(el_movimiento["fecha"])
        formulario = MovimientoFormulario(data=el_movimiento)
            

        return render_template("delete_mov.html", form=formulario, el_id=el_movimiento['id'])
    
    else:
        pass
    #Aquí hay que hacer lo mismo que en la consulta que tenemos, aslvo que con delete
        # consulta = """INSERT INTO movimientos (fecha, concepto, ingreso_gasto, cantidad)
        #                     VALUES (:fecha, :concepto, :ingreso_gasto, :cantidad)"""

        #     try:
        #         dbManager.insertaSQL(consulta, formulario.data)
        #     except Exception as es:
        #         print("Se ha producido un error de acceso a base de datos:", e)
        #         flash("Se ha producido un error en la base de datos. Consulte con su administrador")
        #         return render_template("nuevo_mov.html", el_formulario=formulario)

        #     return redirect(url_for("inicio"))
        # else:
        #     return render_template("nuevo_mov.html", form = formulario)

    
    return 'Hola, soy un post'

