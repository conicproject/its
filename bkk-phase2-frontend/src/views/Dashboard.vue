<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>

    <v-overlay :value="onProgress">
      <v-progress-circular indeterminate size="100" width="7"></v-progress-circular>
    </v-overlay>

    <v-main class="pl-3">
      <v-container fluid class="pl-1 pr-1 full-height">
        <v-row>
          <!-- ฝั่งซ้าย -->
          <v-col cols="12" md="6">
            <v-row>
              <v-col cols="12" md="8">
                <traffic :directionData="direction" :dataText="dataText"></traffic><br>
                <donutchart class="rectangle" :dataChart="dataDonut" :headerShow="dataText.keyCard"
                  :height="donutHeight"></donutchart>
                <div v-show="dataText.keyCard !== 'all'" class="textdonut">
                  <span>ประเภทยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด</span>
                  <div id="chartdiv1"></div>
                </div>
              </v-col>
              <v-col cols="12" md="4">
                <div class="rectangle pa-4">
                  <vehicle :vehicle="car_type" :dataText="dataText"></vehicle>
                </div>
              </v-col>
            </v-row>
          </v-col>

          <!-- ฝั่งขวา -->
          <v-col cols="12" md="6">
            <v-row>
              <v-col cols="12" md="6">
                <div class="rectangle pa-4">
                  <span>จุดที่มีปริมาณจราจร ขาเข้าเมือง มากที่สุด (คัน/วัน)</span>
                  <v-list-item v-for="item in topIn" :key="item.id" class="pl-0">
                    <v-list-item-content>
                      <v-list-item-title>
                        <span>{{ item.full_name }}&nbsp;</span>
                        <span class="intextViolate-3">{{ item.volume }}&nbsp;</span>
                        <span>คัน</span>
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </div>
              </v-col>
              <v-col cols="12" md="6">
                <div class="rectangle pa-4">
                  <span>จุดที่มีปริมาณจราจร ขาออกเมือง มากที่สุด (คัน/วัน)</span>
                  <v-list-item v-for="item in topOut" :key="item.id" class="pl-0">
                    <v-list-item-content>
                      <v-list-item-title>
                        <span>{{ item.full_name }}&nbsp;</span>
                        <span class="intextViolate-3">{{ item.volume }}&nbsp;</span>
                        <span>คัน</span>
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </div>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="6">
                <div class="rectangle pa-4">
                  <span>จุดที่มียานพาหนะฝ่าฝืนกฏจราจร ขาเข้าเมือง มากที่สุด (ครั้ง/วัน)</span>
                  <v-list-item v-for="item in topInViolate" :key="item.id" class="pl-0">
                    <v-list-item-content>
                      <v-list-item-title>
                        <span>{{ item.full_name }}&nbsp;</span>
                        <span class="intextViolate-3">{{ item.volume }}&nbsp;</span>
                        <span>คัน</span>
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </div>
              </v-col>
              <v-col cols="12" md="6">
                <div class="rectangle pa-4">
                  <span>จุดที่มียานพาหนะฝ่าฝืนกฏจราจร ขาออกเมือง มากที่สุด (ครั้ง/วัน)</span>
                  <v-list-item v-for="item in topOutViolate" :key="item.id" class="pl-0">
                    <v-list-item-content>
                      <v-list-item-title>
                        <span>{{ item.full_name }}&nbsp;</span>
                        <span class="intextViolate-3">{{ item.volume }}&nbsp;</span>
                        <span>คัน</span>
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </div>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
        <div class="elevation-0 mt-3" id="border">
          <barchart checkPage="dashboard" :cat="cat" :dataIn="dataIn" :dataOut="dataOut" :options="barOption || {}"
            :series="barSeries || []" :typeChart="typeChart" @color="changecolorChart"></barchart>
        </div>
        <br>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
const baseUrl = require("../../baseUrl.json");

import sidebar from "../components/sidebar-new.vue";
import barchart from "../charts/bar-linechart.vue";
import viewmap from "../components/map-liveview.vue";
import point from "../components/point&camera-number.vue";
import traffic from "../components/all-traffic.vue";
import headerbar from "../components/header-bar.vue";
import Swal from "sweetalert2/dist/sweetalert2.js";
import vehicle from "../components/type-vehicle-dashboard.vue";
import donutchart from "../charts/donutchart.vue";


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
    viewmap,
    point,
    traffic,
    headerbar,
    vehicle,
    donutchart
  },
  data: function () {
    return {
      donutHeight: 300,
      car_type: {},
      dataDonut: [],
      color: ["#FF9800", "#03A9F4"],
      stack: true,
      barOption: "",
      barSeries: "",
      dataText: { keyCard: "all", allText: "ปริมาณจราจรทั้งหมด" },
      dataTextViolate: {
        keyCard: "violate",
        allText: "ปริมาณยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด ทั้งหมด",
      },
      cameraTotal: "",
      checkpointTotal: "",
      timeUpdate: "",
      onProgress: false,
      direction: [],
      directionViolate: [],
      dataOut: [],
      dataIn: [],
      catViolate: [],
      dataOutViolate: [],
      dataInViolate: [],
      cat: [],
      drawer: null,
      typeChart: "bar",
      KeywordPoint2: {
        headL: "จำนวนจุดติดตั้ง",
        headR: "จำนวนกล้องทั้งหมด",
        unitL: "จุด",
        unitR: "กล้อง",
        number1: 27,
        number2: 100,
      },
      topIn: [
        // {
        //   id: 1,
        //   full_name: "จุดตรวจทาง 1",
        // },
        // {
        //   id: 2,
        //   full_name: "จุดตรวจทาง 2",
        // },
        // {
        //   id: 3,
        //   full_name: "จุดตรวจทาง 3",
        // },
      ],
      topOut: [
        // {
        //   id: 1,
        //   full_name: "จุดตรวจทาง 1",
        // },
        // {
        //   id: 2,
        //   full_name: "จุดตรวจทาง 2",
        // },
        // {
        //   id: 3,
        //   full_name: "จุดตรวจทาง 3",
        // },
      ],
      topInViolate: [
        // {
        //   id: 1,
        //   full_name: "จุดตรวจทาง 1",
        // },
        // {
        //   id: 2,
        //   full_name: "จุดตรวจทาง 2",
        // },
        // {
        //   id: 3,
        //   full_name: "จุดตรวจทาง 3",
        // },
      ],
      topOutViolate: [
        // {
        //   id: 1,
        //   full_name: "จุดตรวจทาง 1",
        // },
        // {
        //   id: 2,
        //   full_name: "จุดตรวจทาง 2",
        // },
        // {
        //   id: 3,
        //   full_name: "จุดตรวจทาง 3",
        // },
      ],
    };
  },
  methods: {
    options(cat) {
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
          // categories: this.cat,
          // categories: [
          //   "01/01/2011 GMT",
          //   "01/02/2011 GMT",
          //   "01/03/2011 GMT",
          //   "01/04/2011 GMT",
          //   "01/05/2011 GMT",
          //   "01/06/2011 GMT",
          //   "01/07/2011 GMT",
          //   "01/08/2011 GMT",
          //   "01/09/2011 GMT",
          //   "01/10/2011 GMT",
          //   "01/11/2011 GMT",
          //   "01/12/2011 GMT",
          //   "01/01/2011 GMT",
          //   "01/02/2011 GMT",
          //   "01/03/2011 GMT",
          //   "01/04/2011 GMT",
          //   "01/05/2011 GMT",
          //   "01/06/2011 GMT",
          //   "01/07/2011 GMT",
          //   "01/08/2011 GMT",
          //   "01/09/2011 GMT",
          //   "01/10/2011 GMT",
          //   "01/11/2011 GMT",
          //   "01/12/2011 GMT",
          // ],
        },
        legend: {
          position: "right",
          offsetY: 40,
        },
        fill: {
          opacity: 1,
        },
      }
      this.barOption = option
    },
    setDonutChart(param) {
      if (!param || !param.volume || !Array.isArray(param.volume)) {
        return {
          options: {},
          series: []
        };
      }

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
    series(datain, dataout) {
      //console.log(datain,dataout);
      let series = [
        {
          name: "ขาเข้าเมือง",
          data: datain,
          // data: [44, 55, 41, 67, 22, 43, 12, 65, 12, 23, 21, 11,44, 55, 41, 67, 22, 43, 12, 65, 12, 23, 21, 11],
        },
        {
          name: "ขาออกเมือง",
          data: dataout,
          //  data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14,44, 55, 41, 67, 22, 43, 12, 65, 12, 23, 21, 11],
        },
      ]
      // console.log(series);
      this.barSeries = series
    },
    getDate() {
      this.timeUpdate = new Date(
        Date.now() - new Date().getTimezoneOffset() * 60000
      )
        .toISOString()
        .substr(11, 5);
    },
    changecolorChart(param) {

      this.stack = true
      this.typeChart = "bar"

      if (param === 'all') {
        this.color = ["#FF9800", "#03A9F4"]
        //console.log(this.dataIn,this.dataOut);
        this.options(this.cat)
        this.series(this.dataIn, this.dataOut)

      } else {
        this.color = ["#F44336", "#3F51B5"]
        // console.log(param,this.dataInViolate,this.dataOutViolate);
        this.options(this.catViolate)
        this.series(this.dataInViolate, this.dataOutViolate)
      }

    },
    getDataDashBoard() {
      let session_data = localStorage.getItem("session");
      //let session_data = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTYsInVzZXJfaWQiOjEsImNyZWF0ZWRfYXQiOiIyMDIyLTA4LTE3IDEyOjI1OjQ4In0.215ZrepJ-5oZQ_3jCZmwmmIG9s5k5ze1cvbrq7Kvuuo"
      //.log(session_data);

      //let pathHaveCheckPoint = "/"+myPath[1]+"/";
      this.onProgress = true;
      let url = baseUrl.ipServer + "/dashboard";
      this.axios.get(url, { headers: { session: session_data } }).then((response) => {
        if (response.data.status_code === 200) {
          console.log('response.data.data :>> ', response.data.data);
          this.KeywordPoint2.number2 = response.data.data.camera_total
          this.KeywordPoint2.number1 = response.data.data.checkpoint_total
          //console.log(response.data.data.graph.inbound.length);
          this.dataIn = [];
          this.cat = [];
          this.dataOut = [];
          this.direction = response.data.data.direction
          this.directionViolate = response.data.data.direction_violation
          this.car_type = response.data.data.get_cartype_data
          this.dataDonut = this.setDonutChart(response.data.data.get_cartype_data);
          // this.topIn = response.data.data.top_rank.inbound;
          // this.topOut = response.data.data.top_rank.outbound;
          this.topIn = response.data.data.top_rank.inbound.map((item, index) => ({
            id: 1 + index,
            full_name: item.checkpoint.short_name,
            volume: item.volume
            // short_name: item.checkpoint.short_name,

          }))
          this.topOut = response.data.data.top_rank.outbound.map((item, index) => ({
            id: 1 + index,
            full_name: item.checkpoint.short_name,
            volume: item.volume
            // short_name: item.checkpoint.short_name,

          }))

          this.topInViolate = response.data.data.top_rank_violation.inbound.map((item, index) => ({
            id: 1 + index,
            full_name: item.checkpoint.short_name,
            volume: item.volume
            // short_name: item.checkpoint.short_name,

          }))
          this.topOutViolate = response.data.data.top_rank_violation.outbound.map((item, index) => ({
            id: 1 + index,
            full_name: item.checkpoint.short_name,
            volume: item.volume
            // short_name: item.checkpoint.short_name,

          }))
          //console.log("topin",this.topIn);
          for (let i = 0; i < response.data.data.graph.inbound.length; i++) {
            this.dataIn.push(response.data.data.graph.inbound[i].volume);
            this.cat.push(response.data.data.graph.inbound[i].checkpoint.name);
            this.dataOut.push(response.data.data.graph.outbound[i].volume);
          }

          for (let i = 0; i < response.data.data.graph_violation.inbound.length; i++) {
            this.dataInViolate.push(response.data.data.graph_violation.inbound[i].volume);
            this.catViolate.push(response.data.data.graph_violation.inbound[i].checkpoint.name);
            this.dataOutViolate.push(response.data.data.graph_violation.outbound[i].volume);
          }
          this.options(this.cat)
          this.series(this.dataIn, this.dataOut)
          this.onProgress = false;
        } else {
          this.onProgress = false;
          Toast.fire({
            icon: 'error',
            title: response.data.message,
          })
        }
      }).catch((error) => {
        this.onProgress = false;
        console.log(error.response);
        if (error.response.data.message === 'session timeout') {
          // localStorage.clear();
          // sessionStorage.clear();
          this.$store.dispatch("logout");
          this.$router.push('/login')
          Toast.fire({
            icon: "error",
            title: error.response.data.message,
          });

          return;
        }
        Toast.fire({
          icon: 'error',
          title: 'Cannot connet API',
        })
        // localStorage.clear();
        //     sessionStorage.clear();
        // this.$router.push('/error')
      });
      // this.dataIn = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
      // this.dataOut = [0, 2, 2, 0, 2, 0, 2, 2, 2, 0, 0, 0]
      // this.cat = [
      //       "01/01/2011 GMT",
      //       "01/02/2011 GMT",
      //       "01/03/2011 GMT",
      //       "01/04/2011 GMT",
      //       "01/05/2011 GMT",
      //       "01/06/2011 GMT",
      //       "01/07/2011 GMT",
      //       "01/08/2011 GMT",
      //       "01/09/2011 GMT",
      //       "01/10/2011 GMT",
      //       "01/11/2011 GMT",
      //       "01/12/2011 GMT",
      //     ]
    },

    linktoblacklist() {
      this.$router.push({
        path: "add-vehicle-blacklist",
      });
    },
    headerbar(param) {
      this.drawer = param;
    },
    // getDataCheckPoint(type) {
    //   let session_data = localStorage.getItem("session");
    //   let myPath = this.$route.path.split("/");

    //   this.onProgress = true;
    //   let url = baseUrl.ipServer + "/checkpoint/" + 34 + "/" + type;
    //   this.axios
    //     .get(url, { headers: { session: session_data } })
    //     .then((response) => {
    //       if (response.data.status_code === 200) {
    //         this.KeywordPoint2.number1 =
    //           response.data.data.cameras_status.active;
    //         this.KeywordPoint2.number2 =
    //           response.data.data.cameras_status.deactive;
    //         this.checkPoint = response.data.data.checkpoint;
    //         console.log('response.data :>> ', response.data);
    //         this.dataIn = [];
    //         this.cat = [];
    //         this.dataOut = [];
    //         this.direction = [];
    //         this.car_type = {};
    //         this.direction = response.data.data.direction;
    //         this.car_type = response.data.data.car_type;
    //         this.headerDonutChart = type
    //         if (type == "1") {
    //           this.setNestChart(response.data.data.car_type.volume, response.data.data.graph_inside);
    //         } else {
    //           this.dataDonut = this.setDonutChart(response.data.data.car_type);
    //         }



    //         for (let i = 0; i < response.data.data.graph.inbound.length; i++) {
    //           this.dataIn.push(response.data.data.graph.inbound[i].volume);
    //           this.cat.push(response.data.data.graph.inbound[i].time);
    //           this.dataOut.push(response.data.data.graph.outbound[i].volume);
    //         }
    //         this.options(this.cat);
    //         this.series(this.dataIn, this.dataOut);
    //         //console.log("this.car_type", this.dataIn, this.dataOut);
    //         this.getDataListCamera();
    //         this.onProgress = false;
    //         if (type == 1) {
    //           //this.setNestChart(response.data.data.car_type);
    //         }
    //       } else {
    //         this.onProgress = false;
    //         this.options();
    //         this.series();
    //         this.dataDonut = ''
    //         Toast.fire({
    //           icon: "error",
    //           title: response.data.message,
    //         });
    //       }
    //     })
    //     .catch((error) => {
    //       console.log(error);
    //       this.onProgress = false;
    //       if (error.response.data.message === 'session timeout') {
    //         this.$store.dispatch("logout");
    //         this.$router.push('/')
    //         Toast.fire({
    //           icon: "error",
    //           title: error.response.data.message,
    //         });

    //         return;
    //       }
    //       Toast.fire({
    //         icon: "error",
    //         title: "Cannot connet API",
    //       });
    //     });
    // },
  },
  mounted() {
    // this.getDataCheckPoint(0);
    this.getDate()
    this.getDataDashBoard()

  },
};
</script>
<style scoped>
@import "../assets/css/background.css";

.text-alarm {
  font-weight: bold;
  font-size: 40px;
}

.outtext-3 {
  color: #21b3ff;
}

.outtext-4 {
  color: #21b3ff;
  /* font-weight: bold; */
  font-size: 17px;
}

.intext-3 {
  color: #ff7f09;
  /* font-size: 16px; */
}

.intext-4 {
  color: #ff7f09;
  /* font-weight: bold; */
  font-size: 17px;
}

.intextViolate-3 {
  color: #F44336;

}

.intextViolate-4 {
  color: #F44336;
  font-size: 17px;
}

.outtextViolate-3 {
  color: #3F51B5;
}

.outtextViolate-4 {
  color: #3F51B5;
  font-size: 17px;
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

#bg .full-height {
  height: 100%;
}

#bg .point_camera {
  background: #02754B;
  padding: 0.5rem;
  border-radius: 0.7rem;
  color: #FFFFFF;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  display: flex;
  width: 60%;
  justify-content: center;
  align-items: center;
  pointer-events: none;
}

#bg .point_camera::before {
  content: '';
  background-image: url('../assets/img/icon/Vector.png');
  width: 18px;
  height: 12px;
  margin-right: 1rem;
}

.rectangle {
  background: #F5F6FA;
  border-radius: 10px;
}
</style>
