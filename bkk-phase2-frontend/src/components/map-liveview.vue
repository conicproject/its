<template>
  <v-card color="transparent" class="elevation-0" height="100%" style="width:100% ;height:100%" v-if="keyPage !== 'card'">
    <v-flex v-if="page === 'map'" class="text-center">
      <v-chip id="checkpoint" class="pl-5 pr-5 text-checkpoint ma-2" large style="background-color: transparent">
        <span></span>
      </v-chip>
    </v-flex>
    <!-- <longdo-map :zoom="13" :lastView="false" @load="clickPoint">
        <longdo-map-marker v-for="(item, i) in markers" :key="i" :location="item.location" :detail="item.html"
          :html="item.html" :title="item.title" :popup="item.popup" @click="onClickMarker"/>
      </longdo-map> -->
    <LongdoMap :center="map.center" :apiKey="map.apiKey">
      <template slot-scope="{ map }">
        <LongdoMapMarker :map="map" @click="onClickMarker" @move="onMoveMarker" @hover="onHoverMarker"
          @change="onChageMarker" v-for="marker in markers" :marker="marker"></LongdoMapMarker>

      </template>
    </LongdoMap>

  </v-card>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
// import LongdoMap from "longdo-map-vue";
// import Vue from "vue";
import LongdoMap from '../components/LongdoMap.vue'
import LongdoMapMarker from '../components/LongdoMapMarker.vue'
import Swal from "sweetalert2/dist/sweetalert2.js";
const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});
// Vue.use(LongdoMap, {
//   load: {
//     apiKey: "17882b5b8fc125af5f4d32378f9afe4a",
//   },
// });
export default {
  props: ["lat", "lon", "keyPage", "height", "page", "checkpoint"],
  components: {
    LongdoMap,
    LongdoMapMarker,
  },
  data() {
    return {

      title: "sss",
      myElement3: "",
      map: {
        apiKey: "17882b5b8fc125af5f4d32378f9afe4a",
        center: {
          lon: 100.604202,
          lat: 13.711573
        },
        height: "300px",
      },
      show: false,
      testing: true,
      markers: [],
      mockmarkers: {
        "data": [
          {
            "id": "1",
            "name": "ถนนอ่อนนุช\n",
            "short_name": "ถ.ถนนอ่อนนุช ซ.รพ.2",
            "latitude": "13.711573",
            "longtitude": "100.604202",
            "is_active": false
          },
          {
            "id": "10",
            "name": "ถนนพระรามที่ 4 บริเวณปากซอยโรงพยาบาล 2\n",
            "short_name": "ถ.พระรามที่4 ซ.รพ.2",
            "latitude": "13.712714",
            "longtitude": "100.587765",
            "is_active": true
          }
        ]
      },
      isPublic: false,
      autoplay: "?rel=0&autoplay=1",
    }
  },
  created() {
    if (baseUrl.pathImg === "110.171.165.57") {
      this.isPublic = true;
    }
  },
  watch: {
    myElement3: {
      handler(value, oldValue) {
        // console.log(`Favorite color changed from ${oldValue} to ${value}`);
      }
    }
  },
  computed: {
    location() {
      let loca = { lon: parseFloat(this.lon), lat: parseFloat(this.lat) }
      return loca
    },
  },

  methods: {
    changeCenter: function () {
      this.map.center = {
        lat: 18.7716998,
        lon: 98.816391
      }
    },
    onMoveMarker: function (marker) {
      // console.log('move')
    },
    onHoverMarker: function (marker) {
      // console.log('hover')
    },
    onChageMarker: function (marker) {
      // console.log('change')
    },
    testing_function() {
      // console.log("testing");

    },
    onClickMarker(a) {
      let detail = a.detail
      let checkpoint = detail.title.split(':')
      this.myElement3 = document.getElementById("checkpoint")
      this.myElement3.innerHTML = "จุดติดตั้ง : " + checkpoint[1];
      this.myElement3.style.color = "white";
      this.myElement3.style.fontSize = "20px";
      this.myElement3.style.backgroundColor = "#02754B";
      localStorage.setItem("checkpoint", checkpoint[1]);
    },
    test() {
    },
    clickPoint(map) {
      // this.$emit('mapClick',map);
      map.Event.bind('overlayClick', function (eventData) {
        let test = localStorage.getItem("checkpoint")
        let session_data = localStorage.getItem("session");
        var myHeaders = new Headers();
        myHeaders.append("session", session_data);
        var requestOptions = {
          method: 'GET',
          headers: myHeaders,
          redirect: 'follow'
        };
        let checkpoint = eventData.title.split(':')
        fetch(baseUrl.ipServer + "/traffic-view/live-sample?checkpoint=" + checkpoint[0], requestOptions)
          .then(response => response.text())
          .then(result => {
            //console.log(result);
            const res = JSON.parse(result)
            if (res.data.status_code === 200) {
              const myElement = document.getElementById("link")
              console.log(myElement, res.data.url);
              myElement.href = '/traffic/present/' + checkpoint[0]
              // this.openLiveView = true
              //console.log("this.openLiveView",this.openLiveView);
              //             const myElement2 = document.getElementById("cameraCode")
              // myElement2.innerHTML = `<h2>รหัสกล้อง ${res.data.camera_code}</h2>`
            } else {

              this.$router.push('/error')
            }


          })
          .catch((error) => {
            console.log(error);
            this.$router.push('/error')
          });

        this.myElement3 = document.getElementById("checkpoint")
        //console.log(this.myElement3);
        if (test === checkpoint[1]) {
          localStorage.removeItem("checkpoint")
          this.myElement3.innerHTML = "";
          this.myElement3.style.backgroundColor = "transparent";
        }
        else {
          this.myElement3.innerHTML = "จุดติดตั้ง : " + checkpoint[1];
          this.myElement3.style.color = "white";
          this.myElement3.style.fontSize = "20px";
          this.myElement3.style.backgroundColor = "#02754B";
          localStorage.setItem("checkpoint", checkpoint[1]);

          // document.getElementById("show").style.display = "block";

          // alert(this.checkpoint);
        }

      })
    },
    getCheckPointDetail() {
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/checkpoints/detail";
      this.axios
        .get(url, {
          headers: { session: session_data }
        })
        .then((response) => {
          if (response.status === 200) {
            this.markers = [];
            let datas = response.data.data
            for (let item = 0; item < datas.length; item++) {
              let data = {}
              data["location"] = {
                'lon': parseFloat(datas[item].longtitude),
                'lat': parseFloat(datas[item].latitude),
              }

              if (datas[item].is_active == false) {
                data["detail"] = {
                  title: datas[item].name,
                  closable: false,
                  detail: `
                        <div >
                        <div style="padding-bottom:5%"><h2>ที่ตั้ง :${datas[item].name}</h2></div>
                        
                        <div><span id="link" style="font-size:16px; color:red;" >ไม่สามารถแสดงจุดติดตั้งได้</span></div>
                        </div>
                        `,
                  clickable: true,
                  id: datas[item].id
                }
              } else {
                let cameras = datas[item].cameras

                let html = `<div style="overflow: hidden;">`
                  for (let ii = 0; ii < cameras.length; ii++) {
                    html += `<div style="padding-bottom:5%"><h3>ชื่อกล้อง :${cameras[ii].name}</h2></div>`
                    html += `<iframe frameBorder="0" src='/traffic/live-view/${datas[item].id}/${cameras[ii].camera_id}' height="300" width="400" title="Iframe Example">
                       </iframe><hr style="margin-top:5%;margin-bottom:5%">`
                  }
                  html += `</div>`

                  data["detail"] = {
                    title: datas[item].name,
                    closable: false,
                    detail: `
                          <div >
                           <div style="padding-bottom:5%"><h2>ที่ตั้ง :${datas[item].name}</h2></div>
                           ${html}
                           </div>
                          `,
                    clickable: true,
                    id: datas[item].id,
                    size: { width: 400, height: 400 },
                  };

                // if (this.isPublic) {

                //   let html = `<div style=" overflow-y: auto;">`
                //   for (let ii = 0; ii < cameras.length; ii++) {
                //     cameras[ii].url = cameras[ii].url.slice(0, -1) + this.autoplay;

                //     html += `<div style="padding-bottom:5%"><h3>ชื่อกล้อง :${cameras[ii].name}</h2></div>`
                //     html += ` <iframe frameBorder="0" src='${cameras[ii].url}' height="300" width="400" title="Iframe Example" allow="autoplay; encrypted-media" allowfullscreen>
                //       </iframe><hr style="margin-top:5%;margin-bottom:5%">`
                //   }
                //   html += `</div>`

                //   data["detail"] = {
                //     title: datas[item].id + ":" + datas[item].name,
                //     closable: false,
                //     detail: `
                //           <div style="margin-left: 15px;">
                //           <div style="padding-bottom:5%"><h2>ที่ตั้ง :${datas[item].name}</h2></div>
                //             ${html}
                //           </div>
                //           `,
                //     clickable: true,
                //     id: datas[item].id,
                //     size: { width: 405, height: 400 },
                //   };

                // } else {

                //   //new waiting api

                //   let html = `<div style="overflow: hidden;">`
                //   for (let ii = 0; ii < cameras.length; ii++) {
                //     html += `<div style="padding-bottom:5%"><h3>ชื่อกล้อง :${cameras[ii].name}</h2></div>`
                //     html += `<iframe frameBorder="0" src='/traffic/live-view/${datas[item].id}/${cameras[ii].camera_id}' height="300" width="400" title="Iframe Example">
                //        </iframe><hr style="margin-top:5%;margin-bottom:5%">`
                //   }
                //   html += `</div>`

                //   data["detail"] = {
                //     title: datas[item].id + ":" + datas[item].name,
                //     closable: false,
                //     detail: `
                //           <div >
                //            <div style="padding-bottom:5%"><h2>ที่ตั้ง :${datas[item].name}</h2></div>
                //            ${html}
                //            </div>
                //           `,
                //     clickable: true,
                //     id: datas[item].id,
                //     size: { width: 400, height: 400 },
                //   };
                // }
              }


              data["id"] = parseInt(datas[item].id)
              if (this.keyPage === 'card') {

                if (this.checkpoint === datas[item].short_name) {

                  this.markers.push(data)
                }

              } else {
                this.markers.push(data)
              }

              //console.log(this.markers)

            }
          }
        }).catch((error) => {
          console.log(error);
          if (error.response.data.message === 'session timeout') {
            this.$store.dispatch("logout");
            this.$router.push('/')
            Toast.fire({
              icon: 'error',
              title: 'Cannot connet API',
            })
            return
          }

          Toast.fire({
            icon: 'error',
            title: 'session timeout',
          })
        });
    },

  },
  mounted() {
    this.openLiveView = true
    this.$nextTick(() => {
      this.title = 'Three';
    });

    this.getCheckPointDetail()

  },
  updated: function () { },
  beforeDestroy() { }
};
</script>
<style>
.text-checkpoint {
  font-weight: 600;
  font-size: 18px;
  color: #FFFFFF;
}

.player {
  position: absolute !important;
  width: 100%;
  height: 60%;
}

.vjs-custom-skin {
  height: 60% !important;
}

.vjs-custom-skin /deep/ .video-js {
  height: 60%;
}
</style>
  