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
      @progress="onProgress($event)"
      @hasStartedGeneration="hasStartedGeneration()"
      @hasDownloaded="hasDownloaded($event)"
      ref="html2Pdf"
    >
      <section slot="pdf-content">
        <v-container grid-list-md text-xs-center class="font">
        <v-layout row wrap style="width: 100%">
          <v-flex >       
            <v-card class="elevation-0 pl-16 pt-5 pr-10">
              <v-card-title>
                <v-layout>
                    <v-flex lg2 ><img width="60%" src="@/assets/img/BMALogo3.jpg" /></v-flex>
                    <v-flex lg4><h3>กองระบบเทคโนโลยีจราจร<br />สำนักการจราจรและขนส่ง<br />กรุงเทพมหานคร</h3></v-flex>
                    <v-flex lg4
                      ><h3>Report Volume & Cassification<br />จุดติดตั้ง : <br />ถนน </h3></v-flex>
                    <v-flex lg2></v-flex>
                  </v-layout>
              </v-card-title>
              <v-card-text   class="pt-5">
                <h3 >Current Alarms</h3>
                <br/>         
                <table id="mytable">   
                    <tr class="text-center">
                      <th colspan="3">ไม่ทำงาน(down)</th>
                    </tr>           
                    <tr >
                      <th>อุปกรณ์</th>
                      <th>IP Address</th>
                      <th>จุดติดตั้ง</th>
                    </tr>
                    <tr v-for="item in dataOff" :key="item">
                      <td>{{item.name}}</td>  
                      <td>{{item.ip}}</td>
                      <td>{{item.checkpoint}}</td>              
                    </tr>  
                            
                   
                   
                   
                    
                   
                    
                                   
                       
                </table>

                      <table id="mytableX" data-cols-width="20,20,20">  
                    <tr class="text-center">
                      <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กองระบบเทคโนโลยีจราจร</th>
                      <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">สำนักการจราจรและขนส่ง </th>
                      <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กรุงเทพมหานคร</th> -->
                    </tr>  
                     <tr class="text-center">
                      <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กองระบบเทคโนโลยีจราจร </th> -->
                      <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">สำนักการจราจรและขนส่ง กรุงเทพมหานคร</th>
                      <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กรุงเทพมหานคร</th> -->
                    </tr>  
                     <tr class="text-center">
                      <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กองระบบเทคโนโลยีจราจร </th> -->
                      <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">สำนักการจราจรและขนส่ง </th> -->
                      <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กรุงเทพมหานคร</th>
                    </tr>  
                    <tr class="text-center">           
                    </tr>    
                    <tr data-height="25" class="text-center">
                      <th colspan="3" data-f-sz="15">ไม่ทำงาน(down)</th>
                    </tr>           
                    <tr >
                      <th data-f-sz="15">อุปกรณ์</th>
                      <th data-f-sz="15">IP Address</th>
                      <th data-f-sz="15">จุดติดตั้ง</th>
                    </tr>
                    <tr v-for="item in dataOff" :key="item">
                      <td data-f-sz="15">{{item.name}}</td>  
                      <td data-f-sz="15">{{item.ip}}</td>
                      <td data-f-sz="15">{{item.checkpoint}}</td>              
                    </tr>  
                              
                    
                   
                    
                   
                   
                   
                    
                               
                </table>

                
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
        </v-container>
        
      </section>
    </vue-html2pdf>
    <!-- <v-btn @click="generateReport">download</v-btn> -->
  </div>
  
</template>
<script>
import { jsPDF } from "jspdf";
import fontTH from "../fontTH.js";
import VueHtml2pdf from "vue-html2pdf";
// import VueApexCharts from "vue-apexcharts";
import "jspdf-autotable";
import THSarabunNewBold from "../THSarabunNewBold.js";
import Vue from "vue";
import JsonExcel from "vue-json-excel";
import  * as XLSX from 'xlsx';
Vue.component("downloadExcel", JsonExcel);

import TableToExcel from "@linways/table-to-excel";

export default {
  props: ["downloadpdf","downloadexcel","dataOff"],
  components: {
    VueHtml2pdf,
  },
     watch: { 
      	downloadpdf: function(newVal, oldVal) { // watch it
          console.log('Prop changed: ', newVal, ' | was: ', oldVal)     
            this.generateReport()       
            this.genPDF()
                  setTimeout(() => {
                          this.width = '100%'
                          this.height = '100%'
                      }, 2000) 

        },
        downloadexcel: function(newVal, oldVal) { // watch it
          console.log('Prop changed: ', newVal, ' | was: ', oldVal)     
            this.generateReport()       
            this.genExcel()
        },
        },
  data() {
    return {
         options:{
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
headerTable:[
        {
            text: "ไม่ทำงาน(down)",
            subheader:[
              {text: "อุปกรณ์"},
              {text: "อุปกรณ์"},
              {text: "อุปกรณ์"},
            ]
        },
        {
            text: "เตือน(Warning)",
        },
        {
            text: "01-02",
        } 
      ],
       dataTable:[
        {
            device: "time",
            ip: "time",
            point: "time",
        },
        {
            device: "time",
            ip: "time",
            point: "time",
        },
        {
            device: "time",
            ip: "time",
            point: "time",
        },
        {
            device: "time",
            ip: "time",
            point: "time",
        },
        {
            device: "time",
            ip: "time",
            point: "time",
        }],
    };
  },
  methods: {
     hasDownloaded(e){
      console.log(e);
      this.$emit("onProgress",false);
    },
    genExcel(){
            TableToExcel.convert(document.getElementById("mytableX"), {
  name: "all-alarm.xlsx",
  sheet: {
    name: "Sheet 1"
  }
});
    },
    genPDF(){
      let doc = new jsPDF({ orientation: "l", unit: "pt" ,compress:true});
      doc.addFileToVFS("THSarabunNew.ttf",fontTH.th);
      // doc.addFileToVFS("THSarabunNewBold.ttf",fontTHBold.th);
      doc.addFileToVFS('THSarabunNew-bold.ttf', THSarabunNewBold.font);
      doc.addFont('THSarabunNew-bold.ttf', 'THSarabunNewBold', 'bold');
      doc.addFont("THSarabunNew.ttf", "THSarabunNew", "bold");
      doc.setFont("THSarabunNew", "bold");
      doc.setFontSize(24);
      doc.setFont('THSarabunNewBold', 'bold')
      doc.text("กองระบบเทคโนโลยีจราจร", 550, 53);
      doc.text("สำนักการจราจรและขนส่ง กรุงเทพมหานคร", 500, 75);
       doc.setFontSize(20);
      doc.text("จุดติดตั้ง: ", 150, 110);
       doc.text("All Alarm", 150, 140);
      const logo = require("@/assets/img/BMALogo3.jpg");
      
      var imgLogo = new Image();
      imgLogo.src = logo;
      // console.log("logo", this.imgURL);
      doc.addImage(imgLogo, "JPEG", 40, 20, 100, 100, undefined,'FAST');
      // doc.addImage(this.imgURL, "JPEG", 20, 400, 100, 100);

      // doc.autoTable({body: [[{ content: 'ไม่ทำงาน', colSpan: 1,rowSpan: 1, styles: { halign: 'center' ,font: "THSarabunNew"}}],],startY: 135,theme: 'grid',bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]}})
      // doc.autoTable(this.columns,this.rows,{ startY: 155 ,styles: {font: "THSarabunNew"},theme: 'grid',
      //   headStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0],textColor: [0, 0, 0],lineWidth: 1,},
      //   bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]},});

      // doc.autoTable({body: [[{ content: 'ไม่ทำงาน', colSpan: 1,rowSpan: 1, styles: { halign: 'center' ,font: "THSarabunNew"}}],],startY: 245,theme: 'grid', bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]}})
      // doc.autoTable(this.columns,this.rows,{ startY: 265 ,styles: {font: "THSarabunNew"},theme: 'grid',
      //   headStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0],textColor: [0, 0, 0],lineWidth: 1,},
      //   bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]}});
      //   doc.autoTable({body: [[{ content: 'ไม่ทำงาน', colSpan: 1,rowSpan: 1, styles: { halign: 'center' ,font: "THSarabunNew"}}],],startY: 355,theme: 'grid', bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]}})
      // doc.autoTable(this.columns,this.rows,{ startY: 375 ,styles: {font: "THSarabunNew"},theme: 'grid',
      //   headStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0],textColor: [0, 0, 0],lineWidth: 1,},
      //   bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]}});
      //   doc.autoTable({body: [[{ content: 'ไม่ทำงาน', colSpan: 1,rowSpan: 1, styles: { halign: 'center' ,font: "THSarabunNew"}}],],startY: 465,theme: 'grid',bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]}})
      // doc.autoTable(this.columns,this.rows,{ startY: 485 ,styles: {font: "THSarabunNew"},theme: 'grid',
      //   headStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0],textColor: [0, 0, 0],lineWidth: 1,},
      //   bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]}});


      doc.autoTable({ html: '#mytable', startY: 155,styles: {font: "THSarabunNew",halign: 'center',overflow : 'linebreak',
        cellWidth : 'auto',
        cellPadding : 1},theme: 'grid', headStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0],textColor: [0, 0, 0],lineWidth: 1,},
        bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]},})

      
      doc.save(`all-alarm.pdf`);
    },
    onProgress(e) {
      console.log(e);
      if(e < 100 ){
        console.log("ddd");
       this.$emit("onProgress",true);
      }else{
        //  console.log("dfff");
        // this.$emit("onProgress",false);
       
      }},
    generateReport() {
      console.log("test");
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
  },
};
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Sarabun&display=swap');

.font {
  font-family: 'Sarabun', sans-serif;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
