const elementos = document.getElementsByClassName("suma");
const boton = document.querySelector(".boton");
const resultado = document.querySelector(".resultado")

// Inicializar la variable para almacenar la suma
suma = 0;

// Iterar a través de los elementos y sumar sus valores
boton.addEventListener("click",()=>{

    for (let i = 0; i < elementos.length; i++) {
        // Obtener el contenido del elemento como número (parseando la cadena)
        var valor = parseFloat(elementos[i].textContent);
        
        // Sumar el valor al total si es un número válido
        if (!isNaN(valor)) {
            suma += valor;
        }
    }
    resultado.innerHTML = suma
    console.log("La suma es: " + suma);
    
})

// Mostrar la suma en la consola o en algún otro lugar
