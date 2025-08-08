<template>
<v-card class="elevation-0" id="border" v-if="$vuetify.breakpoint.width > 525" height="100%">
                <v-row>
                  <v-col>
                    <div class="pl-5">
                      <span>จำนวน {{keyword}} ในโครงการ</span>
                    </div>
                      <br/>
                    <div class="text-right">
                      <span class="dtpoint">{{data.total}}</span><span>&nbsp;ชุด</span>
                    </div> 
                    </v-col>
                  <v-divider vertical  class="ma-4"></v-divider>
                  <v-col >
                    <v-row class="pr-5">
                      <v-col><span>จำนวน {{keyword}} ติด</span></v-col>
                      <v-col class="text-right"><span class="ontext-2">{{data.online}}</span><span>&nbsp;ชุด</span></v-col>
                    </v-row>
                    <v-divider  class="mr-4"></v-divider>
                    <v-row class="pr-5">
                      <v-col><span>จำนวน {{keyword}} ดับ</span></v-col>
                      <v-col class="text-right"><span class="offtext-2">{{data.offline}}</span><span>&nbsp;ชุด</span></v-col>
                    </v-row>
                  </v-col>
                </v-row>
</v-card>
<v-card class="elevation-0" id="border" v-else-if="$vuetify.breakpoint.width <= 525 && $vuetify.breakpoint.width > 370" height="100%">
                <v-row>
                  <v-col>
                    <div class="pl-5">
                      <span>จำนวน {{keyword}} ในโครงการ</span>
                    </div>
                      <br/>
                    <div class="text-right">
                      <span class="dtpoint-mobile">{{data.total}}</span><span>&nbsp;ชุด</span>
                    </div> 
                    </v-col>
                  <v-divider vertical  class="ma-4"></v-divider>
                  <v-col >
                    <v-row class="pr-5">
                      <v-col><span>จำนวน {{keyword}} ติด</span></v-col>
                      <v-col class="text-right"><span class="ontext-2-mobile">{{data.online}}</span><span>&nbsp;ชุด</span></v-col>
                    </v-row>
                    <v-divider  class="mr-4"></v-divider>
                    <v-row class="pr-5">
                      <v-col><span>จำนวน {{keyword}} ดับ</span></v-col>
                      <v-col class="text-right"><span class="offtext-2-mobile">{{data.offline}}</span><span>&nbsp;ชุด</span></v-col>
                    </v-row>
                  </v-col>
                </v-row>
</v-card>
<v-card class="elevation-0" id="border" v-else>
                <v-row>
                  <v-col>
                    <div class="pl-5">
                      <span>จำนวน {{keyword}} ในโครงการ</span>
                    </div>
                      <br/>
                    <div class="text-right pr-5">
                      <span class="dtpoint-mobile">{{data.total}}</span><span>&nbsp;ชุด</span>
                    </div> 
                    </v-col>
                   </v-row>
                  <v-divider class="ma-4"></v-divider>              
                    <v-row class="pl-3 pr-3">
                      <v-col><span>จำนวน {{keyword}} ติด</span></v-col>
                      <v-col class="text-right"><span class="ontext-2-mobile">{{data.online}}</span><span>&nbsp;ชุด</span></v-col>
                    </v-row>
                    <v-divider  class="mr-4"></v-divider>
                    <v-row class="pl-3 pr-3">
                      <v-col><span>จำนวน {{keyword}} ดับ</span></v-col>
                      <v-col class="text-right"><span class="offtext-2-mobile">{{data.offline}}</span><span>&nbsp;ชุด</span></v-col>
                    </v-row>
                  
                   <!-- </v-row> -->
</v-card>
</template>
<script>
export default {
    props: ['keyword','data'],
}
</script>
<style>
@import '../assets/css/background.css';
.dtpoint-mobile {
  color: #2463c1;
  font-weight: 700;
  font-size: 30px;
}
.ontext-2{
  color:  #2463C1;
  font-weight: 700;
  font-size: 40px;
}
.offtext-2{
  color: #FF0404;
  font-weight: 700;
  font-size: 40px;
}
.ontext-2-mobile{
  color:  #2463C1;
  font-weight: 700;
  font-size: 30px;
}
.offtext-2-mobile{
  color: #FF0404;
  font-weight: 700;
  font-size: 30px;
}
</style>