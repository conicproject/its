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
        <table id="mytableX_time">
          <tr>
            <th colspan="9" data-f-sz="25" data-a-h="right" data-f-bold="true">
              กองระบบเทคโนโลยีจราจร
            </th>
            <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">สำนักการจราจรและขนส่ง </th>
                      <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กรุงเทพมหานคร</th> -->
          </tr>
          <tr>
            <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กองระบบเทคโนโลยีจราจร </th> -->
            <th colspan="9" data-f-sz="25" data-a-h="right" data-f-bold="true">
              สำนักการจราจรและขนส่ง กรุงเทพมหานคร
            </th>
            <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กรุงเทพมหานคร</th> -->
          </tr>
          <tr></tr>
          <tr>
            <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กองระบบเทคโนโลยีจราจร </th> -->
            <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">สำนักการจราจรและขนส่ง </th> -->
            <th colspan="9" data-f-sz="25" data-a-h="left" data-f-bold="true">
              รายงานปริมาณจราจรแยกตามประเภทยานพาหนะ(ตามช่วงเวลา)
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
              วัน/เดือน/ปี {{ dateText }}
            </th>
          </tr>

          <tr></tr>
          <tr>
            <th data-f-sz="15">
              ปริมาณจราจรในแต่ละช่วงเวลา (ทิศทางการจราจรเข้าเมือง) (คัน)
            </th>
          </tr>
          <tr>
            <th data-f-sz="15" v-for="item in headerTable" :key="item.text">
              {{ item }}
            </th>
          </tr>
          <tr v-for="item in dataInbound" :key="item.type">
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">
              {{ item.type }}
            </td>
            <td
              v-if="item._0 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._0 }}
            </td>
            <td
              v-if="item._1 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._1 }}
            </td>
            <td
              v-if="item._2 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._2 }}
            </td>
            <td
              v-if="item._3 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._3 }}
            </td>
            <td
              v-if="item._4 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._4 }}
            </td>
            <td
              v-if="item._5 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._5 }}
            </td>
            <td
              v-if="item._6 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._6 }}
            </td>
            <td
              v-if="item._7 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._7 }}
            </td>
            <td
              v-if="item._8 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._8 }}
            </td>
            <td
              v-if="item._9 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._9 }}
            </td>
            <td
              v-if="item._10 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._10 }}
            </td>
            <td
              v-if="item._11 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._11 }}
            </td>
            <td
              v-if="item._12 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._12 }}
            </td>
            <td
              v-if="item._13 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._13 }}
            </td>
            <td
              v-if="item._14 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._14 }}
            </td>
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">
              {{ item.all }}
            </td>
            <td
              v-if="item.percent !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item.percent }}
            </td>
          </tr>
          <tr></tr>
          <tr></tr>
          <tr></tr>
          <tr>
            <th data-f-sz="15">
              ปริมาณจราจรในแต่ละช่วงเวลา (ทิศทางการจราจรออกเมือง) (คัน)
            </th>
          </tr>
          <tr>
            <th data-f-sz="15" v-for="item in headerTable" :key="item.text">
              {{ item }}
            </th>
          </tr>
          <tr v-for="item in dataOutbound" :key="item.id">
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">
              {{ item.type }}
            </td>
            <td
              v-if="item._0 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._0 }}
            </td>
            <td
              v-if="item._1 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._1 }}
            </td>
            <td
              v-if="item._2 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._2 }}
            </td>
            <td
              v-if="item._3 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._3 }}
            </td>
            <td
              v-if="item._4 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._4 }}
            </td>
            <td
              v-if="item._5 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._5 }}
            </td>
            <td
              v-if="item._6 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._6 }}
            </td>
            <td
              v-if="item._7 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._7 }}
            </td>
            <td
              v-if="item._8 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._8 }}
            </td>
            <td
              v-if="item._9 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._9 }}
            </td>
            <td
              v-if="item._10 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._10 }}
            </td>
            <td
              v-if="item._11 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._11 }}
            </td>
            <td
              v-if="item._12 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._12 }}
            </td>
            <td
              v-if="item._13 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._13 }}
            </td>
            <td
              v-if="item._14 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._14 }}
            </td>
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">
              {{ item.all }}
            </td>
            <td
              v-if="item.percent !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item.percent }}
            </td>
          </tr>
        </table>

        <table id="mytableT1">
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
            <td v-if="item._12 !== undefined">{{ item._12 }}</td>
            <td v-if="item._13 !== undefined">{{ item._13 }}</td>
            <td v-if="item._14 !== undefined">{{ item._14 }}</td>
            <td>{{ item.all }}</td>
            <td v-if="item.percent !== undefined">{{ item.percent }}</td>
          </tr>
        </table>

        <table id="mytableT2">
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
            <td v-if="item._12 !== undefined">{{ item._12 }}</td>
            <td v-if="item._13 !== undefined">{{ item._13 }}</td>
            <td v-if="item._14 !== undefined">{{ item._14 }}</td>
            <td>{{ item.all }}</td>
            <td v-if="item.percent !== undefined">{{ item.percent }}</td>
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
  props: [
    "downloadpdf",
    "downloadexcel",
    "dataInbound",
    "dataOutbound",
    "dateText",
    "nameCheckPoint",
    "headerTable",
    "textHeaderReport",
  ],
  components: {
    VueHtml2pdf,
    apexchart: VueApexCharts,
  },
  watch: {
    downloadpdf: function (newVal, oldVal) {
      // watch it
      this.genPDF();
      console.log(this.dataInbound);
    },
    downloadexcel: function (newVal, oldVal) {
      // watch it

      this.generateReport();
      this.genExcel();
    },
  },
  data() {
    return {
      dataInboundMock: [
        {
          type: "รถยนต์ส่วนบุคคล",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "รถจักรยานยนต์",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "รถโดยสาร",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "รถบรรทุก",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "รถบรรทุกขนาดเล็ก",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "รถตู้",

          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "รถสามล้อเครื่อง",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "รถ SUV",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "อื่นๆ",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "PCU",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "จำนวนรวมทั้งหมด",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
      ],
      dataOutboundMock: [
        {
          type: "รถยนต์ส่วนบุคคล",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "รถจักรยานยนต์",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "รถโดยสาร",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "รถบรรทุก",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "รถบรรทุกขนาดเล็ก",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "รถตู้",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "รถสามล้อเครื่อง",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "รถ SUV",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "อื่นๆ",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "PCU",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
        {
          type: "จำนวนรวมทั้งหมด",
          _0: "data",
          _1: "data",
          _2: "data",
          _3: "data",
          _4: "data",
          _5: "data",
          _6: "data",
          _7: "data",
          _8: "data",
          _9: "data",
          _10: "data",
          _11: "data",
          _12: "data",
          _13: "data",
          _14: "data",
          _15: "data",
          _16: "data",
          _17: "data",
          _18: "data",
          _19: "data",
          _20: "data",
          _21: "data",
          _22: "data",
          _23: "data",
          _24: "data",
          _25: "data",
          _26: "data",
          _27: "data",
          _28: "data",
          _29: "data",
          _30: "data",
          _31: "data",
          all: "data",
        },
      ],
      headerTableMock: [
        {
          text: "เวลา",
        },
        {
          text: "ว/ด/ป",
        },
        {
          text: "ว/ด/ป",
        },
        {
          text: "ว/ด/ป",
        },
        {
          text: "ว/ด/ป",
        },
        {
          text: "ว/ด/ป",
        },
        {
          text: "ว/ด/ป",
        },
        {
          text: "ว/ด/ป",
        },
        {
          text: "ปริมาณจราจร(คัน)",
        },
      ],

      textCheckPoint: "",
    };
  },
  methods: {
    genExcel() {
      TableToExcel.convert(document.getElementById("mytableX_time"), {
        name: "รายงานผลข้อมูลจราจรแยกตามประเภทยานพาหนะ(ตามช่วงเวลา).xlsx",
        sheet: {
          name: "Sheet 1",
        },
      });
    },
    generateReport() {
      this.$refs.html2Pdf.generatePdf();
    },

    genPDF() {
      let doc = new jsPDF({ orientation: "l", unit: "pt", compress: true });

      this.textCheckPoint = this.nameCheckPoint || "";
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
      doc.text("วัน/เดือน/ปี " + this.dateText, 170, 110);
      doc.setFontSize(24);
      doc.text("กองระบบเทคโนโลยีจราจร", 560, 50);
      doc.text("สำนักการจราจรและขนส่ง กรุงเทพมหานคร", 510, 75);
      const logo = require("@/assets/img/BMALogo3.jpg");

      var imgLogo = new Image();

      imgLogo.src = logo;

      doc.addImage(imgLogo, "JPEG", 40, 20, 100, 100, undefined, "FAST");

      doc.setFontSize(16);
      doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (ขาเข้า) (คัน)", 40, 145);

      doc.autoTable({
        html: "#mytableT1",
        startY: 150,
        styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 10,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: {
          fillColor: [255, 255, 255],
          lineColor: [0, 0, 0],
          textColor: [0, 0, 0],
          lineWidth: 1,
        },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });

      doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (ขาออก) (คัน)", 40, 345);
      doc.autoTable({
        html: "#mytableT2",
        startY: 350,
        styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 10,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: {
          fillColor: [255, 255, 255],
          lineColor: [0, 0, 0],
          textColor: [0, 0, 0],
          lineWidth: 1,
        },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });

      doc.save(`รายงานตามช่วงเวลา.pdf`);
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
