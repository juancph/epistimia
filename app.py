from flask import Flask, render_template, request, send_from_directory
from crear_articulo import leer_json
import os

app = Flask(__name__)


@app.route("/")
def inicio():
    # Sirve el Inicio.html estático que está en la raíz del proyecto
    return send_from_directory(app.root_path, "Inicio.html")


@app.route("/topicos")
def topicos():
    data = leer_json()
    return render_template("index.html", data=data)


@app.route("/articulo/<slug>")
def articulo(slug):
    data = leer_json()
    articulo = data.get(slug)
    return render_template("articulo.html", articulo=articulo, data=data)


@app.route("/buscar")
def buscar():
    data  = leer_json()
    query = request.args.get("q", "").strip().lower()

    resultados = []
    if query:
        for slug, art in data.items():
            titulo    = art.get("titulo", "").lower()
            contenido = art.get("contenido", "").lower()
            resumen   = art.get("resumen", "").lower()
            categorias = " ".join(art.get("categorias", [])).lower()

            if (query in titulo
                    or query in contenido
                    or query in resumen
                    or query in categorias):
                resultados.append((slug, art))

        # Primero los que coinciden en el título
        resultados.sort(key=lambda x: query not in x[1].get("titulo", "").lower())

    return render_template("buscar.html", resultados=resultados, query=query, data=data)


if __name__ == "__main__":
    app.run(debug=True)