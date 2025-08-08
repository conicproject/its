<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer" @loadPageStatus="getDataDeviceStatus()"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="onProgress">
      <v-progress-circular indeterminate size="100" width="7"></v-progress-circular>
    </v-overlay>
    <v-content class="pl-3" >
      <v-container class="pl-1 pr-1">
                <v-chip @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
     <v-icon large color="red">mdi-chevron-left</v-icon>
         <span class="text-left headerback">Back</span>
    </v-chip> 
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">รายงานสถานะอุปกรณ์</span>
        </v-chip>
        <v-container v-if="$vuetify.breakpoint.width > 1025">
                  <v-layout>
                    <v-flex lg5 >
        <v-card large class="ma-2 elevation-0" color="#02754B">
              
              <v-select
              height="54"
          v-model="selectData"
          :items="listCheckPoint"
          item-text="name"
          item-value="id"
          hide-details
          required
          dense
          outlined
          dark
          @change="fn_changChartData(selectData)"
        ></v-select>
            </v-card>
            </v-flex>
        </v-layout>
                    <v-layout class="pb-3">
                <v-flex lg6 md6 class="pr-3">
                <v-card  class="elevation-0 d-flex align-content-space-between flex-wrap" id="border" height="100%">
                  <donutchart :dataChart="chartSensor" :textChart="textSensor" :btnChart="btnSensor" :btnShow="true" :headerShow="false" :height="donutHeight" :point="dataCheckpoint.id"></donutchart>
                  <v-layout class="d-flex justify-end align-end pa-3">
                <v-flex
              ><span class="d-flex justify-end align-end">All Sensors</span></v-flex
                >
                <v-flex
                  ><div class="text-right align-end" >
                    <v-btn @click="viewall('All Sensors')" class="text-right" color="primary" small>ดูรายละเอียด</v-btn>
                  </div></v-flex
                    >
                  </v-layout>
                </v-card>
                </v-flex>
                <v-flex lg6 md6 class="pr-3"  >
              <v-card height="100%" class="elevation-0 d-flex align-content-space-between flex-wrap" id="border" 
                ><donutchart :dataChart="chartAlarm" :textChart="textAlarm" :btnChart="btnAlarm" :btnShow="true" :headerShow="false" :height="donutHeight" :point="dataCheckpoint.id"></donutchart
              >
              <v-layout class="d-flex justify-end align-end pa-3">
                  <v-flex><span class="d-flex justify-end align-end">Current Alarms</span></v-flex>
      <v-flex><div class="text-right align-end" >
          <v-btn @click="viewall('Current Alarms')" class="text-right" color="primary" small>ดูรายละเอียด</v-btn>
        </div></v-flex>
    </v-layout>
            </v-card>
             
              </v-flex>
            </v-layout>
          <v-layout class="mt-3">
            <v-flex lg6 md6 >
              <v-card height="100%" class="mr-3 pl-0 elevation-0">
              <device
               class="pb-3"
                keyword="กล้องสำหรับตรวจจับยานพาหนะ"
                :data="dataCamera_tf"
               ></device>
              </v-card></v-flex>
             <v-flex lg6 md6><v-card  height="100%" class="mr-3 pl-0 elevation-0">
              <device
               class="pb-3"
                keyword="กล้องดูสภาพการจราจร"
                :data="dataCamera_pv"
               ></device>
              </v-card></v-flex>
          </v-layout>

         <v-layout class="mt-3">
            <v-flex lg6 md6 >
              <v-card height="100%" class="mr-3 pl-0 elevation-0">
              <device
               class="pb-3"
                keyword="บันทึกภาพและประมวลผล"
                :data="dataTerminal"
               ></device>
              </v-card>
              </v-flex>
            <v-flex lg6 md6 >
              <v-card height="100%" class="mr-3 pl-0 elevation-0">
              <device
               class="pb-3"
                keyword="Server"
                :data="dataSwitch"
               ></device>
              </v-card>
              </v-flex>
          </v-layout>

          <v-layout class="mt-3">
            <v-flex lg6 md6 >
              <v-card  height="100%" class="mr-3 pl-0 elevation-0">
              <device
               class="pb-3"
                keyword="Switch"
                :data="dataSwitch"
               ></device>
              </v-card>
              </v-flex>
            <v-flex lg6 md6 >
              <v-card  height="100%" class="mr-3 pl-0 elevation-0">
              <device
               class="pb-3"
                keyword="NVR"
                :data="dataNVR"
               ></device>
              </v-card>
              </v-flex>
          </v-layout>
           <v-layout class="mt-3" justify-center>
            <v-flex lg6 md6>
               <v-card  height="100%" class="mr-3 pl-0 elevation-0">
              <device
               class="pb-3"
                keyword="UPS"
                :data="dataUPS"
               ></device>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
        <v-container  v-else>
                  <v-layout>
                    <v-flex lg5>
        <v-card large class="ma-2 elevation-0" color="#02754B">
              
              <v-select
              height="54"
          v-model="selectData"
          :items="items_selectData"
          item-text="name"
          item-value="id"
          hide-details
          required
          dense
          outlined
          dark
          @change="fn_changChartData(selectData)"
        ></v-select>
            </v-card>
            </v-flex>
        </v-layout>
          <v-layout >
                <v-flex  class="pr-3 pb-3">
                <v-card class="elevation-0 d-flex align-content-space-between flex-wrap" id="border"  height="100%">
                  <donutchart :dataChart="chartSensor" :textChart="textSensor" :btnChart="btnSensor" :btnShow="true" :headerShow="false" :height="donutHeight" :point="dataCheckpoint.id"></donutchart>
                  <v-layout class="d-flex justify-end align-end pa-3">
                <v-flex
              ><span class="d-flex justify-end align-end">All Sensors</span></v-flex
                >
                <v-flex
                  ><div class="text-right align-end" >
                    <v-btn @click="viewall('All Sensors')" class="text-right" color="primary" small>ดูรายละเอียด</v-btn>
                  </div></v-flex
                    >
                  </v-layout>
                </v-card>

                </v-flex>
          </v-layout>
                <v-layout class="pb-3">
                <v-flex class="pr-3">
              <v-card class="elevation-0 d-flex align-content-space-between flex-wrap" id="border"  height="100%"  
                ><donutchart :dataChart="chartAlarm" :textChart="textAlarm" :btnChart="btnAlarm" :btnShow="true" :headerShow="false" :height="donutHeight" :point="dataCheckpoint.id"></donutchart
              >
              <v-layout class="d-flex justify-end align-end pa-3">
                  <v-flex><span class="d-flex justify-end align-end">Current Alarms</span></v-flex>
      <v-flex><div class="text-right align-end" >
          <v-btn @click="viewall('Current Alarms')" class="text-right" color="primary" small>ดูรายละเอียด</v-btn>
        </div></v-flex>
    </v-layout>
            </v-card>
              </v-flex>
            </v-layout>
                <v-layout>
            <v-flex height="100%" class="pr-3 pt-3">
              <!-- <v-container class="pr-3 pl-0" height="100%"> -->
              <device
               class="pb-3"
                keyword="กล้องสำหรับตรวจจับยานพาหนะ"
                :data="dataCamera_tf"
               ></device>
              <!-- </v-container> -->
              </v-flex>
          </v-layout>
                       
         <v-layout>
            <v-flex height="100%" class="pr-3 pt-3">
              <!-- <v-container class="pr-3 pl-0" height="100%"> -->
              <device
               class="pb-3"
                keyword="บันทึกภาพและประมวลผล"
                :data="dataTerminal"
               ></device>
              <!-- </v-container> -->
              </v-flex>
              </v-layout>
              <v-layout>
            <v-flex  height="100%" class="pr-3 pt-3">
              <!-- <v-container class="pr-3 pl-0" height="100%"> -->
              <device
               class="pb-3"
                keyword="Switch"
                :data="dataSwitch"
               ></device>
              <!-- </v-container> -->
              </v-flex>
          </v-layout>
 <v-layout>
            <v-flex height="100%" class="pr-3 pt-3">
              <!-- <v-container class="pr-3 pl-0" height="100%"> -->
              <device
               class="pb-3"
                keyword="กล้องดูสภาพการจราจร"
                :data="dataCamera_pv"
               ></device>
              <!-- </v-container> -->
              </v-flex>
          </v-layout>
              <v-layout>
            <v-flex height="100%" class="pr-3 pt-3">
              <!-- <v-container class="pr-3 pl-0" height="100%"> -->
              <device
               class="pb-3"
                keyword="Server"
                :data="dataServer"
               ></device>
              <!-- </v-container> -->
              </v-flex>
          </v-layout>

<v-layout>
            <v-flex height="100%" class="pr-3 pt-3">
              <!-- <v-container class="pr-3 pl-0" height="100%"> -->
              <device
               class="pb-3"
                keyword="NVR"
                :data="dataNVR"
               ></device>
              <!-- </v-container> -->
              </v-flex>
          </v-layout>
          <v-layout>
            <v-flex height="100%" class="pr-3 pt-3">
              <!-- <v-container class="pr-3 pl-0" height="100%"> -->
              <device
               class="pb-3"
                keyword=" UPS "
                :data="dataUPS"
               ></device>
              <!-- </v-container> -->
              </v-flex>
              </v-layout>

        </v-container>
      </v-container>
    </v-content>

  </v-app>
</template>
<script>
  const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
//import barchart from "../charts/bar-linechart.vue";
import donutchart from "../charts/donutchart.vue";
// import point from "../components/point&camera-number.vue";
import device from "../components/status-device.vue";
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
    donutchart,
    // point,
    device,
    headerbar,
  },
  data: function () {
    return {
            dataSensor:{
        percent:[
           {
                    "car_type": "ไม่ทำงาน(Down)",
                    "percent": 10.567943296930611
                },
                {
                    "car_type": "ทำงาน(Up)",
                    "percent": 11.139841207069631
                },
        ],
        volume:[
           {
                    "car_type": "ไม่ทำงาน(Down)",
                    "volume": 12
                },
                {
                    "car_type": "ทำงาน(Up)",
                    "volume": 12
                },
        ],
      },
      dataAlarm:{
          percent:[
           {
                    "car_type": "ไม่ทำงาน(Down)",
                    "percent": 10.567943296930611
           },
        ],
        volume:[
           {
                    "car_type": "ไม่ทำงาน(Down)",
                    "volume": 12
           },
        ],
      },
       textSensor:"All Sensors",
      btnSensor:"ดูรายละเอียด",
      textAlarm:"Current Alarms",
      btnAlarm:"ดูรายละเอียด",
      drawer: true,
      donutHeight:300,
      KeywordPoint2: {
        headL: "จำนวนกล้องติด",
        headR: "จำนวนกล้องดับ",
        unitL: "กล้อง",
        unitR: "กล้อง",
      },
      dataCamera:{total:0,
        online:0,
        offline:0,},
      dataServer:{total:0,
        online:0,
        offline:0,},
      dataTerminal:{total:0,
        online:0,
        offline:0,},
      dataSwitch:{total:0,
        online:0,
        offline:0,},
      dataUPS:{total:0,
        online:0,
        offline:0,},
        dataCamera_pv:{
        total:0,
        online:0,
        offline:0,
      },
       dataCamera_tf:{
        total:0,
        online:0,
        offline:0,
      },
      chartSensor:{},
      chartAlarm:{},
      onProgress:false,
      dataCheckpoint:{},
      listCheckPoint:[],
      selectData:""
    };
  },
    computed:{

  },
  methods: {
    headerbar(drawer){
      console.log("hhh",drawer);
      this.drawer = drawer;
    },
    gobackpage(){
     // console.log("this.$route.params",this.dataSearch);
      //let params = this.dataSearch
      this.$router.push({path:'/device-status'});
    },
    getDataDeviceStatus(param){
      let session_data = localStorage.getItem("session");
      this.onProgress = true;
      let myPath = this.$route.path.split("/");
      let url = param?baseUrl.ipServer + "/device-status/"+param:baseUrl.ipServer + "/device-status/"+myPath[2]
      this.selectData = myPath[2]
      this.axios.get(url,{headers:{session:session_data}})
      .then((response) => {
          if(response.data.status_code === 200){
        
            let res = response.data.data
            this.dataCamera = res.camera
            this.dataServer = res.server        
            this.dataTerminal = res.terminal
            this.dataSwitch = res.switch
            this.dataUPS = res.ups
            this.dataNVR = res.nvr
            this.dataCamera_pv = res.camera_pv
            this.dataCamera_tf = res.camera_tf
            this.setDonutChartSensor(res.all_sensors)
            this.setDonutChartAlarm(res.current_alarm)
            this.dataCheckpoint= res.checkpoint
            this.onProgress = false;
          }else{
            
            Toast.fire({
          icon: 'error',
          title: 'Cannot connet API',     
        })
            this.onProgress = false;
          }
      }).catch((error) => {
        console.log(error);
         if(error.response.data.message === 'session timeout'){
            this.$store.dispatch("logout");
            this.$router.push('/')
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
        this.onProgress = false;
      });
    },
    setDonutChartSensor(param){
      let label = ["ไม่ทำงาน(Down)","ทำงาน(Up)"];
      let series = [param.offline,param.online];
      let options = {
        labels: label,
        total: {
          show: true,
        },
         dataLabels: {
          enabled: false,
        formatter: function (val, opts) {
            return opts.w.config.series[opts.seriesIndex]
        },
      },
      };

      this.chartSensor = {
        options: options,
        series: series,
      };

    },

    setDonutChartAlarm(param){
      let label_raw = Object.keys(param)
      let series = Object.values(param)
      
    for(let i =0 ; i< label_raw.length ; i++){
      label_raw[i] = label_raw[i] =="camera_pv"? "กล้องดูสภาพการจราจร" : label_raw[i] == "camera_tf"? "กล้องสำหรับตรวจจับยานพาหนะ" :label_raw[i]
      

    }
     
      let options = {
        labels: label_raw,
        total: {
          show: true,
        },
         dataLabels: {
          enabled: false,
        formatter: function (val, opts) {
            return opts.w.config.series[opts.seriesIndex]
        },
      },
      };

      this.chartAlarm = {
        options: options,
        series: series,
      };

    },
    fn_changChartData(param){
      this.$router.push({path:'/device-status/'+param});
       //this.getDataDeviceStatus(param)
        this.reload();
    },
        reload(){

      this.$router.go();
     
    },
    getListCheckPoint(){
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/checkpoints"
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
            this.listCheckPoint = response.data.data
          }else{
          Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลจุดติดตั้งได้',     
        })
          }
          }).catch((error) => {
          console.log(error);
          if(error.response.data.message === 'session timeout'){
            this.$store.dispatch("logout");
            this.$router.push('/')
             Toast.fire({
              icon: "error",
              title: error.response.data.message,
            });

            return;
        }
          Toast.fire({
                    icon: 'error',
                    title: 'ไม่สามารถดึงข้อมูลจุดติดตั้งได้',     
                  })
          });
    },
    viewall(param) {
      
        if (param === "All Sensors") {
        this.$router.push({path:'/Device-Status-all-sensors',query:{checkpoint:this.dataCheckpoint.id}});
      } else {
        this.$router.push({path:'/Device-Status-alarm', query:{checkpoint:this.dataCheckpoint.id}});
      }
      
    
     
    },
  },
  mounted() {
    this.getDataDeviceStatus()
    this.getListCheckPoint()
  },
};
</script>
<style>
@import '../assets/css/background.css';
.cardText {
  font-weight: 600;
  font-size: 23px;
  color: #FFFFFF;
}
.dtpoint{
  color: #2463C1;
  font-weight: 700;
  font-size: 40px;
}
  .headerback{
 font-weight: 600;
  font-size: 24px;
    color: red;
}
</style>
