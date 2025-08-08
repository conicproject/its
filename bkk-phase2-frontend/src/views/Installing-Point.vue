<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer" @loadPage="reload()" :listmenu="listMenu"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="onProgress">
      <v-progress-circular indeterminate size="100" width="7"></v-progress-circular>
    </v-overlay>
    <v-content class="pl-3">
      <!-- <v-container class="pl-lg-16 pl-md-1" v-if="$vuetify.breakpoint.width > 950"> -->
      <v-container class="pl-1 pr-1">
        <v-layout v-if="$vuetify.breakpoint.width > 950">
          <v-chip large class="ma-2" color="#02754B">
            <span class="pl-5 pr-5 headertext">จุดติดตั้ง</span>
          </v-chip>
          <v-flex class="text-left">
            <v-card large class="ma-2 elevation-0" color="#02754B">
              <!-- <span class="pl-5 pr-5 text-pointer">จุดติดตั้ง : {{checkPoint.name}}</span> -->
              <v-select class="select" height="54" v-model="selectCheckpoint" :items="listCheckPoint" item-text="name"
                item-value="id" hide-details required dense outlined dark
                @change="fn_changCheckpoint(selectCheckpoint)"></v-select>
            </v-card>
          </v-flex>
          <v-flex>
            <v-card large class="ma-2 elevation-0" color="#02754B">
              <!-- <span class="pl-5 pr-5 text-pointer">จุดติดตั้ง : {{checkPoint.name}}</span> -->
              <v-select height="54" v-model="selectData" :items="items_selectData" item-text="name" item-value="key"
                hide-details required dense outlined dark @change="fn_changChartData(selectData)"></v-select>
            </v-card>
          </v-flex>
        </v-layout>
        <div v-else>
          <v-layout>
            <v-chip large class="ma-2" color="#02754B">
              <span class="pl-5 pr-5 headertext">จุดติดตั้ง</span>
            </v-chip>
          </v-layout>
          <v-layout>
            <v-card large class="ma-2 elevation-0" color="#02754B">
              <!-- <span class="pl-5 pr-5 text-pointer">จุดติดตั้ง : {{checkPoint.name}}</span> -->
              <v-select height="54" v-model="selectCheckpoint" :items="listCheckPoint" item-text="name" item-value="id"
                hide-details required dense outlined dark @change="fn_changCheckpoint(selectCheckpoint)"></v-select>
            </v-card>
          </v-layout>
          <v-layout>
            <v-card large class="ma-2 elevation-0" color="#02754B">
              <!-- <span class="pl-5 pr-5 text-pointer">จุดติดตั้ง : {{checkPoint.name}}</span> -->
              <v-select height="54" v-model="selectData" :items="items_selectData" item-text="name" item-value="key"
                hide-details required dense outlined dark @change="fn_changChartData(selectData)"></v-select>
            </v-card>
          </v-layout>
        </div>
        <v-container>
          <div>
            <v-layout class="mb-8">
              <v-flex lg6 md12 xs12 class="pr-3">
                <v-card height="100%" class="elevation-0" id="border">
                  <div style="width: 100%; height: 100%">
                    <!-- <div style="overflow: hidden; width: 100%;height: 100%;" v-if="isPublic == true"><iframe
                        frameBorder="0" :src="`${cameraPublic}`" style="width: 100%;height: 100%;" title="Iframe Example"
                        allow="autoplay; encrypted-media" allowfullscreen></iframe></div>
                    <video-player v-else ref="videoPlayer" :style="styleVideo" class="video-js vjs-default-skin"
                      :options="playerOptions" @play="onPlayerPlay($event)" @ready="onPlayerReady($event)" /> -->


                      <video-player ref="videoPlayer" :style="styleVideo" class="video-js vjs-default-skin"
                      :options="playerOptions" @play="onPlayerPlay($event)" @ready="onPlayerReady($event)" />
                    <v-flex offset-lg8 lg4 offset-md8 md4>
                      <v-select :disabled="false" v-model="camera" :hint="`${camera.code}`" :items="listCamera"
                        item-value="code" item-text="code" label="Select" flat hide-details dense solo
                        v-on:change="changeCamera" placeholder="กล้อง 1"></v-select>
                    </v-flex>
                  </div>
                </v-card>
                <!-- <v-flex offset-lg10 lg3><v-select :items="listCamera" item-text="code" flat hide-details dense solo placeholder="กล้อง 1"></v-select></v-flex> -->
              </v-flex>
              <v-flex class="mt-3" lg6 md12 xs12 v-if="$vuetify.breakpoint.width > 1400">
                <point class="pb-3" :keyword="KeywordPoint2"></point>
                <br />
                <traffic :directionData="direction" :dataText="dataText" class="mb-3"></traffic>
                <br />
                <vehicle :vehicle="car_type" :dataText="dataText" class="mb-5"></vehicle>
                <span class="note-text" v-if="dataText.keyCard == 'violate'">หมายเหตุ : จำนวนคันและจำนวน %
                  ของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกดในแต่ละประเภท</span>
              </v-flex>
              <v-flex lg6 md12 xs12 v-if="$vuetify.breakpoint.width <= 1400 &&
                $vuetify.breakpoint.width > 950
                ">
                <point class="pb-3" :keyword="KeywordPoint2"></point>
                <br />
                <traffic :directionData="direction" :dataText="dataText" class="mb-3"></traffic>
              </v-flex>
            </v-layout>
            <br />
            <v-layout class="mt-8" v-if="$vuetify.breakpoint.width <= 1400 &&
              $vuetify.breakpoint.width > 950
              ">
              <v-flex lg12 md12>
                <vehicle :vehicle="car_type" :dataText="dataText" class="mb-5"></vehicle>
                <span v-if="dataText.keyCard == 'violate'" class="note-text">หมายเหตุ : จำนวนคันและจำนวน %
                  ของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกดในแต่ละประเภท</span>
              </v-flex>
            </v-layout>

          </div>
          <v-layout v-if="$vuetify.breakpoint.width <= 950">
            <v-flex>
              <point class="pb-3" :keyword="KeywordPoint2"></point>
              <br />
              <traffic :directionData="direction" :dataText="dataText" class="mb-6"></traffic>

              <vehicle :vehicle="car_type" :dataText="dataText" class="mb-5"></vehicle>
              <span class="note-text" v-if="dataText.keyCard == 'violate'">หมายเหตุ : จำนวนคันและจำนวน %
                ของยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกดในแต่ละประเภท</span>
            </v-flex>
          </v-layout>
          <v-layout class="pb-3">
            <v-flex>
              <v-card class="elevation-0" id="border" height="100%" v-if="$vuetify.breakpoint.width <= 950">

                <barchart :cat="cat" :dataIn="dataIn" :dataOut="dataOut" checkPage="installpoint" :dataText="selectData"
                  :options="barOption" :series="barSeries" @color="changecolorChart"></barchart>

              </v-card>
            </v-flex>
          </v-layout>
          <v-layout>
            <v-flex lg6 md12 sm12 xs12 class="pr-3" v-if="$vuetify.breakpoint.width > 950">
              <v-card class="elevation-0" id="border" height="100%">
                <barchart :cat="cat" :dataIn="dataIn" :dataOut="dataOut" checkPage="installpoint" :dataText="selectData"
                  :options="barOption" :series="barSeries" @color="changecolorChart"></barchart>
              </v-card>
            </v-flex>
            <v-flex lg6 md12 sm12 xs12>
              <v-card class="elevation-0" id="border" height="100%">
                <donutchart v-if="headerDonutChart == '0'" :dataChart="dataDonut" :headerShow="dataText.keyCard"
                  :height="donutHeight"></donutchart>
                <div v-show="dataText.keyCard !== 'all'" class="textdonut">
                  <span>ประเภทยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด</span>
                  <div id="chartdiv1"></div>
                </div>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
        <v-layout><v-spacer></v-spacer><v-chip color="white">Update ล่าสุด {{ timeUpdate }} น.</v-chip></v-layout>
      </v-container>
    </v-content>

    <!-- <v-content class="pa-1" >

    </v-content> -->
  </v-app>
</template>
<script>
const baseUrl = require("../../baseUrl.json");
import sidebar from "../components/sidebar-new.vue";
import barchart from "../charts/bar-linechart.vue";
import donutchart from "../charts/donutchart.vue";
import vehicle from "../components/type-vehicle.vue";
import traffic from "../components/all-traffic.vue";
import point from "../components/point&camera-number.vue";
import headerbar from "../components/header-bar.vue";
import VideoPlayer from "../components/VideoPlayer.vue";
import VideoPlayer2 from "../components/VideoPlayer2.vue";
import VideoPlayer3 from "../components/VideoPlayer3.vue";
import * as am5 from "@amcharts/amcharts5";
import * as am5xy from "@amcharts/amcharts5/xy";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import * as am5percent from "@amcharts/amcharts5/percent";
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
    //viewvideo,
    traffic,
    vehicle,
    point,
    headerbar,
    VideoPlayer,
    VideoPlayer2,
    VideoPlayer3,
  },
  data: function () {
    return {
      headerDonutChart: '',
      color: ["#FF9800", "#03A9F4"],
      stack: true,
      barOption: {},
      barSeries: [],
      dataText: { keyCard: "all", allText: "ปริมาณจราจรทั้งหมด" },
      selectData: "all",
      items_selectData: [
        {
          key: "all",
          name: "ข้อมูลจราจร",
        },
        {
          key: "violate",
          name: "ข้อมูลยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด",
        },
      ],
      listCheckPoint: [],
      selectCheckpoint: 1,
      camera: "",
      listCamera: [],
      checkPoint: {},
      timeUpdate: "",
      onProgress: false,
      listMenu: [],
      car_type: {},
      dataDonut: [],
      direction: [],
      dataOut: [],
      dataIn: [],
      cat: [],
      dataBarChart: [],
      heightMd: "300px",
      heightMobile: "300px",
      height: "450px",
      drawer: true,
      donutHeight: 280,
      KeywordPoint2: {
        headL: "จำนวนกล้องติด",
        headR: "จำนวนกล้องดับ",
        unitL: "กล้อง",
        unitR: "กล้อง",
        number1: 0,
        number2: 0,
      },
      playerOptions: {
        autoplay: true,
        controls: true,
        controlBar: {
          timeDivider: false,
          durationDisplay: false,
        },
      },
      src: "",
      isPublic: false,
      cameraPublic: "",
      autoplay: "?rel=0&autoplay=1"
    };
  },
  created() {
    if (baseUrl.pathImg === "110.171.165.57") {
      this.isPublic = true
    }
  },
  computed: {
    player() {
      // return this.isPublic == false ? this.$refs.videoPlayer.player : null
      return this.$refs.videoPlayer.player
    },
    player2() {
      return this.$refs.videoPlayer2.player
    },
    player3() {
      return  this.$refs.videoPlayer3.player
    }, styleVideo() {
      return this.$vuetify.breakpoint.width > 950 ? "width: 100%; height: 100%" : "width : 100%; height : 400px"
    }

  },
  watch: {},
  methods: {
    onPlayerPlay(player) { },
    onPlayerReady(player) {
      this.player.play();
    },
    playVideo: function (source) {

      const video = {
        withCredentials: false,
        type: "application/x-mpegurl",
        src: source,
      };
      // if (this.$vuetify.breakpoint.width > 950) {
      //   // console.log("play");
      //   this.player.reset()
      //   this.player.src(video)
      //   this.player.play()
      // }
      // else {
      //   // console.log("play3");
      //   this.player3.reset()
      //   this.player3.src(video)
      //   this.player3.play()
      // }

      this.player.reset()
        this.player.src(video)
        this.player.play()
    },
    switchPlayer: function () {
      this.playVideo(this.src);
    },
    setNestChart(param) {
      //console.log("chartdonut",param.volume);
      var root = am5.Root.new("chartdonut");

      root.setThemes([am5themes_Animated.new(root)]);

      var chart = root.container.children.push(
        am5percent.PieChart.new(root, {
          radius: am5.percent(80),
          innerRadius: am5.percent(0.1),
        })
      );
      // Create series
      var series = chart.series.push(
        am5percent.PieSeries.new(root, {
          name: "Series",
          valueField: "sales",
          categoryField: "country",
        })
      );
      series
        .get("colors")
        .set("colors", [am5.color(0x0ff000), am5.color(0xf0000f)]);
      series.data.setAll([
        {
          country: "ปริมาณจราจรทั้งหมด",
          sales: 0,
        },
        {
          country: "รถที่ฝ่าฝืนสัญญาไฟ",
          sales: 0,
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

      var series2 = chart.series.push(
        am5percent.PieSeries.new(root, {
          name: "Series",
          valueField: "volume",
          categoryField: "car_type",
          alignLabels: false,
        })
      );

      series2.data.setAll(param.volume);

      // Configuring slices
      series2.slices.template.setAll({
        stroke: am5.color(0xffffff),
        strokeWidth: 2,
      });
      series2.labels.template.setAll({
        text: "{category}",
        textType: "radial",
        centerX: am5.percent(100)
      });

      series.labels.template.set("visible", true);
    },
    options(cat) {
      // console.log("this.option");
      this.barOption = {};
      let option = {
        dataLabels: {
          enabled: false,
        },
        colors: this.color,
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
          categories: cat,
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
    series(datain, dataout) {
      this.barSeries = [];

      let series = [
        {
          name: "ขาเข้าเมือง",
          data: datain,
        },
        {
          name: "ขาออกเมือง",
          data: dataout,
        },
      ];

      this.barSeries = series;
    },
    changecolorChart(param) {
      this.color = param;
      this.options(this.cat);
      this.series(this.dataIn, this.dataOut);
    },
    fn_changChartData(param) {
      this.dataText =
        param == "all"
          ? { keyCard: "all", allText: "ปริมาณจราจรทั้งหมด" }
          : {
            keyCard: "violate",
            allText:
              "ปริมาณยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด ทั้งหมด",
          };
      this.selectData = param;
      if (param == "all") {
        this.getDataCheckPoint(0);
      } else {
        this.getDataCheckPoint(1);
      }


      // this.setNestChart();
    },
    fn_changCheckpoint(param) {
      this.$router.push("/installing/" + param);
      this.getDataCheckPoint(0);
      this.reload();
    },


    getDataListCamera() {

      let session_data = localStorage.getItem("session");
      this.myPath = this.$route.path.split("/");
      let url =
        baseUrl.ipServer +
        "/traffic-view/checkpoint-camera?checkpoint=" +
        this.myPath[2];
      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {
          if (response.data.status_code === 200) {
            this.textCheckPoint = response.data.data.checkpoint.short_name;
            this.listCamera = response.data.data.cameras;
            this.camera = this.listCamera[0].code;

            this.getLiveView(this.listCamera[0].code);

            // if (this.isPublic) {
            //   this.cameraPublic = this.listCamera[0].url.slice(0, -1) + this.autoplay;

            // } else {
            //   this.getLiveView(this.listCamera[0].code);
            // }
          }
        });
    },

    reload() {
      this.$router.go();
    },
    getDate() {
      this.timeUpdate = new Date(
        Date.now() - new Date().getTimezoneOffset() * 60000
      )
        .toISOString()
        .substr(11, 5);
    },
    setNestChart(cartype, pieInside) {
      var root = am5.Root.new("chartdiv1");

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
        scale: 0.75,
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

      let test = [
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
        scale: 0.75,
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
    },
    getDataCheckPoint(type) {
      let session_data = localStorage.getItem("session");
      let myPath = this.$route.path.split("/");
      this.selectCheckpoint = myPath[2];

      this.onProgress = true;
      let url = baseUrl.ipServer + "/checkpoint/" + myPath[2] + "/" + type;
      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {
          if (response.data.status_code === 200) {
            this.KeywordPoint2.number1 =
              response.data.data.cameras_status.active;
            this.KeywordPoint2.number2 =
              response.data.data.cameras_status.deactive;
            this.checkPoint = response.data.data.checkpoint;

            this.dataIn = [];
            this.cat = [];
            this.dataOut = [];
            this.direction = [];
            this.car_type = {};
            this.direction = response.data.data.direction;
            this.car_type = response.data.data.car_type;
            this.headerDonutChart = type
            if (type == "1") {
              this.setNestChart(response.data.data.car_type.volume, response.data.data.graph_inside);
            } else {
              console.log('this.response.data.data.car_type :>> ', response.data.data.car_type);
              this.dataDonut = this.setDonutChart(response.data.data.car_type);
            }



            for (let i = 0; i < response.data.data.graph.inbound.length; i++) {
              this.dataIn.push(response.data.data.graph.inbound[i].volume);
              this.cat.push(response.data.data.graph.inbound[i].time);
              this.dataOut.push(response.data.data.graph.outbound[i].volume);
            }
            this.options(this.cat);
            this.series(this.dataIn, this.dataOut);
            //console.log("this.car_type", this.dataIn, this.dataOut);
            this.getDataListCamera();
            this.onProgress = false;
            if (type == 1) {
              //this.setNestChart(response.data.data.car_type);
            }
          } else {
            this.onProgress = false;
            this.options();
            this.series();
            this.dataDonut = ''
            Toast.fire({
              icon: "error",
              title: response.data.message,
            });
          }
        })
        .catch((error) => {
          console.log(error);
          this.onProgress = false;
          if (error.response.data.message === 'session timeout') {
            this.$store.dispatch("logout");
            this.$router.push('/')
            Toast.fire({
              icon: "error",
              title: error.response.data.message,
            });

            return;
          }
          Toast.fire({
            icon: "error",
            title: "Cannot connet API",
          });
        });
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
        colors: ['#1aa478', '#f79e69', '#8582f2', '#866846', '#96e637', '#f9429e', '#f1cbff', '#3e1379', '#9a1b5b'],
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
    changeCamera(a) {
      this.getLiveView(a, false)

      // if (this.isPublic) {
      //   let filter = this.listCamera.filter(function (creature) {
      //     return creature.code == a;
      //   });
      //   this.cameraPublic = filter[0].url.slice(0, -1) + this.autoplay;

      // } else {
      //   this.getLiveView(a, false)
      // }

    },

    getLiveView(code, init = true) {
      // this.getDataListCamera()

      let session_data = localStorage.getItem("session");
      this.myPath = this.$route.path.split("/");

      let url =
        baseUrl.ipServer +
        "/traffic-view/live?checkpoint=" +
        this.myPath[2] +
        "&camera=" +
        code;
      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {
          if (response.data.status_code === 200) {

            let url = response.data.data.url;
            
            if (this.isPublic) {
              url = url.replace( baseUrl.ipLiveviewInternal, baseUrl.ipLiveviewInternet)
              this.playVideo(url)
            } else {
              this.playVideo(url)
            }
            // this.playVideo("http://10.129.90.105/HLS/channel/101/startTime/20230906T100000/endTime/20230906T100200/playBack.m3u8")
          }
        });
    },

    headerbar(drawer) {
      this.drawer = drawer;
    },



    getListCheckPoint() {
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/checkpoints";
      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {
          if (response.status === 200) {
            this.listCheckPoint = response.data.data;
          } else {
            Toast.fire({
              icon: "error",
              title: "ไม่สามารถดึงข้อมูลจุดติดตั้งได้",
            });
          }
        })
        .catch((error) => {
          if (error.response.data.message === 'session timeout') {
            this.$store.dispatch("logout");
            this.$router.push('/')
            Toast.fire({
              icon: "error",
              title: error.response.data.message,
            });

            return;
          }
          console.log(error);
          Toast.fire({
            icon: "error",
            title: "ไม่สามารถดึงข้อมูลจุดติดตั้งได้",
          });
        });
    },
  },
  mounted() {
    // this.playVideo("http://10.129.90.105/HLS/channel/101/startTime/20230906T100000/endTime/20230906T100200/playBack.m3u8")

    this.getDataCheckPoint(0);
    this.getListCheckPoint();
    this.getDate();
  },
  beforeDestroy() {
    if (this.player != null) {
      this.player.dispose(); // dispose() Will delete Dom Elements
    }

    if (this.player2 != null) {
      this.player2.dispose(); // dispose() Will delete Dom Elements
    }

    if (this.player3 != null) {
      this.player3.dispose(); // dispose() Will delete Dom Elements
    }
  },
};
</script>
<style scoped>
@import "../assets/css/background.css";

#chartdiv1 {
  padding-top: 5%;
  margin-bottom: 8%;
  width: 100%;
  height: 400px;
}

.textdonut {
  padding-top: 2%;
  padding-left: 3%;
}

.textdonut {
  padding-top: 2%;
  padding-left: 3%;
}

#chartdonut {
  padding-top: 5%;
  width: 100%;
  height: 15rem;
}

.note-text {
  font-size: 12px;
  color: red;
}

.v-input {
  font-size: 20px;
}

.dtpoint {
  color: #02754B;
  font-weight: 700;
  font-size: 40px;
}

.text-pointer {
  font-weight: 600;
  font-size: 18px;
  color: #ffffff;
}

.text-pointer-mobile {
  font-weight: 600;
  font-size: 15px;
  color: #ffffff;
}

.scroll {
  width: 100%;
  overflow-x: auto;
  white-space: nowrap;
}

/* width */
::-webkit-scrollbar {
  width: 1px;
  background: #f1f1f100;
}

/* Track */
::-webkit-scrollbar-track {
  background: #f1f1f100;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0);
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0);
}
</style>
