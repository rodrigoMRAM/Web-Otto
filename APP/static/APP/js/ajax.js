// let ciudades = [];
// const cboPais = document.getElementById('cboPais')
// var urlActual = window.location.href;
// const listarCiudades = async () => {
//     try {
//         const response = await fetch(`http://127.0.0.1:8000/incomes/`);
//         const data = await response.json();

//         if (data.data === "Success") {
//             ciudades = data.datos;
//             let opciones = ``;
//             ciudades.forEach((ciudad) => {
//                 opciones += `<option >${ciudad[0]}</option>`;
//             });
//             cboPais.innerHTML = opciones;
//         } else {
//             alert("Países no encontrados...");
//         }
//     } catch (error) {
//         console.log(error);
//     }
// };

// listarCiudades();

// const xa = document.querySelector('.xa')

