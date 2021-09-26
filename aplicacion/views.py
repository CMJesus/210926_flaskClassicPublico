from aplicacion import app

#Rutas

@app.route("/")
def inicio():
    return "Página de Inicio"

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    return "Págnia de alta de movimientos"

@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def borrar(id):
    return f"Página de borrado de {id}"