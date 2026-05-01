from flask import Flask, render_template
from crear_articulo import leer_json

app = Flask(__name__)

@app.route("/")
def inicio():
    data = leer_json()
    return render_template("index.html", data=data)


@app.route("/articulo/<slug>")
def articulo(slug):
    data = leer_json()
    articulo = data.get(slug)

    return render_template("articulo.html", articulo=articulo)

if __name__ == "__main__":
    app.run(debug=True)