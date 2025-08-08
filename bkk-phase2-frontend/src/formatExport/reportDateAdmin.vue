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
          <div id="chartBar"></div>
          <div id="chartPie"></div>
          <table id="mytableIn">
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
              
            </tr>
          </table>
  
          <table id="mytableOut">
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
             
             
            </tr>
          </table>
   
          <table id="mytableX" data-cols-width="20,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15">
            <tr>
              <th colspan="25" data-f-sz="25" data-a-h="right" data-f-bold="true">กองระบบเทคโนโลยีจราจร</th>
              <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">สำนักการจราจรและขนส่ง </th>
                        <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กรุงเทพมหานคร</th> -->
            </tr>
            <tr>
              <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กองระบบเทคโนโลยีจราจร </th> -->
              <th colspan="25" data-f-sz="25" data-a-h="right" data-f-bold="true">สำนักการจราจรและขนส่ง กรุงเทพมหานคร</th>
              <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กรุงเทพมหานคร</th> -->
            </tr>
            <tr></tr>
            <tr>
              <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กองระบบเทคโนโลยีจราจร </th> -->
              <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">สำนักการจราจรและขนส่ง </th> -->
              <th colspan="25" data-f-sz="25" data-a-h="left" data-f-bold="true">รายงานปริมาณจราจรแยกตามประเภทยานพาหนะ(รายวัน)</th>
            </tr>
  
            <tr></tr>
            <tr>
              <th data-f-sz="15">ปริมาณจราจรรายวัน (ทิศทางการจราจรเข้าเมือง) (คัน)</th>
            </tr>
            <tr>
              <th data-a-h="center" data-b-a-s="thin" data-f-sz="15" v-for="item in headerTable" :key="item.text">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataInbound" :key="item.type">
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.type }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._0 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._1 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._2 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._3 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._4 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._5 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._6 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._7 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._8 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._9 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._10 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._11 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._12 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._13}}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._14 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._15 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._16 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._17 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._18 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._19 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._20 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._21 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._22 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._23 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.all }}</td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr>
              <th data-f-sz="15">ปริมาณจราจรรายวัน (ทิศทางการจราจรออกเมือง) (คัน)</th>
            </tr>
            <tr>
              <th data-a-h="center" data-b-a-s="thin" data-f-sz="15" v-for="item in headerTable" :key="item.text">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataOutbound" :key="item.id">
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.type }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._0 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._1 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._2 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._3 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._4 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._5 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._6 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._7 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._8 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._9 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._10 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._11 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._12 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._13}}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._14 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._15 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._16 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._17 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._18 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._19 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._20 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._21 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._22 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._23 }}</td>
              <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.all }}</td>
            </tr>
          </table>
        </section>
      </vue-html2pdf>
      <!-- <v-btn @click="generateReport">download</v-btn> -->
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
  export default {
    props: ["downloadpdf", "downloadexcel", "exportAdmin","dataInbound","dataOutbound","dateText","nameCheckPoint"],
    components: {
      VueHtml2pdf,
      apexchart: VueApexCharts,
    },
    watch: {
      downloadpdf: function(newVal, oldVal) {
        // watch it
        console.log("Prop changed: ", newVal, " | was: ", oldVal);
        console.log(":dataInbound",this.dataInbound);
        this.generateReport();
        this.genChart();
        this.genChartBar();
        this.genChartPie();
  
        setTimeout(() => {
          this.width = "100%";
          this.height = "100%";
        }, 2000);
      },
      downloadexcel: function(newVal, oldVal) {
        // watch it
        console.log("Prop changed: ", newVal, " | was: ", oldVal);
        this.generateReport();
        this.genExcel();
      },
    },
    data() {
      return {
        imgURI: "",
        height: "150",
        width: "150",
        htmlToPdfOptions: {
          margin: 0,
        },
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
        dataTable2: [
          {
            header: "รถยนต์ส่วนบุคคล",
            text: "data",
          },
          {
            header: "รถจักรยานยนต์",
          },
          {
            header: "รถโดยสาร",
          },
          {
            header: "รถบรรทุก",
          },
          {
            header: "รถบรรทุกขนาดเล็ก",
          },
                  {
            header: "รถตู้",
            text: "data",
          },
          {
            header: "รถสามล้อเครื่อง",
            text: "data",
          },
          {
            header: "รถ SUV",
            text: "data",
          },
          {
            header: "อื่นๆ",
            text: "data",
          },
          {
            header: "PCU",
            text: "data",
          },
          {
            header: "จำนวนรวมทั้งหมด",
            text: "data",
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
        headerTable: [
          {
            text: "เวลา",
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
            text: "ปริมาณจราจร(คัน)",
          },
        ],
        imgBar: "",
        imgPie: "",
       textCheckPoint:""
      };
    },
    methods: {
      generateReport() {
        // console.log("test");
        this.$refs.html2Pdf.generatePdf();
      },
      download() {
        //alert('test');
        var doc = new jsPDF("p", "pt", "A4");
        //  let pdfName = 'test';
  
        //  doc.text(100, 20, 'Hello World', 'center');
        //  doc.save(pdfName + '.pdf');
        let margins = {
          top: 80,
          bottom: 60,
          left: 40,
          width: 522,
        };
  
        doc.fromHTML(this.$refs.content, margins.left, margins.top, {
          width: margins.width,
        });
  
        doc.save("test.pdf");
      },
      genChartPie() {
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
            //console.log("PIE",this.imgPie);
           // if(this.exportAdmin === true){
              this.genPDFAdmin();
            //}else{
             // this.genPDF();
            // }
          });
        });
      },
      genChartBar() {
        var options = {
          chart: {
            height: 200,
            type: "bar",
            animations: {
              enabled: false,
            },
          },
          plotOptions: {
            bar: {
              horizontal: false,
              columnWidth: "80%",
              endingShape: "rounded",
            },
          },
          dataLabels: {
            enabled: false,
          },
          colors: ["#008000", "#d4a823", "#f92525"],
          stroke: {
            show: true,
            width: 2,
            colors: ["transparent"],
          },
          series: [
            {
              name: "Net Profit",
              data: [44, 55, 57, 56, 61, 58, 63, 60, 66],
            },
            {
              name: "Revenue",
              data: [76, 85, 101, 98, 87, 105, 91, 114, 94],
            },
            // {
            //   name: 'Free Cash Flow',
            //   data: [35, 41, 36, 26, 45, 48, 52, 53, 41]
            // }
          ],
          xaxis: {
            categories: ["Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
          },
          yaxis: {
            title: {
              text: "$ (thousands)",
            },
          },
          fill: {
            opacity: 1,
          },
          tooltip: {
            y: {
              formatter: function(val) {
                return "$ " + val + " thousands";
              },
            },
          },
        };
  
        var chart = new ApexCharts(document.querySelector("#chartBar"), options);
        chart.render().then(() => {
          chart.dataURI().then(({ imgURI, blob }) => {
            //Here shows error
            this.imgBar = imgURI;
            //  console.log(this.imgBar);
          });
        });
      },
      genPDFAdmin() {
        let doc = new jsPDF({ orientation: "l", unit: "pt" ,compress:true});
  
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
        doc.text("จุดติดตั้ง : อ่อนนุช ซอย 3", 440, 53);
        doc.text("ถนน อ่อนนุช ", 440, 76);
        doc.text("วันที่ : 2022-02-22", 440, 99);
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (Inbound) (คัน)", 40, 145);
        const logo = require("@/assets/img/BMALogo3.jpg");
        const CheckPoint = require("@/assets/img/อ่อนนุช.png");
        var imgLogo = new Image();
        var imgCheckPoint = new Image();
        imgLogo.src = logo;
        imgCheckPoint.src = CheckPoint;
        // console.log("logo", this.imgURL);
        doc.addImage(imgLogo, "JPEG", 40, 20, 100, 100, undefined,'FAST');
        doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
        doc.text("Graph of Traffic Volume", 350, 450);
        doc.setFontSize(15);
        doc.text("(Inbound/Outbound)", 370, 460);
        doc.addImage(this.imgURI, "JPEG", 60, 470, 700, 100, undefined,'FAST');
        // doc.autoTable(this.columns,this.rows,{ startY: 150 ,styles: {font: "THSarabunNew"},theme: 'grid',
        //   headStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0],textColor: [0, 0, 0],lineWidth: 1,},
        //   bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]}});
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (Outbound) (คัน)", 40, 300);
        // doc.autoTable(this.columns,this.rows,{ startY: 305 ,styles: {font: "THSarabunNew"},theme: 'grid',
        //   headStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0],textColor: [0, 0, 0],lineWidth: 1,},
        //   bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]}});
  
        doc.autoTable({
          html: "#mytableIn",
          startY: 150,
          styles: { font: "THSarabunNew",  halign: "center",
            overflow: "linebreak",
            cellWidth: "auto",
            
            textColor: "#000", cellPadding: 1 },
          theme: "grid",
          headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
          bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        });
  
        doc.autoTable({
          html: "#mytableOut",
          startY: 305,
          styles: { font: "THSarabunNew",  halign: "center",
            overflow: "linebreak",
            cellWidth: "auto",
           
            textColor: "#000", cellPadding: 1 },
          theme: "grid",
          headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
          bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        });
  
        doc.addPage("a4", "l");
        doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
        doc.setFont("THSarabunNew", "Bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
        doc.text("Report Volume & Cassification", 440, 30);
        doc.text("จุดติดตั้ง : อ่อนนุช ซอย 3", 440, 53);
        doc.text("ถนน อ่อนนุช ", 440, 76);
        doc.text("วันที่ : 2022-02-22", 440, 99);
        doc.text("ปริมาณจราจรแยกตามประเภทรถในแต่ละช่วงเวลา (Inbound) (คัน)", 40, 145);
        const logo2 = require("@/assets/img/BMALogo3.jpg");
        // const CheckPoint2 = require("@/assets/img/อ่อนนุช.png");
        var imgLogo = new Image();
        var imgCheckPoint = new Image();
        imgCheckPoint.src = CheckPoint;
        imgLogo.src = logo2;
        // console.log("logo", this.imgURL);
        doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
        // doc.autoTable(this.columns,this.rows,{ startY: 150 ,styles: {font: "THSarabunNew"},theme: 'grid',
        //   headStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0],textColor: [0, 0, 0],lineWidth: 1,},
        //   bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]}});
  
        doc.text("ปริมาณจราจรแยกตามประเภทรถในแต่ละช่วงเวลา (Outbound) (คัน)", 40, 300);
        // doc.autoTable(this.columns,this.rows,{ startY: 305 ,styles: {font: "THSarabunNew"},theme: 'grid',
        //   headStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0],textColor: [0, 0, 0],lineWidth: 1,},
        //   bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]}});
  
        doc.autoTable({
          html: "#mytableIn",
          startY: 150,
          styles: { font: "THSarabunNew",  halign: "center",
            overflow: "linebreak",
            cellWidth: "auto",
            
            textColor: "#000", cellPadding: 1 },
          theme: "grid",
          headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
          bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        });
  
        doc.autoTable({
          html: "#mytableOut",
          startY: 305,
          styles: { font: "THSarabunNew", halign: "center",
            overflow: "linebreak",
            cellWidth: "auto",      
            textColor: "#000", cellPadding: 1 },
          theme: "grid",
          headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
          bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        });
        doc.text("Volume&Classification Bar Graph", 150, 460);
        doc.addImage(this.imgBar, "JPEG", 60, 470, 370, 100, undefined,'FAST');
        doc.text("Volume&Classification Pie Graph", 550, 460);
        doc.addImage(this.imgPie, "JPEG", 500, 470, 250, 100, undefined,'FAST');
  
        doc.save(`รายงานผลข้อมูลจราจร(รายวัน).pdf`);
      },
      genExcel() {
        TableToExcel.convert(document.getElementById("mytableX"), {
          name: "รายงานผลข้อมูลจราจรแยกตามประเภทยานพาหนะ(รายวัน).xlsx",
          sheet: {
            name: "Sheet 1",
          },
        });
      },
      genPDF() {
        this.textCheckPoint = this.nameCheckPoint || ''
        let doc = new jsPDF({ orientation: "l", unit: "pt" });
        doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
        doc.addFileToVFS("THSarabunNew-bold.ttf", THSarabunNewBold.font);
        doc.addFont("THSarabunNew-bold.ttf", "THSarabunNewBold", "bold");
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "bold");
        doc.setFont("THSarabunNew", "bold");
        doc.setFontSize(12);
        doc.setFont("THSarabunNewBold", "bold");
        doc.text("รายงานปริมาณจราจรแยกตามประเภทยานพาหนะ (รายวัน)", 170, 65);
        doc.text("จุดติดตั้ง "+this.textCheckPoint, 170, 85);
        doc.text("วัน/เดือน/ปี "+this.dateText, 170, 105);
         doc.setFontSize(14);
        doc.text("กองระบบเทคโนโลยีจราจร", 560, 45);
        doc.text("สำนักการจราจรและขนส่ง กรุงเทพมหานคร", 510, 60);
        const logo = require("@/assets/img/BMALogo3.jpg");
        var imgLogo = new Image();
        imgLogo.src = logo;
        doc.addImage(imgLogo, "JPEG", 40, 20, 100, 100, undefined,'FAST');
        doc.setFontSize(10);
        doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (Outbound) (คัน)", 40, 340);
        doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (Inbound) (คัน)", 40, 155);
        doc.autoTable({
          html: "#mytableIn",
          startY: 160,
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
          html: "#mytableOut",
          startY: 345,
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
  
        // doc.addPage("a4", "l");
        // doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
       
        // doc.addFileToVFS("THSarabunNew-bold.ttf", THSarabunNewBold.font);
        // doc.addFont("THSarabunNew-bold.ttf", "THSarabunNewBold", "bold");
        // doc.addFont("THSarabunNew.ttf", "THSarabunNew", "bold");
        // doc.setFont("THSarabunNew", "bold");
        // doc.setFontSize(12);
        // doc.setFont("THSarabunNewBold", "bold");
        // doc.text("รายงานปริมาณจราจรแยกตามประเภทยานพาหนะ (รายวัน)", 180, 55);
        // doc.text("จุดติดตั้ง.......................", 180, 75);
        // doc.text("วัน/เดือน/ปี...........", 180, 95);
        // doc.setFontSize(16);
        // doc.text("กองระบบเทคโนโลยีจราจร", 550, 53);
        // doc.text("สำนักการจราจรและขนส่ง กรุงเทพมหานคร", 500, 75);
        // var imgLogo = new Image();
        // imgLogo.src = logo;
        // doc.addImage(imgLogo, "JPEG", 40, 20, 100, 100);
        // doc.setFontSize(10);
        // doc.text("ปริมาณจราจรแยกตามประเภทรถในแต่ละช่วงเวลา (Outbound) (คัน)", 40, 340);
        // doc.text("ปริมาณจราจรแยกตามประเภทรถในแต่ละช่วงเวลา (Inbound) (คัน)", 40, 155);
        // doc.autoTable({
        //   html: "#mytable2",
        //   startY: 160,
        //   styles: {
        //     font: "THSarabunNew",
        //     overflow: "linebreak",
        //     columnWidth: "auto",
        //     fontSize: 10,
        //     textColor: "#000",
        //     cellPadding: 1,
        //   },
        //   theme: "grid",
        //   headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
        //   bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        // });
  
        // doc.autoTable({
        //   html: "#mytable2",
        //   startY: 345,
        //   styles: {
        //     font: "THSarabunNew",
        //     overflow: "linebreak",
        //     columnWidth: "auto",
        //     fontSize: 10,
        //     textColor: "#000",
        //     cellPadding: 1,
        //   },
        //   theme: "grid",
        //   headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
        //   bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        // });
        doc.save(`รายงานวัน.pdf`);
      },
      genChart() {
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
          colors: ["#008000", "#d4a823", "#f92525"],
          // stroke: {
          //   show: true,
          //   width: 2,
          //   colors: ['transparent']
          // },
          series: [
            {
              name: "Net Profit",
              data: [44, 55, 57, 56, 61, 58, 63, 60, 66],
            },
            {
              name: "Revenue",
              data: [76, 85, 101, 98, 87, 105, 91, 114, 94],
            },
            // {
            //   name: 'Free Cash Flow',
            //   data: [35, 41, 36, 26, 45, 48, 52, 53, 41]
            // }
          ],
          xaxis: {
            categories: ["Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
          },
          yaxis: {
            title: {
              text: "$ (thousands)",
            },
          },
          fill: {
            opacity: 1,
          },
          tooltip: {
            y: {
              formatter: function(val) {
                return "$ " + val + " thousands";
              },
            },
          },
        };
        var chart = new ApexCharts(document.querySelector("#chartLine"), options);
        chart.render().then(() => {
          chart.dataURI().then(({ imgURI, blob }) => {
            //Here shows error
            //  console.log(imgURI)
            this.imgURI = imgURI;
          });
        });
      },
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
  