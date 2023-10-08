const navbar = document.querySelector('.navbar');
let prevScrollPos = window.pageYOffset;



window.onscroll = function() {
    const currentScrollPos = window.pageYOffset;
    
    if (prevScrollPos > currentScrollPos) {
        // Desplazamiento hacia arriba, muestra la barra de navegación
        navbar.classList.remove('hidden');
    } else {
        // Desplazamiento hacia abajo, oculta la barra de navegación
        navbar.classList.add('hidden');
    }

    prevScrollPos = currentScrollPos;
}

