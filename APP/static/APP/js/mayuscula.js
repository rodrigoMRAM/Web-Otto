
    // Obtén el valor actual del input
    const input = document.querySelector('input[name="patente"]');
    input.setAttribute("oninput", "convertirAMayusculas()")
    function convertirAMayusculas() {
        // Obtén el valor actual del input

        var valor = input.value;
      
        // Convierte el valor a mayúsculas
        valor = valor.toUpperCase();
      
        // Establece el valor del input en mayúsculas
        input.value = valor;
      }
      