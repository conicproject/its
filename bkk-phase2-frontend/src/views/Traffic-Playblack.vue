<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer" @loadPageTraffic="reload()"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-content class="pl-0 pb-16 pt-8">
      <v-container class="pl-1 pr-1" v-if="$vuetify.breakpoint.width > 1025">
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
          <span class="pl-5 pr-5 headertext">ดูสภาพการจราจรย้อนหลัง</span>
        </v-chip>
        <v-layout justify-center>
          <v-flex lg3 class="mb-3 mr-1">
            <v-card large class="ma-2 elevation-0" color="#02754B">
              <!-- <span class="pl-5 pr-5 text-pointer">จุดติดตั้ง : {{checkPoint.name}}</span> -->
              <v-select
                class="select"
                height="54"
                v-model="selectCheckpoint"
                :items="listCheckPoint"
                item-text="name"
                item-value="id"
                hide-details
                required
                dense
                outlined
                dark
                @change="fn_changCheckpoint(selectCheckpoint)"
              ></v-select>
            </v-card>
          </v-flex>
          <v-flex lg4>
            <v-card class="ma-2 elevation-0">
              <v-text-field
                placeholder="วัน เดือน ปี เวลา"
                outlined
                hide-details
                v-model="dayformat"
                readonly
                @click="opendatetime = true"
              >
              </v-text-field>
            </v-card>
          </v-flex>
        </v-layout>
        <v-layout class="pl-5 pr-5" justify-center>
          <v-flex class="pa-1">
            <v-container class="d-flex justify-start" v-if="showVideo">
              <!-- <v-container class="d-flex justify-start" v-if="true"> -->

              <div style="width: 60rem; height: 40rem; margin-right: 3rem">
                <img style="height: 100%; width: 100%" :src="url" />
                <!-- <img style="height: 100%;width: 100%;" src="../assets/img/No signal.png"> -->
                <v-flex offset-lg9 lg3 md1
                  ><v-select
                    v-model="camera"
                    :hint="`${camera.code}`"
                    :items="listCamera"
                    item-value="code"
                    item-text="code"
                    label="Select"
                    flat
                    hide-details
                    dense
                    solo
                    v-on:change="changeCamera"
                  ></v-select
                ></v-flex>
              </div>

              <!-- <div style="width: 60rem; height: 40rem">
                <img style="height: 100%; width: 100%" :src="url" />
                <v-flex offset-lg9 lg3 md1
                  ><v-select
                    v-model="camera"
                    :hint="`${camera.code}`"
                    :items="listCamera"
                    item-value="code"
                    item-text="code"
                    label="Select"
                    flat
                    hide-details
                    dense
                    solo
                    v-on:change="changeCamera"
                  ></v-select
                ></v-flex>
              </div> -->
            </v-container>
          </v-flex>
        </v-layout>
      </v-container>
      <v-container class="pl-1 pr-1" v-else>
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
          <span class="pl-5 pr-5 headertext-mobile"
            >ดูสภาพการจราจรย้อนหลัง</span
          >
        </v-chip>
        <v-layout justify-center>
          <v-flex lg4>
            <v-card large class="ma-2 elevation-0" color="#02754B">
              <!-- <span class="pl-5 pr-5 text-pointer">จุดติดตั้ง : {{checkPoint.name}}</span> -->
              <v-select
                class="select"
                height="54"
                v-model="selectCheckpoint"
                :items="listCheckPoint"
                item-text="name"
                item-value="id"
                hide-details
                required
                dense
                outlined
                dark
                @change="fn_changCheckpoint(selectCheckpoint)"
              ></v-select>
            </v-card>
          </v-flex>
        </v-layout>
        <v-layout>
          <v-flex lg4>
            <v-card class="ma-2 elevation-0">
              <v-text-field
                placeholder="วัน เดือน ปี เวลา"
                outlined
                hide-details
                v-model="dayformat"
                readonly
                @click="opendatetime = true"
              >
              </v-text-field>
            </v-card>
          </v-flex>
        </v-layout>
        <!-- <v-layout justify-center>
            <v-flex sm12 xs12 class="mb-3 mr-1 d-flex justify-center">
                
                <span class="pl-5 pr-5 textTime py-3">
                  Start date</span>
        </v-flex>
         </v-layout><v-layout>
        <v-flex  sm12 xs12>
                <v-select v-model="startYear" :items="years" placeholder="ปี" outlined hide-details class="sl-mobile mb-3"></v-select>
            </v-flex>
          </v-layout><v-layout>
            <v-flex  sm12 xs12>
                <v-select v-model="startMonth" @change="changeMonth()" item-value="key" :items="month" item-text="name" placeholder="เดือน" outlined hide-details class="sl-mobile mb-3"></v-select>
            </v-flex>
          </v-layout><v-layout>
            <v-flex sm12 xs12>          
                <v-select v-model="startDay"  :items="checkMonth === 0? day0 :checkMonth === 1? day1 :day2" placeholder="วัน"  outlined hide-details class="sl-mobile mb-3"></v-select>   
            </v-flex>
          </v-layout><v-layout>
           
            <v-flex class="mr-1" sm12 xs12>          
                    <v-select v-model="startHour" placeholder="ชั่วโมง" :items="hour"  outlined hide-details class="sl-mobile mb-3"></v-select>
            </v-flex> 
            <h1>:</h1>
                <v-flex sm12 xs12 class="ml-1">  
                    <v-select v-model="startMin" placeholder="นาที" :items="minute" outlined hide-details class="sl-mobile mb-3"></v-select>
                </v-flex>
         </v-layout>       
         <v-layout justify-center>
            <v-flex sm12 xs12 class="mb-3 mr-1 d-flex justify-center">
                
                <span class="pl-5 pr-5 textTime py-3">
                End date</span>
    
    </v-flex>
  </v-layout><v-layout>
            <v-flex sm12 xs12>          
                <v-select v-model="endYear" :items="years" placeholder="ปี" outlined hide-details class="sl-mobile mb-3"></v-select>   
            </v-flex>
          </v-layout><v-layout>
            <v-flex  sm12 xs12>
                <v-select v-model="endMonth" @change="changeMonth()" item-value="key" :items="month" item-text="name"  placeholder="เดือน"  outlined hide-details class="sl-mobile mb-3"></v-select>
            </v-flex>
          </v-layout><v-layout>
            <v-flex  lgsm12 xs121>
                <v-select  v-model="startDay"  :items="checkMonth === 0? day0 :checkMonth === 1? day1 :day2" placeholder="วัน"  outlined hide-details class="sl-mobile mb-3"></v-select>
            </v-flex>
          </v-layout><v-layout>
            <v-flex class=" mr-1" sm12 xs12>          
                    <v-select v-model="endHour" placeholder="ชั่วโมง" :items="hour" outlined hide-details class="sl-mobile mb-3"></v-select>
            </v-flex> 
            <h1>:</h1>
                <v-flex sm12 xs12 class="ml-1">  
                    <v-select v-model="endMin" placeholder="นาที" :items="minute" outlined hide-details class="sl-mobile mb-3"></v-select>
                </v-flex>
         </v-layout>
         <v-layout >
         <v-flex class="ml-1 mt-1 d-flex justify-center" >
            <v-btn class="submit-btn py-3" large color="primary" @click="checkDateTime()">Submit</v-btn>
        </v-flex>
    </v-layout> -->
        <v-layout justify-center>
          <v-flex>
            <v-container class="d-flex justify-start" v-if="showVideo">
              <div style="width: 60rem; height: 40rem">
                <img style="height: 100%; width: 100%" :src="url" />
                <v-flex offset-lg9 lg3 md1
                  ><v-select
                    v-model="camera"
                    :hint="`${camera.code}`"
                    :items="listCamera"
                    item-value="code"
                    item-text="code"
                    label="Select"
                    flat
                    hide-details
                    dense
                    solo
                    v-on:change="changeCamera"
                  ></v-select
                ></v-flex>
              </div>
            </v-container>
            <br />
            <!-- <v-container class="d-flex justify-start" v-if="showVideo">
              <div style="width: 60rem; height: 40rem">
                <img style="height: 100%; width: 100%" :src="url" />
                <v-flex offset-lg9 lg3 md1
                  ><v-select
                    v-model="camera"
                    :hint="`${camera.code}`"
                    :items="listCamera"
                    item-value="code"
                    item-text="code"
                    label="Select"
                    flat
                    hide-details
                    dense
                    solo
                    v-on:change="changeCamera"
                  ></v-select
                ></v-flex>
              </div>
            </v-container> -->
          </v-flex>
        </v-layout>
      </v-container>
      <datetimepicker
        :show="opendatetime"
        @close="opendatetime = false"
        @setDateTime="setDateTimePicker"
      ></datetimepicker>
    </v-content>
  </v-app>
</template>
  <script>
const baseUrl = require("../../baseUrl.json");
import sidebar from "../components/sidebar-new.vue";
import datetimepicker from "../components/date-time-picker.vue";
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
    headerbar,
    datetimepicker,
  },
  data() {
    return {
      dayformat: "",
      opendatetime: false,
      min: "2022-08-01",
      menu: false,
      date: [],
      maxSelectDate: new Date().toISOString().substr(0, 10),
      selectCheckpoint: 1,
      selectData: "all",
      listCheckPoint: [],
      enableVideo: false,
      urlVideo: "",
      showVideo: false,
      url: "",
      drawer: true,
      camera: "",
      listCamera: [],
      textCheckPoint: "",
      checkMonth: 0,
      startMonth: "",
      startYear: "",
      startDay: "",
      startMin: "00",
      startHour: "00",
      endYear: "",
      endMonth: "",
      endDay: "",
      endHour: "23",
      endMin: "59",
      day0: [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
        "31",
      ],
      day1: [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
      ],
      day2: [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
      ],
      month: [
        { key: "01", name: "มกราคม" },
        { key: "02", name: "กุมภาพันธ์" },
        { key: "03", name: "มีนาคม" },
        { key: "04", name: "เมษายน" },
        { key: "05", name: "พฤษภาคม" },
        { key: "06", name: "มิถุนายน" },
        { key: "07", name: "กรกฎาคม" },
        { key: "08", name: "สิงหาคม" },
        { key: "09", name: "กันยายน" },
        { key: "10", name: "ตุลาคม" },
        { key: "11", name: "พฤศจิกายน" },
        { key: "12", name: "ธันวาคม" },
      ],
      hour: [
        "00",
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
      ],
      minute: [
        "00",
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
        "31",
        "32",
        "33",
        "34",
        "35",
        "36",
        "37",
        "38",
        "39",
        "40",
        "41",
        "42",
        "43",
        "44",
        "45",
        "46",
        "47",
        "48",
        "49",
        "50",
        "51",
        "52",
        "53",
        "54",
        "55",
        "56",
        "57",
        "58",
        "59",
      ],
    };
  },
  computed: {
    years() {
      const year = new Date().getFullYear() + 543;
      //console.log(year);
      return Array.from(
        { length: year - 2564 },
        (value, index) => 2565 + index
      );
    },
  },
  watch: {},
  methods: {
    setDateTimePicker(startTime, endTime, day) {
      this.opendatetime = false;
      this.loadVideo(startTime, endTime);
      // this.dayformat = day;
    },

    setTimeRange() {
      var now = new Date();
      var endDate = new Date(this.date[0]);
      endDate.setDate(endDate.getDate() + 6);
      now.setDate(now.getDate());
      this.min = this.date[0];
      if (now.getTime() < endDate.getTime()) {
        this.maxSelectDate = now.toISOString().substr(0, 10);
      } else {
        this.maxSelectDate = endDate.toISOString().substr(0, 10);
      }
      //   let end = endDate.toISOString().substr(0, 10)
      //   let data = end.split("-");
      //   let year = parseInt(data[0])+543;
      //   return data[2]+"-"+data[1]+"-"+year.toString();
      //  this.maxSelectDate =
    },
    cancle() {
      this.date = [];
      this.min = "2022-08-01";
      this.maxSelectDate = new Date().toISOString().substr(0, 10);
      //this.menu=false
    },
    fn_changCheckpoint(param) {
      this.$router.push("/traffic/belated/" + param);

      //this.reload();
    },
    headerbar(drawer) {
      this.drawer = drawer;
    },

    changeMonth(params) {
      // alert(this.startMonth)
      this.checkMonth =
        this.startMonth == "02"
          ? 2
          : this.startMonth == "04" ||
            this.startMonth == "06" ||
            this.startMonth == "09" ||
            this.startMonth == "11"
          ? 1
          : 0;
    },
    checkDateTime() {
      if (
        this.startDay === "" ||
        this.startMonth === "" ||
        this.startYear === "" ||
        this.endDay === "" ||
        this.endMonth === "" ||
        this.endYear === ""
      ) {
        Toast.fire({
          icon: "error",
          title: "กรุณากรอกข้อมูลให้ครบ",
        });
      } else {
        this.loadVideo();
      }
    },
    loadVideo(startTime, endTime) {
      this.showVideo = true;
      //let startyear = parseInt(this.startYear-543)
      //let endyear = parseInt(this.endYear-543)
      //let startTime = startyear+'-'+this.startMonth+'-'+this.startDay+'T'+this.startHour+':'+this.startMin+':00'
      //let endTime = endyear+'-'+this.endMonth+'-'+this.endDay+'T'+this.endHour+':'+this.endMin+':00'

      let session_data = localStorage.getItem("session");
      let myPath = this.$route.path.split("/");
      let test =
        baseUrl.ipServer +
        "/traffic-view/playback?checkpoint=" +
        myPath[3] +
        "&camera=" +
        this.camera +
        "&start_time=" +
        startTime +
        "&end_time=" +
        endTime;
      this.url =
        baseUrl.ipServer +
        "/traffic-view/playback?checkpoint=" +
        myPath[3] +
        "&camera=" +
        this.camera +
        "&start_time=" +
        startTime +
        "&end_time=" +
        endTime +
        "&session=" +
        session_data;
    },
    getCameraCode() {
      let session_data = localStorage.getItem("session");
      let myPath = this.$route.path.split("/");
      this.selectCheckpoint = myPath[3];
      let url =
        baseUrl.ipServer +
        "/traffic-view/checkpoint-camera?checkpoint=" +
        myPath[3];

      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {
          if (response.data.status_code === 200) {
            this.textCheckPoint = response.data.data.checkpoint.short_name;
            this.listCamera = response.data.data.cameras;

            if (this.listCamera.length > 0) {
              this.camera = this.listCamera[0].code;
            }
          } else {
            Toast.fire({
              icon: "error",
              title: response.data.message,
            });
          }
        })
        .catch((error) => {

          if (error.response.data.message === "session timeout") {
            this.$store.dispatch("logout");
            this.$router.push("/");
            Toast.fire({
              icon: "error",
              title: error.response.data.message,
            });

            return;
          }
        });
    },
    gobackpage() {
      this.$router.push({ path: "/traffic/present" });
    },
    changeCamera(value) {},
    reload() {
      this.$router.go();
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
          if (error.response.data.message === "session timeout") {
            this.$store.dispatch("logout");
            this.$router.push("/");
            Toast.fire({
              icon: "error",
              title: error.response.data.message,
            });

            return;
          }
          Toast.fire({
            icon: "error",
            title: "ไม่สามารถดึงข้อมูลจุดติดตั้งได้",
          });
        });
    },
  },
  mounted() {
    this.getCameraCode();
    this.getListCheckPoint();
  },
};
</script>
  <style>
.submit-btn {
  border-radius: 15px;
}
.textTime {
  font-weight: 700;
  font-size: 20px;
  color: #02754B;
  text-align: center;
  background-color: white;
  display: block;
  border-radius: 15px;
}
.belate {
  font-weight: 600;
  font-size: 20px;
  color: #ffffff;
}
.belate-mobile {
  font-weight: 600;
  font-size: 15px;
  color: #ffffff;
}
.sl-mobile {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
}
.text-pointer {
  font-weight: 600;
  font-size: 25px;
  color: #ffffff;
  overflow: auto;
  padding: 5%;
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
.headerback {
  font-weight: 600;
  font-size: 24px;
  color: red;
}
</style>
  