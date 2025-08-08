<template>
  <div>
    <canvas id="planet-chart"></canvas>
  </div>
</template>
<script>
import Chart from 'chart.js'
import planetChartData from '../planet-data.js'
export default {
  name: 'PlanetChart',
  data() {
    return {
      planetChartData: planetChartData
    }
  },
  mounted() {
    var chartData = {
    type:"line",
    labels: ["January", "February", "March", "April", "May", "June"],
    datasets: [
        {
            fillColor: "#79D1CF",
            strokeColor: "#79D1CF",
            data: [60, 80, 81, 56, 55, 40]
        }
    ]
};

var ctx = document.getElementById("planet-chart").getContext("2d");
new Chart(ctx).Line(chartData, {
    showTooltips: false,
    onAnimationComplete: function () {

        var ctx = this.chart.ctx;
        ctx.font = this.scale.font;
        ctx.fillStyle = this.scale.textColor
        ctx.textAlign = "center";
        ctx.textBaseline = "bottom";

        this.datasets.forEach(function (dataset) {
            dataset.points.forEach(function (points) {
                ctx.fillText(points.value, points.x, points.y - 10);
            });
        })
    }
});
//     const ctx = document.getElementById('planet-chart');
//     var ctx1 = document.getElementById('planet-chart').getContext("2d");
//      console.log("sd",this.planetChartData,"ddd",ctx1);
     
//     var test = new Chart(ctx, this.planetChartData,{
//     showTooltips: false,
//     onAnimationComplete: function () {
//         console.log("onAnimationComplete");
//         var ctx = this.chart.ctx;
//         ctx.font = this.scale.font;
//         ctx.fillStyle = this.scale.textColor
//         ctx.textAlign = "center";
//         ctx.textBaseline = "bottom";

//         this.datasets.forEach(function (dataset) {
//             dataset.points.forEach(function (points) {
//                 ctx.fillText(points.value, points.x, points.y - 10);
//             });
//         })
//     }
// });
//      console.log("chart",test);
    
  }
}
</script>