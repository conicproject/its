<template>
  <div>
    <vue-html2pdf :show-layout="false" :float-layout="true" :enable-download="false" :preview-modal="false"
      :paginate-elements-by-height="1400" filename="test" :pdf-quality="2" :manual-pagination="false" pdf-format="a3"
      pdf-orientation="landscape" pdf-content-width="100%" ref="html2Pdf" :pdf-margin="10">
      <section slot="pdf-content">
        <!-- <table id="mytableX_year" data-cols-width="20,10,10,10,10,10,10,10,10,10,10,10,10,15"> -->
          <table id="mytableX_year">

          <tr>
            <th colspan="14" data-f-sz="25" data-a-h="right" data-f-bold="true">กองระบบเทคโนโลยีจราจร</th>

          </tr>
          <tr>
            <th colspan="14" data-f-sz="25" data-a-h="right" data-f-bold="true">
              สำนักการจราจรและขนส่ง กรุงเทพมหานคร
            </th>
          </tr>
          <tr></tr>
          <tr>
            <th colspan="14" data-f-sz="25" data-a-h="left" data-f-bold="true">
              รายงานปริมาณจราจรแยกตามประเภทยานพาหนะ(รายปี)
            </th>
          </tr>

          <tr></tr>
          <tr>

            <th colspan="25" data-f-sz="25" data-a-h="left" data-f-bold="true">
              จุดติดตั้ง {{ nameCheckPoint }}
            </th>
          </tr>

          <tr></tr>
          <tr>

            <th colspan="25" data-f-sz="25" data-a-h="left" data-f-bold="true">
              ปี {{ dateText }}
            </th>
          </tr>

          <tr></tr>
          <tr>
            <th data-f-sz="15">ปริมาณจราจรรายปี (ทิศทางการจราจรเข้าเมือง) (คัน)</th>
          </tr>
          <tr>
            <th data-f-sz="15" v-for="item in headerTable" :key="item.text">{{ item }}</th>
          </tr>
          <tr v-for="item in dataInbound" :key="item.type">
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.type }}</td>

            <td v-if="item._0 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._0 }}</td>
            <td v-if="item._1 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._1 }}</td>
            <td v-if="item._2 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._2 }}</td>
            <td v-if="item._3 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._3 }}</td>
            <td v-if="item._4 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._4 }}</td>
            <td v-if="item._5 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._5 }}</td>
            <td v-if="item._6 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._6 }}</td>
            <td v-if="item._7 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._7 }}</td>
            <td v-if="item._8 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._8 }}</td>
            <td v-if="item._9 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._9 }}</td>
            <td v-if="item._10 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._10 }}</td>
            <td v-if="item._11 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._11 }}</td>
            <!-- <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._12 }}</td> -->
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.all }}</td>
            <td v-if="item.percent !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.percent }}
            </td>
          </tr>
          <tr></tr>
          <tr></tr>
          <tr></tr>
          <tr>
            <th data-f-sz="15">ปริมาณจราจรรายปี (ทิศทางการจราจรออกเมือง) (คัน)</th>
          </tr>
          <tr>
            <th data-f-sz="15" v-for="item in headerTable" :key="item">{{ item }}</th>
          </tr>
          <tr v-for="item in dataOutbound" :key="item.id">
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.type }}</td>
            <td v-if="item._0 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._0 }}</td>
            <td v-if="item._1 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._1 }}</td>
            <td v-if="item._2 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._2 }}</td>
            <td v-if="item._3 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._3 }}</td>
            <td v-if="item._4 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._4 }}</td>
            <td v-if="item._5 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._5 }}</td>
            <td v-if="item._6 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._6 }}</td>
            <td v-if="item._7 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._7 }}</td>
            <td v-if="item._8 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._8 }}</td>
            <td v-if="item._9 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._9 }}</td>
            <td v-if="item._10 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._10 }}</td>
            <td v-if="item._11 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._11 }}</td>
            <!-- <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._12 }}</td> -->
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.all }}</td>
            <td v-if="item.percent !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.percent }}
            </td>
          </tr>
        </table>
        <table id="mytableY1">
          <tr>
            <th v-for="item in headerTable" :key="item.text">{{ item }}</th>
          </tr>
          <tr v-for="item in dataInbound" :key="item.id">
            <td>{{ item.type }}</td>
            <td v-if="item._0 !== undefined">{{ item._0 }}</td>
            <td v-if="item._1 !== undefined">{{ item._1 }}</td>
            <td v-if="item._2 !== undefined">{{ item._2 }}</td>
            <td v-if="item._3 !== undefined">{{ item._3 }}</td>
            <td v-if="item._4 !== undefined">{{ item._4 }}</td>
            <td v-if="item._5 !== undefined">{{ item._5 }}</td>
            <td v-if="item._6 !== undefined">{{ item._6 }}</td>
            <td v-if="item._7 !== undefined">{{ item._7 }}</td>
            <td v-if="item._8 !== undefined">{{ item._8 }}</td>
            <td v-if="item._9 !== undefined">{{ item._9 }}</td>
            <td v-if="item._10 !== undefined">{{ item._10 }}</td>
            <td v-if="item._11 !== undefined">{{ item._11 }}</td>
            <td>{{ item.all }}</td>
            <td v-if="item.percent !== undefined">{{ item.percent }}</td>
          </tr>
        </table>

        <table id="mytableY2">
          <tr>
            <th v-for="item in headerTable" :key="item.text">{{ item }}</th>
          </tr>
          <tr v-for="item in dataOutbound" :key="item.id">
            <td>{{ item.type }}</td>
            <td v-if="item._0 !== undefined">{{ item._0 }}</td>
            <td v-if="item._1 !== undefined">{{ item._1 }}</td>
            <td v-if="item._2 !== undefined">{{ item._2 }}</td>
            <td v-if="item._3 !== undefined">{{ item._3 }}</td>
            <td v-if="item._4 !== undefined">{{ item._4 }}</td>
            <td v-if="item._5 !== undefined">{{ item._5 }}</td>
            <td v-if="item._6 !== undefined">{{ item._6 }}</td>
            <td v-if="item._7 !== undefined">{{ item._7 }}</td>
            <td v-if="item._8 !== undefined">{{ item._8 }}</td>
            <td v-if="item._9 !== undefined">{{ item._9 }}</td>
            <td v-if="item._10 !== undefined">{{ item._10 }}</td>
            <td v-if="item._11 !== undefined">{{ item._11 }}</td>
            <td>{{ item.all }}</td>
            <td v-if="item.percent !== undefined">{{ item.percent }}</td>

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
  props: ["downloadpdf", "downloadexcel", "exportAdmin", "dataInbound", "dataOutbound", "dateText", "nameCheckPoint", "headerTable", "textHeaderReport"],
  components: {
    VueHtml2pdf,
    apexchart: VueApexCharts,
  },
  watch: {
    downloadpdf: function (newVal, oldVal) {
      this.genPDF()
      console.log(this.headerTable);
    },
    downloadexcel: function (newVal, oldVal) {

      // this.generateReport();
      this.genExcel();
    },
  },
  data() {
    return {
      textCheckPoint: '',
    };
  },
  methods: {
    genExcel() {
      TableToExcel.convert(document.getElementById("mytableX_year"), {
        name: "รายงานผลข้อมูลจราจรแยกตามประเภทยานพาหนะ(รายปี).xlsx",
        sheet: {
          name: "Sheet 1",
        },
      });
    },
    generateReport() {
      this.$refs.html2Pdf.generatePdf();
    },

    genPDF() {

      this.textCheckPoint = this.nameCheckPoint || ''
      let doc = new jsPDF({ orientation: "l", unit: "pt", compress: true });
      doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
      // doc.addFileToVFS("THSarabunNewBold.ttf",fontTHBold.th);
      doc.addFileToVFS("THSarabunNew-bold.ttf", THSarabunNewBold.font);
      doc.addFont("THSarabunNew-bold.ttf", "THSarabunNewBold", "bold");
      doc.addFont("THSarabunNew.ttf", "THSarabunNew", "bold");
      doc.setFont("THSarabunNew", "bold");
      doc.setFontSize(20);
      doc.setFont("THSarabunNewBold", "bold");
      doc.text(this.textHeaderReport, 170, 45);
      doc.text("จุดติดตั้ง " + this.textCheckPoint, 170, 90);
      doc.text("ปี " + this.dateText, 170, 110);
      doc.setFontSize(24);
      doc.text("กองระบบเทคโนโลยีจราจร", 560, 50);
      doc.text("สำนักการจราจรและขนส่ง กรุงเทพมหานคร", 510, 75);
      const logo = require("@/assets/img/BMALogo3.jpg");
      var imgLogo = new Image();
      imgLogo.src = logo;

      doc.addImage(imgLogo, "JPEG", 40, 20, 100, 100, undefined, 'FAST');

      doc.setFontSize(16);
      doc.text("ปริมาณจราจรในแต่ละเดือน (ขาเข้า) (คัน)", 40, 145);

      doc.autoTable({
        html: "#mytableY1",
        startY: 150,
        styles: {
          font: "THSarabunNew", fontSize: 9, halign: 'center', overflow: 'linebreak',
          cellWidth: 'auto', fontSize: 10, textColor: '#000', cellPadding: 1
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });

      doc.text("ปริมาณจราจรในแต่ละเดือน (ขาออก) (คัน)", 40, 345);
      doc.autoTable({
        html: "#mytableY2",
        startY: 350,
        styles: {
          font: "THSarabunNew", halign: 'center', overflow: 'linebreak',
          cellWidth: 'auto', fontSize: 10, textColor: '#000', cellPadding: 1
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });

      doc.save(`รายงานปี.pdf`);
    },

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
