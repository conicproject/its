<template>
  <v-row justify="center">
    <v-dialog v-model="shower" scrollable persistent max-width="700px">
      <v-card>
        <!-- <v-card-title> date time picker </v-card-title> -->
        <v-card-text>
          <v-container>
                <!-- <v-date-picker no-title range locale="th" :min="min" :max="maxSelectDate" v-model="date" @input="setTimeRange()"> -->
                     <v-date-picker no-title v-model="date" :min="min" :max="maxSelectDate" locale="th" full-width range @input="setTimeRange()"></v-date-picker>
                    <v-layout class="mb-3">                   
                        <v-flex lg6 class="mr-1">
                     <span>เวลาเริ่มต้น</span>
                     <v-row><v-col>
                      <v-select v-model="startHour" placeholder="ชั่วโมง" :items="hour" outlined hide-details ></v-select>
                      </v-col><v-col>
                      <v-select v-model="startMin" placeholder="นาที" :items="minute" outlined hide-details ></v-select>
                      </v-col>
                     </v-row>
                        </v-flex>
                      <v-flex lg6 class="ml-1">
                        <span>เวลาสิ้นสุด</span>
                     <!-- <v-date-picker v-model="picker2" locale="th" full-width></v-date-picker> -->
                     <v-row><v-col>
                      <v-select v-model="endHour" placeholder="ชั่วโมง" :items="hour" outlined hide-details ></v-select>
                      </v-col>
                      <v-col>
                      <v-select v-model="endMin" placeholder="นาที" :items="minute" outlined hide-details ></v-select>
                      </v-col>
                     </v-row>
                        </v-flex>
                    </v-layout>
                   
          </v-container>
           <v-divider  class="mb-3"></v-divider>
            <span>ตัวอย่างวันและเวลาที่เลือก</span>
                    <v-layout  v-if="$vuetify.breakpoint.width > 433">
                       
                         <v-text-field class="pr-1" placeholder="วัน เดือน ปี เวลา"  outlined hide-details readonly v-model="dayformat"></v-text-field><v-btn fab dark color="green" @click="reset()">ล้าง</v-btn>
                    </v-layout>
                     <div v-else>
                       
                         <v-text-field class="pr-1" placeholder="วัน เดือน ปี เวลา"  outlined hide-details readonly v-model="dayformat"></v-text-field>
                         <v-container class="text-center"><v-btn fab dark color="green"  @click="reset()">ล้าง</v-btn></v-container>
                         
                    </div>

        </v-card-text>
     
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" outlined @click="$emit('close')">ปิด</v-btn>
          <v-btn color="primary" dark @click="setDateTimePicker()">ตกลง</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>

import Swal from "sweetalert2/dist/sweetalert2.js";
const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});
export default {
  props: ["show", "dataItem"],
  data() {
    return {
                startMin:'00',
        startHour:'00',
       
        endHour:'00',
        endMin:'00',
        date: [(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)],
        
  min:'2022-08-01',
      menu:false,
      date:[],
        maxSelectDate: new Date().toISOString().substr(0, 10),
              hour:[
        "00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"
      ],
      minute:[
        "00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"
      ],
    };
  },
  computed: {
     dayformat(){
     
      if(this.date.length === 0){
       
        return []

      }else{
        let data1 = this.date[0].split("-");
        let year1 = parseInt(data1[0])+543;
        if(this.date[1] !== undefined){
          let data2 = this.date[1].split("-");
          let year2 = parseInt(data2[0])+543;
          return data1[2]+"-"+data1[1]+"-"+year1.toString()+" "+this.startHour+":"+this.startMin+" ~ "+data2[2]+"-"+data2[1]+"-"+year2.toString()+" "+this.endHour+":"+this.endMin
          
        }
       
        return data1[2]+"-"+data1[1]+"-"+year1.toString()+" "+this.startHour+":"+this.startMin+" ~ "+data1[2]+"-"+data1[1]+"-"+year1.toString()+" "+this.endHour+":"+this.endMin
      }
      
      
    },
    shower: {
      get() {
        if (this.show === true) {
          //  console.log("show",this.dataItem);
        }
        return this.show;
      },
      set(value) {
        if (!value) {
          // console.log("show",this.dataItem);
        }
      },
    },
  },
  methods: {
    reset(){
        this.startMin='00'
        this.startHour='00'
       this.endHour='00'
       this.endMin='00'
       this.date=[]
      this.min='2022-08-01'
     this.maxSelectDate = new Date().toISOString().substr(0, 10)
     
    },
    setDateTimePicker(){
        if(!this.date[0]){
            Toast.fire({
                     icon: "error",
                    title: "กรุณากรอกข้อมูลให้ครบ",
                })

            return
        }
        let start_time = this.date[0]+'T'+this.startHour+':'+this.startMin+':00'
        let end_time;
        if(!this.date[1]){
             end_time = this.date[0]+'T'+this.endHour+':'+this.endMin+':00'
        }else{
            end_time = this.date[1]+'T'+this.endHour+':'+this.endMin+':00'
        }
       
        this.$emit('setDateTime',start_time,end_time,this.dayformat)
        
       
    },
               setTimeRange(){
      
      var now = new Date();
      var endDate = new Date(this.date[0]);
       endDate.setDate(endDate.getDate() + 6);
       now.setDate(now.getDate());
       this.min = this.date[0]
    //    if(now.getTime() < endDate.getTime()){
        
          this.maxSelectDate = now.toISOString().substr(0, 10)
    //    }
    //    else{
    //      this.maxSelectDate = endDate.toISOString().substr(0, 10)
    //    }
      //   let end = endDate.toISOString().substr(0, 10)
      //   let data = end.split("-");
      //   let year = parseInt(data[0])+543;
      //   return data[2]+"-"+data[1]+"-"+year.toString();
      //  this.maxSelectDate =
      },
  },
  mounted() {},
};
</script>
<style scoped>
</style>