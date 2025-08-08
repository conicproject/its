<template>
    <div>
      <vue-html2pdf
        :show-layout="false"
        :float-layout="true"
        :enable-download="false"
        :preview-modal="false"
        :paginate-elements-by-height="1400"
        filename="test"
        :pdf-quality="2"
        :manual-pagination="false"
        pdf-format="a3"
        pdf-orientation="landscape"
        pdf-content-width="100%"
        ref="html2Pdf"
        :pdf-margin="10"
      >
        <section slot="pdf-content">
          <div id="chartLine"></div>
          <div id="chartBar" style="width: 100%; height: 500px;"></div>
          <div id="chartPie" style="width: 100%; height: 500px;"></div>
          <table id="mytableD1">
            <tr>
              <th v-for="item in headerTableQ" :key="item.text">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataQuaterIn" :key="item.type">
              <td>{{ item.type }}</td>
              <td>{{ item._0 }}</td>
              <td>{{ item._1 }}</td>
              <td>{{ item._2 }}</td>
              <td>{{ item._3 }}</td>
              <td>{{ item._4 }}</td>
              <td>{{ item._5 }}</td>
              <td>{{ item._6 }}</td>
              <td>{{ item._7 }}</td>
              <td>{{ item._8 }}</td>
              <td>{{ item._9 }}</td>
              <td>{{ item._10 }}</td>
              <td>{{ item._11 }}</td>
              <td>{{ item._12 }}</td>
              <td>{{ item._13 }}</td>
              <td>{{ item._14 }}</td>
              <td>{{ item._15 }}</td>
              <td>{{ item._16 }}</td>
              <td>{{ item._17 }}</td>
              <td>{{ item._18 }}</td>
              <td>{{ item._19 }}</td>
              <td>{{ item._20 }}</td>
              <td>{{ item._21 }}</td>
              <td>{{ item._22 }}</td>
              <td>{{ item._23 }}</td>
              <td>{{ item.all }}</td>
            </tr>
          </table>
  
          <table id="mytableD2">
            <tr>
              <th v-for="item in headerTableQ" :key="item.text">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataQuaterOut" :key="item.type">
              <td>{{ item.type }}</td>
              <td>{{ item._0 }}</td>
              <td>{{ item._1 }}</td>
              <td>{{ item._2 }}</td>
              <td>{{ item._3 }}</td>
              <td>{{ item._4 }}</td>
              <td>{{ item._5 }}</td>
              <td>{{ item._6 }}</td>
              <td>{{ item._7 }}</td>
              <td>{{ item._8 }}</td>
              <td>{{ item._9 }}</td>
              <td>{{ item._10 }}</td>
              <td>{{ item._11 }}</td>
              <td>{{ item._12 }}</td>
              <td>{{ item._13 }}</td>
              <td>{{ item._14 }}</td>
              <td>{{ item._15 }}</td>
              <td>{{ item._16 }}</td>
              <td>{{ item._17 }}</td>
              <td>{{ item._18 }}</td>
              <td>{{ item._19 }}</td>
              <td>{{ item._20 }}</td>
              <td>{{ item._21 }}</td>
              <td>{{ item._22 }}</td>
              <td>{{ item._23 }}</td>
              <td>{{ item.all }}</td>
            </tr>
          </table>
  
          <table id="mytableD3">
            <tr>
              <th v-for="item in headerTable" :key="item.text">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataInbound" :key="item.id">
              <td>{{ item.type }}</td>
              <td>{{ item._0 }}</td>
              <td>{{ item._1 }}</td>
              <td>{{ item._2 }}</td>
              <td>{{ item._3 }}</td>
              <td>{{ item._4 }}</td>
              <td>{{ item._5 }}</td>
              <td>{{ item._6 }}</td>
              <td>{{ item._7 }}</td>
              <td>{{ item._8 }}</td>
              <td>{{ item._9 }}</td>
              <td>{{ item._10 }}</td>
              <td>{{ item._11 }}</td>
              <td>{{ item._12 }}</td>
              <td>{{ item._13 }}</td>
              <td>{{ item._14 }}</td>
              <td>{{ item._15 }}</td>
              <td>{{ item._16 }}</td>
              <td>{{ item._17 }}</td>
              <td>{{ item._18 }}</td>
              <td>{{ item._19 }}</td>
              <td>{{ item._20 }}</td>
              <td>{{ item._21 }}</td>
              <td>{{ item._22 }}</td>
              <td>{{ item._23 }}</td>
              <td>{{ item.all }}</td>
              <td>{{ item.pcu }}</td>
            </tr>
          </table>
  
          <table id="mytableD4">
            <tr>
              <th v-for="item in headerTable" :key="item.text">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataOutbound" :key="item.id">
              <td>{{ item.type }}</td>
              <td>{{ item._0 }}</td>
              <td>{{ item._1 }}</td>
              <td>{{ item._2 }}</td>
              <td>{{ item._3 }}</td>
              <td>{{ item._4 }}</td>
              <td>{{ item._5 }}</td>
              <td>{{ item._6 }}</td>
              <td>{{ item._7 }}</td>
              <td>{{ item._8 }}</td>
              <td>{{ item._9 }}</td>
              <td>{{ item._10 }}</td>
              <td>{{ item._11 }}</td>
              <td>{{ item._12 }}</td>
              <td>{{ item._13 }}</td>
              <td>{{ item._14 }}</td>
              <td>{{ item._15 }}</td>
              <td>{{ item._16 }}</td>
              <td>{{ item._17 }}</td>
              <td>{{ item._18 }}</td>
              <td>{{ item._19 }}</td>
              <td>{{ item._20 }}</td>
              <td>{{ item._21 }}</td>
              <td>{{ item._22 }}</td>
              <td>{{ item._23 }}</td>
              <td>{{ item.all }}</td>
              <td>{{ item.pcu }}</td>
            </tr>
          </table>

          <!-- violation -->
          <div id="chartLine_in_violation"></div>
          <div id="chartLine_out_violation"></div>
          <div id="chartBar_violation" style="width: 100%; height: 500px;"></div>
          <div id="chartPie_in_violation" style="width: 100%; height: 500px;"></div>
          <div id="chartPie_out_violation" style="width: 100%; height: 500px;"></div>
          <table id="mytableD1_v">
            <tr>
              <th v-for="item in headerTableQ" :key="item.text">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataQuaterIn_violation" :key="item.type">
              <td>{{ item.type }}</td>
              <td>{{ item._0 }}</td>
              <td>{{ item._1 }}</td>
              <td>{{ item._2 }}</td>
              <td>{{ item._3 }}</td>
              <td>{{ item._4 }}</td>
              <td>{{ item._5 }}</td>
              <td>{{ item._6 }}</td>
              <td>{{ item._7 }}</td>
              <td>{{ item._8 }}</td>
              <td>{{ item._9 }}</td>
              <td>{{ item._10 }}</td>
              <td>{{ item._11 }}</td>
              <td>{{ item._12 }}</td>
              <td>{{ item._13 }}</td>
              <td>{{ item._14 }}</td>
              <td>{{ item._15 }}</td>
              <td>{{ item._16 }}</td>
              <td>{{ item._17 }}</td>
              <td>{{ item._18 }}</td>
              <td>{{ item._19 }}</td>
              <td>{{ item._20 }}</td>
              <td>{{ item._21 }}</td>
              <td>{{ item._22 }}</td>
              <td>{{ item._23 }}</td>
              <td>{{ item.all }}</td>
            </tr>
          </table>
  
          <table id="mytableD2_v">
            <tr>
              <th v-for="item in headerTableQ" :key="item.text">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataQuaterOut_violation" :key="item.type">
              <td>{{ item.type }}</td>
              <td>{{ item._0 }}</td>
              <td>{{ item._1 }}</td>
              <td>{{ item._2 }}</td>
              <td>{{ item._3 }}</td>
              <td>{{ item._4 }}</td>
              <td>{{ item._5 }}</td>
              <td>{{ item._6 }}</td>
              <td>{{ item._7 }}</td>
              <td>{{ item._8 }}</td>
              <td>{{ item._9 }}</td>
              <td>{{ item._10 }}</td>
              <td>{{ item._11 }}</td>
              <td>{{ item._12 }}</td>
              <td>{{ item._13 }}</td>
              <td>{{ item._14 }}</td>
              <td>{{ item._15 }}</td>
              <td>{{ item._16 }}</td>
              <td>{{ item._17 }}</td>
              <td>{{ item._18 }}</td>
              <td>{{ item._19 }}</td>
              <td>{{ item._20 }}</td>
              <td>{{ item._21 }}</td>
              <td>{{ item._22 }}</td>
              <td>{{ item._23 }}</td>
              <td>{{ item.all }}</td>
            </tr>
          </table>
  
          <table id="mytableD3_v">
            <tr>
              <th v-for="item in headerTable" :key="item.text">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataInbound_violation" :key="item.id">
              <td>{{ item.type }}</td>
              <td>{{ item._0 }}</td>
              <td>{{ item._1 }}</td>
              <td>{{ item._2 }}</td>
              <td>{{ item._3 }}</td>
              <td>{{ item._4 }}</td>
              <td>{{ item._5 }}</td>
              <td>{{ item._6 }}</td>
              <td>{{ item._7 }}</td>
              <td>{{ item._8 }}</td>
              <td>{{ item._9 }}</td>
              <td>{{ item._10 }}</td>
              <td>{{ item._11 }}</td>
              <td>{{ item._12 }}</td>
              <td>{{ item._13 }}</td>
              <td>{{ item._14 }}</td>
              <td>{{ item._15 }}</td>
              <td>{{ item._16 }}</td>
              <td>{{ item._17 }}</td>
              <td>{{ item._18 }}</td>
              <td>{{ item._19 }}</td>
              <td>{{ item._20 }}</td>
              <td>{{ item._21 }}</td>
              <td>{{ item._22 }}</td>
              <td>{{ item._23 }}</td>
              <td>{{ item.all }}</td>
              <td>{{ item.pcu }}</td>
            </tr>
          </table>
  
          <table id="mytableD4_v">
            <tr>
              <th v-for="item in headerTable" :key="item.text">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataOutbound_violation" :key="item.id">
              <td>{{ item.type }}</td>
              <td>{{ item._0 }}</td>
              <td>{{ item._1 }}</td>
              <td>{{ item._2 }}</td>
              <td>{{ item._3 }}</td>
              <td>{{ item._4 }}</td>
              <td>{{ item._5 }}</td>
              <td>{{ item._6 }}</td>
              <td>{{ item._7 }}</td>
              <td>{{ item._8 }}</td>
              <td>{{ item._9 }}</td>
              <td>{{ item._10 }}</td>
              <td>{{ item._11 }}</td>
              <td>{{ item._12 }}</td>
              <td>{{ item._13 }}</td>
              <td>{{ item._14 }}</td>
              <td>{{ item._15 }}</td>
              <td>{{ item._16 }}</td>
              <td>{{ item._17 }}</td>
              <td>{{ item._18 }}</td>
              <td>{{ item._19 }}</td>
              <td>{{ item._20 }}</td>
              <td>{{ item._21 }}</td>
              <td>{{ item._22 }}</td>
              <td>{{ item._23 }}</td>
              <td>{{ item.all }}</td>
              <td>{{ item.pcu }}</td>
            </tr>
          </table>

        </section>
      </vue-html2pdf>
    </div>
  </template>
  <script>
    let doc = new jsPDF({ orientation: "l", unit: "pt",compress:true });
  import { jsPDF } from "jspdf";
  import fontTH from "../fontTH.js";
  import VueHtml2pdf from "vue-html2pdf";
  import VueApexCharts from "vue-apexcharts";
  import "jspdf-autotable";
  import TableToExcel from "@linways/table-to-excel";
  import THSarabunNewBold from "../THSarabunNewBold.js";
  import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";

am4core.useTheme(am4themes_animated);
  export default {
    props: ["downloadpdf","dataExport","date"],
    components: {
      VueHtml2pdf,
      apexchart: VueApexCharts,
    },
    watch: {
      downloadpdf: function(newVal, oldVal) {
        console.log(this.dataExport);
        this.exportPDF();
        setTimeout(() => {
          this.width = "100%";
          this.height = "100%";
        }, 2000);
      },
    },
    data() {
      return {
        textCheckpoint :"",
       textDate:"",
        imgURI: "",
        height: "150",
        width: "150",
        width2: "150",
        height2: "150",
        optionspie: {
          charts: {
            type: "pie",
          },
  
          labels: ["Apple", "Mango", "Orange", "Watermelon"],
          total: {
            show: true,
          },
        },
        seriespie: [44, 55, 41, 17, 15],
  
        options2: {
          type: "bar",
          colors: ["#FF9800", "#03A9F4"],
          chart: {
            type: "bar",
            stacked: true,
            toolbar: {
              show: false,
            },
            zoom: {
              enabled: true,
            },
          },
          responsive: [
            {
              breakpoint: 480,
              options: {
                legend: {
                  position: "bottom",
                  offsetX: -10,
                  offsetY: 0,
                },
              },
            },
          ],
          plotOptions: {
            bar: {
              horizontal: false,
              borderRadius: 10,
            },
          },
          xaxis: {
            type: "datetime",
            categories: [
              "01/01/2011 GMT",
              "01/02/2011 GMT",
              "01/03/2011 GMT",
              "01/04/2011 GMT",
              "01/05/2011 GMT",
              "01/06/2011 GMT",
              "01/07/2011 GMT",
              "01/08/2011 GMT",
              "01/09/2011 GMT",
              "01/10/2011 GMT",
              "01/11/2011 GMT",
              "01/12/2011 GMT",
            ],
          },
          legend: {
            position: "right",
            offsetY: 40,
          },
          fill: {
            opacity: 1,
          },
        },
        series2: [
          {
            name: "PRODUCT A",
            data: [44, 55, 41, 67, 22, 43, 12, 65, 12, 23, 21, 11],
          },
        ],
        headerTable2: [
          {
            text: "type",
          },
          {
            text: "00-01",
          },
          {
            text: "01-02",
          },
          {
            text: "02-03",
          },
          {
            text: "03-04",
          },
          {
            text: "04-05",
          },
          {
            text: "05-06",
          },
          {
            text: "06-07",
          },
          {
            text: "07-08",
          },
          {
            text: "08-09",
          },
          {
            text: "09-10",
          },
          {
            text: "11-12",
          },
          {
            text: "12-13",
          },
          {
            text: "13-14",
          },
          {
            text: "14-15",
          },
          {
            text: "15-16",
          },
          {
            text: "16-17",
          },
          {
            text: "17-18",
          },
          {
            text: "18-19",
          },
          {
            text: "19-20",
          },
          {
            text: "20-21",
          },
          {
            text: "21-22",
          },
          {
            text: "22-23",
          },
          {
            text: "23-24",
          },
          {
            text: "ALL",
          },
          {
            text: "PCU",
          },
        ],
        options: {
          markers: {
            size: 4,
          },
          dataLabels: {
            enabled: true,
            style: {
              colors: ["#000"],
            },
            offsetX: 0,
            offsetY: -10,
            background: {
              enabled: false,
            },
          },
          colors: ["#FF9800", "#03A9F4"],
          chart: {
            type: "line",
            stacked: false,
            toolbar: {
              show: false,
            },
            zoom: {
              enabled: true,
            },
          },
          responsive: [
            {
              breakpoint: 480,
              options: {
                legend: {
                  position: "bottom",
                  offsetX: -10,
                  offsetY: 0,
                },
              },
            },
          ],
          plotOptions: {
            bar: {
              horizontal: false,
              borderRadius: 10,
            },
          },
          xaxis: {
            type: "datetime",
            categories: [
              "01/01/2011 GMT",
              "01/02/2011 GMT",
              "01/03/2011 GMT",
              "01/04/2011 GMT",
              "01/05/2011 GMT",
              "01/06/2011 GMT",
              "01/07/2011 GMT",
              "01/08/2011 GMT",
              "01/09/2011 GMT",
              "01/10/2011 GMT",
              "01/11/2011 GMT",
              "01/12/2011 GMT",
            ],
          },
          legend: {
            position: "right",
            offsetY: 40,
          },
          fill: {
            opacity: 1,
          },
        },
        series: [
          {
            name: "PRODUCT A",
            data: [44, 55, 41, 67, 22, 43, 12, 65, 12, 23, 21, 11],
          },
          {
            name: "PRODUCT B",
            data: [11, 23, 20, 8, 13, 27, 34, 13, 23, 18, 45, 3],
          },
          // {
          //   name: 'PRODUCT C',
          //   data: [11, 17, 15, 15, 21, 14]
          // }, {
          //   name: 'PRODUCT D',
          //   data: [21, 7, 25, 13, 22, 8]
          // }
        ],
        headerTableQ: [
          {
            text: "TIME",
          },
          {
            text: "00-01",
          },
          {
            text: "01-02",
          },
          {
            text: "02-03",
          },
          {
            text: "03-04",
          },
          {
            text: "04-05",
          },
          {
            text: "05-06",
          },
          {
            text: "06-07",
          },
          {
            text: "07-08",
          },
          {
            text: "08-09",
          },
          {
            text: "09-10",
          },
          {
            text: "10-11",
          },
          {
            text: "11-12",
          },
          {
            text: "12-13",
          },
          {
            text: "13-14",
          },
          {
            text: "14-15",
          },
          {
            text: "15-16",
          },
          {
            text: "16-17",
          },
          {
            text: "17-18",
          },
          {
            text: "18-19",
          },
          {
            text: "19-20",
          },
          {
            text: "20-21",
          },
          {
            text: "21-22",
          },
          {
            text: "22-23",
          },
          {
            text: "23-24",
          },
          {
            text: "All",
          }
        ],
        headerTable: [
          {
            text: "TYPE",
          },
          {
            text: "00-01",
          },
          {
            text: "01-02",
          },
          {
            text: "02-03",
          },
          {
            text: "03-04",
          },
          {
            text: "04-05",
          },
          {
            text: "05-06",
          },
          {
            text: "06-07",
          },
          {
            text: "07-08",
          },
          {
            text: "08-09",
          },
          {
            text: "09-10",
          },
          {
            text: "10-11",
          },
          {
            text: "11-12",
          },
          {
            text: "12-13",
          },
          {
            text: "13-14",
          },
          {
            text: "14-15",
          },
          {
            text: "15-16",
          },
          {
            text: "16-17",
          },
          {
            text: "17-18",
          },
          {
            text: "18-19",
          },
          {
            text: "19-20",
          },
          {
            text: "20-21",
          },
          {
            text: "21-22",
          },
          {
            text: "22-23",
          },
          {
            text: "23-24",
          },
          {
            text: "All",
          },
          {
            text: "PCU",
          },
        ],
        imgBar: "",
        imgPie: "",
        dataInbound:[],
        dataOutbound:[],
        dataQuaterOut:[],
        dataQuaterIn:[],
        imgBar_violation: "",
        imgPie_violation: "",
        dataInbound_violation:[],
        dataOutbound_violation:[],
        dataQuaterOut_violation:[],
        dataQuaterIn_violation:[],
        roadName:"",
        percent_violation_in:0,
        percent_violation_out:0
      };
    },
    methods: {
      generateReport() {
        this.$refs.html2Pdf.generatePdf();
      },
      async genChartPie(data) {

return new Promise(async(resolve, reject) => {

  var chart = am4core.create("chartPie", am4charts.PieChart);
  data[0].color = am4core.color("#ED1C24")
  data[1].color = am4core.color("#235789")
  data[2].color =am4core.color("#F1D302")
  data[3].color = am4core.color("#020100")
  data[4].color = am4core.color("#eb8334")
  data[5].color = am4core.color("#34eb4c")
  data[6].color = am4core.color("#34e8eb")
  data[7].color = am4core.color("#9634eb")
  data[8].color = am4core.color("#eb34cc")
  chart.data = data
  //console.log(this.dataExport.dataPieChart);
  var pieSeries = chart.series.push(new am4charts.PieSeries());
pieSeries.dataFields.value = "volume";
pieSeries.dataFields.category = "car_type";
pieSeries.slices.template.propertyFields.fill = "color";

chart.legend = new am4charts.Legend();
pieSeries.hiddenInLegend = true;
var options = chart.exporting.getFormatOptions("png");
options.keepTainted = false;
chart.exporting.setFormatOptions("png", options);

//chart.exporting.export("png");
this.imgPie = await chart.exporting.getImage("png");

      resolve({
          status: "success",
        });
    
  // });
// });
})
},
     async genChartPieApex(cat,data) {
      
        return new Promise(async(resolve, reject) => {
          let img = '';
      var options = {
        chart: {
          type: "pie",
          width: "300",
          animations: {
            enabled: false,
          },

        },
legend: {
    show: false,
          labels: {
            
            colors: "#ffff",
            useSeriesColors: false,
          },
        },
        series: data,
        labels: cat,
        colors: ['#1aa478', '#f79e69', '#8582f2', '#866846', '#96e637','#f9429e','#f1cbff','#3e1379','#9a1b5b'],
      };

      var chart = new ApexCharts(document.querySelector("#chartPie"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
          img = imgURI;
          //console.log("PIE",this.imgPie);
          // if(this.exportAdmin === true){
          //   this.genPDFAdmin();
          // }else{
          //   this.genPDF();
          // }
          resolve({
                  status: "success",
                  data: img
                });
        });
       
      });
        
      
   });
    },
    async genChartPieApex_in_violation(cat,data,test) {
      console.log(cat,data,test)
        return new Promise(async(resolve, reject) => {
          let img = '';
      var options = {
        chart: {
          type: "pie",
          width: "300",
          animations: {
            enabled: false,
          },

        },
legend: {
    show: false,
          labels: {
            
            colors: "#ffff",
            useSeriesColors: false,
          },
        },
        series: data,
        labels: cat,
       colors: ['#1aa478', '#f79e69', '#8582f2', '#866846', '#96e637','#f9429e','#f1cbff','#3e1379','#9a1b5b'],
      };

      var chart = new ApexCharts(document.querySelector("#chartPie_in_violation"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
          img = imgURI;
          console.log("PIE",img);
          // if(this.exportAdmin === true){
          //   this.genPDFAdmin();
          // }else{
          //   this.genPDF();
          // }
          resolve({
                  status: "success",
                  data: img
                });
        });
       
      });
        
      
   });
    },
        async genChartPieApex_out_violation(cat,data) {
      
        return new Promise(async(resolve, reject) => {
          let img = '';
      var options = {
        chart: {
          type: "pie",
          width: "300",
          animations: {
            enabled: false,
          },

        },
legend: {
    show: false,
          labels: {
            
            colors: "#ffff",
            useSeriesColors: false,
          },
        },
        series: data,
        labels: cat,
        colors: ['#1aa478', '#f79e69', '#8582f2', '#866846', '#96e637','#f9429e','#f1cbff','#3e1379','#9a1b5b'],
      };

      var chart = new ApexCharts(document.querySelector("#chartPie_out_violation"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
          img = imgURI;
          console.log("PIE",img);
          // if(this.exportAdmin === true){
          //   this.genPDFAdmin();
          // }else{
          //   this.genPDF();
          // }
          resolve({
                  status: "success",
                  data: img
                });
        });
       
      });
        
      
   });
    },
    async genChartBar(data) {
        return new Promise(async(resolve, reject) =>  {
  
          var chart = am4core.create("chartBar", am4charts.XYChart);
          data[0].color = am4core.color("#ED1C24")
  data[1].color = am4core.color("#235789")
  data[2].color =am4core.color("#F1D302")
  data[3].color = am4core.color("#020100")
  data[4].color = am4core.color("#eb8334")
  data[5].color = am4core.color("#34eb4c")
  data[6].color = am4core.color("#34e8eb")
  data[7].color = am4core.color("#9634eb")
  data[8].color = am4core.color("#eb34cc")
// Add data
chart.data = data
// Create axes
let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
categoryAxis.dataFields.category = "car_type";
// categoryAxis.renderer.grid.template.location = 0;
// categoryAxis.renderer.minGridDistance = 200;

let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

// Create series
var series = chart.series.push(new am4charts.ColumnSeries());
series.dataFields.valueY = "volume";
series.dataFields.categoryX = "car_type";
series.columns.template.propertyFields.fill = "color";
//series.name = "volume";


var options = chart.exporting.getFormatOptions("png");
options.keepTainted = true;
chart.exporting.setFormatOptions("png", options);
this.imgBar = await chart.exporting.getImage("png");
        
              resolve({
                  status: "success",
                });
            
          });
 
      
      },
      async genChartBarApex(cat,data) {
        
        return new Promise(async(resolve, reject) => {
          let img = '';
          var options = {
          series: [{
          data: data
        }],
          chart: {
          height: 350,
          type: 'bar',
          animations: {
            enabled: false,
          },
        },
        colors: ['#1aa478', '#f79e69', '#8582f2', '#866846', '#96e637','#f9429e','#f1cbff','#3e1379','#9a1b5b'],
        plotOptions: {
          bar: {
            columnWidth: '45%',
            distributed: true,
          }
        },
        dataLabels: {
          enabled: false
        },
        legend: {
          show: false
        },
        xaxis: {
          categories:cat,
          labels: {
            style: {
              // colors: colors,
              fontSize: '12px'
            }
          }
        }
        };

      var chart = new ApexCharts(document.querySelector("#chartBar"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
          img = imgURI;
           console.log("Bar Chart",img);
           resolve({
                  status: "success",
                  data: img
                });
        });
       
      });

      
   });
    },
    async genChartBarApex_violation(cat,data) {
        
        return new Promise(async(resolve, reject) => {
          let img = '';
          var options = {
          series: [{
          data: data
        }],
          chart: {
          height: 350,
          type: 'bar',
          animations: {
            enabled: false,
          },
        },
        colors: ['#1aa478', '#f79e69', '#8582f2', '#866846', '#96e637','#f9429e','#f1cbff','#3e1379','#9a1b5b'],
        plotOptions: {
          bar: {
            columnWidth: '45%',
            distributed: true,
          }
        },
        dataLabels: {
          enabled: false
        },
        legend: {
          show: false
        },
        xaxis: {
          categories:cat,
          labels: {
            style: {
              // colors: colors,
              fontSize: '12px'
            }
          }
        }
        };

      var chart = new ApexCharts(document.querySelector("#chartBar_violation"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
          img = imgURI;
           console.log("Bar Chart",img);
           resolve({
                  status: "success",
                  data: img
                });
        });
       
      });

      
   });
    },
      genPDFAdmin(imgLine,index_pic) {
        //let doc = new jsPDF({ orientation: "l", unit: "pt" });
        doc.addPage("a4", "l");
        doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
        doc.addFileToVFS("THSarabunNew-bold.ttf", THSarabunNewBold.font);
        doc.addFont("THSarabunNew-bold.ttf", "THSarabunNewBold", "bold");
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
        doc.setFont("THSarabunNew", "Bold");
        // doc.setFont("THSarabunNewBold", "bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
        doc.text("Report Volume & Cassification", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 53);
       doc.text("ถนน : "+this.roadName, 440, 74);
        doc.text("วันที่ : "+this.date, 440, 96);
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (Inbound) (คัน)", 40, 145);
        const logo = require("@/assets/img/BMALogo3.jpg");
        const CheckPoint = require("@/assets/img/checkpointPicture/"+index_pic+".png");
        var imgLogo = new Image();
        var imgCheckPoint = new Image();
        imgLogo.src = logo;
        imgCheckPoint.src = CheckPoint;
         //console.log("pic1", this.imgURI);
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
        doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
        doc.text("Graph of Traffic Volume", 350, 420);
        doc.setFontSize(15);
        doc.text("(Inbound/Outbound)", 360, 435);
        doc.addImage(imgLine, "JPEG", 60, 470, 700, 100, undefined,'FAST');
       
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (Outbound) (คัน)", 40, 280);
       
  
        doc.autoTable({
          html: "#mytableD1",
          startY: 150,
          styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 9,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
  
        doc.autoTable({
          html: "#mytableD2",
          startY: 285,
          styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 9,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
       
  
        //doc.save(`รายงานผลข้อมูลจราจร(รายวัน).pdf`);
      },
      genPDFAdmin_violation(imgLine,imgPie,index_pic){
        doc.addPage("a4", "l");
        doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
        doc.setFont("THSarabunNew", "Bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
        doc.text("รายงานยานพาหนะฝ่าฝืนสัญญาณ\nไฟจราจรทางข้ามชนิดปุ่มกด", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 73);
        doc.text("ถนน : "+this.roadName, 440, 94);
        doc.text("วันที่ : "+this.date, 440, 115);
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรแยกตามประเภทรถในแต่ละช่วงเวลา (ขาเข้า) (คัน)", 40, 135);
        const logo2 = require("@/assets/img/BMALogo3.jpg");
        const CheckPoint = require("@/assets/img/checkpointPicture/"+index_pic+".png");
        var imgLogo = new Image();
        var imgCheckPoint = new Image();
        imgCheckPoint.src = CheckPoint;
        imgLogo.src = logo2;
        // console.log("logo", this.imgURL);
       doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
        
        doc.setFontSize(15);
        doc.text("ปริมาณยานพาหนะฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกดในแต่ละช่วงเวลา (ขาเข้า) (คัน)", 40, 290);
        

        doc.autoTable({
        html: "#mytableD3",
        startY: 140,
        styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 8,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
  
       


        doc.autoTable({
        html: "#mytableD3_v",
        startY: 295,
        styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 8,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
      doc.setFontSize(12);
        doc.text("จำนวนของการฝ่าสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด คิดเป็น "+this.percent_violation_in+"% ของปริมาณจราจรทั้งหมด", 40, 445);
        doc.setFontSize(15);
        doc.text("Traffic Volume Graph", 200, 465);
        doc.addImage(imgLine, "JPEG", 60, 475, 370, 100, undefined,'FAST');
        doc.text("Volume&Classification of Violation Pie Graph", 550, 465);
        doc.addImage(imgPie, "JPEG", 550, 475, 200, 100, undefined,'FAST');
        
      },
  

      genPDFAdmin2(imgBar,imgPie,index_pic){
        doc.addPage("a4", "l");
        doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
        doc.setFont("THSarabunNew", "Bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
        doc.text("Report Volume & Cassification", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 53);
        doc.text("ถนน : "+this.roadName, 440, 74);
        doc.text("วันที่ : "+this.date, 440, 96);
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรแยกตามประเภทรถในแต่ละช่วงเวลา (Inbound) (คัน)", 40, 135);
        const logo2 = require("@/assets/img/BMALogo3.jpg");
        const CheckPoint = require("@/assets/img/checkpointPicture/"+index_pic+".png");
        var imgLogo = new Image();
        var imgCheckPoint = new Image();
        imgCheckPoint.src = CheckPoint;
        imgLogo.src = logo2;
        // console.log("logo", this.imgURL);
        doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
        
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรแยกตามประเภทรถในแต่ละช่วงเวลา (Outbound) (คัน)", 40, 290);
        

        doc.autoTable({
        html: "#mytableD3",
        startY: 140,
        styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 8,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
  
       


        doc.autoTable({
        html: "#mytableD4",
        startY: 295,
        styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 8,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });

        doc.text("Volume&Classification Bar Graph", 150, 460);
        doc.addImage(imgBar, "JPEG", 60, 470, 370, 100, undefined,'FAST');
        doc.text("Volume&Classification Pie Graph", 550, 460);
        doc.addImage(imgPie, "JPEG", 550, 470, 200, 100, undefined,'FAST');
      },
      genPDFAdmin_violation2(imgLine,imgPie,index_pic){
        doc.addPage("a4", "l");
        doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
        doc.setFont("THSarabunNew", "Bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
        doc.text("รายงานยานพาหนะฝ่าฝืนสัญญาณ\nไฟจราจรทางข้ามชนิดปุ่มกด", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 73);
        doc.text("ถนน : "+this.roadName, 440, 94);
        doc.text("วันที่ : "+this.date, 440, 115);
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรแยกตามประเภทรถในแต่ละช่วงเวลา (ขาออก) (คัน)", 40, 135);
        const logo2 = require("@/assets/img/BMALogo3.jpg");
        const CheckPoint = require("@/assets/img/checkpointPicture/"+index_pic+".png");
        var imgLogo = new Image();
        var imgCheckPoint = new Image();
        imgCheckPoint.src = CheckPoint;
        imgLogo.src = logo2;
        // console.log("logo", this.imgURL);
        doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
        
        doc.setFontSize(15);
        doc.text("ปริมาณยานพาหนะฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกดในแต่ละช่วงเวลา (ขาออก) (คัน)", 40, 290);
        

        doc.autoTable({
        html: "#mytableD4",
        startY: 140,
        styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 8,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
  
       


        doc.autoTable({
        html: "#mytableD4_v",
        startY: 295,
        styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 8,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
       doc.setFontSize(12);
        doc.text("จำนวนของการฝ่าสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด คิดเป็น "+this.percent_violation_out+"% ของปริมาณจราจรทั้งหมด", 40, 445);
        doc.setFontSize(15);
        doc.text("Traffic Volume Graph", 200, 465);
        doc.addImage(imgLine, "JPEG", 60, 475, 370, 100, undefined,'FAST');
        doc.text("Volume&Classification of Violation Pie Graph", 550, 465);
        doc.addImage(imgPie, "JPEG", 550, 475, 200, 100, undefined,'FAST');
      },
      async genChartLine(data) {
        return new Promise(async(resolve, reject) =>  {
        var chart = am4core.create("chartLine", am4charts.XYChart);
        chart.data = data

        var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
categoryAxis.dataFields.category = "year";
categoryAxis.renderer.minGridDistance = 50;
categoryAxis.renderer.grid.template.location = 0.5;
categoryAxis.startLocation = 0.5;
categoryAxis.endLocation = 0.5;

var series = chart.series.push(new am4charts.LineSeries());
series.dataFields.valueY = "volume_in";
series.dataFields.dateX = "time_in";
series.strokeWidth = 2;
series.minBulletDistance = 10;
//series.tooltipText = "[bold]{date.formatDate()}:[/] {value1}\n[bold]{previousDate.formatDate()}:[/] {value2}";
series.tooltip.pointerOrientation = "vertical";

// Create series
var series2 = chart.series.push(new am4charts.LineSeries());
series2.dataFields.valueY = "volume_out";
series2.dataFields.dateX = "time_in";
series2.strokeWidth = 2;
series2.stroke = series.stroke;

var options = chart.exporting.getFormatOptions("png");
options.keepTainted = true;
chart.exporting.setFormatOptions("png", options);
this.imgURI = await chart.exporting.getImage("png");
       console.log(this.imgURI);

       resolve({
                  status: "success",
                });
            
          });
      },
      async genChartLineApex(cat,data) {
       
        return new Promise(async(resolve, reject) =>  {
          let img = '';
      var options = {
        chart: {
          height: 200,
          type: "line",
          animations: {
            enabled: false,
          },
          stacked: false,
          toolbar: {
            show: false,
          },
          zoom: {
            enabled: true,
          },
        },
        markers: {
          size: 4,
        },
        plotOptions: {
          bar: {
            horizontal: false,
            borderRadius: 10,
          },
        },
        dataLabels: {
          enabled: false,
          style: {
            colors: ["#000"],
          },
          offsetX: 0,
          offsetY: -10,
          background: {
            enabled: false,
          },
        },
        colors: ["#ff7f09", "#21b3ff"],
        // stroke: {
        //   show: true,
        //   width: 2,
        //   colors: ['transparent']
        // },
        series: data,
        xaxis: {
          categories: cat,
        },
        yaxis: {
          title: {
            text: "",
          },
        },
        fill: {
          opacity: 1,
        },
        tooltip: {
          y: {
            formatter: function(val) {
              return val ;
            },
          },
        },
      };
      var chart = new ApexCharts(document.querySelector("#chartLine"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
           //console.log(imgURI)
          img = imgURI;
          resolve({
                  status: "success",
                  data: img
                });
        });

        
      });
     
   });
    },
    async genChartLineApex_in_violation(cat,data) {
       
        return new Promise(async(resolve, reject) =>  {
          let img = '';
      var options = {
        chart: {
          height: 200,
          type: "line",
          animations: {
            enabled: false,
          },
          stacked: false,
          toolbar: {
            show: false,
          },
          zoom: {
            enabled: true,
          },
        },
        markers: {
          size: 4,
        },
        plotOptions: {
          bar: {
            horizontal: false,
            borderRadius: 10,
          },
        },
        dataLabels: {
          enabled: false,
          style: {
            colors: ["#000"],
          },
          offsetX: 0,
          offsetY: -10,
          background: {
            enabled: false,
          },
        },
        colors: ["#ff7f09", "#21b3ff"],
        // stroke: {
        //   show: true,
        //   width: 2,
        //   colors: ['transparent']
        // },
        series: data,
        xaxis: {
          categories: cat,
        },
        yaxis: {
          title: {
            text: "",
          },
        },
        fill: {
          opacity: 1,
        },
        tooltip: {
          y: {
            formatter: function(val) {
              return val ;
            },
          },
        },
      };
      var chart = new ApexCharts(document.querySelector("#chartLine_in_violation"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
           //console.log(imgURI)
          img = imgURI;
          resolve({
                  status: "success",
                  data: img
                });
        });

        
      });
     
   });
    },
    async genChartLineApex_out_violation(cat,data) {
       
        return new Promise(async(resolve, reject) =>  {
          let img = '';
      var options = {
        chart: {
          height: 200,
          type: "line",
          animations: {
            enabled: false,
          },
          stacked: false,
          toolbar: {
            show: false,
          },
          zoom: {
            enabled: true,
          },
        },
        markers: {
          size: 4,
        },
        plotOptions: {
          bar: {
            horizontal: false,
            borderRadius: 10,
          },
        },
        dataLabels: {
          enabled: false,
          style: {
            colors: ["#000"],
          },
          offsetX: 0,
          offsetY: -10,
          background: {
            enabled: false,
          },
        },
        colors: ["#ff7f09", "#21b3ff"],
        // stroke: {
        //   show: true,
        //   width: 2,
        //   colors: ['transparent']
        // },
        series: data,
        xaxis: {
          categories: cat,
        },
        yaxis: {
          title: {
            text: "",
          },
        },
        fill: {
          opacity: 1,
        },
        tooltip: {
          y: {
            formatter: function(val) {
              return val ;
            },
          },
        },
      };
      var chart = new ApexCharts(document.querySelector("#chartLine_out_violation"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
           //console.log(imgURI)
          img = imgURI;
          resolve({
                  status: "success",
                  data: img
                });
        });

        
      });
     
   });
    },
     async exportPDF(){
        console.log("exportDate");
        
        let res = await this.loopGenPdf()

        if(res.status == 'success'){
          doc.save(`รายงานผลข้อมูลจราจร(รายวัน).pdf`);
          this.$emit('closePDF')
        }
       
      },
      async loopGenPdf(){
        return new Promise(async(resolve, reject) =>  {
        for(let i = 0; i < this.dataExport.length;i++){
          let index_pic = this.dataExport[i].checkpoint_id
          this.generateReport();
       this.textCheckpoint = this.dataExport[i].checkpoint_name
       this.textDate= this.date
       this.percent_violation_in = this.dataExport[i].percent_violation_in
       this.percent_violation_out = this.dataExport[i].percent_violation_out
       this.roadName = this.dataExport[i].road_name
        this.dataInbound = this.dataExport[i].dataInbound
        this.dataOutbound = this.dataExport[i].dataOutbound
        this.dataQuaterIn = this.dataExport[i].quaterInbound
        this.dataQuaterOut = this.dataExport[i].quaterOutbound
       // let bar = this.dataExport[i].dataPieChart.length > 0 ?await this.genChartBar(this.dataExport[i].dataPieChart): { status: "error"}
        let bar = await this.genChartBarApex(this.dataExport[i].categories,this.dataExport[i].dataChart)
        //let pie = this.dataExport[i].dataPieChart.length > 0 ?await this.genChartPie(this.dataExport[i].dataPieChart) : { status: "success"}
        let pie = await this.genChartPieApex(this.dataExport[i].categories,this.dataExport[i].dataChart)
        let line = await this.genChartLineApex(this.dataExport[i].apex_cat,this.dataExport[i].apex_line) 

        //-----------violation------------
        console.log("pie_in_violation",this.dataExport[i].PieChart_in_violation,this.dataExport[i].categories_violation)
        this.dataInbound_violation = this.dataExport[i].dataInbound_violation
        this.dataOutbound_violation = this.dataExport[i].dataOutbound_violation
        this.dataQuaterIn_violation = this.dataExport[i].quaterInbound_violation
        this.dataQuaterOut_violation = this.dataExport[i].quaterOutbound_violation
       // let bar = this.dataExport[i].dataPieChart.length > 0 ?await this.genChartBar(this.dataExport[i].dataPieChart_violation): { status: "error"}
        let bar_violation = await this.genChartBarApex_violation(this.dataExport[i].categories_violation,this.dataExport[i].dataChart_violation)
        //let pie = this.dataExport[i].dataPieChart.length > 0 ?await this.genChartPie(this.dataExport[i].dataPieChart_violation) : { status: "success"}
        let pie_in_violation = await this.genChartPieApex_in_violation(this.dataExport[i].categories_violation,this.dataExport[i].PieChart_in_violation)
        let pie_out_violation = await this.genChartPieApex_out_violation(this.dataExport[i].categories_violation,this.dataExport[i].PieChart_out_violation)
        let line_in_violation = await this.genChartLineApex_in_violation(this.dataExport[i].apex_cat_violation,this.dataExport[i].apex_line_in_violation)
        let line_out_violation = await this.genChartLineApex_out_violation(this.dataExport[i].apex_cat_violation,this.dataExport[i].apex_line_out_violation) 
  
         console.log("line", pie_in_violation,pie_out_violation);
   
        if(bar.status === 'success' && pie.status === 'success' && line.status === 'success' && line_in_violation.status === 'success' && line_out_violation.status === 'success' && pie_in_violation.status === 'success' && pie_out_violation.status === 'success'){
           console.log("gen chart success",line);
            if(i == 0){
              doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
        doc.addFileToVFS("THSarabunNew-bold.ttf", THSarabunNewBold.font);
        doc.addFont("THSarabunNew-bold.ttf", "THSarabunNewBold", "bold");
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
        doc.setFont("THSarabunNew", "Bold");
        // doc.setFont("THSarabunNewBold", "bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
        doc.text("Report Volume & Cassification", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 53);
        doc.text("ถนน : "+this.roadName, 440, 74);
        doc.text("วันที่ : "+this.date, 440, 96);
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (Inbound) (คัน)", 40, 145);
        const logo = require("@/assets/img/BMALogo3.jpg");
        const CheckPoint = require("@/assets/img/checkpointPicture/"+index_pic+".png");
        var imgLogo = new Image();
        var imgCheckPoint = new Image();
        imgLogo.src = logo;
        imgCheckPoint.src = CheckPoint;
        // console.log("logo", this.imgURL);
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
        doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
        doc.text("Graph of Traffic Volume", 350, 450);
        doc.setFontSize(15);
        doc.text("(Inbound/Outbound)", 370, 460);
        //console.log("0",this.imgURI);
        doc.addImage(line.data, "JPEG", 60, 470, 700, 100, undefined,'FAST');
        
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (Outbound) (คัน)", 40, 280);
       
        doc.autoTable({
          html: "#mytableD1",
          startY: 150,
          styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 9,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
  
        doc.autoTable({
          html: "#mytableD2",
          startY: 285,
          styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 9,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
        this.genPDFAdmin2(bar.data,pie.data,index_pic)
         this.genPDFAdmin_violation(line_in_violation.data,pie_in_violation.data,index_pic)
          this.genPDFAdmin_violation2(line_out_violation.data,pie_out_violation.data,index_pic)
            }

          else{
              this.genPDFAdmin(line.data,index_pic)
              this.genPDFAdmin2(bar.data,pie.data,index_pic)
              this.genPDFAdmin_violation(line_in_violation.data,pie_in_violation.data,index_pic)
              this.genPDFAdmin_violation2(line_out_violation.data,pie_out_violation.data,index_pic)
            }
           
          }
 
        }
        resolve({
                  status: "success",
                });
            
          });
      }
      
      
      
    },
    mounted() {
      setTimeout(() => {
        this.width = "100%";
        this.height = "100%";
      }, 500);
    },
  };
  </script>
  <style scoped>
  @import url("https://fonts.googleapis.com/css2?family=Sarabun&display=swap");
  #chart {
    max-width: 650px;
    margin: 35px auto;
  }
  .font {
    font-family: "Sarabun", sans-serif;
  }
  table,
  th,
  td {
    border: 1px solid black;
    border-collapse: collapse;
  }
  </style>
  