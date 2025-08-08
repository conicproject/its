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
          <div id="chartLine" style="width: 100%; height: 500px;"></div>
          <div id="chartPie" style="width: 100%; height: 500px;"></div>
  
          <table id="mytableW1">
            <tr>
              <th v-for="item in headerTable" :key="item.text">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataInbound" :key="item.id">
              <td>{{ item.type }}</td>
              <td v-if="item._Monday !== undefined">{{ item._Monday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Tuesday !== undefined">{{ item._Tuesday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Wednesday !== undefined">{{ item._Wednesday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Thursday !== undefined">{{ item._Thursday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Friday !== undefined">{{ item._Friday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Saturday !== undefined">{{ item._Saturday}}</td>
              <td v-else >0</td>
              <td  v-if="item._Sunday !== undefined">{{ item._Sunday }}</td>
              <td v-else >0</td>
              <td >{{ item.all }}</td>
            </tr>
          </table>
  
          <table id="mytableW2">
            <tr>
              <th v-for="item in headerTable" :key="item.text">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataOutbound" :key="item.id">
              <td>{{ item.type }}</td>
             <td v-if="item._Monday !== undefined">{{ item._Monday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Tuesday !== undefined">{{ item._Tuesday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Wednesday !== undefined">{{ item._Wednesday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Thursday !== undefined">{{ item._Thursday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Friday !== undefined">{{ item._Friday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Saturday !== undefined">{{ item._Saturday}}</td>
              <td v-else >0</td>
              <td  v-if="item._Sunday !== undefined">{{ item._Sunday }}</td>
              <td v-else >0</td>
              <td>{{ item.all }}</td>
             
            </tr>
          </table>
  
          <table id="mytableW3">              
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


<!-- violation -->

         <div id="chartLine_in_v" style="width: 100%; height: 500px;"></div>
         <div id="chartPie_in_v" style="width: 100%; height: 500px;"></div>
          <div id="chartLine_out_v" style="width: 100%; height: 500px;"></div>
         <div id="chartPie_out_v" style="width: 100%; height: 500px;"></div>
  
          <table id="mytableW1_v">
            <tr>
              <th v-for="item in headerTable" :key="item.text">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataInbound_violation" :key="item.id">
              <td>{{ item.type }}</td>
              <td v-if="item._Monday !== undefined">{{ item._Monday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Tuesday !== undefined">{{ item._Tuesday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Wednesday !== undefined">{{ item._Wednesday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Thursday !== undefined">{{ item._Thursday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Friday !== undefined">{{ item._Friday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Saturday !== undefined">{{ item._Saturday}}</td>
              <td v-else >0</td>
              <td  v-if="item._Sunday !== undefined">{{ item._Sunday }}</td>
              <td v-else >0</td>
              <td >{{ item.all }}</td>
            </tr>
          </table>
  
          <table id="mytableW2_v">
            <tr>
              <th v-for="item in headerTable" :key="item.text">{{ item.text }}</th>
            </tr>
            <tr v-for="item in dataOutbound_violation" :key="item.id">
              <td>{{ item.type }}</td>
               <td v-if="item._Monday !== undefined">{{ item._Monday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Tuesday !== undefined">{{ item._Tuesday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Wednesday !== undefined">{{ item._Wednesday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Thursday !== undefined">{{ item._Thursday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Friday !== undefined">{{ item._Friday }}</td>
              <td v-else >0</td>
              <td  v-if="item._Saturday !== undefined">{{ item._Saturday}}</td>
              <td v-else >0</td>
              <td  v-if="item._Sunday !== undefined">{{ item._Sunday }}</td>
              <td v-else >0</td>
              <td>{{ item.all }}</td>
             
            </tr>
          </table>

        </section>
      </vue-html2pdf>
  
    </div>
    
  </template>
  <script>
    let doc = new jsPDF({ orientation: "l", unit: "pt" ,compress:true});
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
            downloadpdf: function(newVal, oldVal) { // watch it
            console.log('Prop changed: ', newVal, ' | was: ', oldVal)     
            this.exportPDF();
            
              
      setTimeout(() => {
              this.width = '100%'
              this.height = '100%'
          }, 2000) 
  
             
          },
          },
    data() {
      return {
        textCheckpoint :"",
       textDate:"",
       dataInbound:[],
        dataOutbound:[],
        dataInbound_violation:[],
        dataOutbound_violation:[],
       dataDirection:{},
        optionspie: {
          
           labels: ['Apple', 'Mango', 'Orange', 'Watermelon'],
            total: {
            show: true,
            },
        },    
        seriespie: [44, 55, 41, 17, 15],
        
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
            data: [0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10],
          },
          {
            name: "PRODUCT B",
            data: [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
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
              text: "เวลา",
          },
          {
              text: "วันจันทร์",
          },
          {
              text: "วันอังคาร",
          },
          {
              text: "วันพุธ",
          },
          {
              text: "วันพฤหัสบดี",
          },
          {
              text: "วันศุกร์",
          },
          {
              text: "วันเสาร์",
          },
          {
              text: "วันอาทิตย์",
          },
          {
              text: "ปริมาณจราจร(คัน)",
          }
        ],
      headerTabletime:[
          
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
          }
        ],
          imgPie:"",
          imgURI:"",
          percent_violation_in:"",
       percent_violation_out:"",
       roadName:"",
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


      genPDFAdmin(imgLine,imgPie,index_pic){
        doc.addPage("a4", "l");
        doc.addFileToVFS("THSarabunNew.ttf",fontTH.th);
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
        doc.setFont("THSarabunNew", "Bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
       doc.text("Report Volume & Cassification", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 76);
        doc.text("ถนน : "+this.roadName, 440, 53);
        doc.text("วันที่ : "+this.date, 440, 98);
         doc.setFontSize(15);
        doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (ทิศทางการจราจรเข้าเมือง) (คัน)", 40, 105);
        const logo = require("@/assets/img/BMALogo3.jpg");
        
        var imgLogo = new Image();
        imgLogo.src = logo;
         console.log("logo", this.imgURI);
         doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
  
        const CheckPoint1 = require("@/assets/img/checkpointPicture/"+index_pic+".png");
         var imgCheckPoint = new Image();
       imgCheckPoint.src = CheckPoint1;
       doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
  
        doc.setFontSize(17);
            doc.text("Graph of Traffic Volume", 600, 310);
        doc.setFontSize(15);
        doc.text("(Inbound/Outbound)", 620, 320);
        doc.addImage(imgLine, "JPEG", 500, 330, 300, 100, undefined,'FAST');
           doc.setFontSize(17);
           doc.text("Volume&Classification Pie Graph", 550, 140);
       doc.addImage(imgPie, "JPEG", 550, 150, 200, 100, undefined,'FAST');
        doc.setFontSize(15);
  
       
        doc.autoTable({
        html: "#mytableW1",
        tableWidth:400,
        startY: 110,
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
  
        doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (ทิศทางจราจรออกเมือง) (คัน)", 40, 285);
       
  
        doc.autoTable({
        html: "#mytableW2",
        tableWidth:400,
        startY: 290,
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
  
         doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (คัน)", 40, 470);
      
         doc.autoTable({
        html: "#mytableW3",
        startY: 475,
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
      genPDFAdmin_in_v(imgLine,imgPie,index_pic){
        doc.addPage("a4", "l");
        doc.addFileToVFS("THSarabunNew.ttf",fontTH.th);
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
        doc.text("ปริมาณจราจรในแต่ละวัน (ขาเข้า) (คัน)", 40, 120);
        const logo = require("@/assets/img/BMALogo3.jpg");
        
        var imgLogo = new Image();
        imgLogo.src = logo;
         console.log("logo", this.imgURI);
         doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
  
         const CheckPoint1 = require("@/assets/img/checkpointPicture/"+index_pic+".png");
         var imgCheckPoint = new Image();
         imgCheckPoint.src = CheckPoint1;
         doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
  
        doc.setFontSize(17);
            
        doc.text("Traffic Volume Graph", 620, 320);
        doc.addImage(imgLine, "JPEG", 500, 335, 300, 100, undefined,'FAST');
           doc.setFontSize(17);
           doc.text("Volume&Classification of Violation Pie Graph", 550, 145);
       doc.addImage(imgPie, "JPEG", 550, 155, 200, 100, undefined,'FAST');
        doc.setFontSize(15);
  
       
        doc.autoTable({
        html: "#mytableW1",
        tableWidth:450,
        startY: 125,
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
  
        doc.text("ปริมาณยานพาหนะฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกดในแต่ละวัน (ขาเข้า) (คัน)", 40, 300);
       
  
        doc.autoTable({
        html: "#mytableW1_v",
        tableWidth:450,
        startY: 305,
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

      doc.setFontSize(12);
        doc.text("จำนวนของการฝ่าสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด คิดเป็น "+this.percent_violation_in+"% ของปริมาณจราจรทั้งหมด", 40, 467);
         
      },
      genPDFAdmin_out_v(imgLine,imgPie,index_pic){
        doc.addPage("a4", "l");
        doc.addFileToVFS("THSarabunNew.ttf",fontTH.th);
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
        doc.text("ปริมาณจราจรในแต่ละวัน (ขาออก) (คัน)", 40, 120);
        const logo = require("@/assets/img/BMALogo3.jpg");
        
        var imgLogo = new Image();
        imgLogo.src = logo;
         console.log("logo", this.imgURI);
         doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
  
         const CheckPoint1 = require("@/assets/img/checkpointPicture/"+index_pic+".png");
         var imgCheckPoint = new Image();
         imgCheckPoint.src = CheckPoint1;
         doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
  
        doc.setFontSize(17);
         
        doc.text("Traffic Volume Graph", 620, 320);
        doc.addImage(imgLine, "JPEG", 500, 335, 300, 100, undefined,'FAST');
           doc.setFontSize(17);
           doc.text("Volume&Classification of Violation Pie Graph", 550, 145);
       doc.addImage(imgPie, "JPEG", 550, 155, 200, 100, undefined,'FAST');
        doc.setFontSize(15);
  
       
        doc.autoTable({
        html: "#mytableW2",
        tableWidth:450,
        startY: 125,
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
  
        doc.text("ปริมาณยานพาหนะฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกดในแต่ละวัน (ขาออก) (คัน)", 40, 300);
       
  
        doc.autoTable({
        html: "#mytableW2_v",
        tableWidth:450,
        startY: 305,
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
  
      doc.setFontSize(12);
        doc.text("จำนวนของการฝ่าสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด คิดเป็น "+this.percent_violation_out+"% ของปริมาณจราจรทั้งหมด", 40, 467);
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
          async genChartPieApex_in_v(cat,data) {
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
          async genChartPieApex_out_v(cat,data) {
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
    async genChartLineApex(cat,data) {
        return new Promise(async(resolve, reject) =>  {
          let img = ''
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
          //  console.log(imgURI)
        img = imgURI;

          resolve({
                  status: "success",
                  data: img
                });

        });
      });
     
   });
    },
        async genChartLineApex_in_v(cat,data) {
        return new Promise(async(resolve, reject) =>  {
          let img = ''
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
      var chart = new ApexCharts(document.querySelector("#chartLine_in_v"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
          //  console.log(imgURI)
        img = imgURI;

          resolve({
                  status: "success",
                  data: img
                });

        });
      });
     
   });
    },
        async genChartLineApex_out_v(cat,data) {
        return new Promise(async(resolve, reject) =>  {
          let img = ''
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
      var chart = new ApexCharts(document.querySelector("#chartLine_out_v"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
          //  console.log(imgURI)
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
        console.log("exportWeek");
        let res = await this.loopGenPdf()
        if(res.status == 'success'){
       doc.save(`รายงานผลข้อมูลจราจร(รายสัปดาห์).pdf`);
        this.$emit('closePDF')
        }
      },
      async loopGenPdf(){
        return new Promise(async(resolve, reject) =>  {
        for(let i = 0; i < this.dataExport.length;i++){
          let index_pic = this.dataExport[i].checkpoint_id
        this.textCheckpoint = this.dataExport[i].checkpoint_name
        this.textDate= this.date
         this.dataInbound = this.dataExport[i].dataInbound
         this.dataOutbound = this.dataExport[i].dataOutbound
          this.dataDirection = this.dataExport[i].dataDirection
        this.percent_violation_in = this.dataExport[i].percent_violation_in
       this.percent_violation_out = this.dataExport[i].percent_violation_out
       this.roadName = this.dataExport[i].road_name
 
        // let bar = this.dataExport[i].dataPieChart.length > 0 ?await this.genChartBarApex(this.dataExport[i].categories,this.dataExport[i].dataPieChart): { status: "success"}
        // let pie = this.dataExport[i].dataPieChart.length > 0 ?await this.genChartPie(this.dataExport[i].dataPieChart) : { status: "success"}
         let pie = await this.genChartPieApex(this.dataExport[i].categories,this.dataExport[i].dataChart) 
         let line = await this.genChartLineApex(this.dataExport[i].apex_cat,this.dataExport[i].apex_line) 
         //console.log(bar);
         

         //--------------violation
         this.dataInbound_violation = this.dataExport[i].dataInbound_violation
         this.dataOutbound_violation = this.dataExport[i].dataOutbound_violation
         let pie_in_v = await this.genChartPieApex_in_v(this.dataExport[i].categories_violation,this.dataExport[i].PieChart_in_violation) 
         let pie_out_v = await this.genChartPieApex_out_v(this.dataExport[i].categories_violation,this.dataExport[i].PieChart_out_violation) 
         let line_in_v = await this.genChartLineApex_in_v(this.dataExport[i].apex_cat_violation,this.dataExport[i].apex_line_in_violation) 
         console.log(this.dataExport[i].apex_line_in_violation)
         let line_out_v = await this.genChartLineApex_out_v(this.dataExport[i].apex_cat_violation,this.dataExport[i].apex_line_out_violation) 
         this.generateReport();
         if(pie.status === 'success' && line.status === 'success' && pie_in_v.status === 'success' && line_in_v.status === 'success' && pie_out_v.status === 'success' && line_out_v.status === 'success' ){
            // console.log("success");
            
            if(i ==0){
         doc.addFileToVFS("THSarabunNew.ttf",fontTH.th);
         doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
         doc.setFont("THSarabunNew", "Bold");
         doc.setFontSize(18);
         doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
         doc.text("สำนักการจราจรและขนส่ง", 200, 50);
         doc.text("กรุงเทพมหานคร", 200, 70);
         doc.text("Report Volume & Cassification", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 76);
        doc.text("ถนน : "+this.roadName, 440, 53);
        doc.text("วันที่ : "+this.date, 440, 98);
       
          doc.setFontSize(15);
         doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (ทิศทางการจราจรเข้าเมือง) (คัน)", 40, 105);
         const logo = require("@/assets/img/BMALogo3.jpg");
         
         var imgLogo = new Image();
         imgLogo.src = logo;
          console.log("logo", this.imgURI);
          doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
   
          const CheckPoint1 = require("@/assets/img/checkpointPicture/"+index_pic+".png");
          var imgCheckPoint = new Image();
          imgCheckPoint.src = CheckPoint1;
           doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
   
         doc.setFontSize(17);
             doc.text("Graph of Traffic Volume", 600, 310);
         doc.setFontSize(15);
         doc.text("(Inbound/Outbound)", 620, 320);
            doc.addImage(line.data, "JPEG", 500, 330, 300, 100, undefined,'FAST');
            doc.setFontSize(17);
            doc.text("Volume&Classification Pie Graph", 550, 140);
        doc.addImage(pie.data, "JPEG",550, 150, 200, 100, undefined,'FAST');
         doc.setFontSize(15);
   
        
          doc.autoTable({ html: '#mytableW1',tableWidth:400, startY: 110 ,styles: {font: "THSarabunNew",halign: 'center',overflow : 'linebreak',
           cellWidth : 'auto',textColor:'#000',
           cellPadding : 1},theme: 'grid', headStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0],textColor: [0, 0, 0],lineWidth: 1,},
           bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]},})
   
         doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (ทิศทางจราจรออกเมือง) (คัน)", 40, 285);
        
   
           doc.autoTable({ html: '#mytableW2',tableWidth:400, startY: 290,styles: {font: "THSarabunNew",halign: 'center',overflow : 'linebreak',
           cellWidth : 'auto',textColor:'#000',
           cellPadding : 1},theme: 'grid', headStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0],textColor: [0, 0, 0],lineWidth: 1,},
           bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]},})
   
          doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (คัน)", 40, 470);
       
          doc.autoTable({ html: '#mytableW3', startY: 475,styles: {font: "THSarabunNew",halign: 'center',overflow : 'linebreak',
           cellWidth : 'auto',textColor:'#000',
           cellPadding : 1},theme: 'grid', headStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0],textColor: [0, 0, 0],lineWidth: 1,},
           bodyStyles: {fillColor: [255, 255, 255],lineColor: [0, 0, 0]},})

           this.genPDFAdmin_in_v(line_in_v.data,pie_in_v.data,index_pic)
           this.genPDFAdmin_out_v(line_out_v.data,pie_out_v.data,index_pic)
         }
           
               
           else{
            
               this.genPDFAdmin(line.data,pie.data,index_pic)
               this.genPDFAdmin_in_v(line_in_v.data,pie_in_v.data,index_pic)
              this.genPDFAdmin_out_v(line_out_v.data,pie_out_v.data,index_pic)

               
             }
           }
        
 
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
  @import url('https://fonts.googleapis.com/css2?family=Sarabun&display=swap');
  
  .font {
    font-family: 'Sarabun', sans-serif;
  }
  table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
  }
  </style>
  