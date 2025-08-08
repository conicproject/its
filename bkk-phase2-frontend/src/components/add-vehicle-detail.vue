<template>
    <v-container>       
    <v-layout v-if="$vuetify.breakpoint.width > 1264">
      <v-flex xs12 lg6 >
        <v-card style="background: #9EC6FA;" id="borderblue" height="100%" class="d-flex align-center">
          <v-card-text class="pa-0 pt-5">
            <v-layout
              row
              wrap
              align-center
              justify-center
              fill-height
              class="mt-10"
            >
              <v-flex lg12 md12 xs12 class="text-center pa-2">
                <v-flex class="ma-2">
                  <img
                  :src="dataCard.image_url"
                  width="100%"
                  height="100%"
                 
                />
                </v-flex>  
                <v-flex>
                  <!-- <viewvideo  :height="height" :installCheck='false'></viewvideo> -->
                </v-flex>
                <v-flex>
                  <img
                  :src="dataCard.plate_picture"
                  width="50%"
                  height="50%"
                  
                />
                </v-flex>            
              </v-flex>
            </v-layout>
              </v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs12 lg6 >
               <v-card style="background: white" class="pa-3" id="borderflex" height="100%" >
               <v-card-text class="pa-0">
                <v-layout>
              <v-flex lg12 md12 xs12 >
                <br/>
                  <v-row>
                    <v-col>
                        <span class="title-style">ทะเบียนยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataCard.plate_no}}</span></v-card>
                    </v-col>
                    <v-col><span class="title-style">จังหวัด</span>
                       <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataCard.province}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>           
                        <span class="title-style">สียานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataCard.color}}</span></v-card>
                    </v-col>
                    <v-col><span class="title-style">ประเภทยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataCard.type}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                        <span class="title-style">สถานที่</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF" ><span class="text-style d-inline-block text-truncate" >{{dataCard.checkpoint}}</span></v-card>
                    </v-col>
                    <v-col><span class="title-style">วัน/เดือน/ปี</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF" ><span class="text-style d-inline-block text-truncate">{{dataCard.date}}</span></v-card>
                    </v-col>
                    <v-col>
                        <span class="title-style">เวลา</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF" ><span class="text-style d-inline-block text-truncate">{{dataCard.time}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-card class="elevation-0 pa-3" style="width:100% ;height:450px">
                    <viewmap :lat="dataCard.lat" :lon="dataCard.lon" keyPage="card" :checkpoint="dataCard.checkpoint"></viewmap>
                    </v-card>
                  </v-row>
                  <br/>
              </v-flex>
            </v-layout>
          </v-card-text>
               </v-card>
         <exportfile class="pt-4"></exportfile>
      </v-flex>
    </v-layout>
     <v-layout row wrap align-center justify-center v-else>
      <v-flex xs12 lg12 class="ma-5">
        <v-card style="background: #9EC6FA;" id="border" class="d-flex align-center">
          <v-card-text class="pa-0">
            <v-layout
              row
              wrap
              align-center
              justify-center
              fill-height
              class="ma-0"
            >
              <v-flex lg12 md12 xs12 class="text-center pa-2  align-center justify-center">
                <v-flex class="ma-2">
                  <img
                  :src="dataCard.image_url"
                  width="100%"
                  height="100%"
                 
                />
                </v-flex>  
                <v-flex>
                  <img
                  :src="dataCard.plate_picture"
                  width="50%"
                  height="50%"
                  
                />
                </v-flex>
                <!-- <v-flex>
                  <img
                  src="@/assets/img/logo_side.jpg"
                  width="50%"
                  height="50%"
                  
                />
                </v-flex>             -->
              </v-flex>
              <v-flex lg12 md12 xs12 style="background: white" class="pa-3" id="borderflex-mobile">
                <br/>
                  
                    
                        <span class="title-style">ทะเบียนยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{dataCard.plate_no}}</span></v-card>
                   
                    <span class="title-style">จังหวัด</span>
                       <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{dataCard.province}}</span></v-card>
                   
                  
                            
                        <span class="title-style">สียานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{dataCard.color}}</span></v-card>
                   
                   <span class="title-style">ประเภทยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{dataCard.type}}</span></v-card>
                   
                        <span class="title-style">สถานที่</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span  class="text-style">{{dataCard.checkpoint}}</span></v-card>
                      <v-row>
                    <v-col><span class="title-style">วัน/เดือน/ปี</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{dataCard.date}}</span></v-card>
                    </v-col>
                    <v-col>
                        <span class="title-style">เวลา</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{dataCard.time}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-card class="elevation-0 pa-3" style="width:100% ;height:450px">
                    <viewmap :lat="dataCard.lat" :lon="dataCard.lon" keyPage="card" :checkpoint="dataCard.location"></viewmap>
                    </v-card>
                  </v-row>
                  <br/>
              </v-flex>
            </v-layout>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>

    </v-container>
</template>
<script>
import viewmap from '@/components/map.vue'
export default {
  props:["dataCard"],
    components: {
        viewmap
    },
    data() {
    return {
      
    }
  },
  watch:{
    dataCard: function(newVal, oldVal) {
      // watch it
      console.log(newVal);
    },
  },
  mounted(){
    console.log(this.dataCard);
  }
}
</script>
<style scoped>
#borderblue{
  border-radius: 15px 0px 0px 15px;
  
}
.text-style{
  color:#2463C1;
  font-weight: bold;
   font-size: 18px;
}
</style>