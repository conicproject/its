<template>
    <div style="width:100% ;height:100%" v-if="keyPage !== 'card'">
      <v-flex v-if="page === 'map'" class="text-center">
        <v-chip id="checkpoint" class="pl-5 pr-5 text-pointer ma-2" >
                  <span ></span>
                  </v-chip>
                  </v-flex>
      <longdo-map :zoom="11" :lastView="false"  @load="clickPoint" >
              <longdo-map-marker         
              v-for="(item, i) in markers"             
              :key="i"          
              :location="item.location"        
              :detail="item.html" 
              :html="item.html"  
              :title="item.title"
              :popup="item.popup"
              
          /> 
      </longdo-map>
      
      <!-- <video-player
        align-center
        class=" video-player-box "
        ref="videoPlayer"
        :options="playerOptions"
        :playsinline="true"
        customEventName="customstatechangedeventname"
        @play="onPlayerPlay($event)"
        @pause="onPlayerPause($event)"
        @ended="onPlayerEnded($event)"
        @waiting="onPlayerWaiting($event)"
        @playing="onPlayerPlaying($event)"
        @timeupdate="onPlayerTimeupdate($event)"
        @statechanged="playerStateChanged($event)"
        @ready="playerReadied"
      >
      </video-player> -->
      <!-- <video-player ref="videoPlayer"
                    class="vjs-custom-skin"
                    :options="playerOptions"
                    @play="onPlayerPlay($event)"
                    @ready="onPlayerReady($event)">
      </video-player> -->
      <!-- <video id="video" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto">
  <source src="http://10.151.1.70:83/openUrl/nOvKQlq/live.m3u8" type="application/x-mpegURL">
  </video> -->
  
  <!-- <v-btn @click="testing_function()">Button</v-btn> -->
  
  
  
   <!-- <liveview :show="openLiveView"></liveview> -->
      <!-- <iframe src="http://10.151.1.70:83/openUrl/izZbjvq/live.m3u8" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->
    </div>
    <div style="width:100% ;height:100%" v-else >
    
      <longdo-map :zoom="12" :lastView="false"  @load="clickPoint" >
              <longdo-map-marker         
              v-for="(item, i) in markers"             
              :key="i"          
              :location="item.location"        
              :detail="item.html" 
              :html="item.html"  
              :title="item.title"
              :popup="item.popup"
              
          /> 
      </longdo-map>
      <!-- <video-player
        align-center
        class=" video-player-box "
        ref="videoPlayer"
        :options="playerOptions"
        :playsinline="true"
        customEventName="customstatechangedeventname"
        @play="onPlayerPlay($event)"
        @pause="onPlayerPause($event)"
        @ended="onPlayerEnded($event)"
        @waiting="onPlayerWaiting($event)"
        @playing="onPlayerPlaying($event)"
        @timeupdate="onPlayerTimeupdate($event)"
        @statechanged="playerStateChanged($event)"
        @ready="playerReadied"
      >
      </video-player> -->
    </div>
  </template>
  <script>
  const baseUrl = require('../../baseUrl.json')
  import Vue from "vue";
  import LongdoMap from "longdo-map-vue";
  import "video.js/dist/video-js.css";
  import videojs from 'video.js'
  //import 'videojs-contrib-hls'
  import "@videojs/http-streaming"
  //import liveview from "./live-view.vue";
  const liveview = () => import("./live-view");
   //import { videoPlayer } from "vue-video-player";
   //import {VideoPlayer} from 'vue-videojs7'
  //  Vue.use(VideoPlayer, /* {
  //   options: global default videojs options,
  //   events: global videojs videojs events
  // } */)
  Vue.use(LongdoMap, {
    load: {
      apiKey: "17882b5b8fc125af5f4d32378f9afe4a",
    },
  });
  export default {
    props:["lat","lon","keyPage","height","page","checkpoint"],
    components: {
      // VideoPlayer,
      videojs,
      liveview
    },
      data: function() {
      return {
        title:"sss",
        myElement3:"",
        openLiveView:false,
        player: null,
        // playerOptions: {
        //   // videojs options
        //   muted: true,
        //   language: "en",
        //   playbackRates: [0.7, 1.0, 1.5, 2.0],
        //   sources: [
        //     {
        //       type: "http/mp4",
        //       src: "http://10.151.1.70:83/openUrl/izZbjvq/live.m3u8",
        //     },
        //   ],
        //   poster: "../static/images/author.jpg",
        // },
        playerOptions: {
          autoplay: true,
          controls: true,
          controlBar: {
            timeDivider: false,
            durationDisplay: false
          }
          // poster: 'https://surmon-china.github.io/vue-quill-editor/static/images/surmon-5.jpg'
        },
        show:false,
        testing: true,
            markers: [],
      }
      },
      watch:{
        myElement3:{
      handler(value, oldValue) {
        console.log(`Favorite color changed from ${oldValue} to ${value}`);
      }
    }
      },
      computed:{
        location(){
          let loca = { lon: parseFloat(this.lon), lat: parseFloat(this.lat) }
          return loca
        },   
      //    player () {
      //   return this.$refs.videoPlayer.player
      // }
      },
  
      methods:{
        testing_function() {
          console.log("testing");
          this.openLiveView = true
        },
  
        init() {
  
              // Player initialization 
              this.$nextTick(() => {
  
                  this.player = videojs('video' , {
  
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
      //   playerReadied(player) {
      //   console.log("the player is readied", player);
      //   // you can use it to do something...
      //   // player.[methods]
      // },
      test(){
      },
  //         clickPoint(map){
            
  //       map.Event.bind('overlayClick',function(eventData){
  //         this.$nextTick(() => {
  
  // this.player = videojs('video' , {
  
  //       bigPlayButton: false,
  //       textTrackDisplay: false,
  //       posterImage: true,
  //       errorDisplay: false,
  //       controlBar: false,
  //       muted: true // Mute mode 、、 Solve the problem of first page loading and playing .
  // }, function () {
  
  //      this.play() // Auto play 
  //    })
  // })
  //       })
  //     },
          clickPoint(map){
            // this.$emit('mapClick',map);
            map.Event.bind('overlayClick', function(eventData){
              let test= localStorage.getItem("checkpoint")
              let session_data = localStorage.getItem("session");
              var myHeaders = new Headers();
              myHeaders.append("session", session_data);
              var requestOptions = {
                method: 'GET',
                headers: myHeaders,
                redirect: 'follow'
              };
              let checkpoint = eventData.title.split(':')
              fetch(baseUrl.ipServer + "/traffic-view/live-sample?checkpoint="+checkpoint[0], requestOptions)
                .then(response => response.text())
                .then(result => {
                  //console.log(result);
                  const res = JSON.parse(result)
                  if(res.data.status_code === 200){
                const myElement = document.getElementById("link")
                console.log(myElement,res.data.url);
                myElement.href = '/traffic/present/'+checkpoint[0]
                // this.openLiveView = true
                //console.log("this.openLiveView",this.openLiveView);
            //             const myElement2 = document.getElementById("cameraCode")
            // myElement2.innerHTML = `<h2>รหัสกล้อง ${res.data.camera_code}</h2>`
                  }else{
  
                    this.$router.push('/error')
                    }
                   
            
            })
            .catch((error) => {
                    console.log(error);
                    this.$router.push('/error')
                    });
  
            this.myElement3 = document.getElementById("checkpoint")
            //console.log(this.myElement3);
            if(test ===checkpoint[1]){
                        localStorage.removeItem("checkpoint")
                        this.myElement3.innerHTML = "";
                        this.myElement3.style.backgroundColor = "";
                      }
             else{
              this.myElement3.innerHTML = "จุดติดตั้ง : "+checkpoint[1];
              this.myElement3.style.color = "white";
              this.myElement3.style.fontSize = "20px";
              this.myElement3.style.backgroundColor = "#02754B";
                localStorage.setItem("checkpoint",checkpoint[1]);
  
                // document.getElementById("show").style.display = "block";
                
              // alert(this.checkpoint);
             }
             
          }) 
         
            
          },
          getCheckPointDetail(){
            let session_data = localStorage.getItem("session");
            let url = baseUrl.ipServer + "/checkpoints/detail";
        this.axios
          .get(url, {
            headers: { session: session_data }
          })
          .then((response) => {
            console.log(response);
            if(response.status === 200){
              this.markers = [];
              for(let item = 0;item < response.data.data.length;item++){
                let data = {}
                data["location"] = {
                  'lon' : parseFloat(response.data.data[item].longtitude),
                  'lat' :  parseFloat(response.data.data[item].latitude),
                }
                data["popup"] = {
                  closable : false,
                  detail: `
            <div >
            <div style="padding-bottom:5%"><h2>ที่ตั้ง :${response.data.data[item].name}</h2></div>
            
            <div><a id="link" style="font-size:16px" href="">ไปที่จุดติดตั้ง</a></div>
            </div>`
                }
                data["clickable"] = true
                data["title"] =  response.data.data[item].id+':'+response.data.data[item].name
                data["id"] =  response.data.data[item].id
                if(this.keyPage === 'card' ){              
                  if( this.checkpoint === response.data.data[item].short_name){
                  this.markers.push(data)
                  }
                 
                }else{
                  this.markers.push(data)
                }
              }
             // console.log(this.markers);
            }else{
  
              this.$router.push('/error')
              }
  
  
              })
              .catch((error) => {
              console.log(error);
              this.$router.push('/error')
              });
          },
      //     onPlayerPlay (player) {
      //   console.log('player play!', player)
      // },
      // onPlayerReady (player) {
      //   console.log('player ready!', player)
      //   this.player.play()
      // },
      // playVideo: function (source) {
      //   const video = {
      //     withCredentials: false,
      //     type: 'application/x-mpegurl',
      //     src: source
      //   }
      //  // this.player.reset() // in IE11 (mode IE10) direct usage of src() when <src> is already set, generated errors,
      //   this.player.src(video)
      //   // this.player.load()
      //   this.player.play()
      // }
      },
      mounted(){
        //this.openLiveView = true
        this.$nextTick(() => {
            this.title = 'Three';
        });
  
        this.init()
  
  // const src = 'http://10.151.1.70:83/openUrl/izZbjvq/live.m3u8'
  //     this.playVideo(src)
  
     //   this.getCheckPointDetail()
    //       const myElement = document.getElementById("checkpoint")
    //             myElement.innerHTML = "";
    //     // document.getElementById("show").style.display = "none";
    //     console.log('mounted');
  
    //     var popup1 = new longdo.Popup({  lon: 100.55, lat: 13.77 },
    // {
    //   title: 'Popup',
    //   detail: 'Simple popup'
    // });
  
    // map.Overlays.add(popup1);
      },
      updated: function() {
      console.log("updated()")
    },
      beforeDestroy() {
  
  if (this.player != null) {
  
  this.player.dispose() // dispose() Will delete Dom Elements 
  }
  }
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
  