<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer" @loadPageTraffic="reload()"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="onProgress">
      <v-progress-circular indeterminate size="100" width="7"></v-progress-circular>
    </v-overlay>
    <v-content class="pl-3">
      <v-container class="pl-1 pr-1">
        <v-chip @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
          <v-icon large color="red">mdi-chevron-left</v-icon>
          <span class="text-left headerback">Back</span>
        </v-chip>
        <v-chip large class="ma-2" color="#02754B" v-if="$vuetify.breakpoint.width > 1025">
          <span class="pl-5 pr-5 headertext">ดูสภาพการจราจร</span>
          <!-- <div>
              <button @click="switchPlayer">Play</button> &nbsp;
              <input type="text" v-model="src" style="width: 500px">
          </div> -->
        </v-chip>
        <v-chip large class="ma-2" color="#02754B" v-else>
          <span class="pl-5 pr-5 headertext-mobile">ดูสภาพการจราจร</span>

        </v-chip>
        <v-layout>
          <v-flex lg4 class="text-left">
            <v-card large class="ma-2 elevation-0" color="#02754B">
              <!-- <span class="pl-5 pr-5 text-pointer">จุดติดตั้ง : {{checkPoint.name}}</span> -->
              <v-select class="select" height="54" v-model="selectCheckpoint" :items="listCheckPoint" item-text="name"
                item-value="id" hide-details required dense outlined dark
                @change="fn_changCheckpoint(selectCheckpoint)"></v-select>
            </v-card>
          </v-flex>
        </v-layout>
        <v-container>
          <v-layout v-if="$vuetify.breakpoint.width > 1025">
            <v-flex lg6 xs12 class="pa-1">
              <div style="width: 100%;height: 30rem;">
                <!-- <div style="overflow: hidden; width: 100%;height:40rem;" v-if="isPublic == true"><iframe frameBorder="0" :src="`${cameraPublic1}`" style="width: 100%;height: 100%;" title="Iframe Example" allow="autoplay; encrypted-media" allowfullscreen></iframe></div>
                  <video-player ref="videoPlayer"
                      style="width: 100%;height: 100%;"
                      class="video-js vjs-default-skin"
                      :options="playerOptions"
                      v-else
                      /> -->

                <video-player ref="videoPlayer" style="width: 100%;height: 100%;" class="video-js vjs-default-skin"
                  :options="playerOptions" />

                <v-flex offset-lg8 lg4 md1>
                  <v-select :disabled="false" v-model="cameraLT" :hint="`${cameraLT.code}`" :items="listCamera"
                    item-value="code" item-text="code" label="Select" flat hide-details dense solo
                    v-on:change="changeCamera1" placeholder="กล้อง 1"></v-select>
                </v-flex>
              </div>
            </v-flex>

            <v-flex lg6 xs12 class=" pa-1">
              <div style="width: 100%;height: 30rem;">
                <!-- <div style="overflow: hidden; width: 100%;height:40rem;" v-if="isPublic == true"><iframe frameBorder="0"
                    :src="`${cameraPublic2}`" style="width: 100%;height: 100%;" title="Iframe Example"
                    allow="autoplay; encrypted-media" allowfullscreen></iframe></div>
                <video-player ref="videoPlayer2" style="width: 100%;height: 100%;" class="video-js vjs-default-skin"
                  :options="playerOptions" @play="onPlayerPlay($event)" @ready="onPlayerReady($event)" v-else /> -->

                <video-player ref="videoPlayer2" style="width: 100%;height: 100%;" class="video-js vjs-default-skin"
                  :options="playerOptions" @play="onPlayerPlay($event)" @ready="onPlayerReady($event)" />

                <v-flex offset-lg8 lg4 md1>
                  <v-select :disabled="false" v-model="cameraRT" :hint="`${cameraRT.code}`" :items="listCamera"
                    item-value="code" item-text="code" label="Select" flat hide-details dense solo
                    v-on:change="changeCamera2" placeholder="กล้อง 1"></v-select>
                </v-flex>
              </div>
            </v-flex>
          </v-layout>
          <div v-else>
            <v-layout>

              <div style="width: 100%;height: 30rem;">
                <!-- <div style="overflow: hidden; width: 100%;height:40rem;" v-if="isPublic == true"><iframe frameBorder="0"
                    :src="`${cameraPublic1}`" style="width: 100%;height: 100%;" title="Iframe Example"
                    allow="autoplay; encrypted-media" allowfullscreen></iframe></div>
                <video-player ref="videoPlayer" style="width: 100%;height: 100%;" class="video-js vjs-default-skin"
                  :options="playerOptions" v-else /> -->

                <video-player ref="videoPlayer" style="width: 100%;height: 100%;" class="video-js vjs-default-skin"
                  :options="playerOptions" />

                <v-flex offset-lg8 lg4 md1>
                  <v-select :disabled="false" v-model="cameraLT" :hint="`${cameraLT.code}`" :items="listCamera"
                    item-value="code" item-text="code" label="Select" flat hide-details dense solo
                    v-on:change="changeCamera1" placeholder="กล้อง 1"></v-select>
                </v-flex>
              </div>

            </v-layout>
            <br /><br />
            <v-layout>

              <div style="width: 100%;height: 30rem;">
                <!-- <div style="overflow: hidden; width: 100%;height:40rem;" v-if="isPublic == true"><iframe frameBorder="0"
                    :src="`${cameraPublic2}`" style="width: 100%;height: 100%;" title="Iframe Example"
                    allow="autoplay; encrypted-media" allowfullscreen></iframe></div>
                <video-player ref="videoPlayer2" style="width: 100%;height: 100%;" class="video-js vjs-default-skin"
                  :options="playerOptions" @play="onPlayerPlay($event)" @ready="onPlayerReady($event)" v-else /> -->

                <video-player ref="videoPlayer2" style="width: 100%;height: 100%;" class="video-js vjs-default-skin"
                  :options="playerOptions" @play="onPlayerPlay($event)" @ready="onPlayerReady($event)" />
                <v-flex offset-lg8 lg4 md1>
                  <v-select :disabled="false" v-model="cameraRT" :hint="`${cameraRT.code}`" :items="listCamera"
                    item-value="code" item-text="code" label="Select" flat hide-details dense solo
                    v-on:change="changeCamera2" placeholder="กล้อง 1"></v-select>
                </v-flex>
              </div>

            </v-layout>
          </div>
          <!-- <br /><br />
          <v-layout class="pl-5 pr-5">
            <v-flex lg6 class="pa-1">
              <div style="width: 90%;height: 30rem;">
                <video-player ref="videoPlayer3"
                  style="width: 100%;height: 100%;"
                  class="video-js vjs-default-skin"
                  :options="playerOptions"
                  @play="onPlayerPlay($event)"
                  @ready="onPlayerReady($event)" />

                  <v-flex offset-lg8 lg4 md1>
                    <v-select :disabled="false" v-model="cameraLB" :hint="`${cameraLB.code}`" :items="listCamera"
                      item-value="code" item-text="code" label="Select" flat hide-details dense solo
                      v-on:change="changeCamera3" placeholder="กล้อง 1"></v-select>
                  </v-flex>
              </div>

            </v-flex>
            <v-flex lg6 class="pa-1">
              <div style="width: 90%;height: 30rem;">
                <video-player ref="videoPlayer4"
                  style="width: 100%;height: 100%;"
                  class="video-js vjs-default-skin"
                  :options="playerOptions"
                  @play="onPlayerPlay($event)"
                  @ready="onPlayerReady($event)" />
                <v-flex offset-lg8 lg4 md1>
                  <v-select :disabled="false" v-model="cameraRB" :hint="`${cameraRB.code}`" :items="listCamera"
                    item-value="code" item-text="code" label="Select" flat hide-details dense solo
                    v-on:change="changeCamera4" placeholder="กล้อง 1"></v-select>
                </v-flex>
              </div>
            </v-flex>
          </v-layout> -->

        </v-container>
      </v-container>
    </v-content>
  </v-app>
</template>
<script>
const baseUrl = require("../../baseUrl.json");
import sidebar from "../components/sidebar-new.vue";
//import viewvideo from "../components/view-video.vue";
import headerbar from "../components/header-bar.vue";
import VideoPlayer from '@/components/VideoPlayer.vue';
import VideoPlayer2 from '@/components/VideoPlayer2.vue';
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
    // viewvideo,
    headerbar,
    VideoPlayer,
    VideoPlayer2,
  },
  data() {
    return {
      selectData: 'all',
      selectCheckpoint: '',
      listCheckPoint: [],
      drawer: true,
      textCheckPoint: "",
      onProgress: false,
      cameraLB: "",
      cameraLT: "",
      cameraRT: "",
      cameraRB: "",
      listCamera: [],
      src: 'https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8',
      playerOptions: {
        autoplay: true,
        controls: true,
        controlBar: {
          timeDivider: false,
          durationDisplay: false
        }
      },
      mock: {
        "cameras": [
          {
            "id": "1",
            "code": "https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8"
          },
          {
            "id": "2",
            "code": "https://bitdash-a.akamaihd.net/content/MI201109210084_1/m3u8s/f08e80da-bf1d-4e3d-8899-f0f6155f6efa.m3u8"
          }
        ]
      },
      isPublic: false,
      cameraPublic1: "",
      cameraPublic2: "",
      autoplay: "?rel=0&autoplay=1"
    };
  },
  created() {
    if (baseUrl.pathImg === "110.171.165.57") {
      this.isPublic = true
    }
  },
  computed: {
    years() {
      const year = new Date().getFullYear();
      return Array.from(
        { length: year - 2000 },
        (value, index) => 2001 + index
      );
    },
    player() {
      // return this.isPublic == false ? this.$refs.videoPlayer.player : null
      return this.$refs.videoPlayer.player
    },
    player2() {
      return this.$refs.videoPlayer2.player
    },

  },
  methods: {
    fn_changCheckpoint(param) {
      //console.log(param);
      this.$router.push("/traffic/present/" + param);

      this.reload();
    },
    reload() {

      this.$router.go();

    },
    gobackpage() {
      this.$router.push({ path: "/traffic/present" })

    },
    headerbar(drawer) {
      this.drawer = drawer;
    },
    onPlayerPlay(player) {
    },
    onPlayerReady(player) {
      this.player.play()
    },
    playVideo: function (source, camNo = 1) {

      const video = {
        withCredentials: false,
        type: 'application/x-mpegurl',
        src: source
      }
      switch (camNo) {
        case 1:
          this.player.reset() // in IE11 (mode IE10) direct usage of src() when <src> is already set, generated errors,
          this.player.src(video)
          break;
        case 2:
          this.player2.reset() // in IE11 (mode IE10) direct usage of src() when <src> is already set, generated errors,
          this.player2.src(video)
          break;
        case 3:
          this.player3.reset() // in IE11 (mode IE10) direct usage of src() when <src> is already set, generated errors,
          this.player3.src(video)
          break;
        case 4:
          this.player4.reset() // in IE11 (mode IE10) direct usage of src() when <src> is already set, generated errors,
          this.player4.src(video)
          break;
      }
      // this.player.reset() // in IE11 (mode IE10) direct usage of src() when <src> is already set, generated errors,

      // this.player.load()
      // this.player.play()
    },
    switchPlayer: function () {
      this.playVideo(this.src, 3)
    },
    getDataCameraCode() {

      let session_data = localStorage.getItem("session");
      this.myPath = this.$route.path.split("/");
      let url = baseUrl.ipServer + "/traffic-view/checkpoint-camera?checkpoint=" + this.myPath[3];
      this.selectCheckpoint = this.myPath[3]
      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {
          if (response.data.status_code === 200) {
            this.textCheckPoint = response.data.data.checkpoint.short_name;
            this.listCamera = response.data.data.cameras;

            if (this.listCamera.length > 0) {
              this.cameraLT = this.listCamera[0].code;
              this.cameraRT = this.listCamera[0].code;
              this.cameraLB = this.listCamera[0].code;
              this.cameraRB = this.listCamera[0].code;

              this.getDataLiveView(this.listCamera[0].code)

              // if (this.isPublic) {
              //   this.cameraPublic1 = this.listCamera[0].url.slice(0, -1) + this.autoplay
              //   this.cameraPublic2 = this.listCamera[0].url.slice(0, -1) + this.autoplay
              // } else {
              //   this.getDataLiveView(this.listCamera[0].code)
              // }
            }
          } else {
            Toast.fire({
              icon: "error",
              title: response.data.message,
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
        });
      // this.listCamera = this.mock.cameras;


    },
    changeCamera1(a) {
      this.getDataLiveView(a, 1, false)

      // if (this.isPublic) {
      //   let filter = this.listCamera.filter(function (creature) {
      //     return creature.code == a;
      //   });
      //   this.cameraPublic1 = filter[0].url.slice(0, -1) + this.autoplay

      // } else {
      //   this.getDataLiveView(a, 1, false)
      // }
    },
    changeCamera2(a) {
      this.getDataLiveView(a, 2, false)

      // if (this.isPublic) {
      //   let filter = this.listCamera.filter(function (creature) {
      //     return creature.code == a;
      //   });
      //   this.cameraPublic2 = filter[0].url.slice(0, -1) + this.autoplay

      // } else {
      //   this.getDataLiveView(a, 2, false)
      // }
    },

    getDataLiveView(code, camNo = 0, init = true) {
      let session_data = localStorage.getItem("session");
      this.myPath = this.$route.path.split("/");
      this.selectCheckpoint = this.myPath[3];
      let url =
        baseUrl.ipServer +
        "/traffic-view/live?checkpoint=" +
        this.myPath[3] +
        "&camera=" +
        code;
      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {
          if (response.data.status_code === 200) {
            let url = response.data.data.url
            if (this.isPublic) {
              url = url.replace(baseUrl.ipLiveviewInternal, baseUrl.ipLiveviewInternet)
            }

            if (init) {
              for (let x = 1; x <= 4; x++) {
                this.playVideo(url, x)
              }
            } else {
              this.playVideo(url, camNo)
            }

            // this.playVideo(url, 1)
          }
        });
    },
    getListCheckPoint() {
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/checkpoints"
      this.axios.get(url, { headers: { session: session_data } })
        .then((response) => {
          if (response.status === 200) {
            this.listCheckPoint = response.data.data
          } else {
            Toast.fire({
              icon: 'error',
              title: 'ไม่สามารถดึงข้อมูลจุดติดตั้งได้',
            })
          }
        }).catch((error) => {
          console.log(error);
          if (error.response.data.message === 'session timeout') {
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
            title: 'ไม่สามารถดึงข้อมูลจุดติดตั้งได้',
          })
        });
    },
  },
  mounted() {

    // phase test
    const src = 'https://bitdash-a.akamaihd.net/content/MI201109210084_1/m3u8s/f08e80da-bf1d-4e3d-8899-f0f6155f6efa.m3u8'
    // const src2 = 'https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8'
    const src2 = ''

    // phase test
    this.getDataCameraCode();
    this.getListCheckPoint()

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

    if (this.player4 != null) {
      this.player4.dispose(); // dispose() Will delete Dom Elements
    }
  }
};
</script>
<style>
.headerback {
  font-weight: 600;
  font-size: 24px;
  color: red;
}

.belate {
  font-weight: 600;
  font-size: 20px;
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
</style>
  