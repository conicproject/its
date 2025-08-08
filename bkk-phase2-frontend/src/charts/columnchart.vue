<template>
    <div>
        <apexchart width="100%"  type="bar" :options="options" :series="series"></apexchart>
</div>
</template>
<script>
import VueApexCharts from "vue-apexcharts";
export default {
    components:{
     apexchart: VueApexCharts,
    },
    data :function(){
    return{
        options: {
        chart: {
          type: 'bar',
          height: 350,
          
          toolbar: {
            show: true
          },
          zoom: {
            enabled: true
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              position: 'bottom',
              offsetX: -10,
              offsetY: 0
            }
          }
        }],
        plotOptions: {
          bar: {
            horizontal: false,
            borderRadius: 10
          },
        },
        xaxis: {
          type: 'datetime',
          categories: ['01/01/2011 GMT', '01/02/2011 GMT', '01/03/2011 GMT', '01/04/2011 GMT',
            '01/05/2011 GMT', '01/06/2011 GMT', '01/07/2011 GMT', '01/08/2011 GMT', '01/09/2011 GMT'
          ],
        },
        legend: {
          position: 'right',
          offsetY: 40
        },
        fill: {
          opacity: 1
        }
      },
      series: [{
          name: 'PRODUCT A',
          data: [44, 55, 41, 67, 22, 43,12,65,12]
        }, {
          name: 'PRODUCT B',
          data: [13, 23, 20, 8, 13, 27,34,6,23]
        }, 
        // {
        //   name: 'PRODUCT C',
        //   data: [11, 17, 15, 15, 21, 14]
        // }, {
        //   name: 'PRODUCT D',
        //   data: [21, 7, 25, 13, 22, 8]
        // }
        ]
    }
    }
    

}
</script>
<style>

</style>