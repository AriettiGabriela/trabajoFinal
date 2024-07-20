from flask import Flask, render_template  # llamar al framework

app = Flask(__name__)  # guarda en una variable la ruta de inicio de la app

# Rutas de procesamiento (direccionan a algun lugar)
@app.route('/')    # método que crea una url
def home():        # función  que devuelve información al navegador
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/tienda')
def tienda():
    return render_template("tienda.html")

@app.route('/aula')
def aula():
    return render_template("aula.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/registro')
def registro():
    return render_template("registro.html")

@app.route('/detalle')
def detalle():
    return render_template("detalle.html")

@app.route('/compra')
def compra():
    return render_template("compra.html")

@app.route('/curso')
def curso():
    return render_template("curso.html")

@app.route('/modificar')
def modificar():
    return render_template("modificar.html")
# validamos si estamos en el archivo principal para que siempre se quede
# escuchando una peticion del usuario y si se cumple ejecuta el app.run
if __name__ == '__main__':
    app.run(debug=True)
