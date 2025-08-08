<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="onProgress">
      <v-progress-circular
        indeterminate
        size="100"
        width="7"
      ></v-progress-circular>
    </v-overlay>
    <v-content class="pl-3">
      <v-container class="pl-1 pr-1">
        <v-chip
          @click="gobackpage()"
          large
          class="ma-2 pl-0"
          color="transparent"
        >
          <v-icon large color="red">mdi-chevron-left</v-icon>
          <span class="text-left headerback">Back</span>
        </v-chip>
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">รายงานผลข้อมูลจราจร</span>
        </v-chip>
        <v-container>
          <div v-if="$vuetify.breakpoint.width > 1350">
          <v-layout  v-if="
                $route.query.type === 'week' || $route.query.type === 'range'
              " class="pb-3">
              <v-flex lg4>
              <v-card class="elevation-0 pa-3 ml-1" id="border">{{
                dateReport
              }}</v-card>
            </v-flex>
              </v-layout>
          <v-layout  class="pb-3">
            <v-flex lg2 v-if="$route.query.type !== 'week' && $route.query.type !== 'range'">
              <v-card class="elevation-0 pa-3" id="border">{{
                dateReport
              }}</v-card>
            </v-flex>
            <v-flex class="pl-1">
              <v-card class="elevation-0 pa-3" id="border">{{
                headerReport
              }}</v-card>
            </v-flex>
            <v-flex class="pl-1"
              ><v-select
                class="elevation-0"
                @change="changeCheckPoint()"
                :items="itemCheckPoint"
                v-model="checkSelect"
                item-value="id"
                item-text="name"
                flat
                solo
                hide-details
                placeholder="เลือกจุดติดตั้ง"
              ></v-select
            ></v-flex>
            <v-flex class="text-right"
              ><v-chip large id="chip"
                ><span class="pl-5 pr-5 chip-text">{{
                  textReport
                }}</span></v-chip
              ></v-flex
            >
          </v-layout>
            </div>
            <div  v-else-if="
            $vuetify.breakpoint.width > 700 && $vuetify.breakpoint.width < 1350
          ">
            <v-layout class="pb-3">
            <v-flex
              
              v-if="
                $route.query.type === 'week' || $route.query.type === 'range'
              "
            >
              <v-card class="elevation-0 pa-3" id="border">{{
                dateReport
              }}</v-card>
            </v-flex>
            <v-flex  v-else>
              <v-card class="elevation-0 pa-3" id="border">{{
                dateReport
              }}</v-card>
            </v-flex>
            <v-flex class="pl-1">
              <v-card class="elevation-0 pa-3" id="border">{{
                headerReport
              }}</v-card>
            </v-flex>
            </v-layout >
            <v-layout class="pb-3">
            <v-flex  class="pl-1"
              ><v-select
                class="elevation-0"
                @change="changeCheckPoint()"
                :items="itemCheckPoint"
                v-model="checkSelect"
                item-value="id"
                item-text="name"
                flat
                solo
                hide-details
                placeholder="เลือกจุดติดตั้ง"
              ></v-select
            ></v-flex>
            <v-flex class="text-right"
              ><v-chip large id="chip"
                ><span class="pl-5 pr-5 chip-text">{{
                  textReport
                }}</span></v-chip
              ></v-flex
            >
            </v-layout>
            </div>
          <div v-else>
            <v-layout class="pb-3">
            <v-flex
              v-if="
                $route.query.type === 'week' || $route.query.type === 'range'
              "
            >
              <v-card class="elevation-0 pa-3" id="border">{{
                dateReport
              }}</v-card>
            </v-flex>
            <v-flex v-else>
              <v-card class="elevation-0 pa-3" id="border">{{
                dateReport
              }}</v-card>
            </v-flex>
          </v-layout>
          <v-layout class="pb-3">
            <v-flex class="pl-1">
              <v-card class="elevation-0 pa-3" id="border">{{
                headerReport
              }}</v-card>
            </v-flex>
          </v-layout>
          <v-layout>
            <v-flex class="pl-1"
              ><v-select
                class="elevation-0"
                @change="changeCheckPoint()"
                :items="itemCheckPoint"
                v-model="checkSelect"
                item-value="id"
                item-text="name"
                flat
                solo
                hide-details
                placeholder="เลือกจุดติดตั้ง"
              ></v-select
            ></v-flex>
          </v-layout>
          <v-layout>
            <v-flex class="text-right pt-3 pb-3"
              ><v-chip large id="chip"
                ><span class="pl-5 pr-5 chip-text">{{
                  textReport
                }}</span></v-chip
              ></v-flex
            >
          </v-layout>
          </div>
          <v-layout>
            <v-flex lg6 md12 sm12 xs12 class="mb-3">
              <v-card class="elevation-0" id="border" height="100%">
                <donutchart
                  v-if="headerDonutChart == 'all'"
                  :dataChart="dataDonut"
                  :height="donutHeight"
                  :headerShow="headerDonutChart"
                ></donutchart>
                <div v-else class="textdonut">
                  <span
                    >ประเภทยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด</span
                  >
                  <div id="chartdiv"></div>
                </div>
              </v-card>
            </v-flex>
            <v-flex lg6 md6 sm6 xs6 class="pl-3" v-if="$vuetify.breakpoint.width > 1263">
              <v-container class="pr-0" height="100%">
                <traffic
                  height="100%"
                  :directionData="direction"
                  :dataText="dataText"
                ></traffic>
              </v-container>
              <v-container class="pr-0" height="100%">
                <vehicle
                  class="pt-2 mb-5"
                  height="100%"
                  :vehicle="car_type"
                  :dataText="dataText"
                ></vehicle>
                 <span class="note-text" v-if="dataText.keyCard == 'violate'"
                >หมายเหตุ : จำนวนคันและจำนวน %
                ของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกดในแต่ละประเภท</span
              >
                <!-- <span v-if="dataText.keyCard == 'violate'" class="note-text">หมายเหตุ : จำนวนคันและจำนวน % ของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกดในแต่ละประเภท</span> -->
              </v-container>
            </v-flex>
          </v-layout>
         
         <div v-if="
            $vuetify.breakpoint.width > 700 && $vuetify.breakpoint.width < 1264
          ">
           
            <traffic
            class="pt-3"
            :directionData="direction"
            :dataText="dataText"
          ></traffic>
          <br />
        
          <v-layout class="pb-3">
            <v-flex class="pt-3 mb-3"><vehicle
              :vehicle="car_type"
              :dataText="dataText"
            ></vehicle></v-flex>
          </v-layout>
          <span class="note-text" v-if="dataText.keyCard == 'violate'"
                >หมายเหตุ : จำนวนคันและจำนวน %
                ของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกดในแต่ละประเภท</span
              >
         </div>
          
          <div  v-if="
            $vuetify.breakpoint.width < 700
          ">
             <v-layout class="pt-3">
            <v-flex>
              <traffic
                class="pt-3"
                :directionData="direction"
                :dataText="dataText"
              ></traffic>
              <br />
              <vehicle
                class="pt-3 mb-3"
                :vehicle="car_type"
                :dataText="dataText"
              ></vehicle>
               <span class="note-text" v-if="dataText.keyCard == 'violate'"
                >หมายเหตุ : จำนวนคันและจำนวน %
                ของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกดในแต่ละประเภท</span
              >
              <!-- <span v-if="dataText.keyCard == 'violate'" class="note-text">หมายเหตุ : จำนวนคันและจำนวน % ของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกดในแต่ละประเภท</span> -->
            </v-flex>
          </v-layout>
          </div>

         
          <v-layout >
            <v-flex lg12>
              <v-card class="elevation-0" id="border">
                <barchart
                  :cat="cat"
                  :dataIn="dataIn"
                  :dataOut="dataOut"
                  checkPage="traffic"
                  :typeText="selectDataBarChart"
                  :options="barOption"
                  :series="barSeries"
                  @color="changecolorChart"
                ></barchart>
              </v-card>
            </v-flex>
          </v-layout>
          <v-layout class="pt-4">
            <v-flex>
              <exportfile
                class="pt-4"
                :keypage="keypage"
                @download="exportPDF"
                :title="titletext"
                :header="header"
                @downloadEx="genEX"
              ></exportfile>
            </v-flex>
          </v-layout>
        </v-container>

      </v-container>
    </v-content>
    <datepdf
      :downloadpdf="downloadpdfD"
      :downloadexcel="downloadexcelD"
      :dataInbound="dataInbound"
      :dataOutbound="dataOutbound"
      :dateText="dateReport"
      :nameCheckPoint="nameCheckPoint"
      :textHeaderReport="textHeaderReport"
      :dataKey="dataText"
    ></datepdf>
    <weekpdf
      :downloadpdf="downloadpdfW"
      :downloadexcel="downloadexcelW"
      :dataInbound="dataInbound"
      :dataOutbound="dataOutbound"
      :dateText="dateReport"
      :nameCheckPoint="nameCheckPoint"
      :textHeaderReport="textHeaderReport"
      :headerTable="headerTable"
      :dataKey="dataText"
    ></weekpdf>
    <monthpdf
      :downloadpdf="downloadpdfM"
      :downloadexcel="downloadexcelM"
      :dataInbound="dataInbound"
      :dataOutbound="dataOutbound"
      :headerTable="headerTable"
      :dateText="dateReport"
      :nameCheckPoint="nameCheckPoint"
      :checkMonth="checkMonthReport"
      :textHeaderReport="textHeaderReport"
      :dataKey="dataText"
    ></monthpdf>
    <yearpdf
      :downloadpdf="downloadpdfY"
      :downloadexcel="downloadexcelY"
      :dataInbound="dataInbound"
      :dataOutbound="dataOutbound"
      :dateText="dateReport"
      :nameCheckPoint="nameCheckPoint"
      :headerTable="headerTable"
      :textHeaderReport="textHeaderReport"
      :dataKey="dataText"
    ></yearpdf>
    <timepdf
      :downloadpdf="downloadpdfT"
      :downloadexcel="downloadexcelT"
      :dataInbound="dataInbound"
      :dataOutbound="dataOutbound"
      :dateText="dateReport"
      :nameCheckPoint="nameCheckPoint"
      :headerTable="headerTable"
      :textHeaderReport="textHeaderReport"
      :dataKey="dataText"
    ></timepdf>
  </v-app>
</template>
<script>
const baseUrl = require("../../baseUrl.json");
import sidebar from "../components/sidebar-new.vue";
import vehicle from "../components/type-vehicle.vue";
import traffic from "../components/all-traffic.vue";
import barchart from "../charts/bar-linechart.vue";
import donutchart from "../charts/donutchart.vue";
import exportfile from "../components/export-file.vue";
import headerbar from "../components/header-bar.vue";
import datepdf from "../formatExport/trafficDatePDF.vue";
import weekpdf from "../formatExport/trafficWeekPDF.vue";
import monthpdf from "../formatExport/trafficMonthPDF.vue";
import yearpdf from "../formatExport/trafficYearPDF.vue";
import timepdf from "../formatExport/trafficTimePDF.vue";
import * as am5 from "@amcharts/amcharts5";
import * as am5xy from "@amcharts/amcharts5/xy";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import * as am5percent from "@amcharts/amcharts5/percent";
//import { jsPDF } from "jspdf";
//import * as jsPDF from 'jspdf'
//import * as autoTable from 'jspdf-autotable'
import "jspdf-autotable";
import Swal from "sweetalert2/dist/sweetalert2.js";
const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});

export default {
  components: {
    sidebar,
    barchart,
    donutchart,
    vehicle,
    traffic,
    exportfile,
    headerbar,
    datepdf,
    weekpdf,
    monthpdf,
    yearpdf,
    timepdf,
  },
  data() {
    return {
      selectDataBarChart: "",
      headerDonutChart: "",
      headerReport: "",
      textHeaderReport: "",
      dataText: {
        keyCard: "violate",
        allText:
          "ปริมาณยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด ทั้งหมด",
      },
      nameCheckPoint: "",
      dataOutbound: [],
      dataInbound: [],
      checkSelect: "34",
      itemCheckPoint: [
        {
          id: "1",
          name: "ถนนอ่อนนุช (ซอยสุขุมวิท 77) บริเวณปากซอยอ่อนนุช 3\n",
          short_name: "ถ.อ่อนนุช สุขุมวิท77\n",
          is_active: true,
          path: "/installing/1",
          is_checkpoint: true,
          child_obj: [],
        },
        {
          id: "2",
          name: "ถนนอ่อนนุช บริเวณแยกอ่อนนุช\n",
          short_name: "ถ.อ่อนนุช แยกอ่อนนุช\n",
          is_active: true,
          path: "/installing/2",
          is_checkpoint: true,
          child_obj: [],
        },
        {
          id: "3",
          name: "ถนนอ่อนนุช (ซอยสุขุมวิท 48) บริเวณหน้าโรงแรมไอบิส\n",
          short_name: "ถ.อ่อนนุช สุขุมวิท48\n",
          is_active: true,
          path: "/installing/3",
          is_checkpoint: true,
          child_obj: [],
        },
        {
          id: "4",
          name: "แยกราชประสงค์ เซ็นทรัลเวิลด์\n",
          short_name: "แยกราชประสงค์ CTW\n",
          is_active: true,
          path: "/installing/4",
          is_checkpoint: true,
          child_obj: [],
        },
      ],
      dateReport: "",
      textReport: "",
      cat: [],
      dataIn: [],
      dataOut: [],
      car_type: {},
      direction: [],
      dataDonut: {},
      titletext: "ปริมาณจราจรรายวัน",
      header: "ปริมาณจราจรรายวัน (ทิศทางการจราจรเข้าเมือง) (คัน)",
      downloadsuccess: false,
      onProgress: false,
      downloadpdfD: false,
      downloadpdfW: false,
      downloadpdfM: false,
      downloadpdfY: false,
      downloadpdfT: false,
      downloadexcelD: false,
      downloadexcelW: false,
      downloadexcelM: false,
      downloadexcelY: false,
      downloadexcelT: false,
      keypage: "allsensor",
      drawer: true,
      donutHeight: 300,
      donutHeightMd: 250,
      exportF: [
        {
          i: 1,
          name: "save as..",
        },
        {
          i: 2,
          name: "Export PDF",
        },
        {
          i: 3,
          name: "Export Excel",
        },
      ],
      imgURL: "",
      dataDate: [],
      headerTable: [],
      checkMonthReport: 0,
      barOption: "",
      barSeries: "",
      color: ["#FF9800", "#03A9F4"],
      stack: true,
      chartDiv:null,
      chartNest:null
    };
  },
  computed: {
    getDate: function () {
      const d = new Date();
      const monthNames = [
        "มกราคม",
        "กุมภาพันธ์",
        "มีนาคม",
        "เมษายน",
        "พฤษภาคม",
        "มิถุนายน",
        "กรกฎาคม",
        "สิงหาคม",
        "กันยายน",
        "ตุลาคม",
        "พฤศจิกายน",
        "ธันวาคม",
      ];
      const month = d.getMonth();
      const date = `${d.getDate()}   ${monthNames[month]} ${d.getFullYear()}`;
      // const time = new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().substr(11,5);
      return { date };
    },
  },
  created() {
    //this.getData();
  },
  methods: {
    createNestChart(){
      this.chartDiv = am5.Root.new("chartdiv");

      this.chartDiv.setThemes([am5themes_Animated.new(this.chartDiv)]);

      var chart = this.chartDiv.container.children.push(
        am5percent.PieChart.new(this.chartDiv, {
          radius: am5.percent(80),
          innerRadius: am5.percent(0.1),
          layout: this.chartDiv.verticalLayout
        })
      );

      this.chartNest = chart
    },
    changecolorChart(param) {
      this.color = param;
      this.options();
    },
    setNestChart(cartype,pieInside) {

      var root = am5.Root.new("chartdiv");

      root.setThemes([am5themes_Animated.new(root)]);
      
      var chart = root.container.children.push(
        am5percent.PieChart.new(root, {
          radius: am5.percent(80),
          innerRadius: am5.percent(0.1),
          layout: root.verticalLayout
        })
      );

      // Create series
      var series = chart.series.push(
        am5percent.PieSeries.new(root, {
          name: "Series",
          valueField: "volume",
          categoryField: "dataType",
        })
      );
      series
        .get("colors")
        .set("colors", [am5.color(0x0ff000), am5.color(0xf0000f)]);
      series.data.setAll([
        {
          dataType: "ปริมาณจราจรทั้งหมด",
          volume: pieInside.normal,
        },
        {
          dataType: "ปริมาณรถที่ฝ่าฝืนสัญญาไฟ",
          volume: pieInside.violation,
        },
      ]);

      // Configuring slices
      series.slices.template.setAll({
        stroke: am5.color(0xffffff),
        strokeWidth: 2,
      });

      // Disabling labels and ticks
      series.labels.template.set("visible", false);
      series.ticks.template.set("visible", false);

      legend = chart.children.push(am5.Legend.new(root, {
        x: am5.percent(50),
        centerX: am5.percent(50),
         scale:0.75,
      }));

      legend.data.setAll(series.dataItems);
      
      var series2 = chart.series.push(
        am5percent.PieSeries.new(root, {
          name: "Series",
          valueField: "volume",
          categoryField: "car_type",
          alignLabels: false,
        })
      );

      series2.get("colors")
        .set("colors", [
          am5.color(0x1aa478),
          am5.color(0xf79e69),
          am5.color(0x8582f2),
          am5.color(0x866846),
          am5.color(0x96e637),
          am5.color(0xf9429e),
          am5.color(0xf1cbff),
          am5.color(0x3e1379),
          am5.color(0x9a1b5b),
          am5.color(0x3364ce),
        ]);

       let test =  [    
      {
        country: "รถจักรยานยนต์",
        sales: 60000,
      },
      {
        country: "รถบรรทุก",
        sales: 60000,
      },
      {
        country: "รถยนต์ส่วนบุคคล",
        sales: 120000,
      },
      {
        country: "รถโดยสาร",
        sales: 90000,
      },
       {
        country: "รถบรรทุกขนาดเล็ก",
        sales: 60000,
      },
      {
        country: "รถตู้",
        sales: 60000,
      },
      {
        country: "รถ SUV",
        sales: 120000,
      },
      {
        country: "รถสามล้อเครื่อง",
        sales: 90000,
      },
    ]
     
      series2.data.setAll(cartype);

      // Configuring slices
      series2.slices.template.setAll({
        stroke: am5.color(0xffffff),
        strokeWidth: 2,
      });

       series2.labels.template.set("visible", false);
       series2.ticks.template.set("visible", false);
        var legend = chart.children.push(am5.Legend.new(root, {
          centerX: am5.percent(50),
          x: am5.percent(50),
          scale:0.75,
          layout: am5.GridLayout.new(root, {
            maxColumns: 3,
            fixedWidthGrid: true
          })
        }));

        legend.data.setAll(series2.dataItems);
      // series2.labels.template.setAll({
      //   fontSize: 9,
      //   text: "{category}",
      //   textType: "circular",
      //   radius: 10,
      //   location:0

        
      // });

      // this.chartNest = chart;
    },
    options(color) {
      let option = {
        dataLabels: {
          enabled: false,
        },
        colors: color,
        chart: {
          type: "bar",
          stacked: this.stack,
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
            borderRadius: 1,
          },
        },
        xaxis: {
          labels: {
            show: false,
          },
          type: "category",
          categories: this.cat,
          
        },
        legend: {
          position: "right",
          offsetY: 40,
        },
        fill: {
          opacity: 1,
        },
      };
      this.barOption = option;
    },
    series() {
      let series = [
        {
          name: "ขาเข้าเมือง",
          data: this.dataIn,
          // data: [44, 55, 41, 67, 22, 43, 12, 65, 12, 23, 21, 11,44, 55, 41, 67, 22, 43, 12, 65, 12, 23, 21, 11],
        },
        {
          name: "ขาออกเมือง",
          data: this.dataOut,
          //  data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14,44, 55, 41, 67, 22, 43, 12, 65, 12, 23, 21, 11],
        },
      ];
      this.barSeries = series;
    },
    reload() {
      this.$router.go();
    },
    headerbar(drawer) {
      this.drawer = drawer;
    },
    gobackpage() {
      // console.log("this.$route.params",this.dataSearch);
      //let params = this.dataSearch
      this.$router.push({ path: "/traffic-detail" });
    },
    exportPDF() {
      const data = this.$route.query;
      data.type === "day"
        ? (this.downloadpdfD = !this.downloadpdfD)
        : data.type === "week"
        ? (this.downloadpdfW = !this.downloadpdfW)
        : data.type === "month"
        ? (this.downloadpdfM = !this.downloadpdfM)
        : data.type === "year"
        ? (this.downloadpdfY = !this.downloadpdfY)
        : (this.downloadpdfT = !this.downloadpdfT);
    },
    genEX() {
      // console.log("genEX");
      // this.downloadexcel = !this.downloadexcel;
      const data = this.$route.query;
      data.type === "day"
        ? (this.downloadexcelD = !this.downloadexcelD)
        : data.type === "week"
        ? (this.downloadexcelW = !this.downloadexcelW)
        : data.type === "month"
        ? (this.downloadexcelM = !this.downloadexcelM)
        : data.type === "year"
        ? (this.downloadexcelY = !this.downloadexcelY)
        : (this.downloadexcelT = !this.downloadexcelT);
    },
    changeCheckPoint() {
      const data = this.$route.query;
      // console.log(data);
      let param = {
        type: data.type,
        date: data.date,
        checkpoint: this.checkSelect,
        typeData: data.typeData
      };
      this.$router.push({ path: "/traffic-report", query: param });
      // this.getData();
      //this.reload();
      location.reload();
    },
    getDataCheckPoint() {
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/checkpoints";
      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {
          if (response.status === 200) {
            this.itemCheckPoint = response.data.data;

            const data = this.$route.query;
            for (let i = 0; i < this.itemCheckPoint.length; i++) {
              if (data.checkpoint === this.itemCheckPoint[i]["id"]) {
                this.nameCheckPoint = this.itemCheckPoint[i]["name"];
              }
            }
          }
        });
    },
    setNameCheckPoint(data) {
      for (let i = 0; i < this.itemCheckPoint.length; i++) {
        if (data.checkpoint === this.itemCheckPoint[i]["id"]) {
          return this.itemCheckPoint[i]["name"];
        }
      }
    },
    getData() {
      this.onProgress = true;
      const data = this.$route.query;
      // console.log(data);
      data.type === "day"
        ? (this.textReport = "ข้อมูลรายวัน")
        : data.type === "week"
        ? (this.textReport = "ข้อมูลรายสัปดาห์")
        : data.type === "month"
        ? (this.textReport = "ข้อมูลรายเดือน")
        : data.type === "year"
        ? (this.textReport = "ข้อมูลรายปี")
        : (this.textReport = "ข้อมูลรายช่วงเวลา");
      this.setDateReport(data);
      this.dateTextReport = data.date;
      this.headerDonutChart = data.typeData == "0" ? "all" : "violate";
      this.headerReport =
        data.typeData == "0"
          ? "ข้อมูลจราจร"
          : "ข้อมูลยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด";
      this.dataText =
        data.typeData == "0"
          ? { keyCard: "all", allText: "ปริมาณจราจรทั้งหมด" }
          : {
              keyCard: "violate",
              allText:
                "ปริมาณยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด ทั้งหมด",
            };
      this.selectDataBarChart =
        data.typeData == "0"
          ? "ปริมาณจราจรขาเข้าเมืองและขาออกเมือง (คัน)"
          : "จำนวนยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด ขาเข้าและขาออกเมือง(คัน)";
      const type = data.type;
      if (this.$route.query.type == "day") {
        this.textHeaderReport =
          data.typeData == "0"
            ? "รายงานข้อมูลปริมาณจราจรรายวัน"
            : "รายงานข้อมูลปริมาณจราจรรายวัน\nของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด";
      } else if (this.$route.query.type == "week") {
        this.textHeaderReport =
          data.typeData == "0"
            ? "รายงานข้อมูลปริมาณจราจรรายสัปดาห์"
            : "รายงานข้อมูลปริมาณจราจรรายสัปดาห์\nของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด";
      } else if (this.$route.query.type == "month") {
        this.textHeaderReport =
          data.typeData == "0"
            ? "รายงานข้อมูลปริมาณจราจรรายเดือน"
            : "รายงานข้อมูลปริมาณจราจรรายเดือน\nของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด";
      } else if (this.$route.query.type == "year") {
        this.textHeaderReport =
          data.typeData == "0"
            ? "รายงานข้อมูลปริมาณจราจรรายปี"
            : "รายงานข้อมูลปริมาณจราจรรายปี\nของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด";
      } else {
        this.textHeaderReport =
          data.typeData == "0"
            ? "รายงานข้อมูลปริมาณจราจรตามช่วงเวลา"
            : "รายงานข้อมูลปริมาณจราจรตามช่วงเวลา\nของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด";
      }
      let session_data = localStorage.getItem("session");
      let url =
        baseUrl.ipServer +
        "/traffic-detail/" +
        data.typeData +
        "?type=" +
        data.type +
        "&date=" +
        data.date +
        "&checkpoint=" +
        data.checkpoint;
      this.axios
        .get(url, {
          headers: { session: session_data },
        })
        .then((response) => {
          if (response.status === 200) {
            // this.dataIn = [];
            // this.cat = [];
            // this.dataOut = [];

            this.checkSelect = response.data.checkpoint.id;
            this.car_type = response.data.car_type;
            this.dataDonut = this.setDonutChart(response.data.car_type);
            this.direction = response.data.direction;
            
            //* set nest donut chart/
            if (data.typeData == "1") {
              this.setNestChart(response.data.car_type.volume,response.data.graph_inside);
            }

            for (let i = 0; i < response.data.graph.inbound.length; i++) {
              this.dataIn.push(response.data.graph.inbound[i].volume);
              this.cat.push(response.data.graph.inbound[i].time ||
                  response.data.graph.inbound[i].date ||
                  response.data.graph.inbound[i].month
              );
              this.dataOut.push(response.data.graph.outbound[i].volume);
            }
            this.setFormatReport(response.data.report, type,data.typeData);
            //set bar  data chart
            let color =  data.typeData == "0" ? ["#FF9800", "#03A9F4"] :["#F44336", "#3F51B5"]
            this.options(color);
            this.series();
            this.onProgress = false;
          }else {
            this.onProgress = false;
            //this.$router.push("/error");
            Toast.fire({
              icon: "error",
              title: response.data.message,
            });
          }
        })
        .catch((error) => {
          // console.log(error);
          this.onProgress = false;
        //   if(error.response.data.message === 'session timeout'){
        //     this.$store.dispatch("logout");
        //     this.$router.push('/')
        //      Toast.fire({
        //       icon: "error",
        //       title: error.response.data.message,
        //     });

        //     return;
        // }
          Toast.fire({
            icon: "error",
            title: "Cannot connet API",
          });
        });
    },
    setFormatReport(param, type,data_type) {
      this.dataInbound = [];
      this.dataOutbound = [];
      const carTypeHeader = [
        "รถยนต์ส่วนบุคคล",
        "รถจักรยานยนต์",
        "รถโดยสาร",
        "รถบรรทุก",
        "รถตู้",
        "รถสามล้อเครื่อง",
        "รถ SUV",
        "อื่นๆ",
        "pcu",
        "total",
      ];

      if (type == "day") {
        var type_key = "time";
      } else if (type == "week" || type == "range" || type == "month") {
        var type_key = "date";
      } else if (type == "year") {
        var type_key = "month";
      }

      const ReportDataExtractTime = param.inbound[carTypeHeader[0]]["data"];

      let header = {};
      let formatDate;
      for (let i = 0; i < ReportDataExtractTime.length; i++) {
        
        if (type_key == "month") {
          formatDate = this.settextMonth(ReportDataExtractTime[i][type_key]);
        }else if(type == "week" || type == "range"){
          //formatDate = ReportDataExtractTime[i][type_key].replace(/-/g, "/");
          formatDate = ReportDataExtractTime[i][type_key].split("T")[0].replace(/-/g, "/");
        }else if(type == "month"){
          formatDate = ReportDataExtractTime[i][type_key].split("T")[0].split("-")[2]
        }else {
          formatDate = ReportDataExtractTime[i][type_key].replace(/-/g, "/");
        }
        header["text"] = formatDate;
        this.headerTable.push(formatDate);
      }

      this.headerTable = ["เวลา"].concat(this.headerTable);
      this.headerTable.push("ปริมาณจราจร(คัน)");
      if(data_type !== "0"){
         this.headerTable.push("เทียบกับปริมาณจราจรทั้งหมด(%)");
      }
 

      var count1 = 0;
      for (const carType of carTypeHeader) {
        const data = param.inbound[carType]["data"];
        const total = param.inbound[carType]["total"];
        
        
        let extract_data = {};
        extract_data["type"] = carType;
        for (let i = 0; i < data.length; i++) {
          extract_data["_" + i] = data[i]["volume"];  
        }
        extract_data["all"] = total;   
        extract_data["id"] = count1++;
        if(param.inbound[carType]["percent"] !== undefined){       
          extract_data["percent"] = param.inbound[carType]["percent"].toFixed(2) 
        }
        this.dataInbound.push(extract_data);
      }
      var count2 = 0;
      for (const carType of carTypeHeader) {
        const data = param.outbound[carType]["data"];
        const total = param.outbound[carType]["total"];

        let extract_data = {};
        extract_data["type"] = carType;
        extract_data["id"] = count2++;
        for (let i = 0; i < data.length; i++) {
          extract_data["_" + i] = data[i]["volume"];
        }
        extract_data["all"] = total;
        if(param.outbound[carType]["percent"] !== undefined){
          extract_data["percent"] = param.outbound[carType]["percent"].toFixed(2) 
        }
        this.dataOutbound.push(extract_data);
      }
      
    },
    settextMonth(param) {
      let month =
        param == 1
          ? "ม.ค."
          : param == 2
          ? "ก.พ."
          : param == 3
          ? "มี.ค."
          : param == 4
          ? "เม.ษ."
          : param == 5
          ? "พ.ค."
          : param == 6
          ? "มิ.ย."
          : param == 7
          ? "ก.ค."
          : param == 8
          ? "ส.ค."
          : param == 9
          ? "ก.ย."
          : param == 10
          ? "ต.ค."
          : param == 11
          ? "พ.ย."
          : "ธ.ค.";

      return month;
    },
    setDateReport(param) {
      let monthNames = [
        "มกราคม",
        "กุมภาพันธ์",
        "มีนาคม",
        "เมษายน",
        "พฤษภาคม",
        "มิถุนายน",
        "กรกฎาคม",
        "สิงหาคม",
        "กันยายน",
        "ตุลาคม",
        "พฤศจิกายน",
        "ธันวาคม",
      ];

      if (param.type === "day") {
        let date = param.date.split("-") || [];
        let month =
          date[1] === "01"
            ? monthNames[0]
            : date[1] === "02"
            ? monthNames[1]
            : date[1] === "03"
            ? monthNames[2]
            : date[1] === "04"
            ? monthNames[3]
            : date[1] === "05"
            ? monthNames[4]
            : date[1] === "06"
            ? monthNames[5]
            : date[1] === "07"
            ? monthNames[6]
            : date[1] === "08"
            ? monthNames[7]
            : date[1] === "09"
            ? monthNames[8]
            : date[1] === "10"
            ? monthNames[9]
            : date[1] === "11"
            ? monthNames[10]
            : date[1] === "12"
            ? monthNames[11]
            : "";
        let year = parseInt(date[0]) + 543;
        this.dateReport = `${date[2]} ${month} ${year.toString()}`;
      } else if (param.type === "week") {
        var endDate = new Date(param.date);
        let date1 = param.date.split("-") || [];
        let year1 = parseInt(date1[0]) + 543;
        let month1 = date1[1] === "01"
            ? monthNames[0]
            : date1[1] === "02"
            ? monthNames[1]
            : date1[1] === "03"
            ? monthNames[2]
            : date1[1] === "04"
            ? monthNames[3]
            : date1[1] === "05"
            ? monthNames[4]
            : date1[1] === "06"
            ? monthNames[5]
            : date1[1] === "07"
            ? monthNames[6]
            : date1[1] === "08"
            ? monthNames[7]
            : date1[1] === "09"
            ? monthNames[8]
            : date1[1] === "10"
            ? monthNames[9]
            : date1[1] === "11"
            ? monthNames[10]
            : date1[1] === "12"
            ? monthNames[11]
            : "";
        endDate.setDate(endDate.getDate() + 6);
        let week2 = endDate.toISOString().substr(0, 10);
        let date2 = week2.split("-");
        let year2 = parseInt(date2[0]) + 543;
        let month2= date2[1] === "01"
            ? monthNames[0]
            : date2[1] === "02"
            ? monthNames[1]
            : date2[1] === "03"
            ? monthNames[2]
            : date2[1] === "04"
            ? monthNames[3]
            : date2[1] === "05"
            ? monthNames[4]
            : date2[1] === "06"
            ? monthNames[5]
            : date2[1] === "07"
            ? monthNames[6]
            : date2[1] === "08"
            ? monthNames[7]
            : date2[1] === "09"
            ? monthNames[8]
            : date2[1] === "10"
            ? monthNames[9]
            : date2[1] === "11"
            ? monthNames[10]
            : date2[1] === "12"
            ? monthNames[11]
            : "";
        this.dateReport =
          date1[2] +
          " " +
          month1 +
          " " +
          year1.toString() +
          " ~ " +
          date2[2] +
          " " +
          month2 +
          " " +
          year2.toString();
      } else if (param.type === "month") {
        let date = param.date.split("-") || [];
        let month =
          date[1] === "01"
            ? monthNames[0]
            : date[1] === "02"
            ? monthNames[1]
            : date[1] === "03"
            ? monthNames[2]
            : date[1] === "04"
            ? monthNames[3]
            : date[1] === "05"
            ? monthNames[4]
            : date[1] === "06"
            ? monthNames[5]
            : date[1] === "07"
            ? monthNames[6]
            : date[1] === "08"
            ? monthNames[7]
            : date[1] === "09"
            ? monthNames[8]
            : date[1] === "10"
            ? monthNames[9]
            : date[1] === "11"
            ? monthNames[10]
            : date[1] === "12"
            ? monthNames[11]
            : "";
        let year = parseInt(date[0]) + 543;
        this.dateReport = `${month} ${year.toString()}`;
        this.checkMonthReport =
          date[1] == "02"
            ? 2
            : date[1] == "04" ||
              date[1] == "06" ||
              date[1] == "09" ||
              date[1] == "11"
            ? 1
            : 0;
      } else if (param.type === "range") {
        let date = param.date.split(",") || [];

        let date1 = date[0].split("-") || [];
        let year1 = parseInt(date1[0]) + 543;
        let month1 = date1[1] === "01"
            ? monthNames[0]
            : date1[1] === "02"
            ? monthNames[1]
            : date1[1] === "03"
            ? monthNames[2]
            : date1[1] === "04"
            ? monthNames[3]
            : date1[1] === "05"
            ? monthNames[4]
            : date1[1] === "06"
            ? monthNames[5]
            : date1[1] === "07"
            ? monthNames[6]
            : date1[1] === "08"
            ? monthNames[7]
            : date1[1] === "09"
            ? monthNames[8]
            : date1[1] === "10"
            ? monthNames[9]
            : date1[1] === "11"
            ? monthNames[10]
            : date1[1] === "12"
            ? monthNames[11]
            : "";
        let date2 = date[1].split("-");
        let year2 = parseInt(date2[0]) + 543;
        let month2= date2[1] === "01"
            ? monthNames[0]
            : date2[1] === "02"
            ? monthNames[1]
            : date2[1] === "03"
            ? monthNames[2]
            : date2[1] === "04"
            ? monthNames[3]
            : date2[1] === "05"
            ? monthNames[4]
            : date2[1] === "06"
            ? monthNames[5]
            : date2[1] === "07"
            ? monthNames[6]
            : date2[1] === "08"
            ? monthNames[7]
            : date2[1] === "09"
            ? monthNames[8]
            : date2[1] === "10"
            ? monthNames[9]
            : date2[1] === "11"
            ? monthNames[10]
            : date2[1] === "12"
            ? monthNames[11]
            : "";
        this.dateReport =
          date1[2] +
          " " +
          month1 +
          " " +
          year1.toString() +
          " ~ " +
          date2[2] +
          " " +
          month2 +
          " " +
          year2.toString();
      } else {
        let year = parseInt(param.date) + 543;
        this.dateReport = year;
      }
    },
    setDonutChart(param) {
      let label = [];
      let series = [];
      for (let i = 0; i < param.volume.length; i++) {
        label.push(param.volume[i].car_type);
        series.push(param.volume[i].volume);
      }

      let options = {
        labels: label,
        total: {
          show: true,
        },
        colors: ['#1aa478', '#f79e69', '#8582f2', '#866846', '#96e637','#f9429e','#f1cbff','#3e1379','#9a1b5b'],
        dataLabels: {
          formatter: function (val, opts) {
            return opts.w.config.series[opts.seriesIndex];
          },
        },
      };

      return {
        options: options,
        series: series,
      };
    },

    generateReport() {
      //this.downloadpdf = !this.downloadpdf;
      const data = this.$route.query;
      data.type === "day"
        ? (this.downloadpdfD = !this.downloadpdfD)
        : data.type === "week"
        ? (this.downloadpdfW = !this.downloadpdfW)
        : data.type === "month"
        ? (this.downloadpdfM = !this.downloadpdfM)
        : data.type === "year"
        ? (this.downloadpdfY = !this.downloadpdfY)
        : (this.downloadpdfT = !this.downloadpdfT);
    },
  },
  mounted() {
    this.getDataCheckPoint();
    //     console.log(this.$route.query);
    //     this.selectDataBarChart = this.$route.query.typeData == 'all' ? "all" : "violate"
    //    // this.dataText = this.$route.query.typeData == 'all' ? "all" : "violate"
    //     this.headerDonutChart = this.$route.query.typeData == 'all' ? "all" : "violate"
    //     this.textReport = this.$route.query.type == 'day' ? 'ข้อมูลรายวัน' :this.$route.query.type == 'week' ? 'ข้อมูลรายสัปดาห์':this.$route.query.type == 'month' ? 'ข้อมูลรายเดือน':this.$route.query.type == 'year' ? 'ข้อมูลรายปี':'ข้อมูลรายช่วงเวลา';
    //     this.dateReport = this.$route.query.date
    //     this.dataText =  this.$route.query.typeData == 'all' ? {keyCard:"all",allText:"ปริมาณจราจรทั้งหมด"} :{keyCard:"violate",allText:"ปริมาณยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด ทั้งหมด"}
    //     this.headerReport = this.$route.query.typeData == 'all' ? "ข้อมูลจราจร" : "ข้อมูลยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด"
    //  if(this.$route.query.type == 'day'){
    //   this.dataIn = [44, 55, 41, 67, 22, 43, 12, 65, 12, 23, 21, 11,44, 55, 41, 67, 22, 43, 12, 65, 12, 23, 21, 11]
    //   this.dataOut = [44, 55, 41, 67, 22, 43, 12, 65, 12, 23, 21, 11,44, 55, 41, 67, 22, 43, 12, 65, 12, 23, 21, 11]
    //     this.textHeaderReport = this.$route.query.typeData == 'all' ? "รายงานข้อมูลปริมาณจราจรรายวัน" : "รายงานข้อมูลปริมาณจราจรรายวัน\nของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด"
    //   }else if(this.$route.query.type == 'week'){
    //     this.textHeaderReport = this.$route.query.typeData == 'all' ? "รายงานข้อมูลปริมาณจราจรรายสัปดาห์" : "รายงานข้อมูลปริมาณจราจรรายสัปดาห์\nของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด"
    //  this.dataIn = [12, 65, 12, 23, 21, 11,44]
    //   this.dataOut = [44, 55, 41, 67, 22, 43, 12]
    //  }else if(this.$route.query.type == 'month'){
    //     this.textHeaderReport = this.$route.query.typeData == 'all' ? "รายงานข้อมูลปริมาณจราจรรายเดือน" : "รายงานข้อมูลปริมาณจราจรรายเดือน\nของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด"
    //   this.dataIn = [12, 65, 12, 23, 21, 11,44,12, 65, 12, 23, 21, 11,44,12, 65, 12, 23, 21, 11,44,44, 55, 41, 67, 22, 43, 12,12, 65, 12]
    //   this.dataOut = [44, 55, 41, 67, 22, 43, 12,12, 65, 12, 23, 21, 11,44,44, 55, 41, 67, 22, 43, 12,12, 65, 12, 23, 21, 11,44,44, 55, 41]
    //   }else if(this.$route.query.type == 'year'){
    //     this.textHeaderReport = this.$route.query.typeData == 'all' ? "รายงานข้อมูลปริมาณจราจรรายปี" : "รายงานข้อมูลปริมาณจราจรรายปี\nของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด"
    //   this.dataIn = [12, 65, 12, 23, 21, 11,44,1,23,34,45,6]
    //   this.dataOut = [44, 55, 41, 67, 22, 43, 12,34,45,6,1,23]
    //   }else{
    //     this.dataIn = [12, 65, 12, 23, 21, 11,44]
    //   this.dataOut = [44, 55, 41, 67, 22, 43, 12]
    //     this.textHeaderReport = this.$route.query.typeData == 'all' ? "รายงานข้อมูลปริมาณจราจรตามช่วงเวลา" : "รายงานข้อมูลปริมาณจราจรตามช่วงเวลา\nของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด"
    //   }
    this.getData();
    //this.setNestChart()
  },
};
</script>
<style>
@import "../assets/css/background.css";
#chartdiv {
  padding-top: 5%;
  margin-bottom: 8%;
  width: 100%;
  height: 400px;
}

.textdonut {
  padding-top: 2%;
  padding-left: 3%;
}
.headerback {
  font-weight: 600;
  font-size: 24px;
  color: red;
}
.chip-text {
  font-weight: 500;
  font-size: 20px;
}
#chip {
  background-color: #02754B;
  color: #fff;
}

.note-text {
  font-size: 12px;
  color: red;
}
</style>
