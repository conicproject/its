<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>

    <v-overlay :value="onProgress">
      <v-progress-circular indeterminate size="100" width="7"></v-progress-circular>
    </v-overlay>

    <v-main class="pl-3">
      <v-container class="pl-1 pr-1">
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">หน้าหลัก</span>
        </v-chip>

        <v-container v-if="$vuetify.breakpoint.width > 1024">
          <v-layout>
            <v-flex lg12 md12 sm12 class="mr-3">
              <v-card style="height: 40rem" class="elevation-0" height="100%">
                <viewmap></viewmap>
              </v-card>
            </v-flex>
          </v-layout>

          <v-layout class="pt-10">
            <v-flex lg12 md12 sm12>
              <traffic :directionData="direction" :dataText="dataText"></traffic>
              <br />
              <v-row>
                <v-col>
                  <v-card class="elevation-0 pa-3" id="border" height="100%">
                    <span class="intext-3">จุดที่มีปริมาณจราจรขาเข้ามากที่สุด </span>
                    <v-list>
                      <v-list-item v-for="item in topIn" :key="item.id" class="pl-0">
                        <v-list-item-content>
                          <v-list-item-title>
                            <span class="intext-3">อันดับ&nbsp;{{ item.id }}&nbsp;</span>
                            <span class="intext-4">&nbsp;{{ item.full_name }}</span>
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-card>
                </v-col>

                <v-col>
                  <v-card class="elevation-0 pa-3" id="border" height="100%">
                    <span class="outtext-3">จุดที่มีปริมาณจราจรขาออกมากที่สุด </span>
                    <v-list>
                      <v-list-item v-for="item in topOut" :key="item.id" class="pl-0">
                        <v-list-item-content>
                          <v-list-item-title>
                            <span class="outtext-3">อันดับ&nbsp;{{ item.id }}&nbsp;</span>
                            <span class="outtext-4">&nbsp;{{ item.full_name}}</span>
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-card>
                </v-col>
              </v-row>
            </v-flex>
          </v-layout>

          <v-layout class="pt-10">
            <v-flex lg12 md12 sm12>
              <traffic :directionData="directionViolate" :dataText="dataTextViolate"></traffic>
              <br />
              <v-row>
                <v-col>
                  <v-card class="elevation-0 pa-3" id="border" height="100%">
                    <span class="intextViolate-3">
                      จุดที่มีปริมาณยานพาหนะฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด ขาเข้ามากที่สุด
                    </span>
                    <v-list>
                      <v-list-item v-for="item in topInViolate" :key="item.id" class="pl-0">
                        <v-list-item-content>
                          <v-list-item-title>
                            {{ item.id }}
                            <span class="intextViolate-3">อันดับ&nbsp;{{ item.id }}&nbsp;</span>
                            <span class="intextViolate-4">&nbsp;{{ item.full_name }}</span>
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-card>
                </v-col>

                <v-col>
                  <v-card class="elevation-0 pa-3" id="border" height="100%">
                    <span class="outtextViolate-3">
                      จุดที่มีปริมาณยานพาหนะฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด ขาออกมากที่สุด
                    </span>
                    <v-list>
                      <v-list-item v-for="item in topOutViolate" :key="item.id" class="pl-0">
                        <v-list-item-content>
                          <v-list-item-title>
                            <span class="outtextViolate-3">อันดับ&nbsp;{{ item.id }}&nbsp;</span>
                            <span class="outtextViolate-4">&nbsp;{{ item.full_name }}</span>
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-card>
                </v-col>
              </v-row>
            </v-flex>
          </v-layout>

          <v-card class="elevation-0 mt-3 pt-5" id="border">
            <barchart
              checkPage="dashboard"
              :cat="cat"
              :dataIn="dataIn"
              :dataOut="dataOut"
              :options="barOption || {}"
              :series="barSeries || []"
              :typeChart="typeChart"
              @color="changecolorChart"
            ></barchart>
          </v-card>

          <v-layout class="mt-3">
            <v-spacer></v-spacer>
            <v-chip color="white">Update ล่าสุด {{ timeUpdate }} น.</v-chip>
          </v-layout>
        </v-container>

        <v-container v-else>
          <div style="height: 40rem">
            <viewmap></viewmap>
          </div>
          <br />
          <point class="pb-3" :keyword="KeywordPoint2"></point>
          <br />
          <traffic :directionData="direction" :dataText="dataText"></traffic>
          <br />
          <v-card class="elevation-0 pa-3" id="border">
            <span class="intext-3">จุดที่มีปริมาณจราจรขาเข้ามากที่สุด</span>
            <v-list>
              <v-list-item v-for="item in topInViolate" :key="item.id">
                <v-list-item-content>
                  <span class="intext-3">อันดับ&nbsp;{{ item.id }}&nbsp;</span>
                </v-list-item-content>
                <v-list-item-content>
                  <v-list-item-title>
                    <span class="intext-4 scroll">&nbsp;{{ item.full_name }}</span>
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>

          <v-card class="elevation-0 pa-3 mt-3" id="border">
            <span class="outtext-3">จุดที่มีปริมาณจราจรขาออกมากที่สุด</span>
            <v-list>
              <v-list-item v-for="item in topOutViolate" :key="item.id">
                <v-list-item-content>
                  <span class="outtext-3 pl-0">อันดับ&nbsp;{{ item.id }}&nbsp;</span>
                </v-list-item-content>
                <v-list-item-content>
                  <v-list-item-title>
                    <span class="outtext-4 pl-0 scroll">&nbsp;{{ item.full_name }}</span>
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>

          <br />
          <traffic :directionData="directionViolate" :dataText="dataTextViolate"></traffic>
          <br />

          <v-card class="elevation-0 pa-3" id="border">
            <span class="intextViolate-3">
              จุดที่มีปริมาณยานพาหนะฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด ขาเข้ามากที่สุด
            </span>
            <v-list>
              <v-list-item v-for="item in topIn" :key="item.id">
                <v-list-item-content>
                  <span class="intextViolate-3">อันดับ&nbsp;{{ item.id }}&nbsp;</span>
                </v-list-item-content>
                <v-list-item-content>
                  <v-list-item-title>
                    <span class="intextViolate-4 scroll">&nbsp;{{ item.full_name }}</span>
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>

          <v-card class="elevation-0 pa-3 mt-3" id="border">
            <span class="outtextViolate-3">
              จุดที่มีปริมาณยานพาหนะฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด ขาออกมากที่สุด
            </span>
            <v-list>
              <v-list-item v-for="item in topOut" :key="item.id">
                <v-list-item-content>
                  <span class="outtextViolate-3 pl-0">อันดับ&nbsp;{{ item.id }}&nbsp;</span>
                </v-list-item-content>
                <v-list-item-content>
                  <v-list-item-title>
                    <span class="outtextViolate-4 pl-0 scroll">&nbsp;{{ item.full_name }}</span>
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>

          <v-card class="elevation-0 mt-3" id="border">
            <barchart
              checkPage="dashboard"
              :cat="cat"
              :dataIn="dataIn"
              :dataOut="dataOut"
              :options="barOption || {}"
              :series="barSeries || []"
              :typeChart="typeChart"
              @color="changecolorChart"
            ></barchart>
          </v-card>

          <v-layout class="mt-3">
            <v-spacer></v-spacer>
            <v-chip color="white">Update ล่าสุด {{ timeUpdate }} น.</v-chip>
          </v-layout>
        </v-container>
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
  },
  data: function () {
    return {
       color: ["#FF9800", "#03A9F4"],
      stack: true,
      barOption:"",
      barSeries:"",
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
      typeChart:"bar",
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
      options(cat){
    let option = {
          dataLabels: {
          enabled: false,
        },
       colors:this.color,
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
  series(datain,dataout){
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
      changecolorChart(param){
       
        this.stack = true
        this.typeChart = "bar"
        
       if(param === 'all'){
         this.color = ["#FF9800", "#03A9F4"]
        //console.log(this.dataIn,this.dataOut);
         this.options(this.cat)
        this.series(this.dataIn,this.dataOut)
        
     }else{
       this.color = ["#F44336", "#3F51B5"]
     // console.log(param,this.dataInViolate,this.dataOutViolate);
        this.options(this.catViolate)
        this.series(this.dataInViolate,this.dataOutViolate)
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
          this.KeywordPoint2.number2 =response.data.data.camera_total
          this.KeywordPoint2.number1 =response.data.data.checkpoint_total
          //console.log(response.data.data.graph.inbound.length);
          this.dataIn = [];
          this.cat = [];
          this.dataOut = [];
          this.direction = response.data.data.direction
          this.directionViolate = response.data.data.direction_violation
          // this.topIn = response.data.data.top_rank.inbound;
          // this.topOut = response.data.data.top_rank.outbound;
           this.topIn = response.data.data.top_rank.inbound.map((item,index) => ({
             id: 1+index,
             full_name: item.checkpoint.short_name,
             // short_name: item.checkpoint.short_name,
           
           }))
          this.topOut = response.data.data.top_rank.outbound.map((item,index) => ({
            id: 1+index,
             full_name: item.checkpoint.short_name,
            // short_name: item.checkpoint.short_name,
           
          }))
          
          this.topInViolate = response.data.data.top_rank_violation.inbound.map((item,index) => ({
             id: 1+index,
             full_name: item.checkpoint.short_name,
             // short_name: item.checkpoint.short_name,
           
           }))
          this.topOutViolate = response.data.data.top_rank_violation.outbound.map((item,index) => ({
            id: 1+index,
             full_name: item.checkpoint.short_name,
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
            this.series(this.dataIn,this.dataOut)
          this.onProgress = false;
        }else{
           this.onProgress = false;
                 Toast.fire({
          icon: 'error',
          title: response.data.message,     
        })
        }
      }).catch((error) => {
         this.onProgress = false;
        console.log(error.response);
        if(error.response.data.message === 'session timeout'){
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
  },
  mounted() {
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
.intextViolate-3{
  color: #F44336	;
  
}
.intextViolate-4{
  color: #F44336	;
 font-size: 17px;
}
.outtextViolate-3{
  color: #3F51B5;
}
.outtextViolate-4{
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
</style>
