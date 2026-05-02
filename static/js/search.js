const input = document.getElementById("searchInput");
const suggestionsBox = document.getElementById("suggestions");

input.addEventListener("input", function () {
    const query = this.value.toLowerCase().trim();
    suggestionsBox.innerHTML = "";

    if (!query) return;

    let resultados = [];

    // Buscar coincidencias
    for (let slug in articulos) {
        const articulo = articulos[slug];
        const titulo = articulo.titulo.toLowerCase();

        if (titulo.includes(query)) {
            resultados.push({ slug, titulo: articulo.titulo });
        }
    }

    // Limitar resultados
    resultados = resultados.slice(0, 5);

    // Mostrar resultados
    resultados.forEach(item => {
        const div = document.createElement("div");
        div.classList.add("suggestion-item");

        div.innerHTML = `<a href="/articulo/${item.slug}">${item.titulo}</a>`;

        suggestionsBox.appendChild(div);
    });
});


// Cerrar sugerencias al hacer click fuera
document.addEventListener("click", function (e) {
    if (!e.target.closest("#searchInput") && !e.target.closest("#suggestions")) {
        suggestionsBox.innerHTML = "";
    }
});