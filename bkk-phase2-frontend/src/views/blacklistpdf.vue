<template>
  <div>
    <vue-html2pdf
      :show-layout="false"
      :float-layout="true"
      :enable-download="false"
      :preview-modal="false"
      :paginate-elements-by-height="20000"
      filename="test"
      :pdf-quality="2"
      :manual-pagination="false"
      pdf-format="a4"
      pdf-orientation="portrait"
      pdf-content-width="100%"
      @progress="onProgress($event)"
      @hasStartedGeneration="hasStartedGeneration()"
      @hasDownloaded="hasDownloaded($event)"
      ref="html2Pdf"
    >
      <section slot="pdf-content">
        <v-container grid-list-md text-xs-center class="font">
          <v-card class="elevation-0">
            <v-card-text>
                <v-layout>
                
                <v-flex style="padding-left:30%"><h3>{{title}}</h3></v-flex> 
           </v-layout>
              <v-layout style="padding-top:4%">
                <v-flex>
                  <v-container>
                    <v-row>
                        <v-col cols="9" class="pa-4 solid">
                            <div class="text-style">User ที่ใช้งาน...........................</div>
                            <div class="text-style">วันที่...................................</div>
                            <div class="text-style">หน่วยงาน...............................</div>
                        </v-col>
                        
                        <v-col class="pa-4 ml-1 solid">
                            <div ><img src="@/assets/img/car1.png" width="70%" height="70%" /></div>
                        </v-col>
                    </v-row>
                    <!-- <v-card outlined >
                      <v-card-text >
                        <div>User ที่ใช้งาน.........</div>
                        <div>วันที่.................</div>
                        <div>หน่วยงาน..............</div>
                      </v-card-text>
                    </v-card> -->
                  </v-container>
                </v-flex>
                
              </v-layout>
              <v-layout style="padding-top:3%">
                <v-flex lg3></v-flex>
                <v-flex lg8>
                <v-card class="elevation-0">
                  <div ><img src="@/assets/img/car1.png" width="80%" height="00%" /></div>
                </v-card>
                </v-flex>
               <!-- <v-flex lg2></v-flex> -->
              </v-layout>
              <v-layout>
            
                  <v-container style="padding-left:30%">
                    <v-card class="elevation-0">
                      <v-card-text>
                        <div class="text-style">ทะเบียนยานพาหนะ............................</div>
                        <div class="text-style">จังหวัด.....................................</div>
                        <div class="text-style">ประเภทยานพาหนะ............................</div>
                        <div class="text-style">สียานพาหนะ.................................</div>
                        <div class="text-style">สถานที่.....................................</div>
                        <div class="text-style">วันที่.......................................</div>
                        <div class="text-style">เวลา......................................</div>
                      </v-card-text>
                    </v-card>
                  </v-container>
                
              </v-layout>
            </v-card-text>
          </v-card>
        </v-container>
      </section>   
    </vue-html2pdf>
     <!-- <v-btn @click="generateReport">download</v-btn> -->
  </div>
</template>
<script>
import { jsPDF } from "jspdf";

import VueHtml2pdf from "vue-html2pdf";
// import VueApexCharts from "vue-apexcharts";
export default {
   props: ["downloadpdf",'title'],
  components: {
    VueHtml2pdf,
    // apexchart: VueApexCharts,
  },
  watch: { 
      	downloadpdf: function(newVal, oldVal) { // watch it
          console.log('Prop changed: ', newVal, ' | was: ', oldVal)
          // if(newVal === true){
            this.generateReport()
          // }
        },},
  data() {
    return {
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
          text: "time",
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
          text: "All",
        },
      ],
      dataTable: [
        {
          text: "time",
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
      ],
    };
  },
  methods: {
     hasDownloaded(e){
      console.log(e);
      this.$emit("onProgress",false);
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
  color:black;
}

.text-style{
    font-size: 18px;
    padding: 5px;
    
}
.solid{
     border: 1px solid black;
}
table,
th,
td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
