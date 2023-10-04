

    const eliminarElemento = document.getElementById("eliminarX");
    const deleteHref = eliminarElemento.getAttribute("href")
    const botonOk = document.getElementById("botonOk")
    const botonNo = document.getElementById("botonNo")
    const eliminarConfirmar = document.querySelector(".eliminarConfirmar")
    eliminarElemento.addEventListener("click", function (event) {
        event.preventDefault();
        eliminarConfirmar.classList.toggle("togle")
        botonOk.addEventListener("click",(ev)=>{
            window.location.href = deleteHref
        })

        botonNo.addEventListener("click",(ev)=>{
            window.location.href = deleteHref
        })
        // Muestra una ventana emergente de confirmación
      
   

        
        // Si el usuario confirma la eliminación, redirige a la vista de eliminación de Django
        // if (confirmar) {

        //     window.location.href = deleteHref
        // }
    });


