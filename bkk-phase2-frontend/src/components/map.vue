<template>
  <div style="width:100% ;height:100%" v-if="keyPage !== 'vehicle'">
      <v-flex v-if="page === 'map'" class="text-center">
          <v-chip id="checkpoint" class="pl-5 pr-5 text-pointer ma-2" large>
              <span></span>
          </v-chip>
      </v-flex>
      <!-- <longdo-map :zoom="13" :lastView="false" @load="clickPoint">
      <longdo-map-marker v-for="(item, i) in markers" :key="i" :location="item.location" :detail="item.html"
        :html="item.html" :title="item.title" :popup="item.popup" @click="onClickMarker"/>
    </longdo-map> -->
    <LongdoMap :center="map.center" :apiKey="map.apiKey">
      <template slot-scope="{ map }">
        <LongdoMapMarker
          :map="map"
          @click="onClickMarker"
          @move="onMoveMarker"
          @hover="onHoverMarker"
          @change="onChageMarker"
          v-for="marker in markers"
          :marker="marker"></LongdoMapMarker>

      </template>
    </LongdoMap>

  </div>
  <div style="width:100% ;height:100%" v-else>

      <!-- <longdo-map :zoom="13" :lastView="false" @load="clickPoint">
      <longdo-map-marker v-for="(item, i) in markers" :key="i" :location="item.location" :detail="item.html"
        :html="item.html" :title="item.title" :popup="item.popup" />
    </longdo-map> -->
    <LongdoMap :center="map.center" :apiKey="map.apiKey">
      <template slot-scope="{ map }">
        <LongdoMapMarker
          :map="map"
          @click="onClickMarker"
          @move="onMoveMarker"
          @hover="onHoverMarker"
          @change="onChageMarker"
          v-for="marker in markers"
          :marker="marker"></LongdoMapMarker>

      </template>
    </LongdoMap>

  </div>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
// import LongdoMap from "longdo-map-vue";
// import Vue from "vue";
import LongdoMap from '../components/LongdoMap.vue'
import LongdoMapMarker from '../components/LongdoMapMarker.vue'

// Vue.use(LongdoMap, {
//   load: {
//     apiKey: "6399f33eb7f50daf3913410f8c89a587",
//   },
// });
export default {
  props: ["lat", "lon", "keyPage", "height", "page","checkpoint","destination_lat","destination_lon"],
  components: {
    LongdoMap,
    LongdoMapMarker,
  },
  data() {
    return {
      title: "sss",
      myElement3: "",
      map: {
          apiKey: "6399f33eb7f50daf3913410f8c89a587",
          center: {
              lon: 100.604202,
              lat: 13.711573
          },
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
      }
    }
  },
  watch: {
    myElement3: {
      handler(value, oldValue) {
        // console.log(`Favorite color changed from ${oldValue} to ${value}`);
      }
    },
    lat: {
      handler(value, oldValue) {
       console.log("dddd",this.destination_lon);
       this.getCheckPointDetail()
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
                //console.log(myElement, res.data.url);
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
            this.myElement3.style.backgroundColor = "";
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
    getCheckPoint(){
       this.markers = [
       { 'location' : {
        'lon': parseFloat(this.lat),
        'lat': parseFloat(this.lon),
       }}
       ]
       //console.log(this.markers);
    },
    getCheckPointDetail() {
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/checkpoints/detail";

      if(this.keyPage == 'destination'){
        this.markers = [{
          'location':{
                  'lon': this.lon,
                  'lat': this.lat,
                }
        },{
          'location':{
                  'lon': this.destination_lon,
                  'lat': this.destination_lat,
                }
        }]
        
        
           //console.log(this.markers);
            return   
      }

      this.axios
          .get(url, {
            headers: { session: session_data }
          })
          .then((response) => {
            //console.log(response);
            if(response.status === 200){
              this.markers = [];
              let datas = response.data.data
              
              for (let item = 0; item < datas.length; item++) {
                let data = {}
                if(this.lat == datas[item].latitude && this.lon == datas[item].longtitude ){

             
                data["location"] = {
                  'lon': parseFloat(datas[item].longtitude),
                  'lat': parseFloat(datas[item].latitude),
                }

                

                data["id"] = parseInt(datas[item].id)

                this.markers.push(data)
                   }
      }

      //console.log(this.markers);
            }else{

            }
          }).catch((error) => {
            console.log(error);

         if(error.response.data.message === 'session timeout'){
            this.$store.dispatch("logout");
            this.$router.push('/')
         }

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
