var circPos = 0;
var teste=0;
function espRequest() {
  const params = {
    exp: 'fis1',
    sensor: 'temperature'
  };
    fetch('api/espRequest.php',{
      method: 'POST',
      headers: {
      'Content-Type': 'application/json'
      },
      body: JSON.stringify(params)
    })
    .then(response => response.text())
    .then(data => {
      console.log("Teste FUNC ",data);
      teste=data;
    })
    .catch(error => console.error(error));
}
function downloadCSV(data) {
  const csvString = Papa.unparse(data); // Convert array to CSV string using PapaParse library
  const blob = new Blob([csvString], { type: 'text/csv' }); // Create a Blob object with the CSV string
  const url = URL.createObjectURL(blob); // Create object URL for the Blob object
  const link = document.createElement('a'); // Create a download link
  link.setAttribute('href', url);
  link.setAttribute('download', 'data.csv'); // Set the download filename
  document.body.appendChild(link); // Add the link to the DOM
  link.click(); // Simulate a click on the link to trigger the download
  document.body.removeChild(link); // Remove the link from the DOM
}
const start = document.getElementById("start");
const exportData = document.getElementById("export");
let b = document.getElementById("simulation");
let w = b.clientWidth;
let h = b.clientHeight;
console.log('simulation: ',w, h);
var chartD = new Highcharts.Chart({
chart: { renderTo: 'chart-distance' },
title: { text: 'Sharp IR Distance' },
series: [{
showInLegend: false,
data: []
}],
plotOptions: {
line: {
animation: false,
dataLabels: { enabled: true }
},
series: { color: '#059e8a' }
},
xAxis: {
title: { text: 'Tempo (ms)' },
min: 0,
max: 3000,
},
yAxis: {
title: { text: 'Distância (cm)' },
min: 0,
max: 31,
minorTickInterval: 5
},
credits: { enabled: false }
});
start.addEventListener("click", () => {
  chartD.series[0].setData([]);
  var x=0,y=0;
  const test = setInterval(function () {
    espRequest();
        //console.log(this.responseText);
        if (chartD.series[0].data.length > 100) {
          chartD.series[0].addPoint([x, y], true, false, false);
        } else {
          chartD.series[0].addPoint([x, y], true, false, false);
        }
        x +=100;
        y = parseFloat(teste);
        circPos = teste;
  }, 100);
  setTimeout(() => {
    clearInterval(test);
  }, 3000);
});
exportData.addEventListener("click", () => {
  dataExp = chartD.series[0].data;
  var exp=[];
  for (i in dataExp){
    console.log(dataExp[i].x,dataExp[i].y);
    exp.push([dataExp[i].x,dataExp[i].y]);
  }
  for (i in exp){
    console.log(exp[i]);
  }
  let jsonData = JSON.stringify(exp);
  console.log(jsonData);
  fetch('api/sql.php', {
    method: 'POST',
    headers: { 'Content-Type': 'text/plain' },
    body: jsonData
  }).then(response => response.text()).then(data => {
    console.log(data);
  }).catch(error => {
    console.error(error);
  });
  downloadCSV(exp);
});
