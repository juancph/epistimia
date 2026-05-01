import json

RUTA = "data/contenidos.json"

def escribir_json(data, ruta=RUTA):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return data


def leer_json(ruta=RUTA):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        return data

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}


def crear_slug(titulo):
    return titulo.lower().replace(" ", "-")


def nuevo_contenido():
    data = leer_json()

    while True:

        while True:
            titulo = input("Titulo: ").strip()
            contenido = input("Contenido: ").strip()
            categoria = input("Categoria: ").strip()
            
            if not titulo or not contenido:
                print("Los campos no pueden estar vacios")
                continue

            for i in data:
                if data[i]["titulo"] == titulo:
                    print(f"'{titulo}' ya existe")
                    break
            break
        
        slug = crear_slug(titulo)

        data[slug] = {
            "titulo": titulo,
            "contenido": contenido,
            "categoria": categoria
        }

        continuar = input("Deseas agregar más contenido (s/n): ")
        
        if continuar == "n": return data


if __name__ == "__main__":
    escribir_json(nuevo_contenido())