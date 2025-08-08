<template>
  <div>
    <vue-html2pdf :show-layout="false" :float-layout="true" :enable-download="false" :preview-modal="false"
      :paginate-elements-by-height="1400" filename="test" :pdf-quality="2" :manual-pagination="false" pdf-format="a3"
      pdf-orientation="landscape" pdf-content-width="100%" ref="html2Pdf" :pdf-margin="10">
      <section slot="pdf-content">

        <table id="mytableIn">
          <tr v-if="dataKey.keyCard === 'violate'">
            <th v-for="item in headerTableViolate" :key="item.text">{{ item.text }}</th>
          </tr>
          <tr v-else>
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
            <td>{{ item.percent }}</td>

          </tr>
        </table>

        <table id="mytableOut">
          <tr v-if="dataKey.keyCard === 'violate'">
            <th v-for="item in headerTableViolate" :key="item.text">{{ item.text }}</th>
          </tr>
          <tr v-else>
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
            <td>{{ item.percent }}</td>


          </tr>
        </table>

        <table id="mytableX" data-cols-width="20,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15">
          <tr>
            <th colspan="25" data-f-sz="25" data-a-h="right" data-f-bold="true">กองระบบเทคโนโลยีจราจร</th>

          </tr>
          <tr>

            <th colspan="25" data-f-sz="25" data-a-h="right" data-f-bold="true">สำนักการจราจรและขนส่ง กรุงเทพมหานคร</th>

          </tr>
          <tr></tr>
          <tr>

            <th colspan="25" data-f-sz="25" data-a-h="left" data-f-bold="true">
              รายงานปริมาณจราจรแยกตามประเภทยานพาหนะ(รายวัน)</th>
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
              วัน/เดือน/ปี {{ dateText }}
            </th>
          </tr>
          <tr></tr>
          <tr>
            <th data-f-sz="15">ปริมาณจราจรรายวัน (ทิศทางการจราจรเข้าเมือง) (คัน)</th>
          </tr>
          <tr v-if="dataKey.keyCard === 'violate'">
            <th data-a-h="center" data-b-a-s="thin" data-f-sz="15" v-for="item in headerTableViolate" :key="item.text">{{
              item.text }}</th>
          </tr>
          <tr v-else>
            <th data-a-h="center" data-b-a-s="thin" data-f-sz="15" v-for="item in headerTable" :key="item.text">{{
              item.text }}</th>
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
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._13 }}</td>
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
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.percent }}</td>

          </tr>
          <tr></tr>
          <tr></tr>
          <tr></tr>
          <tr>
            <th data-f-sz="15">ปริมาณจราจรรายวัน (ทิศทางการจราจรออกเมือง) (คัน)</th>
          </tr>
          <tr v-if="dataKey.keyCard === 'violate'">
            <th data-a-h="center" data-b-a-s="thin" data-f-sz="15" v-for="item in headerTableViolate" :key="item.text">{{
              item.text }}</th>
          </tr>
          <tr v-else>
            <th data-a-h="center" data-b-a-s="thin" data-f-sz="15" v-for="item in headerTable" :key="item.text">{{
              item.text }}</th>
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
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._13 }}</td>
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
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.percent }}</td>

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
export default {
  props: ["downloadpdf", "downloadexcel", "exportAdmin", "dataInbound", "dataOutbound", "dateText", "nameCheckPoint", "textHeaderReport", "dataKey"],
  components: {
    VueHtml2pdf,
    apexchart: VueApexCharts,
  },
  watch: {
    downloadpdf: function (newVal, oldVal) {
      console.log("textHeaderReport", this.dataInbound[0].percent);
      this.generateReport();
      this.genPDF();
    },
    downloadexcel: function (newVal, oldVal) {

      this.generateReport();
      this.genExcel();
    },
  },
  data() {
    return {
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
        }
      ],
      headerTableViolate: [
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
        {
          text: "เทียบกับปริมาณจราจรทั้งหมด(%)",
        },
      ],
      textCheckPoint: ""
    };
  },
  methods: {
    generateReport() {
      this.$refs.html2Pdf.generatePdf();
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
      let doc = new jsPDF({ orientation: "l", unit: "pt", compress: true });
      doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
      doc.addFileToVFS("THSarabunNew-bold.ttf", THSarabunNewBold.font);
      doc.addFont("THSarabunNew-bold.ttf", "THSarabunNewBold", "bold");
      doc.addFont("THSarabunNew.ttf", "THSarabunNew", "bold");
      doc.setFont("THSarabunNew", "bold");
      doc.setFontSize(20);
      doc.setFont("THSarabunNewBold", "bold");
      doc.text(this.textHeaderReport, 170, 45);
      doc.text("จุดติดตั้ง " + this.textCheckPoint, 170, 90);
      doc.text("วัน/เดือน/ปี " + this.dateText, 170, 115);
      doc.setFontSize(24);
      doc.text("กองระบบเทคโนโลยีจราจร", 560, 40);
      doc.text("สำนักการจราจรและขนส่ง กรุงเทพมหานคร", 510, 65);
      const logo = require("@/assets/img/BMALogo3.jpg");
      var imgLogo = new Image();
      imgLogo.src = logo;
      doc.addImage(imgLogo, "JPEG", 40, 20, 100, 100, undefined, 'FAST');
      doc.setFontSize(16);
      doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (ขาออก) (คัน)", 40, 340);
      doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (ขาเข้า) (คัน)", 40, 155);
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


      doc.save(`รายงานวัน.pdf`);
    },

  },
  mounted() {

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
