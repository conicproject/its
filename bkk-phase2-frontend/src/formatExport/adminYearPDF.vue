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
          <div id="chartLine" style="width: 100%; height: 500rem;"></div>
          <div id="chartPie" style="width: 100%; height: 1000rem;"></div>
  
          <table id="mytableY1">
            <tr>
              <th rowspan="2">TYPE/TIME</th>
              <th v-for="item in headerTable" :key="item" colspan="2">{{ item }}</th>
            </tr>
            <tr>
              <th v-for="item in head" :key="item.id">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataYear" :key="item.id">
              <td>{{ item.type }}</td>
              <td v-if="item.in_0 !== undefined">{{ item.in_0 }}</td>
                            <td v-if="item.out_0 !== undefined">{{ item.out_0 }}</td>
                            <td v-if="item.in_1 !== undefined">{{ item.in_1}}</td>
                            <td v-if="item.out_1 !== undefined">{{ item.out_1 }}</td>
                            <td v-if="item.in_2 !== undefined">{{ item.in_2 }}</td>
                            <td v-if="item.out_2 !== undefined">{{ item.out_2 }}</td>
                            <td v-if="item.in_3 !== undefined">{{ item.in_3 }}</td>
                            <td v-if="item.out_3 !== undefined">{{ item.out_3 }}</td>
                            <td v-if="item.in_4 !== undefined">{{ item.in_4}}</td>
                            <td v-if="item.out_4 !== undefined">{{ item.out_4 }}</td>
                            <td v-if="item.in_5 !== undefined">{{ item.in_5 }}</td>
                            <td v-if="item.out_5 !== undefined">{{ item.out_5 }}</td>
                            <td v-if="item.in_6 !== undefined">{{ item.in_6}}</td>
                            <td v-if="item.out_6 !== undefined">{{ item.out_6 }}</td>
                            <td v-if="item.in_7 !== undefined">{{ item.in_7 }}</td>
                            <td v-if="item.out_7 !== undefined">{{ item.out_7 }}</td>
                            <td v-if="item.in_8 !== undefined">{{ item.in_8 }}</td>
                            <td v-if="item.out_8 !== undefined">{{ item.out_8 }}</td>
                            <td v-if="item.in_9 !== undefined">{{ item.in_9}}</td>
                            <td v-if="item.out_9 !== undefined">{{ item.out_9 }}</td>
                            <td v-if="item.in_10 !== undefined">{{ item.in_10}}</td>
                            <td v-if="item.out_11 !== undefined">{{ item.out_11 }}</td>
                            <td v-if="item.in_12 !== undefined">{{ item.in_12 }}</td>
                            <td v-if="item.out_12 !== undefined">{{ item.out_12 }}</td>
                            <td>{{ item.in_all }}</td>
                            <td>{{ item.out_all }}</td>
            </tr>
          </table>
  
          <table id="mytableY2">              
                      <tr>
                        <th colspan="2" >time</th>
                         <th  v-for="item in headerTabletime" :key="item.text">{{item.text}}</th>
                      </tr>                 
                      <tr >
                        <th rowspan="2">Inbound</th> 
                        <th >Volume</th>   
                        <td v-for="item in dataDirection.volume_inbound" :key="item">{{item}}</td>  
                       
                      </tr>  
                      <tr>
                        <th>Volume/day</th>  
                        <td  v-for="item in dataDirection.volume_mean_inbound" :key="item">{{item}}</td> 
                                                                
                      </tr>  
                      <tr >
                        <th rowspan="2">Outbound</th> 
                        <th >Volume</th>   
                        <td v-for="item in dataDirection.volume_outbound" :key="item">{{ item }}</td>
                                  
                      </tr>   
                      <tr >   
                        <th>Volume/day</th> 
                        <td v-for="item in dataDirection.volume_mean_volume_outbound" :key="item">{{ item }}</td>              
                      </tr>             
                     
          </table>
  

          <table  id="mytableY3">
                          <tr>
                            <th rowspan="2">TYPE/TIME</th>
                            <th v-for="item in headerTable3" :key="item.id" colspan="2">{{ item.text }}</th>
                          </tr>
                          <tr>
                            <th v-for="child in head" :key="child.id">{{ child.text }}</th>
                          </tr>
                          <tr v-for="item in dataRush" :key="item.id">
                            <th>{{ item.type }}</th>
                            <td>{{ item.in_0 }}</td>
                            <td>{{ item.out_0 }}</td>
                            <td>{{ item.in_1}}</td>
                            <td>{{ item.out_1 }}</td>
                            <td>{{ item.in_2 }}</td>
                            <td>{{ item.out_2 }}</td>
                            <td>{{ item.in_3 }}</td>
                            <td>{{ item.out_3 }}</td>
                            <td>{{ item.in_4}}</td>
                            <td>{{ item.out_4 }}</td>
                            <td>{{ item.in_5 }}</td>
                            <td>{{ item.out_5 }}</td>
                            <td>{{ item.in_all }}</td>
                            <td>{{ item.out_all }}</td>
                            
                            
                           
                          </tr>
          </table>

          <!-- violation  -->

          <div id="chartLine_in_v" style="width: 100%; height: 500rem;"></div>
          <div id="chartPie_in_all" style="width: 100%; height: 1000rem;"></div>
          <div id="chartPie_in_v" style="width: 100%; height: 1000rem;"></div>
                    <table id="mytableY1_in">
            <tr>
              <th>TYPE/TIME</th>
              <th v-for="item in headerTable" :key="item">{{ item }}</th>
            </tr>
            <!-- <tr>
              <th v-for="item in head" :key="item.id">{{ item.text }}</th>
            </tr> -->
            <tr v-for="item in dataYear_in" :key="item.id">
              <td>{{ item.type }}</td>
              
                            <td v-if="item.all_0 !== undefined">{{ item.all_0 }}</td>
                            <td v-if="item.all_1 !== undefined">{{ item.all_1}}</td>
                            
                            <td v-if="item.all_2 !== undefined">{{ item.all_2 }}</td>
                            
                            <td v-if="item.all_3 !== undefined">{{ item.all_3 }}</td>
                           
                            <td v-if="item.all_4 !== undefined">{{ item.all_4}}</td>
                            
                            <td v-if="item.all_5 !== undefined">{{ item.all_5 }}</td>
                            
                            <td v-if="item.all_6 !== undefined">{{ item.all_6}}</td>
                           
                            <td v-if="item.all_7 !== undefined">{{ item.all_7 }}</td>
                           
                            <td v-if="item.all_8 !== undefined">{{ item.all_8 }}</td>
                            
                            <td v-if="item.all_9 !== undefined">{{ item.all_9}}</td>
                            
                            <td v-if="item.all_10 !== undefined">{{ item.all_10}}</td>
                            
                            <td v-if="item.all_12 !== undefined">{{ item.all_12 }}</td>
                            
                            
                            <td>{{ item.all_all }}</td>
            </tr>
          </table>
  
          <table id="mytableY1_in_v">
            <tr>
              <th>TYPE/TIME</th>
              <th v-for="item in headerTable" :key="item">{{ item }}</th>
            </tr>
            <!-- <tr>
              <th v-for="item in head" :key="item.id">{{ item.text }}</th>
            </tr> -->
            <tr v-for="item in dataYear_violation_in" :key="item.id">
              <td>{{ item.type }}</td>
              
                            <td v-if="item.all_0 !== undefined">{{ item.all_0 }}</td>
                            <td v-if="item.all_1 !== undefined">{{ item.all_1}}</td>
                            
                            <td v-if="item.all_2 !== undefined">{{ item.all_2 }}</td>
                            
                            <td v-if="item.all_3 !== undefined">{{ item.all_3 }}</td>
                           
                            <td v-if="item.all_4 !== undefined">{{ item.all_4}}</td>
                            
                            <td v-if="item.all_5 !== undefined">{{ item.all_5 }}</td>
                            
                            <td v-if="item.all_6 !== undefined">{{ item.all_6}}</td>
                           
                            <td v-if="item.all_7 !== undefined">{{ item.all_7 }}</td>
                           
                            <td v-if="item.all_8 !== undefined">{{ item.all_8 }}</td>
                            
                            <td v-if="item.all_9 !== undefined">{{ item.all_9}}</td>
                            
                            <td v-if="item.all_10 !== undefined">{{ item.all_10}}</td>
                            
                            <td v-if="item.all_12 !== undefined">{{ item.all_12 }}</td>
                            
                            
                            <td>{{ item.all_all }}</td>
            </tr>
          </table>

          <div id="chartLine_out_v" style="width: 100%; height: 500rem;"></div>
          <div id="chartPie_out_all" style="width: 100%; height: 1000rem;"></div>
          <div id="chartPie_out_v" style="width: 100%; height: 1000rem;"></div>
  
          <table id="mytableY1_out">
            <tr>
              <th>TYPE/TIME</th>
              <th v-for="item in headerTable" :key="item" >{{ item }}</th>
            </tr>
            <!-- <tr>
              <th v-for="item in head" :key="item.id">{{ item.text }}</th>
            </tr> -->
            <tr v-for="item in dataYear_out" :key="item.id">
              <td>{{ item.type }}</td>
              <td v-if="item.all_0 !== undefined">{{ item.all_0 }}</td>
                           
                            <td v-if="item.all_1 !== undefined">{{ item.all_1}}</td>
                            
                            <td v-if="item.all_2 !== undefined">{{ item.all_2 }}</td>
                            
                            <td v-if="item.all_3 !== undefined">{{ item.all_3 }}</td>
                            
                            <td v-if="item.all_4 !== undefined">{{ item.all_4}}</td>
                            
                            <td v-if="item.all_5 !== undefined">{{ item.all_5 }}</td>
                            
                            <td v-if="item.all_6 !== undefined">{{ item.all_6}}</td>
                            
                            <td v-if="item.all_7 !== undefined">{{ item.all_7 }}</td>
                            
                            <td v-if="item.all_8 !== undefined">{{ item.all_8 }}</td>
                           
                            <td v-if="item.all_9 !== undefined">{{ item.all_9}}</td>
                           
                            <td v-if="item.all_10 !== undefined">{{ item.all_10}}</td>
                           
                            <td v-if="item.all_12 !== undefined">{{ item.all_12 }}</td>
                            
                            <td>{{ item.all_all }}</td>
                           
            </tr>
          </table>

          <table id="mytableY1_out_v">
            <tr>
              <th>TYPE/TIME</th>
              <th v-for="item in headerTable" :key="item" >{{ item }}</th>
            </tr>
            <!-- <tr>
              <th v-for="item in head" :key="item.id">{{ item.text }}</th>
            </tr> -->
            <tr v-for="item in dataYear_violation_out" :key="item.id">
              <td>{{ item.type }}</td>
              <td v-if="item.all_0 !== undefined">{{ item.all_0 }}</td>
                           
                            <td v-if="item.all_1 !== undefined">{{ item.all_1}}</td>
                            
                            <td v-if="item.all_2 !== undefined">{{ item.all_2 }}</td>
                            
                            <td v-if="item.all_3 !== undefined">{{ item.all_3 }}</td>
                            
                            <td v-if="item.all_4 !== undefined">{{ item.all_4}}</td>
                            
                            <td v-if="item.all_5 !== undefined">{{ item.all_5 }}</td>
                            
                            <td v-if="item.all_6 !== undefined">{{ item.all_6}}</td>
                            
                            <td v-if="item.all_7 !== undefined">{{ item.all_7 }}</td>
                            
                            <td v-if="item.all_8 !== undefined">{{ item.all_8 }}</td>
                           
                            <td v-if="item.all_9 !== undefined">{{ item.all_9}}</td>
                           
                            <td v-if="item.all_10 !== undefined">{{ item.all_10}}</td>
                           
                            <td v-if="item.all_12 !== undefined">{{ item.all_12 }}</td>
                            
                            <td>{{ item.all_all }}</td>
                           
            </tr>
          </table>

        </section>
      </vue-html2pdf>
    </div>
  </template>
  <script>
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
  let doc = new jsPDF({ orientation: "l", unit: "pt" ,compress:true});
  export default {
    props: ["downloadpdf","dataExport","date","test"],
    components: {
      VueHtml2pdf,
      apexchart: VueApexCharts,
    },
    watch: {
      downloadpdf: function(newVal, oldVal) {
        // watch it
        console.log(this.dataExport);
        this.exportPDF();
  
        setTimeout(() => {
          this.width = "100%";
          this.height = "100%";
        }, 2000);
      },
      test: function(newVal, oldVal){
        this.testclose()
      }

    },
    data() {
      return {
        dataDirection:{},
        dataRush:[],
        dataYear:[],
        dataYear_violation_in:[],
        dataYear_violation_out:[],
        textCheckpoint :"",
       textDate:"",
        imgPie: "",
        imgURI: "",
        headerTable3: [
          {
            text: "00-07",
          },
          {
            text: "07-09",
          },
          {
            text: "09-12",
          },
          {
            text: "12-16",
          },
          {
            text: "16-19",
          },
          {
            text: "19-24",
          },
          {
            text: "ALL",
          },
        ],
        dataTable3: [
          {
            header: "รถยนต์ส่วนบุคคล",
            in: "time",
            out: "time",
          },
          {
            header: "รถจักรยานยนต์",
            in: "time",
            out: "time",
          },
          {
            header: "รถโดยสาร",
            in: "time",
            out: "time",
          },
          {
            header: "รถบรรทุก",
            in: "time",
            out: "time",
          },
          {
            header: "รถบรรทุกขนาดเล็ก",
            in: "time",
            out: "time",
          },
          {
            header: "รถตู้",
            in: "time",
            out: "time",
          },
          {
            header: "รถสามล้อเครื่อง",
            in: "time",
            out: "time",
          },
          {
            header: "รถSUV",
            in: "time",
            out: "time",
          },
          {
            header: "อื่นๆ",
            in: "time",
            out: "time",
          },
          {
            header: "จำนวนรวมทั้งหมด",
            in: "",
            out: "",
          },
          {
            header: "PCU",
            in: "",
            out: "",
          },
        ],
        head: [
          { text: "IN" ,id:1 },
          { text: "OUT",id:2 },
          { text: "IN",id:3 },
          { text: "OUT",id:4 },
          { text: "IN" ,id:5},
          { text: "OUT" ,id:6},
          { text: "IN",id:7 },
          { text: "OUT",id:8 },
          { text: "IN",id:9 },
          { text: "OUT",id:10 },
          { text: "IN" ,id:11},
          { text: "OUT" ,id:12},
          { text: "IN" ,id:13},
          { text: "OUT",id:14 },
          { text: "IN" ,id:15},
          { text: "OUT",id:16 },
          { text: "IN" ,id:17},
          { text: "OUT",id:18 },
          { text: "IN" ,id:19},
          { text: "OUT",id:20 },
          { text: "IN",id:21 },
          { text: "OUT",id:22},
          { text: "IN" ,id:23},
          { text: "OUT",id:24 },
          { text: "IN" ,id:25},
          { text: "OUT",id:26 },
        ],
        optionspie: {
          labels: ["Apple", "Mango", "Orange", "Watermelon"],
          total: {
            show: true,
          },
        },
        seriespie: [44, 55, 41, 17, 15],
  
        options: {
          markers: {
            size: 4,
          },
          dataLabels: {
            enabled: true,
          },
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
        series: [
          {
            name: "PRODUCT A",
            data: [44, 55, 41, 67, 22, 43, 12, 65, 12, 23, 21, 11],
          },
          {
            name: "PRODUCT B",
            data: [13, 23, 20, 8, 13, 27, 34, 6, 23, 3, 45, 3],
          },
          // {
          //   name: 'PRODUCT C',
          //   data: [11, 17, 15, 15, 21, 14]
          // }, {
          //   name: 'PRODUCT D',
          //   data: [21, 7, 25, 13, 22, 8]
          // }
        ],
        headerTable: [
          // {
          //   text: "ม.ค.",
          // },
          // {
          //   text: "ก.พ.",
          // },
          // {
          //   text: "มี.ค.",
          // },
          // {
          //   text: "เม.ย.",
          // },
          // {
          //   text: "พ.ค.",
          // },
          // {
          //   text: "มิ.ย.",
          // },
          // {
          //   text: "ก.ค.",
          // },
          // {
          //   text: "ส.ค.",
          // },
          // {
          //   text: "ก.ย.",
          // },
          // {
          //   text: "ต.ค.",
          // },
          // {
          //   text: "พ.ย.",
          // },
          // {
          //   text: "ธ.ค.",
          // },
          // {
          //   text: "all",
          // },
        ],
        dataTable: [
          {
            header: "รถยนต์ส่วนบุคคล",
            in: "time",
            out: "time",
          },
          {
            header: "รถจักรยานยนต์",
            in: "time",
            out: "time",
          },
          {
            header: "รถโดยสาร",
            in: "time",
            out: "time",
          },
          {
            header: "รถบรรทุก",
            in: "time",
            out: "time",
          },
          {
            header: "รถบรรทุกขนาดเล็ก",
            in: "time",
            out: "time",
          },
          {
            header: "รถตู้",
            in: "time",
            out: "time",
          },
          {
            header: "รถสามล้อเครื่อง",
            in: "time",
            out: "time",
          },
          {
            header: "รถSUV",
            in: "time",
            out: "time",
          },
          {
            header: "อื่นๆ",
            in: "time",
            out: "time",
          },
          {
            header: "จำนวนรวมทั้งหมด",
            in: "",
            out: "",
          },
          {
            header: "PCU",
            in: "",
            out: "",
          },
        ],
        headerTabletime: [
         
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
            text: "ALL",
          },
        ],
        dataTabletime: [
          {
            text: "1145",
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
            text: "",
          },
          {
            text: "",
          },
          {
            text: "02-03",
          },
          {
            text: "",
          },
          {
            text: "",
          },
          {
            text: "02-03",
          },
          {
            text: "",
          },
          {
            text: "",
          },
          {
            text: "02-03",
          },
          {
            text: "",
          },
          {
            text: "",
          },
          {
            text: "02-03",
          },
          {
            text: "",
          },
          {
            text: "",
          },
          {
            text: "02-03",
          },
          {
            text: "",
          },
          {
            text: "",
          },
          {
            text: "02-03",
          },
          {
            text: "",
          },
          {
            text: "",
          },
          {
            text: "",
          },
        ],
        datatableR: [
          {
            header: "รถยนต์ส่วนบุคคล",
            jan: "data",
            feb: "data",
          },
          {
            header: "รถจักรยานยนต์",
            text: "",
          },
          {
            header: "รถโดยสาร",
            text: "",
          },
          {
            header: "รถบรรทุก",
            text: "",
          },
          {
            header: "รถบรรทุกขนาดเล็ก",
            text: "",
          },
          {
            header: "รถตู้",
            text: "",
          },
          {
            header: "รถสามล้อเครื่อง",
            text: "",
          },
          {
            header: "รถSUV",
            text: "",
          },
          {
            header: "อื่นๆ",
            text: "",
          },
  
          {
            header: "PCU",
            text: "",
          },
          {
            header: "จำนวนรวมทั้งหมด",
            text: "",
          },
        ],
        roadName:'',
        percent_violation_in:'',
        percent_violation_out:'',
        dataYear_in:[],
        dataYear_out:[]
      };
    },
    methods: {
      testclose(){
        this.$emit('testclose')
      },
      generateReport() {
        console.log("test");
        this.$refs.html2Pdf.generatePdf();
      },
      genChartPiea() {
        var options = {
          chart: {
            type: "pie",
            width: "300",
            animations: {
              enabled: false,
            },
          },
  
          series: [44, 55, 13, 33],
          labels: ["Apple", "Mango", "Orange", "Watermelon"],
        };
  
        var chart = new ApexCharts(document.querySelector("#chartPie"), options);
        chart.render().then(() => {
          chart.dataURI().then(({ imgURI, blob }) => {
            //Here shows error
            this.imgPie = imgURI;
            
          });
        });
      },
      genPDFAdmin(index_pic) {
        doc.addPage("a4", "l");
        doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
        doc.setFont("THSarabunNew", "Bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
        doc.text("Report Volume & Cassification", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 76);
        doc.text("ถนน : "+this.roadName, 440, 53);
        doc.text("ปี : "+this.date, 440, 98);
        doc.setFontSize(15);
        doc.text("ปริมาณการจราจรแยกตามประเภทรถในแต่ละเดือน (คัน)", 40, 120);
        const logo = require("@/assets/img/BMALogo3.jpg");
  
        var imgLogo = new Image();
        imgLogo.src = logo;
        // console.log("logo", this.imgURL);
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
  
       const CheckPoint1 = require("@/assets/img/checkpointPicture/"+index_pic+".png");
        var imgCheckPoint = new Image();
       imgCheckPoint.src = CheckPoint1;
       doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
        // doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (Outbound) (คัน)", 40, 285);
  
        doc.autoTable({
          html: "#mytableY1",
          startY: 125,
          styles: {
            font: "THSarabunNew",
            fontSize: 9,
            halign: "center",
            overflow: "linebreak",
            cellWidth: "auto",
            textColor: "#000",
            cellPadding: 1,
          },
          theme: "grid",
          headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
          bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        });
  
        doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (คัน)", 40, 450);
        doc.autoTable({
          html: "#mytableY2",
          startY: 455,
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
  
        
      },
      genPDFAdmin_in_v(imgLine,imgPie_all,imgPie,index_pic) {
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
        doc.text("ปี : "+this.date, 440, 115);
        doc.setFontSize(14);
        doc.text("ปริมาณจราจรในแต่ละเดือน (ขาออก) (คัน)", 40, 130);
        const logo = require("@/assets/img/BMALogo3.jpg");
  
        var imgLogo = new Image();
        imgLogo.src = logo;
        // console.log("logo", this.imgURL);
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
  
       const CheckPoint1 = require("@/assets/img/checkpointPicture/"+index_pic+".png");
        var imgCheckPoint = new Image();
       imgCheckPoint.src = CheckPoint1;
       doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
      doc.text("ปริมาณยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางงข้ามชนิดปุ่มกดในแต่ละเดือน (ขาเข้า) (คัน)", 40, 285);
  
        doc.autoTable({
          html: "#mytableY1_in",
          tableWidth:550,
          startY: 135,
          styles: {
            font: "THSarabunNew",
            fontSize: 8,
            halign: "center",
            overflow: "linebreak",
            cellWidth: "auto",
            textColor: "#000",
            cellPadding: 1,
          },
          theme: "grid",
          headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
          bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        });

        doc.autoTable({
          html: "#mytableY1_in_v",
          tableWidth:550,
          startY: 290,
          styles: {
            font: "THSarabunNew",
            fontSize: 8,
            halign: "center",
            overflow: "linebreak",
            cellWidth: "auto",
            textColor: "#000",
            cellPadding: 1,
          },
          theme: "grid",
          headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
          bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        });
        doc.setFontSize(12);
        doc.text("จำนวนของการฝ่าสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด คิดเป็น "+this.percent_violation_in+"% ของปริมาณจราจรทั้งหมด", 40, 437);
        doc.setFontSize(15);
        doc.text("Traffic Volume Graph", 350, 460);
        doc.addImage(imgLine, "JPEG", 150, 475, 500, 100 ,undefined,'FAST');
        doc.setFontSize(15);
        doc.text("Violation Pie Graph", 650, 140);
        doc.addImage(imgPie, "JPEG", 600, 145, 200, 100,undefined,'FAST');
         doc.text("Volume&Classification of Violation Pie Graph", 620, 300);
        doc.addImage(imgPie_all, "JPEG", 600, 305, 200, 100,undefined,'FAST');
        
      },
      genPDFAdmin_out_v(imgLine,imgPie_all,imgPie,index_pic) {
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
        doc.text("ปี : "+this.date, 440, 115);
        doc.setFontSize(14);
        doc.text("ปริมาณจราจรในแต่ละเดือน (ขาเข้า) (คัน)", 40, 130);
        const logo = require("@/assets/img/BMALogo3.jpg");
  
        var imgLogo = new Image();
        imgLogo.src = logo;
        // console.log("logo", this.imgURL);
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70,undefined,'FAST');
  
        const CheckPoint1 = require("@/assets/img/checkpointPicture/"+index_pic+".png");
        var imgCheckPoint = new Image();
        imgCheckPoint.src = CheckPoint1;
        doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100,undefined,'FAST');
        doc.text("ปริมาณยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางงข้ามชนิดปุ่มกดในแต่ละเดือน (ขาออก) (คัน)", 40, 285);
  
        doc.autoTable({
          html: "#mytableY1_out",
           tableWidth:550,
          startY: 135,
          styles: {
            font: "THSarabunNew",
            fontSize: 8,
            halign: "center",
            overflow: "linebreak",
            cellWidth: "auto",
            textColor: "#000",
            cellPadding: 1,
          },
          theme: "grid",
          headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
          bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        });

        doc.autoTable({
          html: "#mytableY1_out_v",
           tableWidth:550,
          startY: 290,
          styles: {
            font: "THSarabunNew",
            fontSize: 8,
            halign: "center",
            overflow: "linebreak",
            cellWidth: "auto",
            textColor: "#000",
            cellPadding: 1,
          },
          theme: "grid",
          headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
          bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        });
        doc.setFontSize(12);
        doc.text("จำนวนของการฝ่าสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด คิดเป็น "+this.percent_violation_out+"% ของปริมาณจราจรทั้งหมด", 40, 437);
       
        doc.setFontSize(15);
        doc.text("Traffic Volume Graph", 350, 460);
        doc.addImage(imgLine, "JPEG", 150, 475, 500, 100,undefined,'FAST');
        doc.setFontSize(15);
        doc.text("Violation Pie Graph", 650, 140);
        doc.addImage(imgPie, "JPEG", 600, 145, 200, 100,undefined,'FAST');
         doc.text("Volume&Classification of Violation Pie Graph", 620, 300);
        doc.addImage(imgPie_all, "JPEG", 600, 305, 200, 100,undefined,'FAST');
        
      },
      genPDFAdmin2(imgLine,imgPie,index_pic) {
       
        doc.addPage("a4", "l");
        doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
        doc.setFont("THSarabunNew", "Bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
        doc.text("Report Volume & Cassification", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 76);
        doc.text("ถนน : "+this.roadName, 440, 53);
        doc.text("ปี : "+this.date, 440, 98);
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรเฉลี่ยแยกตามประเภทรถในและนอกเวลาเร่งด่วน (คัน/วัน)", 40, 145);
        const logo2 = require("@/assets/img/BMALogo3.jpg");
  
        var imgLogo = new Image();
        imgLogo.src = logo2;
        // console.log("logo", this.imgURL);
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
  
       const CheckPoint1 = require("@/assets/img/checkpointPicture/"+index_pic+".png");
        var imgCheckPoint = new Image();
       imgCheckPoint.src = CheckPoint1;
       doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100,undefined,'FAST');
  
        doc.autoTable({
          html: "#mytableY3",
          startY: 150,
          tableWidth: 500,
          styles: {
            font: "THSarabunNew",
            fontSize: 9,
            halign: "center",
            overflow: "linebreak",
            cellWidth: "auto",
            textColor: "#000",
            cellPadding: 1,
          },
          theme: "grid",
          headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
          bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        });
  
        doc.setFontSize(17);
        doc.text("Graph of Traffic Volume", 340, 340);
        doc.setFontSize(15);
        doc.text("(Inbound/Outbound)", 355, 355);
        doc.addImage(imgLine, "JPEG", 60, 360, 700, 200,undefined,'FAST');
        doc.setFontSize(17);
        doc.text("Volume&Classification Pie Graph", 620, 170);
        doc.addImage(imgPie, "JPEG", 600, 180, 200, 100,undefined,'FAST');
  
       
      },

      async genChartPieApex(cat,data) {
        return new Promise(async(resolve, reject) => {
          let img = ''
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
          resolve({
                  status: "success",
                  data: img
                });
          
        });
      });

      
   });
    },
          async genChartPieApex_in(cat,data) {
        return new Promise(async(resolve, reject) => {
          let img = ''
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

      var chart = new ApexCharts(document.querySelector("#chartPie_in_v"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
         img = imgURI;
          resolve({
                  status: "success",
                  data: img
                });
          
        });
      });

      
   });
    },
          async genChartPieApex_in_all(cat,data) {
        return new Promise(async(resolve, reject) => {
          let img = ''
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
      colors: ["#ff7f09", "#21b3ff"],
      };

      var chart = new ApexCharts(document.querySelector("#chartPie_in_all"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
         img = imgURI;
          resolve({
                  status: "success",
                  data: img
                });
          
        });
      });

      
   });
    },
          async genChartPieApex_out(cat,data) {
        return new Promise(async(resolve, reject) => {
          let img = ''
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

      var chart = new ApexCharts(document.querySelector("#chartPie_out_v"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
         img = imgURI;
          resolve({
                  status: "success",
                  data: img
                });
          
        });
      });

      
   });
    },
          async genChartPieApex_out_all(cat,data) {
        return new Promise(async(resolve, reject) => {
          let img = ''
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
       colors: ["#ff7f09", "#21b3ff"],
      };

      var chart = new ApexCharts(document.querySelector("#chartPie_out_all"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
         img = imgURI;
          resolve({
                  status: "success",
                  data: img
                });
          
        });
      });

      
   });
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
 let imgPie = await chart.exporting.getImage("png");

      resolve({
          status: "success",
          data : imgPie
        });
    
  // });
// });
})
},
    async genChartLineApex(cat,data) {
        return new Promise(async(resolve, reject) =>  {
          let img = ""
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
              return val;
            },
          },
        },
      };
      var chart = new ApexCharts(document.querySelector("#chartLine"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
          img = imgURI;
          resolve({
                  status: "success",
                  data: img
                });

        });
      });
      
   });
    },
        async genChartLineApex_in(cat,data) {
        return new Promise(async(resolve, reject) =>  {
          let img = ""
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
              return val;
            },
          },
        },
      };
      var chart = new ApexCharts(document.querySelector("#chartLine_in_v"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
          img = imgURI;
          resolve({
                  status: "success",
                  data: img
                });

        });
      });
      
   });
    },
            async genChartLineApex_out(cat,data) {
        return new Promise(async(resolve, reject) =>  {
          let img = ""
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
              return val;
            },
          },
        },
      };
      var chart = new ApexCharts(document.querySelector("#chartLine_out_v"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
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
        console.log("exportYear");
        
        let res = await this.loopGenPdf()
        if(res.status == 'success'){
          console.log("success");
        doc.save(`รายงานผลข้อมูลจราจร(รายปี).pdf`);
        this.$emit('closePDF')
        }
      },
      async loopGenPdf(){
        return new Promise(async(resolve, reject) =>  {
          for(let i = 0; i < this.dataExport.length;i++){
            let index_pic = this.dataExport[i].checkpoint_id
          this.generateReport();
        //this.genChartLine();
       this.headerTable = this.dataExport[i].headerTable
       this.textCheckpoint = this.dataExport[i].checkpoint_name
       this.textDate= this.date
       this.roadName = this.dataExport[i].road_name
        this.dataInbound = this.dataExport[i].dataInbound
        this.dataOutbound = this.dataExport[i].dataOutbound
        this.dataDirection= this.dataExport[i].dataDirection
        this.dataRush = this.dataExport[i].dataRush
        this.dataYear = this.dataExport[i].dataYear
         this.dataYear_in = this.dataExport[i].dataYear_in
          this.dataYear_out = this.dataExport[i].dataYear_out
         this.percent_violation_in = this.dataExport[i].percent_violation_in
         this.percent_violation_out = this.dataExport[i].percent_violation_out
      
       // let pie =await this.genChartPie(this.dataExport[i].dataPieChart)
        let pie = await this.genChartPieApex(this.dataExport[i].categories,this.dataExport[i].dataChart) 
        let line =  await this.genChartLineApex(this.dataExport[i].apex_cat,this.dataExport[i].apex_line) 

         //-----------violation

         this.dataYear_violation_in = this.dataExport[i].dataYear_violation_in
         this.dataYear_violation_out = this.dataExport[i].dataYear_violation_out
         let pie_in = await this.genChartPieApex_in(this.dataExport[i].categories_violation,this.dataExport[i].PieChart_in_violation)
         let pie_in_all = await this.genChartPieApex_in_all(this.dataExport[i].categories_all_v,this.dataExport[i].PieChart_all_in_violation) 
         let line_in =  await this.genChartLineApex_in(this.dataExport[i].apex_cat_violation,this.dataExport[i].apex_line_in_violation) 
         let pie_out = await this.genChartPieApex_out(this.dataExport[i].categories_all_v,this.dataExport[i].PieChart_out_violation) 
         let pie_out_all = await this.genChartPieApex_out_all(this.dataExport[i].categories_violation,this.dataExport[i].PieChart_all_out_violation)
         let line_out =  await this.genChartLineApex_out(this.dataExport[i].apex_cat_violation,this.dataExport[i].apex_line_out_violation) 
        
  
        if(pie.status === 'success' && line.status === 'success' &&
        pie_in.status === 'success' && pie_in_all.status === 'success' &&
        line_in.status === 'success' && pie_out.status === 'success' &&
        pie_out_all.status === 'success' && line_out.status === 'success' 
        ){
           // console.log("success");
            if(i ==0){
              doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
        doc.setFont("THSarabunNew", "Bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
        doc.text("Report Volume & Cassification", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 76);
       doc.text("ถนน : "+this.roadName, 440, 53);
       // doc.text("ปี : "+this.date, 440, 99);
       doc.text("ปี : "+this.date, 440, 98);
        doc.setFontSize(15);
        doc.text("ปริมาณการจราจรแยกตามประเภทรถในแต่ละเดือน (คัน)", 40, 120);
        const logo = require("@/assets/img/BMALogo3.jpg");
  
        var imgLogo = new Image();
        imgLogo.src = logo;
        // console.log("logo", this.imgURL);
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70,undefined,'FAST');
  
        const CheckPoint1 = require("@/assets/img/checkpointPicture/"+index_pic+".png");
        var imgCheckPoint = new Image();
        imgCheckPoint.src = CheckPoint1;
        doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100,undefined,'FAST');
       //  doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (Outbound) (คัน)", 40, 285);
  
        doc.autoTable({
          html: "#mytableY1",
          startY: 125,
          styles: {
            font: "THSarabunNew",
            fontSize: 9,
            halign: "center",
            overflow: "linebreak",
            cellWidth: "auto",
            textColor: "#000",
            cellPadding: 1,
          },
          theme: "grid",
          headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
          bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        });
  
        doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (คัน)", 40, 450);
        doc.autoTable({
          html: "#mytableY2",
          startY: 455,
          styles: {
            font: "THSarabunNew",
            halign: "center",
            overflow: "linebreak",
            cellWidth: "auto",
            textColor: "#000",
            cellPadding: 1,
          },
          theme: "grid",
          headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
          bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        });
        this.genPDFAdmin2(line.data,pie.data,index_pic)
         this.genPDFAdmin_in_v(line_in.data,pie_in_all.data,pie_in.data,index_pic)
          this.genPDFAdmin_out_v(line_out.data,pie_out_all.data,pie_out.data,index_pic)
            }
        
              
          else{
              this.genPDFAdmin(index_pic)
              this.genPDFAdmin2(line.data,pie.data,index_pic)
               this.genPDFAdmin_in_v(line_in.data,pie_in_all.data,pie_in.data,index_pic)
          this.genPDFAdmin_out_v(line_out.data,pie_out_all.data,pie_out.data,index_pic)
            }
           
          }
        //console.log(i);

        }
          resolve({
                  status: "success",
                });
            
          });
                
      }
    },
  };
  </script>
  <style scoped>
  @import url("https://fonts.googleapis.com/css2?family=Sarabun&display=swap");
  
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
  