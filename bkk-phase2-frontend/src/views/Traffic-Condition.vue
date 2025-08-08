<template>
  <v-app id="bg" >
    <sidebar :sideNav="drawer"></sidebar> 
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-content class="pl-3">
      <v-container class="pl-1 pr-1" >
       <v-chip large class="ma-2 ml-0" color="#02754B" v-if="$vuetify.breakpoint.width > 1025">
          <span class="pl-5 pr-5 headertext">ดูสภาพการจราจร</span>
        </v-chip>
        <v-chip large class="ma-2 ml-0" color="#02754B" v-else>
          <span class="pl-5 pr-5 headertext-mobile">ดูสภาพการจราจร</span>
        </v-chip>
        <v-container>

        <v-flex class="map">    
            <viewmap @mapClick="setCheckPoint" page="map"></viewmap>
        </v-flex>
        </v-container>   
      </v-container>
      <liveview :show="openLiveView"></liveview>
    </v-content>
 
  </v-app>
</template>
<script>
import sidebar from "../components/sidebar-new.vue";
import viewmap from "../components/map-liveview.vue";
import headerbar from "../components/header-bar.vue";
//import liveview from "./live-view.vue";
export default {
  components: {
    sidebar,
    viewmap,
    headerbar,
   // liveview
  },
  data(){
    return{
      openLiveView:false,
      drawer: true,
      checkPoint:"",
        checkDevice
    }
  },
  updated(){
    console.log("mounted",this.checkPoint);
  },
  methods:{
    confirm(){
        this.$router.push( {path: '/traffic-detail'});
    },
    headerbar(drawer){
     
      this.drawer = drawer;
    },
    setCheckPoint(map){
     
          map.Event.bind('overlayClick', function(eventData){
            console.log('click',map,eventData.title);
              this.checkPoint = eventData.title;
             //alert("Hello World!");
             
            
        }) 
        
           
    }
  },
  mounted(){
   
  }
};
</script>
<style>
@import '../assets/css/background.css';
.map{
  width:100vw;
  height:70vh;
}
.text-pointer{
  font-weight: 600;
  font-size: 25px;
  color: #FFFFFF;
}
.chip-pointer{
 overflow: scroll;
white-space: nowrap;
}
</style>
