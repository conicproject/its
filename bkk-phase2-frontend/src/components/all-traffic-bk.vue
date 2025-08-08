<template>
    <v-card class="elevation-0" id="border" v-if="$vuetify.breakpoint.width > 420" >
                <v-row>
                  <v-col>
                    <div class="pl-5">
                      <span>{{dataText.allText}}</span>
                    </div>
                      <br/>
                    <div class="text-right">
                      <span class="dtpoint">{{total}}</span><span>&nbsp;คัน</span>
                       <!-- <span class="dtpoint">0</span><span>&nbsp;คัน</span> -->
                    </div> 
                    </v-col>
                  <v-divider vertical  class="ma-4"></v-divider>
                  <v-col >
                    <v-row class="pr-5">
                      <v-col v-if="dataText.keyCard === 'all'" class="ml-1">ปริมาณจราจร<br/><span class="intext-1">ขาเข้าเมือง</span></v-col>
                      <v-col v-else class="ml-1">ปริมาณยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด<br/><span class="intextViolate-1">ขาเข้าเมือง</span></v-col>
                      <!-- <v-col class="text-right"><span class="intext-2">{{inbound}}</span><span>&nbsp;คัน</span></v-col> -->
                       <v-col  v-if="dataText.keyCard === 'all'"  class="text-right"><span class="intext-2">{{inbound}}</span><span>&nbsp;คัน</span></v-col>
                       <v-col v-else class="text-right"><span class="intextViolate-2">{{inbound}}</span><span>&nbsp;คัน</span></v-col>
                    </v-row>
                    <v-divider  class="mr-4"></v-divider>
                    <v-row class="pr-5">
                      <v-col v-if="dataText.keyCard === 'all'" class="ml-1">ปริมาณจราจร<br/><span class="outtext-1">ขาออกเมือง</span></v-col>
                      <v-col v-else class="ml-1">ปริมาณยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด<br/><span class="outtextViolate-1">ขาออกเมือง</span></v-col>
                      <!-- <v-col class="text-right"><span class="outtext-2">{{outbound}}</span><span>&nbsp;คัน</span></v-col> -->
                       <v-col  v-if="dataText.keyCard === 'all'"  class="text-right"><span class="outtext-2">{{outbound}}</span><span>&nbsp;คัน</span></v-col>
                      <v-col v-else class="text-right"><span class="outtextViolate-2">{{outbound}}</span><span>&nbsp;คัน</span></v-col>
                    </v-row>
                  </v-col>
                </v-row>
              </v-card>
                 <v-card class="elevation-0" id="border" v-else>
                <v-row>
                  <v-col>
                    <div class="pl-3">
                      <span>ปริมาณจราจรทั้งหมด</span>
                    </div>
                  </v-col>
                  <v-col>
                    <div class="text-right pr-2">
                      <span class="dtpoint">{{total}}</span><span>&nbsp;คัน</span>
                    </div> 
                  </v-col>
                </v-row>
                  <v-divider class="ma-4"></v-divider>
                  
                    <v-row class="pr-2 pl-2">
                      <v-col v-if="dataText.keyCard === 'all'" class="ml-1">ปริมาณจราจร<br/><span class="intext-1">ขาเข้าเมือง</span></v-col>
                       <v-col v-else class="ml-1">ปริมาณจราจร<br/><span class="intext-1">ขาเข้าเมือง</span></v-col>
                      <v-col v-if="dataText.keyCard === 'all'" class="text-right"><span class="intext-2">{{inbound}}</span><span>&nbsp;คัน</span></v-col>
                       <v-col  v-else class="text-right"><span class="intext-2">{{inbound}}</span><span>&nbsp;คัน</span></v-col>
                    </v-row>
                    <v-divider  class="ma-4"></v-divider>
                    <v-row class="pr-2 pl-2">
                      <v-col v-if="dataText.keyCard === 'all'" class="ml-1">ปริมาณจราจร<br/><span class="outtext-1">ขาออกเมือง</span></v-col>
                       <v-col v-else class="ml-1">ปริมาณจราจร<br/><span class="outtext-1">ขาออกเมือง</span></v-col>
                      <v-col v-if="dataText.keyCard === 'all'" class="text-right"><span class="outtext-2">{{outbound}}</span><span>&nbsp;คัน</span></v-col>
                      <v-col  v-else class="text-right"><span class="outtext-2">{{outbound}}</span><span>&nbsp;คัน</span></v-col>
                    </v-row>
              </v-card>
</template>
<script>
export default {
    props:['directionData','dataText'],
    data: function() {
    return {
      inbound: 0,
      outbound: 0,
      total:0
    }
    },
    watch: { 
      	directionData: function(newVal, oldVal) { // watch it
             
           this.inbound = this.numberWithCommas(newVal.inbound) || 0
           this.outbound = this.numberWithCommas(newVal.outbound) || 0
           this.total =this.numberWithCommas(newVal.inbound+newVal.outbound) || 0
        },},
    methods: {
      numberWithCommas(x) {
        if(x){
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        }
},
      setDataDirection(){
        this.inbound = this.numberWithCommas(this.directionData.inbound);
        this.outbound = this.numberWithCommas(this.directionData.outbound);
        this.total =this.numberWithCommas(this.directionData.inbound+this.directionData.outbound);
        console.log(' this.total :>> ',  this.total);
      }
    },
    mounted(){
     
      this.setDataDirection()
    }
}
</script>
<style scoped>
.intext-1{
  color: #FF7F09;
}
.intext-2{
  color: #FF7F09;
  font-weight: 700;
  font-size: 30px;
}
.outtext-1{
  color: #21B3FF;
}
.outtext-2{
  color: #21B3FF;
  font-weight: 700;
  font-size: 30px;
}
.toptext-n{
  color: #FF7F09;
  font-weight: bold;
}
.intextViolate-1{
  color: #F44336	;
}
.intextViolate-2{
  color: #F44336	;
  font-weight: 700;
  font-size: 30px;
}
.outtextViolate-1{
  color: #3F51B5;
}
.outtextViolate-2{
  color: #3F51B5;
  font-weight: 700;
  font-size: 30px;
}
.toptext-n{
  color: #FF7F09;
  font-weight: bold;
}
.dtpoint{
  color: #2463C1;
  font-weight: 700;
  font-size: 30px;
}
.headertext{
  font-weight: 600;
  font-size: 24px;
  color: #FFFFFF;
}

#border {
  border-radius: 15px;
}
</style>