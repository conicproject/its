<template>
  <div>
    <vue-html2pdf :show-layout="false" :float-layout="true" :enable-download="false" :preview-modal="false"
      :paginate-elements-by-height="1400" filename="test" :pdf-quality="2" :manual-pagination="false" pdf-format="a3"
      pdf-orientation="landscape" pdf-content-width="100%" @progress="onProgress($event)"
      @hasStartedGeneration="hasStartedGeneration()" @hasDownloaded="hasDownloaded($event)" ref="html2Pdf">
      <section slot="pdf-content">
        <v-container grid-list-md text-xs-center class="font">
          <v-layout row wrap style="width: 100%">
            <v-flex>
              <v-card class="elevation-0">
                <v-card-title>
                  <v-layout>
                    <v-flex lg2><img width="60%" src="@/assets/img/BMALogo3.jpg" /></v-flex>
                    <v-flex lg4>
                      <h3>กองระบบเทคโนโลยีจราจร<br />สำนักการจราจรและขนส่ง<br />กรุงเทพมหานคร</h3>
                    </v-flex>
                    <v-flex lg4>
                      <h3>Report Volume & Cassification<br />จุดติดตั้ง : <br />ถนน </h3>
                    </v-flex>
                    <v-flex lg2></v-flex>
                  </v-layout>
                </v-card-title>
                <v-card-text class="pt-5">
                  <h3>ข้อมูลยานพาหนะ</h3>
                  <br />
                  <table id="mytable">
                    <thead>
                      <tr>
                        <th>ลำดับ</th>
                        <th>ป้ายทะเบียนยานพาหนะ</th>
                        <th>เลขทะเบียนยานพาหนะ</th>
                        <th>จังหวัด</th>
                        <th>ประเภทยานพาหนะ</th>
                        <th>สียานพาหนะ</th>
                        <th>วัน/เดือน/ปี</th>
                        <th>เวลา</th>
                        <th>สถานที่</th>
                        <th>ทิศทางการจราจร</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="item in dataReports" :key="item.index">
                        <td>{{ item.index }}</td>
                        <td v-if="item.img_base64 !== ''"><img :src="item.img_base64" /></td>
                        <td v-else></td>
                        <td>{{ item.license }}</td>
                        <td>{{ item.province }}</td>
                        <td>{{ item.type }}</td>
                        <td>{{ item.color }}</td>
                        <td>{{ item.date }}</td>
                        <td>{{ item.time }}</td>
                        <td>{{ item.location }}</td>
                        <td>{{ item.direction }}</td>
                      </tr>



                    </tbody>
                  </table>

                  <table id="mytableX" data-cols-width="10,30,20,30,20,20,20,20,20">
                    <tr>
                      <th colspan="9" data-f-sz="20" data-a-h="right" data-f-bold="true">กองระบบเทคโนโลยีจราจร</th>
                      <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">สำนักการจราจรและขนส่ง </th>
                      <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กรุงเทพมหานคร</th> -->
                    </tr>
                    <tr>
                      <th colspan="9" data-f-sz="20" data-a-h="right" data-f-bold="true">สำนักการจราจรและขนส่ง
                        กรุงเทพมหานคร</th>
                      <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">สำนักการจราจรและขนส่ง </th>
                      <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กรุงเทพมหานคร</th> -->
                    </tr>
                    <tr>
                      <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กองระบบเทคโนโลยีจราจร </th> -->
                      <th colspan="9" data-f-sz="20" data-a-h="left" data-f-bold="true">รายงานการค้นหาข้อมูลยานพาหนะ</th>
                      <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กรุงเทพมหานคร</th> -->
                    </tr>

                    <tr>
                    </tr>
                    <tr data-height="25">
                      <th data-a-h="center" data-b-a-s="thin" data-f-sz="15">ลำดับ</th>
                      <th data-a-h="center" data-b-a-s="thin" data-f-sz="15">เลขทะเบียนยานพาหนะ</th>
                      <th data-a-h="center" data-b-a-s="thin" data-f-sz="15">จังหวัด</th>
                      <th data-a-h="center" data-b-a-s="thin" data-f-sz="15">ประเภทยานพาหนะ</th>
                      <th data-a-h="center" data-b-a-s="thin" data-f-sz="15">สียานพาหนะ</th>
                      <th data-a-h="center" data-b-a-s="thin" data-f-sz="15">วัน/เดือน/ปี</th>
                      <th data-a-h="center" data-b-a-s="thin" data-f-sz="15">เวลา</th>
                      <th data-a-h="center" data-b-a-s="thin" data-f-sz="15">สถานที่</th>
                      <th data-a-h="center" data-b-a-s="thin" data-f-sz="15">ทิศทางการจราจร</th>
                    </tr>
                    <tr v-for="item in dataReports" :key="item.index">
                      <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.index }}</td>
                      <!-- <td data-a-h="center" data-b-a-s="thin" data-f-sz="15"><img :src="item.img_base64" /></td> -->
                      <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.license }}</td>
                      <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.province }}</td>
                      <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.type }}</td>
                      <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.color }}</td>
                      <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.date }}</td>
                      <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.time }}</td>
                      <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.location }}</td>
                      <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.direction }}</td>
                    </tr>


                  </table>
                </v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>

      </section>
    </vue-html2pdf>
  </div>
</template>
<script>
import VueHtml2pdf from "vue-html2pdf";
import { jsPDF } from "jspdf";
const baseUrl = require('../../baseUrl.json')
import "jspdf-autotable";
import fontTH from "../fontTH.js";
import TableToExcel from "@linways/table-to-excel";
import THSarabunNewBold from "../THSarabunNewBold.js";
import Swal from "sweetalert2/dist/sweetalert2.js";
const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});
export default {
  props: ["downloadpdf", "downloadexcel", "headers", "dataTableRe"],
  components: {
    VueHtml2pdf,
  },
  watch: {
    downloadpdf: function (newVal, oldVal) { // watch it
      this.getReport(this.dataTableRe, "pdf")
      return

      this.generateReport()
      this.genPDF()

      setTimeout(() => {
        this.width = '100%'
        this.height = '100%'
      }, 2000)


    },
    downloadexcel: function (newVal, oldVal) { // watch it
      this.getReport(this.dataTableRe)
      return

      this.generateReport()
      this.genExcel()
    },
  },
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
          text: "ไม่ทำงาน(down)",
        },
        {
          text: "00-01",
        },
        {
          text: "01-02",
        }
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
        }],
      dataReports: []
    };
  },
  methods: {
    genExcel() {
      TableToExcel.convert(document.getElementById("mytableX"), {
        name: "ข้อมูลค้นหายานพาหนะ.xlsx",
        sheet: {
          name: "Sheet 1"
        }
      });
    },
    genPDF() {

      let doc = new jsPDF({ orientation: "l", unit: "pt", compress: true });

      doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
      doc.addFileToVFS('THSarabunNew-bold.ttf', THSarabunNewBold.font);
      doc.addFont('THSarabunNew-bold.ttf', 'THSarabunNewBold', 'bold');
      doc.addFont("THSarabunNew.ttf", "THSarabunNew", "bold");
      doc.setFont("THSarabunNew", "bold");
      doc.setFontSize(24);

      doc.setFont('THSarabunNewBold', 'bold')
      doc.text("รายงานการค้นหาข้อมูลยานพาหนะ", 250, 130);

      doc.text("กองระบบเทคโนโลยีจราจร", 550, 53);
      doc.text("สำนักการจราจรและขนส่ง กรุงเทพมหานคร", 500, 75);

      const logo = require("@/assets/img/BMALogo3.jpg");

      var imgLogo = new Image();
      imgLogo.src = logo;
      console.log("logo", imgLogo);
      doc.addImage(imgLogo, "JPEG", 40, 20, 100, 100, undefined, 'FAST');
      doc.autoTable({
        html: '#mytable', startY: 155, styles: {
          font: "THSarabunNew", halign: 'center', overflow: 'linebreak',
          cellWidth: 'auto', fontSize: 16, textColor: '#000', minCellHeight: 50,
          cellPadding: 1
        }, theme: 'grid', headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1, },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
        didDrawCell: function (data) {
          if (data.column.index === 1 && data.cell.section === 'body') {
            var td = data.cell.raw;

            var img = td.getElementsByTagName('img')[0]
            var dim = data.cell.height - data.cell.padding('vertical');

            if (img !== undefined) {

              let base64 = img.src

              doc.addImage(base64, data.cell.x + 20, data.cell.y, dim, dim);
            }

          }
        }
      })

      doc.save(`ข้อมูลค้นหายานพาหนะ.pdf`);
    },
    hasDownloaded(e) {
      console.log(e);
    },
    onProgress(e) {
      console.log(e);
      if (e < 100) {
        console.log("ddd");
        this.$emit("onProgress", true);
      } else {


      }
    },
    generateReport() {
      this.$refs.html2Pdf.generatePdf();
    },
    download() {
      var doc = new jsPDF("p", "pt", "A4");

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
    getReport(data, exportType = "excel") {
      Toast.fire({
        icon: "success",
        title: "กำลังทำการสร้างรายงาน กรุณารอซักครู่",
      });
      let session_data = sessionStorage.getItem("session");
      let url = baseUrl.ipServer + "/vehicle-report";
      // console.log(data)
      // return

      this.axios
        .post(url, data, {
          headers: { session: session_data }
        })
        .then((response) => {
          // console.log("then", response)
          const records = response.data.data.records

          this.dataReports = records
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {
          console.log("finally")
          if (exportType == "excel") {
            this.generateReport()
            this.genExcel()
          } else {
            this.generateReport()
            this.genPDF()

            setTimeout(() => {
              this.width = '100%'
              this.height = '100%'
            }, 2000)
          }
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

table,
th,
td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
