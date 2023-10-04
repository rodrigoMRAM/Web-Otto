// Obtén una lista de todos los elementos con la clase "mi-label"
var labels = document.querySelectorAll("label");

// Usa un ciclo for para recorrer y manipular los elementos
labelFiltro = ["Nombre: ", "Patente: ", "Mes: "]

for (var i = 0; i < labels.length; i++) {
  labels[i].textContent = labelFiltro[i];
}
