<template>
  <div>
    <vue-html2pdf :show-layout="false" :float-layout="true" :enable-download="false" :preview-modal="false"
      :paginate-elements-by-height="1400" filename="test" :pdf-quality="2" :manual-pagination="false" pdf-format="a3"
      pdf-orientation="landscape" pdf-content-width="100%" ref="html2Pdf" :pdf-margin="10">
      <section slot="pdf-content">


        <table id="mytableW1">
          <tr v-if="dataKey.keyCard === 'violate'">
            <th v-for="item in headerTable" :key="item.text">{{ item }}</th>
          </tr>
          <tr v-else>
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
            <td>{{ item.all }}</td>
            <td v-if="item.percent !== undefined">{{ item.percent }}</td>


          </tr>
        </table>

        <table id="mytableW2">
          <tr v-if="dataKey.keyCard === 'violate'">
            <th v-for="item in headerTable" :key="item.text">{{ item }}</th>
          </tr>
          <tr v-else>
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
            <td>{{ item.all }}</td>
            <td v-if="item.percent !== undefined">{{ item.percent }}</td>

          </tr>
        </table>

        <table id="mytableX_week" data-cols-width="20,15,15,15,15,15,15,15,15">
          <tr>
            <th colspan="9" data-f-sz="25" data-a-h="right" data-f-bold="true">กองระบบเทคโนโลยีจราจร</th>

          </tr>
          <tr>
            <th colspan="9" data-f-sz="25" data-a-h="right" data-f-bold="true">สำนักการจราจรและขนส่ง กรุงเทพมหานคร</th>
          </tr>
          <tr>
          </tr>
          <tr>

            <th colspan="9" data-f-sz="25" data-a-h="left" data-f-bold="true">
              รายงานปริมาณจราจรแยกตามประเภทยานพาหนะ(รายสัปดาห์)</th>
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
            <th data-f-sz="15">ปริมาณจราจรรายสัปดาห์ (ทิศทางการจราจรเข้าเมือง) (คัน)</th>
          </tr>
          <tr v-if="dataKey.keyCard === 'violate'">
            <th data-f-sz="15" v-for="item in headerTable" :key="item.text">{{ item }}</th>
          </tr>
          <tr v-else>
            <th data-f-sz="15" v-for="item in headerTable" :key="item.text">{{ item }}</th>
          </tr>
          <tr v-for="item in dataInbound" :key="item.id">
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.type }}</td>
            <td v-if="item._0 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._0 }}</td>
            <td v-if="item._1 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._1 }}</td>
            <td v-if="item._2 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._2 }}</td>
            <td v-if="item._3 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._3 }}</td>
            <td v-if="item._4 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._4 }}</td>
            <td v-if="item._5 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._5 }}</td>
            <td v-if="item._6 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._6 }}</td>
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.all }}</td>

            <td v-if="item.percent !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.percent }}
            </td>


          </tr>
          <tr>
          </tr>
          <tr>
          </tr>
          <tr>
          </tr>
          <tr>
            <th data-f-sz="15">ปริมาณจราจรรายสัปดาห์ (ทิศทางการจราจรออกเมือง) (คัน)</th>
          </tr>
          <tr v-if="dataKey.keyCard === 'violate'">
            <th data-f-sz="15" v-for="item in headerTable" :key="item.text">{{ item }}</th>
          </tr>
          <tr v-else>
            <th data-f-sz="15" v-for="item in headerTable" :key="item.text">{{ item }}</th>
          </tr>
          <tr v-for="item in dataOutbound" :key="item.type">
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.type }}</td>
            <td v-if="item._0 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._0 }}</td>
            <td v-if="item._1 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._1 }}</td>
            <td v-if="item._2 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._2 }}</td>
            <td v-if="item._3 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._3 }}</td>
            <td v-if="item._4 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._4 }}</td>
            <td v-if="item._5 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._5 }}</td>
            <td v-if="item._6 !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item._6 }}</td>
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.all }}</td>

            <td v-if="item.percent !== undefined" data-a-h="center" data-b-a-s="thin" data-f-sz="15">{{ item.percent }}
            </td>

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
  props: ["downloadpdf", "downloadexcel", "exportAdmin", "dateText", "nameCheckPoint", "dataInbound", "dataOutbound", "textHeaderReport", "dataKey", "headerTable"],
  components: {
    VueHtml2pdf,
    apexchart: VueApexCharts,
  },
  watch: {
    downloadpdf: function (newVal, oldVal) { // watch it
      this.genPDF()
    },
    downloadexcel: function (newVal, oldVal) { // watch it

      // this.generateReport()
      this.genExcel()

    },
  },
  data() {
    return {
      textCheckPoint: "",
    };
  },
  methods: {
    genExcel() {
      console.log("รายสัปดาห์");
      TableToExcel.convert(document.getElementById("mytableX_week"), {
        name: "รายงานผลข้อมูลจราจรแยกตามประเภทยานพาหนะ(รายสัปดาห์).xlsx",
        sheet: {
          name: "Sheet 1"
        }
      });
    },
    generateReport() {

      this.$refs.html2Pdf.generatePdf();
    },

    genPDF() {
      let doc = new jsPDF({ orientation: "l", unit: "pt", compress: true });

      this.textCheckPoint = this.nameCheckPoint || ''
      doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
      doc.addFileToVFS('THSarabunNew-bold.ttf', THSarabunNewBold.font);
      doc.addFont('THSarabunNew-bold.ttf', 'THSarabunNewBold', 'bold');
      doc.addFont("THSarabunNew.ttf", "THSarabunNew", "bold");
      doc.setFont("THSarabunNew", "bold");
      doc.setFontSize(20)
      doc.setFont('THSarabunNewBold', 'bold')
      doc.text(this.textHeaderReport, 170, 45);
      doc.text("จุดติดตั้ง " + this.textCheckPoint, 170, 90);
      doc.text("วัน/เดือน/ปี " + this.dateText, 170, 110);
      doc.setFontSize(24);
      doc.text("กองระบบเทคโนโลยีจราจร", 560, 50);
      doc.text("สำนักการจราจรและขนส่ง กรุงเทพมหานคร", 510, 75);
      const logo = require("@/assets/img/BMALogo3.jpg");

      var imgLogo = new Image();
      // var imgCheckPoint = new Image();
      imgLogo.src = logo;

      doc.addImage(imgLogo, "JPEG", 40, 20, 100, 100, undefined, 'FAST');



      doc.setFontSize(16);
      doc.text("ปริมาณจราจรในแต่ละวัน (ขาเข้า) (คัน)", 40, 145);
      doc.autoTable({
        html: '#mytableW1', startY: 150, styles: {
          font: "THSarabunNew", halign: 'center', overflow: 'linebreak',
          cellWidth: 'auto', fontSize: 10, textColor: '#000',
          cellPadding: 1
        }, theme: 'grid', headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1, },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      })

      doc.text("ปริมาณจราจรในแต่ละวัน (ขาออก) (คัน)", 40, 330);

      doc.autoTable({
        html: '#mytableW2', startY: 335, styles: {
          font: "THSarabunNew", halign: 'center', overflow: 'linebreak',
          cellWidth: 'auto', fontSize: 10, textColor: '#000',
          cellPadding: 1
        }, theme: 'grid', headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1, },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      })

      doc.save(`รายงานสัปดาห์.pdf`);
    },

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
