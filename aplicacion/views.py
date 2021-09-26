from aplicacion import app
from flask import render_template
from aplicacion.models import DBManager

ruta_basedatos = app.config.get("RUTA_BASE_DE_DATOS")
dbManager = DBManager(ruta_basedatos)

#Rutas

@app.route("/")
def inicio():

    consulta = """
        SELECT * 
            FROM movimientos 
            ORDER BY fecha;"
    """
    movimientos = dbManager.consultaSQL(consulta)
    
    return render_template("index.html", items=movimientos)

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    return "Págnia de alta de movimientos"

@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def borrar(id):
    return f"Página de borrado de {id}"