var myChart = echarts.init(document.getElementById('main'));
const ga = document.querySelector('.xa')
const clase1 = document.querySelector('.vacio')
const valormas = document.querySelector('.valormas')

meses =  ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov','Dic']
var mesesDelAno = [
  'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
  'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
];
var valorMasAlto = 0;
var posicionMasAlta = 0;

// Iterar sobre el array para encontrar el valor más alto y su posición
for (var i = 0; i < clase1.children.length; i++) {
    if (parseInt(clase1.children[i].innerHTML) > valorMasAlto) {
        valorMasAlto = parseInt(clase1.children[i].innerHTML)
        posicionMasAlta = i;
    }
}
valormas.innerHTML = `<p>El valor mas alto corresponde al mes de ${mesesDelAno[posicionMasAlta]} total : ${valorMasAlto}</p>`

console.log("El valor más alto es:", valorMasAlto);
console.log("", mesesDelAno[posicionMasAlta]);



miarray = []
for (let index = 0; index < clase1.children.length; index++) {
  valor= parseInt(clase1.children[index].innerHTML)
  valores = {
      value : valor,
      name : meses[index]

  };

  miarray.push(valores)
  
}

option = {
  tooltip: {
    trigger: 'item'
  },
  legend: {
    top: '5%',
    left: 'center'
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      label: {
        show: false,
        position: 'center'
      },
      emphasis: {
        label: {
          show: true,
          fontSize: 40,
          fontWeight: 'bold'
        }
      },
      labelLine: {
        show: false
      },
      data:miarray
    }
  ]
};

myChart.setOption(option);