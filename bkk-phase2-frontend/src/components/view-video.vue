<template>
  <div style="width:100rem ;height:100rem">
   
  

  <video id="video" style="width: 100%;height: 100%;" class="video-js vjs-default-skin" preload="auto">
  <source :src="urlLiveView" type="application/x-mpegURL">
  </video>

    <!-- <iframe src="http://10.151.1.70:83/openUrl/izZbjvq/live.m3u8" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->
  </div>
</template>
<script>
import Vue from "vue";
import "video.js/dist/video-js.css";
// import { videoPlayer } from "vue-video-player";
import videojs from 'video.js'
//import 'videojs-contrib-hls'
import "@videojs/http-streaming"

export default {
  props:['height' , 'installCheck','urlLiveView'],
  components: {
    // videoPlayer,
    videojs,
  },
  data: function() {
    return {
      player: null,
      url:"",
    };
  },
  // watch:{
  //   urlLiveView:{
  //   handler(value, oldValue) {
  //     //this.init();
  //     this.url = value
  //     console.log(` ${oldValue} to ${value}`);
  //   }
  // }
  // },
  computed: {
  },
  methods: {
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
     }
  },
  mounted() {
console.log("url",this.urlLiveView);
this.init()
},
beforeDestroy() {

if (this.player != null) {

this.player.dispose() // dispose() Will delete Dom Elements 
}
}
};
</script>
<style>
.video{
  object-fit: cover;
}
</style>
