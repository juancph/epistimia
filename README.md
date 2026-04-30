# Epistimia

**Epistimia** es una enciclopedia web sobre epistemología desarrollada como proyecto académico. Su objetivo es organizar y presentar de forma clara los principales conceptos, corrientes filosóficas, problemas y autores relacionados con el conocimiento.

---

## Tecnologías utilizadas

- Flask → Backend y renderizado de plantillas
- HTML + Jinja2 → Estructura de páginas dinámicas
- Tailwind CSS → Estilos y diseño visual
- JSON → Almacenamiento de contenido

---

## Estructura del proyecto

```
epistimia/
│
├── app.py
├── crear_articulo.py
│
├── /data
│   └── contenidos.json
│
├── /templates
│   ├── base.html
│   ├── index.html
│   ├── articulo.html
│   └── categoria.html
│
├── /static
│   ├── /css
│   │   └── styles.css
│   ├── /js
│   │   └── main.js
│   └── /img
```

---

## Estructura de los artículos

Cada artículo se guarda en formato JSON con la siguiente estructura:

```json
{
  "slug": {
    "titulo": "Título del artículo",
    "categoria": "categoria",
    "contenido": "Texto del contenido...",
    "relacionados": ["otro_slug"]
  }
}
```

---

## Uso del script de contenido

Para facilitar la creación de artículos:

```bash
python crear_articulo.py
```

Este script permite:

- Crear nuevos artículos
- Guardarlos automáticamente en el JSON
- Mantener consistencia en la estructura

---

## Cómo ejecutar el proyecto

1. Crear entorno virtual:

```bash
python -m venv venv
source venv/bin/activate   # Linux
venv\Scripts\activate      # Windows
```

2. Instalar dependencias:

```bash
pip install Flask
```

3. Ejecutar la aplicación:

```bash
python app.py
```

4. Abrir en el navegador:

```
http://127.0.0.1:5000/
```

---

## Objetivo del proyecto

Construir una enciclopedia digital que permita:

- Explorar conceptos de epistemología
- Navegar entre artículos relacionados
- Comprender las bases del conocimiento de forma estructurada

---

## Notas

Este proyecto tiene fines educativos y busca aplicar conocimientos de desarrollo web junto con contenidos filosóficos.
