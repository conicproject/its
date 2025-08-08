<template>
    <v-app id="bg" >
      <sidebar :sideNav="drawer" @loadPage="getDataCameraCode(), reload()"></sidebar>
      <headerbar @close="headerbar" class="nav-header"></headerbar>
      <v-overlay :value="onProgress">
        <v-progress-circular indeterminate size="100" width="7"></v-progress-circular>
      </v-overlay>
      <v-content class="ps-16 pe-16 pb-16 pt-8" v-if="$vuetify.breakpoint.width > 1025">
        <v-container class="pl-16">
          <v-chip large class="ma-2" color="#02754B">
            <span class="pl-5 pr-5 headertext">ดูสภาพการจราจร</span>
          </v-chip>
          <v-layout v-if="myPath[2] === 'belated'">
            <v-flex>
              <v-chip large class="ma-2 " color="#02754B">
                <span class="pl-5 pr-5 belate">
                  จุดติดตั้ง : {{ textCheckPoint }}</span>
              </v-chip>
            </v-flex>
            <v-flex lg1>
              <v-select placeholder="วัน" :items="day" outlined hide-details class="sl-mobile mb-3"></v-select>
            </v-flex>
            <v-flex lg2>
              <v-select placeholder="เดือน" :items="month" item-text="name" outlined hide-details class="sl-mobile mb-3">
              </v-select>
            </v-flex>
            <v-flex lg1>
              <v-select placeholder="ปี" :items="years" outlined hide-details class="sl-mobile mb-3"></v-select>
            </v-flex>
            <v-flex class="ml-3 mr-1" lg1>
              <v-select :items="hour" placeholder="ชั่วโมง" outlined hide-details class="sl-mobile mb-3"></v-select>
            </v-flex>
            <h1>:</h1>
            <v-flex lg1 class="ml-1">
              <v-select placeholder="นาที" :items="minute" outlined hide-details class="sl-mobile mb-3"></v-select>
            </v-flex>
  
          </v-layout>
          <v-layout v-else>
            <v-flex class="text-center">
              <v-chip large class="ma-2" color="#02754B">
                <span class="pl-5 pr-5 text-pointer">จุดติดตั้ง : {{ textCheckPoint }}</span>
              </v-chip>
            </v-flex>
          </v-layout>
          <v-container>
            <v-layout class="pl-5 pr-5">
              <v-flex lg6 class="pa-1">
                <!-- <viewvideo :urlLiveView="urlVideoLT" :height="height"></viewvideo> -->
                <div style="width: 50rem;height: 30rem;">
                  <video id="videoLT" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto">
                    <source id="sourcevideoLT" :src="urlVideoLT" type="application/x-mpegURL">
                  </video>
                  <v-flex offset-lg8 lg4 md1>
                    <v-select :disabled="false" v-model="cameraLT" :items="listCamera" item-value="code" item-text="code"
                      flat hide-details dense solo placeholder="กล้อง 1" @change="changeRoute"></v-select>
                  </v-flex>
                </div>
              </v-flex>
  
              <v-flex lg6 class=" pa-1">
                <!-- <viewvideo :urlLiveView="urlVideoLT" :height="height"></viewvideo> -->
                <div style="width: 50rem;height: 30rem;">
                  <video id="videoRT" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto">
                    <source :src="urlVideoRT" type="application/x-mpegURL">
                  </video>
                  <v-flex offset-lg8 lg4 md1>
                    <v-select :disabled="true" v-model="cameraRT" :items="listCamera" item-value="code" item-text="code"
                      flat hide-details dense solo placeholder="กล้อง 1"></v-select>
                  </v-flex>
                </div>
              </v-flex>
            </v-layout>
            <br /><br />
            <v-layout class="pl-5 pr-5">
              <v-flex lg6 class="pa-1">
                <!-- <viewvideo :urlLiveView="urlVideoLT" :height="height"></viewvideo> -->
                <div style="width: 50rem;height: 30rem;">
                  <video id="videoLB" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto">
                    <source :src="urlVideoLB" type="application/x-mpegURL">
                  </video>
                  <v-flex offset-lg8 lg4 md1>
                    <v-select :disabled="true" v-model="cameraLB" :items="listCamera" item-value="code" item-text="code"
                      flat hide-details dense solo placeholder="กล้อง 1"></v-select>
                  </v-flex>
                </div>
              </v-flex>
              <v-flex lg6 class="pa-1">
                <!-- <viewvideo :urlLiveView="urlVideoLT" :height="height"></viewvideo> -->
                <div style="width: 50rem;height: 30rem;">
                  <video id="videoRB" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto">
                    <source :src="urlVideoRB" type="application/x-mpegURL">
                  </video>
                  <v-flex offset-lg8 lg4 md1>
                    <v-select :disabled="true" v-model="cameraRB" :items="listCamera" item-value="code" item-text="code"
                      flat hide-details dense solo placeholder="กล้อง 1"></v-select>
                  </v-flex>
                </div>
              </v-flex>
            </v-layout>
            <!-- <v-row></v-row> -->
            <!-- <v-layout class="pr-3"><v-spacer></v-spacer><v-flex lg1 md1 ><v-select :items="listCamera" item-text="code" flat hide-details dense solo placeholder="กล้อง 1"></v-select></v-flex></v-layout> -->
          </v-container>
        </v-container>
      </v-content>
      <v-content class="pa-1" v-else>
        <v-container class="pl-5 pr-5">
          <v-chip large class="ma-2" color="#02754B">
            <span class="pl-5 pr-5 headertext-mobile">ดูสภาพการจราจร</span>
          </v-chip>
          <v-layout v-if="myPath[2] === 'belated'">
            <v-flex>
              <v-chip large class="ma-2 " color="#02754B">
                <span class="pl-5 pr-5 belate">
                  จุดติดตั้ง : {{ textCheckPoint }}</span>
              </v-chip>
            </v-flex>
            <v-flex lg1>
              <v-select placeholder="วัน" :items="day" outlined hide-details class="sl-mobile mb-3"></v-select>
            </v-flex>
            <v-flex lg2>
              <v-select placeholder="เดือน" :items="month" item-text="name" outlined hide-details class="sl-mobile mb-3">
              </v-select>
            </v-flex>
            <v-flex lg1>
              <v-select placeholder="ปี" :items="years" outlined hide-details class="sl-mobile mb-3"></v-select>
            </v-flex>
            <v-flex class="ml-3 mr-1" lg1>
              <v-select :items="hour" placeholder="ชั่วโมง" outlined hide-details class="sl-mobile mb-3"></v-select>
            </v-flex>
            <h1>:</h1>
            <v-flex lg1 class="ml-1">
              <v-select placeholder="นาที" :items="minute" outlined hide-details class="sl-mobile mb-3"></v-select>
            </v-flex>
  
          </v-layout>
          <v-layout v-else>
            <v-flex class="text-center">
              <v-chip large class="ma-2" color="#02754B">
                <span class="pl-5 pr-5 text-pointer">จุดติดตั้ง : {{ textCheckPoint }}</span>
              </v-chip>
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
                  <v-flex offset-lg8 lg4 md1>
                    <v-select :disabled="true" v-model="cameraLT" :items="listCamera" item-value="code" item-text="code"
                      flat hide-details dense solo placeholder="กล้อง 1"></v-select>
                  </v-flex>
                </div>
              </v-flex>
            </v-layout> <br /><br />
            <v-layout>
              <v-flex class=" pa-1">
                <!-- <viewvideo :urlLiveView="urlVideoLT" :height="height"></viewvideo> -->
                <div style="width: 50rem;height: 30rem;">
                  <video id="videoRT" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto">
                    <source :src="urlVideoRT" type="application/x-mpegURL">
                  </video>
                  <v-flex offset-lg8 lg4 md1>
                    <v-select :disabled="true" v-model="cameraRT" :items="listCamera" item-value="code" item-text="code"
                      flat hide-details dense solo placeholder="กล้อง 1"></v-select>
                  </v-flex>
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
                  <v-flex offset-lg8 lg4 md1>
                    <v-select :disabled="true" v-model="cameraLB" :items="listCamera" item-value="code" item-text="code"
                      flat hide-details dense solo placeholder="กล้อง 1"></v-select>
                  </v-flex>
                </div>
              </v-flex>
            </v-layout> <br /><br />
            <v-layout>
              <v-flex class="pa-1">
                <!-- <viewvideo :urlLiveView="urlVideoLT" :height="height"></viewvideo> -->
                <div style="width: 50rem;height: 30rem;">
                  <video id="videoRB" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto">
                    <source :src="urlVideoRB" type="application/x-mpegURL">
                  </video>
                  <v-flex offset-lg8 lg4 md1>
                    <v-select :disabled="true" v-model="cameraRB" :items="listCamera" item-value="code" item-text="code"
                      flat hide-details dense solo placeholder="กล้อง 1"></v-select>
                  </v-flex>
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
  import checkDevice from "../components/check-device.vue";
  import "video.js/dist/video-js.css";
  // import { videoPlayer } from "vue-video-player";
  import videojs from 'video.js'
  //import 'videojs-contrib-hls'
  import "@videojs/http-streaming"
  export default {
    components: {
      sidebar,
      viewvideo,
      headerbar,
      videojs,
        checkDevice
    },
    data() {
      return {
        onProgress: false,
        player: null,
        playerLT: null,
        day: [
          "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"
        ],
        month: [
          { key: 1, name: "มกราคม" },
          { key: 2, name: "กุมภาพันธ์" },
          { key: 3, name: "มีนาคม" },
          { key: 4, name: "เมษายน" },
          { key: 5, name: "พฤษภาคม" },
          { key: 6, name: "มิถุนายน" },
          { key: 7, name: "กรกฎาคม" },
          { key: 8, name: "สิงหาคม" },
          { key: 9, name: "กันยายน" },
          { key: 10, name: "ตุลาคม" },
          { key: 11, name: "พฤศจิกายน" },
          { key: 12, name: "ธันวาคม" }
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
      }
    },
    computed: {
      years() {
        const year = new Date().getFullYear();
        return Array.from({ length: year - 2000 }, (value, index) => 2001 + index);
      },
    },
    methods: {
      reload() {
        console.log("reload");
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
        console.log(this.listCamera);
        let url = baseUrl.ipServer + "/traffic-view/live?checkpoint=" + this.myPath[3] + "&camera=" + camera
        this.axios.get(url, { headers: { session: session_data } })
          .then((response) => {
            console.log(response.data);
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
      
      testing() {
        this.player.src({
          src: this.urlVideoLB,
          type: 'video/mp4'
        })
        
        this.player.play()
  
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
        this.drawer = drawer;
      },
      getDataLiveView() {
        //this.onProgress = true
        // this.urlVideoLB=""
        // this.urlVideoLT=""
        // this.urlVideoRB=""
        // this.urlVideoRT=""
        //this.player = null
        // this.player.dispose()
        //this.$router.go()
  
        let session_data = localStorage.getItem("session");
        this.myPath = this.$route.path.split("/");
        let cameraCodeIndex = this.listCamera[0].code
        let url = baseUrl.ipServer + "/traffic-view/live?checkpoint=" + this.myPath[3] + "&camera=" + cameraCodeIndex
  
        this.axios.get(url, { headers: { session: session_data } })
          .then((response) => {
            if (response.data.status_code === 200) {
              this.urlVideoLB = response.data.data.url
              this.urlVideoLT = response.data.data.url
              this.urlVideoRB = response.data.data.url
              this.urlVideoRT = response.data.data.url
            }
  
            setTimeout(() => {
              this.initLT()
              this.initRT()
              this.initRB()
              this.initLB()
            }, 2000);
          })
  
  
        // for (let cameraCodeIndex = 0; cameraCodeIndex < this.listCamera.length; cameraCodeIndex++) {
        //     let url = baseUrl.ipServer + "/traffic-view/live?checkpoint=" + this.myPath[3] + "&camera=" + this.listCamera[cameraCodeIndex].code
        //     this.axios.get(url, { headers: { session: session_data } })
        //       .then((response) => {
        //         if (response.data.status_code === 200) {
        //           if (cameraCodeIndex == 0) {
        //             this.urlVideoLB = response.data.data.url
        //           } else if (cameraCodeIndex == 1) {
        //             this.urlVideoLT = response.data.data.url
        //           } else if (cameraCodeIndex == 2) {
        //             this.urlVideoRB = response.data.data.url
        //           } else if (cameraCodeIndex == 3) {
        //             this.urlVideoRT = response.data.data.url
        //           }
        //           setTimeout(() => {
        //             this.initLT()
        //             this.initRT()
        //             this.initRB()
        //             this.initLB()
        //           }, 2000);
        //         }
        //       });
        // }
  
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
  
              this.getDataLiveView();
            }
          });
      },
      changeRoute(selectObj) {
          console.log("Object Name", selectObj)
          console.log("Checkpoint id",this.myPath[3])
  
          let src = ''
          let session_data = localStorage.getItem("session");
  
          let url = baseUrl.ipServer + "/traffic-view/live?checkpoint=" + this.myPath[3] + "&camera=" + selectObj
          this.axios.get(url, { headers: { session: session_data } })
            .then((response) => {
                if (response.data.status_code === 200) {
                  console.log("Api url response", response.data.data.url)
  
                  this.urlVideoLB = 'http://www.w3schools.com/html/mov_bbb.mp4'
                  this.testing() 
                }
              })
  
          // if (!videoElm.paused) {
          //       videoElm.pause();
          //   }
  
          // this.urlVideoLT = 'http://www.w3schools.com/html/mov_bbb.mp4';
          // this.type_test = 'video/mp4'
       
  
          // let session_data = localStorage.getItem("session");
      
          // this.axios.get(url, { headers: { session: session_data } })
          // .then((response) => {
          //   if (response.data.status_code === 200) {
              
          //   }
          // })
      }
    },
    mounted() {
  
      this.getDataCameraCode();
      if (this.player != null) {
  
        this.player.dispose() // dispose() Will delete Dom Elements 
      }
    },
    beforeDestroy() {
  
      // if (this.player != null) {
  
      //   this.player.dispose() // dispose() Will delete Dom Elements 
      // }
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
  </style>
  