campo.addEventListener('change', (event)=>{
    traerValoresEcharts(event.target.value)
  })
  
  function traerValoresEcharts(id){
    $(document).ready(function () {
      $.ajax({
          url: `http://127.0.0.1:8000/getapi/${id}/` , // Actualiza esto con tu URL
          type: 'GET',
          dataType: 'json',
          success: function (data) {
              // 'data' ahora contiene los datos del modelo en formato JSON
              console.log(data.mesesArray);
              echarFuncion(data.mesesArray)
              // Puedes procesar los datos aquí según tus necesidades
          },
          error: function (error) {
              console.log('Error al obtener datos:', error);
          }
      });
    });
  }
  
  var myChart = echarts.init(document.getElementById('main'));
 
  function echarFuncion(datos){
    const valormas = document.querySelector('.valormas')
    meses =  ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov','Dic']
    var mesesDelAno = [
      'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
      'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ];
    var valorMasAlto = 0;
    var posicionMasAlta = 0;
    
    // Iterar sobre el array para encontrar el valor más alto y su posición
    for (var i = 0; i < datos.length; i++) {
        if(datos[i] > valorMasAlto) {
            valorMasAlto = datos[i]
            posicionMasAlta = i;
        }
    }
    if(valorMasAlto != 0){
      valormas.innerHTML = `<p>El valor mas alto corresponde al mes de ${mesesDelAno[posicionMasAlta]} total : ${valorMasAlto}</p>`
    }else{
      valormas.innerHTML = `<p>No hubo ingresos este año</p>`
    }
    
    console.log("El valor más alto es:", valorMasAlto);
    console.log("", mesesDelAno[posicionMasAlta]);
    
    miarray = []
    for(let i =0; i< datos.length;i++){
        valores = {
            value : datos[i],
            name : meses[i]
      
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
  }
  
  
  