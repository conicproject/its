<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer" @loadPage="getDataCameraCode(), reload()"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="onProgress">
      <v-progress-circular indeterminate size="100" width="7"></v-progress-circular>
    </v-overlay>
    <v-content class="ps-16 pe-16 pb-16 pt-8" v-if="$vuetify.breakpoint.width > 1025">
      <v-container class="pl-16">
        <v-chip @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
          <v-icon large color="red">mdi-chevron-left</v-icon>
          <span class="text-left headerback">Back</span>
        </v-chip>
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">ดูสภาพการจราจรย้อนหลัง</span>
        </v-chip>
        <v-layout>
          <v-flex>
            <v-chip large class="ma-2 " color="#02754B">
              <span class="pl-5 pr-5 belate">
                จุดติดตั้ง : {{ textCheckPoint }}</span>
            </v-chip>
          </v-flex>
          <v-spacer></v-spacer>
          <v-flex lg1><v-chip large class="mr-16" color="#02754B">
              <span class="pl-5 pr-5 belate">
                Start date</span>
            </v-chip></v-flex>
          <v-flex lg1>
            <v-select @change="loadData()" v-model="startDay" placeholder="วัน" :items="day" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
          <v-flex lg2>
            <v-select @change="loadData()" v-model="startMonth" item-value="key" placeholder="เดือน" :items="month"
              item-text="name" outlined hide-details class="sl-mobile mb-3"></v-select>
          </v-flex>
          <v-flex lg1>
            <v-select @change="loadData()" v-model="startYear" placeholder="ปี" :items="years" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
          <v-flex class="ml-3 mr-1" lg1>
            <v-select @change="loadData()" v-model="startHour" :items="hour" placeholder="ชั่วโมง" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
          <h1>:</h1>
          <v-flex lg1 class="ml-1">
            <v-select @change="loadData()" v-model="startMin" placeholder="นาที" :items="minute" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
        </v-layout>

        <v-layout>
          <v-spacer></v-spacer>
          <v-flex lg1><v-chip large class="mr-16" color="#02754B">
              <span class="pl-5 pr-5 belate">
                End date</span>
            </v-chip>
          </v-flex>
          <v-flex lg1>
            <v-select @change="loadData()" v-model="endDay" placeholder="วัน" :items="day" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
          <v-flex lg2>
            <v-select @change="loadData()" v-model="endMonth" item-value="key" placeholder="เดือน" :items="month"
              item-text="name" outlined hide-details class="sl-mobile mb-3"></v-select>
          </v-flex>
          <v-flex lg1>
            <v-select @change="loadData()" v-model="endYear" placeholder="ปี" :items="years" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
          <v-flex class="ml-3 mr-1" lg1>
            <v-select @change="loadData()" v-model="endHour" :items="hour" placeholder="ชั่วโมง" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
          <h1>:</h1>
          <v-flex lg1 class="ml-1">
            <v-select @change="loadData()" v-model="endMin" placeholder="นาที" :items="minute" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
        </v-layout>

        <v-container>
          <v-layout class="pl-5 pr-5">
            <v-flex lg6 class="pa-1">
              <!-- <viewvideo :urlLiveView="urlVideoLT" :height="height"></viewvideo> -->
              <div style="width: 50rem;height: 30rem;">
                <video id="videoLT" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto"
                  poster="@/assets/img/No signal.png">
                  <source id="sourcevideoLT" :src="urlVideoLT" type="application/x-mpegURL">
                </video>
                <v-flex offset-lg8 lg4 md1><v-select :disabled="true" v-model="cameraLT" :items="listCamera"
                    item-value="code" item-text="code" flat hide-details dense solo
                    placeholder="กล้อง 1"></v-select></v-flex>
              </div>
            </v-flex>

            <v-flex lg6 class=" pa-1">
              <!-- <viewvideo :urlLiveView="urlVideoLT" :height="height"></viewvideo> -->
              <div style="width: 50rem;height: 30rem;">
                <video id="videoRT" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto"
                  poster="@/assets/img/No signal.png">
                  <source :src="urlVideoRT" type="application/x-mpegURL">
                </video>
                <v-flex offset-lg8 lg4 md1><v-select :disabled="true" v-model="cameraRT" :items="listCamera"
                    item-value="code" item-text="code" flat hide-details dense solo
                    placeholder="กล้อง 1"></v-select></v-flex>
              </div>
            </v-flex>
          </v-layout>
          <br /><br />
          <v-layout class="pl-5 pr-5">
            <v-flex lg6 class="pa-1">
              <!-- <viewvideo :urlLiveView="urlVideoLT" :height="height"></viewvideo> -->
              <div style="width: 50rem;height: 30rem;">
                <video id="videoLB" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto"
                  poster="@/assets/img/No signal.png">
                  <source :src="urlVideoLB" type="application/x-mpegURL">
                </video>
                <v-flex offset-lg8 lg4 md1><v-select :disabled="true" v-model="cameraLB" :items="listCamera"
                    item-value="code" item-text="code" flat hide-details dense solo
                    placeholder="กล้อง 1"></v-select></v-flex>
              </div>
            </v-flex>
            <v-flex lg6 class="pa-1">
              <!-- <viewvideo :urlLiveView="urlVideoLT" :height="height"></viewvideo> -->
              <div style="width: 50rem;height: 30rem;">
                <video id="videoRB" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto"
                  poster="@/assets/img/No signal.png">
                  <source :src="urlVideoRB" type="application/x-mpegURL">
                </video>
                <v-flex offset-lg8 lg4 md1><v-select :disabled="true" v-model="cameraRB" :items="listCamera"
                    item-value="code" item-text="code" flat hide-details dense solo
                    placeholder="กล้อง 1"></v-select></v-flex>
              </div>
            </v-flex>
          </v-layout>
          <v-row></v-row>
          <!-- <v-layout class="pr-3"><v-spacer></v-spacer><v-flex lg1 md1 ><v-select :items="listCamera" item-text="code" flat hide-details dense solo placeholder="กล้อง 1"></v-select></v-flex></v-layout> -->
        </v-container>
      </v-container>
    </v-content>
    <v-content class="pa-1" v-else>
      <v-container class="pl-5 pr-5">
        <v-chip @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
          <v-icon large color="red">mdi-chevron-left</v-icon>
          <span class="text-left headerback">Back</span>
        </v-chip>
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext-mobile">ดูสภาพการจราจรย้อนหลัง</span>
        </v-chip>
        <v-layout>
          <v-flex>
            <v-chip large class="ma-2 " color="#02754B">
              <span class="pl-5 pr-5 belate">
                จุดติดตั้ง : {{ textCheckPoint }}</span>
            </v-chip>
          </v-flex>
          <v-spacer></v-spacer>
          <v-flex lg3><v-chip large class="mr-16" color="#02754B">
              <span class="pl-5 pr-5 belate">
                Start date</span>
            </v-chip></v-flex>
          <v-flex lg1>
            <v-select @change="loadData()" v-model="startDay" placeholder="วัน" :items="day" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
          <v-flex lg2>
            <v-select @change="loadData()" v-model="startMonth" item-value="key" placeholder="เดือน" :items="month"
              item-text="name" outlined hide-details class="sl-mobile mb-3"></v-select>
          </v-flex>
          <v-flex lg1>
            <v-select @change="loadData()" v-model="startYear" placeholder="ปี" :items="years" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
          <v-flex class="ml-3 mr-1" lg1>
            <v-select @change="loadData()" v-model="startHour" :items="hour" placeholder="ชั่วโมง" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
          <h1>:</h1>
          <v-flex lg1 class="ml-1">
            <v-select @change="loadData()" v-model="startMin" placeholder="นาที" :items="minute" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
        </v-layout>

        <v-layout>
          <v-spacer></v-spacer>
          <v-flex lg3><v-chip large class="mr-16" color="#02754B">
              <span class="pl-5 pr-5 belate">
                End date</span>
            </v-chip>
          </v-flex>
          <v-flex lg1>
            <v-select @change="loadData()" v-model="endDay" placeholder="วัน" :items="day" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
          <v-flex lg2>
            <v-select @change="loadData()" v-model="endMonth" item-value="key" placeholder="เดือน" :items="month"
              item-text="name" outlined hide-details class="sl-mobile mb-3"></v-select>
          </v-flex>
          <v-flex lg1>
            <v-select @change="loadData()" v-model="endYear" placeholder="ปี" :items="years" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
          <v-flex class="ml-3 mr-1" lg1>
            <v-select @change="loadData()" v-model="endHour" :items="hour" placeholder="ชั่วโมง" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
          <h1>:</h1>
          <v-flex lg1 class="ml-1">
            <v-select @change="loadData()" v-model="endMin" placeholder="นาที" :items="minute" outlined hide-details
              class="sl-mobile mb-3"></v-select>
          </v-flex>
        </v-layout>
        <v-container>
          <v-layout class="pl-5 pr-5">
            <v-flex class="pa-1">
              <!-- <viewvideo :urlLiveView="urlVideoLT" :height="height"></viewvideo> -->
              <div style="width: 50rem;height: 30rem;">
                <video id="videoLT" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto">
                  <source id="sourcevideoLT" :src="urlVideoLT" type="application/x-mpegURL">
                </video>
                <v-flex offset-lg8 lg4 md1><v-select :disabled="true" v-model="cameraLT" :items="listCamera"
                    item-value="code" item-text="code" flat hide-details dense solo
                    placeholder="กล้อง 1"></v-select></v-flex>
              </div>
            </v-flex>
          </v-layout> <br /><br /><v-layout>
            <v-flex class=" pa-1">
              <!-- <viewvideo :urlLiveView="urlVideoLT" :height="height"></viewvideo> -->
              <div style="width: 50rem;height: 30rem;">
                <video id="videoRT" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto">
                  <source :src="urlVideoRT" type="application/x-mpegURL">
                </video>
                <v-flex offset-lg8 lg4 md1><v-select :disabled="true" v-model="cameraRT" :items="listCamera"
                    item-value="code" item-text="code" flat hide-details dense solo
                    placeholder="กล้อง 1"></v-select></v-flex>
              </div>
            </v-flex>
          </v-layout>
          <br /><br />
          <v-layout class="pl-5 pr-5">
            <v-flex class="pa-1">
              <!-- <viewvideo :urlLiveView="urlVideoLT" :height="height"></viewvideo> -->
              <div style="width: 50rem;height: 30rem;">
                <video id="videoLB" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto">
                  <source :src="urlVideoLB" type="application/x-mpegURL">
                </video>
                <v-flex offset-lg8 lg4 md1><v-select :disabled="true" v-model="cameraLB" :items="listCamera"
                    item-value="code" item-text="code" flat hide-details dense solo
                    placeholder="กล้อง 1"></v-select></v-flex>
              </div>
            </v-flex>
          </v-layout> <br /><br /><v-layout>
            <v-flex class="pa-1">
              <!-- <viewvideo :urlLiveView="urlVideoLT" :height="height"></viewvideo> -->
              <div style="width: 50rem;height: 30rem;">
                <video id="videoRB" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto">
                  <source :src="urlVideoRB" type="application/x-mpegURL">
                </video>
                <v-flex offset-lg8 lg4 md1><v-select :disabled="true" v-model="cameraRB" :items="listCamera"
                    item-value="code" item-text="code" flat hide-details dense solo
                    placeholder="กล้อง 1"></v-select></v-flex>
              </div>
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
import viewvideo from "../components/view-video.vue";
import headerbar from "../components/header-bar.vue";
import "video.js/dist/video-js.css";
// import { videoPlayer } from "vue-video-player";
import videojs from 'video.js'
//import 'videojs-contrib-hls'
import "@videojs/http-streaming"
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
    viewvideo,
    headerbar,
    videojs,
  },
  data() {
    return {
      onProgress: false,
      player: null,
      playerLT: null,
      day: [
        "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"
      ],
      month: [
        { key: '01', name: "มกราคม" },
        { key: '02', name: "กุมภาพันธ์" },
        { key: '03', name: "มีนาคม" },
        { key: '04', name: "เมษายน" },
        { key: '05', name: "พฤษภาคม" },
        { key: '06', name: "มิถุนายน" },
        { key: '07', name: "กรกฎาคม" },
        { key: '08', name: "สิงหาคม" },
        { key: '09', name: "กันยายน" },
        { key: '10', name: "ตุลาคม" },
        { key: '11', name: "พฤศจิกายน" },
        { key: '12', name: "ธันวาคม" }
      ],
      hour: [
        "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"
      ],
      minute: [
        "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"
      ],
      height: '450px',
      drawer: true,
      textCheckPoint: "",
      listCamera: [],
      myPath: [],
      cameraLB: "",
      cameraLT: "",
      cameraRT: "",
      cameraRB: "",
      urlVideoLB: "",
      urlVideoLT: "",
      urlVideoRB: "",
      urlVideoRT: "",
      startDay: '', endDay: '',
      startMonth: '', endMonth: '',
      startYear: '', endYear: '',
      startHour: '', endHour: '',
      startMin: '', endMin: ''
    }
  },
  computed: {
    years() {
      const year = new Date().getFullYear();
      return Array.from({ length: year - 2000 }, (value, index) => 2001 + index);
    },
  },
  methods: {
    gobackpage() {
      this.$router.push({ path: "/traffic/present" })

    },
    loadData() {
      if (this.startDay == '' || this.endDay == '' ||
        this.startMonth == '' || this.endMonth == '' ||
        this.startYear == '' || this.endYear == '' ||
        this.startHour == '' || this.endHour == '' ||
        this.startMin == '' || this.endMin == '') {

        //   Toast.fire({
        //   icon: "error",
        //   title: "กรุณากรอกข้อมูลใหเครบ",
        // });

      } else if (this.startDay !== '' && this.endDay !== '' &&
        this.startMonth !== '' && this.endMonth !== '' &&
        this.startYear !== '' && this.endYear !== '' &&
        this.startHour !== '' && this.endHour !== '' &&
        this.startMin !== '' && this.endMin !== '') {
        const startTime = this.startYear + '-' + this.startMonth + '-' + this.startDay + 'T' + this.startHour + ':' + this.startMin + ':00'
        const endTime = this.endYear + '-' + this.endMonth + '-' + this.endDay + 'T' + this.endHour + ':' + this.endMin + ':00'
        // console.log(startTime,endTime);
        this.getDataLiveView(startTime, endTime);
      }
    },
    reload() {
      // console.log("reload");
      this.$router.go();
    },
    playVideo(videoSource) {
      var videoElm = document.getElementById('videoLT');
      var videoSourceElm = document.getElementById('sourcevideoLT');
      console.log(videoElm)

      if (videoElm !== null) {
        videoElm.src = videoSource
      }

      //  videoSourceElm.src = videoSource;
      //  //videoSourceElm.type = type;

      //   // videoElm.load();
      //   videoElm.play();
    },
    changeCamera(param) {
      // this.onProgress = true
      let camera = param === 'lt' ? this.cameraLT : param === 'lb' ? this.cameraLB : param === 'rt' ? this.cameraRT : this.cameraRB
      let session_data = localStorage.getItem("session");
      this.myPath = this.$route.path.split("/");
      //console.log(this.listCamera);
      let url = baseUrl.ipServer + "/traffic-view/playback?checkpoint=" + this.myPath[3] + "&camera=" + camera
      this.axios.get(url, { headers: { session: session_data } })
        .then((response) => {
          // console.log(response.data);
          if (response.data.status_code === 200) {
            console.log(response.data.data.url);
            if (param === 'lt') {
              this.urlVideoLT = response.data.data.url
              this.playVideo(this.urlVideoLT)
              setTimeout(() => {
                this.initLT()

              }, 2000);
            } else if (param === 'lb') {
              this.urlVideoLB = response.data.data.url
              setTimeout(() => {

                this.initLB()
              }, 2000);
            } else if (param === 'rb') {
              this.urlVideoRB = response.data.data.url
              setTimeout(() => {

                this.initRB()

              }, 2000);
            } else {
              this.urlVideoRT = response.data.data.url
              setTimeout(() => {

                this.initRT()

              }, 2000);
            }




            console.log(this.urlVideoRT, " this.urlVideoRT");


            this.onProgress = false
          }
        });
    },
    initLT() {


      // Player initialization 
      this.$nextTick(() => {

        this.player = videojs('videoLT', {

          bigPlayButton: false,
          textTrackDisplay: false,
          posterImage: true,
          errorDisplay: false,
          controlBar: false,
          muted: true // Mute mode 、、 Solve the problem of first page loading and playing .
        }, function () {

          this.play() // Auto play 
        })
      })
    },

    initLB() {


      // Player initialization 
      this.$nextTick(() => {

        this.player = videojs('videoLB', {

          bigPlayButton: false,
          textTrackDisplay: false,
          posterImage: true,
          errorDisplay: false,
          controlBar: false,
          muted: true // Mute mode 、、 Solve the problem of first page loading and playing .
        }, function () {

          this.play() // Auto play 
        })
      })
    },
    initRT() {


      // Player initialization 
      this.$nextTick(() => {

        this.player = videojs('videoRT', {

          bigPlayButton: false,
          textTrackDisplay: false,
          posterImage: true,
          errorDisplay: false,
          controlBar: false,
          muted: true // Mute mode 、、 Solve the problem of first page loading and playing .
        }, function () {

          this.play() // Auto play 
        })
      })
    },

    initRB() {


      // Player initialization 
      this.$nextTick(() => {

        this.player = videojs('videoRB', {

          bigPlayButton: false,
          textTrackDisplay: false,
          posterImage: true,
          errorDisplay: false,
          controlBar: false,
          muted: true // Mute mode 、、 Solve the problem of first page loading and playing .
        }, function () {

          this.play() // Auto play 
        })
      })
    },
    confirm() {
      this.$router.push({ path: '/traffic-detail' });
    },
    headerbar(drawer) {
      console.log("hhh", drawer);
      this.drawer = drawer;
    },
    getDataLiveView(start, end) {

      let session_data = localStorage.getItem("session");
      this.myPath = this.$route.path.split("/");

      if (this.listCamera.length > 4) {
        this.listCamera = this.listCamera.slice(0, 4)

        for (let cameraCodeIndex = 0; cameraCodeIndex < this.listCamera.length; cameraCodeIndex++) {
          let url = baseUrl.ipServer + "/traffic-view/playback?checkpoint=" + this.myPath[3] + "&camera=" + this.listCamera[cameraCodeIndex].code + "&start_time=" + start + "&end_time=" + end
          this.axios.get(url, { headers: { session: session_data } })
            .then((response) => {
              if (response.data.status_code === 200) {
                if (cameraCodeIndex == 0) {
                  this.urlVideoLB = response.data.data.url
                } else if (cameraCodeIndex == 1) {
                  this.urlVideoLT = response.data.data.url
                } else if (cameraCodeIndex == 2) {
                  this.urlVideoRB = response.data.data.url
                } else if (cameraCodeIndex == 3) {
                  this.urlVideoRT = response.data.data.url
                }
                setTimeout(() => {
                  this.initLT()
                  this.initRT()
                  this.initRB()
                  this.initLB()
                }, 2000);
              } else {
                Toast.fire({
                  icon: "error",
                  title: "",
                });
              }
            }).catch((error) => {
              console.log(error);
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
                title: "",
              });
            });
        }
      } else if (this.listCamera.length < 4) {
        const diff = 4 - this.listCamera.length
        for (let number_ = 0; number_ < diff; number_++) {
          this.listCamera.push(this.listCamera[0])
        }

        for (let cameraCodeIndex = 0; cameraCodeIndex < this.listCamera.length; cameraCodeIndex++) {
          let url = baseUrl.ipServer + "/traffic-view/playback?checkpoint=" + this.myPath[3] + "&camera=" + this.listCamera[cameraCodeIndex].code + "&start_time=" + start + "&end_time=" + end
          this.axios.get(url, { headers: { session: session_data } })
            .then((response) => {
              if (response.data.status_code === 200) {
                if (cameraCodeIndex == 0) {
                  this.urlVideoLB = response.data.data.url
                } else if (cameraCodeIndex == 1) {
                  this.urlVideoLT = response.data.data.url
                } else if (cameraCodeIndex == 2) {
                  this.urlVideoRB = response.data.data.url
                } else if (cameraCodeIndex == 3) {
                  this.urlVideoRT = response.data.data.url
                }
                setTimeout(() => {
                  this.initLT()
                  this.initRT()
                  this.initRB()
                  this.initLB()
                }, 2000);
              } else {
                Toast.fire({
                  icon: "error",
                  title: "",
                });
              }
            }).catch((error) => {
              console.log(error);
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
                title: "",
              });
            });
        }
      } else if (this.listCamera.length == 4) {
        for (let cameraCodeIndex = 0; cameraCodeIndex < this.listCamera.length; cameraCodeIndex++) {
          let url = baseUrl.ipServer + "/traffic-view/playback?checkpoint=" + this.myPath[3] + "&camera=" + this.listCamera[cameraCodeIndex].code + "&start_time=" + start + "&end_time=" + end
          this.axios.get(url, { headers: { session: session_data } })
            .then((response) => {
              if (response.data.status_code === 200) {
                if (cameraCodeIndex == 0) {
                  this.urlVideoLB = response.data.data.url
                } else if (cameraCodeIndex == 1) {
                  this.urlVideoLT = response.data.data.url
                } else if (cameraCodeIndex == 2) {
                  this.urlVideoRB = response.data.data.url
                } else if (cameraCodeIndex == 3) {
                  this.urlVideoRT = response.data.data.url
                }
                setTimeout(() => {
                  this.initLT()
                  this.initRT()
                  this.initRB()
                  this.initLB()
                }, 2000);
              } else {
                Toast.fire({
                  icon: "error",
                  title: "",
                });
              }
            }).catch((error) => {
              console.log(error);
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
                title: "",
              });
            });
        }
      }

    },
    getDataCameraCode() {
      // this.$router.go(0)
      let session_data = localStorage.getItem("session");
      this.myPath = this.$route.path.split("/");
      // console.log(myPath);
      //  let pathHaveCheckPoint = "/"+myPath[1]+"/";
      let url = baseUrl.ipServer + "/traffic-view/checkpoint-camera?checkpoint=" + this.myPath[3]
      this.axios.get(url, { headers: { session: session_data } })
        .then((response) => {
          console.log(response);
          if (response.data.status_code === 200) {
            this.textCheckPoint = response.data.data.checkpoint.short_name
            this.listCamera = response.data.data.cameras
            let listcam = response.data.data.cameras
            if (response.data.data.cameras.length >= 4) {
              this.cameraLB = response.data.data.cameras[0].code
              this.cameraLT = response.data.data.cameras[1].code
              this.cameraRT = response.data.data.cameras[2].code
              this.cameraRB = response.data.data.cameras[3].code
            } else {
              const diff = 4 - this.listCamera.length
              for (let number_ = 0; number_ < diff; number_++) {
                this.listCamera.push(this.listCamera[0])
              }

              this.cameraLB = listcam[0].code
              this.cameraLT = listcam[1].code
              this.cameraRT = listcam[2].code
              this.cameraRB = listcam[3].code
            }

            //this.getDataLiveView();
          }
        });
    }
  },
  mounted() {

    this.getDataCameraCode();
    if (this.player != null) {

      this.player.dispose() // dispose() Will delete Dom Elements 
    }
  },
  beforeDestroy() {

    if (this.player != null) {

      this.player.dispose() // dispose() Will delete Dom Elements 
    }
  }
};
</script>
<style>
.belate {
  font-weight: 600;
  font-size: 20px;
  color: #FFFFFF;

}

.sl-mobile {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
}

.text-pointer {
  font-weight: 600;
  font-size: 25px;
  color: #FFFFFF;
  overflow: auto;
  padding: 5%;
}

.text-pointer-mobile {
  font-weight: 600;
  font-size: 15px;
  color: #FFFFFF;
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
}</style>
