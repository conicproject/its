<template>
  <v-app id="bg" >
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="onProgress">
      <v-progress-circular
        indeterminate
        size="64"
      ></v-progress-circular>
    </v-overlay>
    <v-content class="pl-3" >
      <v-container class="pl-1 pr-1">
                        <v-chip @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
     <v-icon large color="red">mdi-chevron-left</v-icon>
         <span class="text-left headerback">Back</span>
    </v-chip> 
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">จัดการอัพเดทรายงาน</span>
        </v-chip>
        <v-container>
           <v-layout d-flex flex-column justify-center align-center>
        
          <v-chip large class="ma-2" color="#02754B">
            <span class="pl-5 pr-5 headertext">เลือกรายงานที่จะอัพเดท</span>
        </v-chip>
            </v-layout>
          <v-layout child-flex class="pt-5" v-if="$vuetify.breakpoint.width > 754">
        <v-container d-flex flex-column justify-center align-center>
          <v-row>
            <v-col class="d-flex justify-end"><span class="textSR py-3">ข้อมูลยานพาหนะ</span></v-col>
            <v-col >
              <v-menu
                v-model="menu"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field placeholder="วัน เดือน ปี" outlined hide-details class="sl" v-model="dayformat" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
               <v-date-picker no-title range locale="th" :min="min" :max="maxSelectDate" v-model="date" @input="setTimeRange()" >
                  <v-spacer></v-spacer>
                  <v-btn outlined color="error" @click="cancle">ล้าง</v-btn>
                  <v-btn color="primary" @click="menu=false">ตกลง</v-btn></v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
          <v-row class="justify-center mt-6">
            <v-btn color="primary" @click="updateList()" :loading="loading">อัพเดท</v-btn>
          </v-row>
 
           <v-row class="mt-16">
            <v-col class="d-flex justify-end"><span class="textSR py-3">ข้อมูลยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด</span></v-col>
            <v-col >
              <v-menu
                v-model="menuViolation"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field placeholder="วัน เดือน ปี" outlined hide-details class="sl" v-model="dayformatViolation" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker no-title range locale="th" :min="minViolation" :max="maxSelectDateViolation" v-model="dateViolation" @input="setTimeRangeViolation()" >
                  <v-spacer></v-spacer>
                  <v-btn outlined color="error" @click="cancleViolation">ล้าง</v-btn>
                  <v-btn color="primary" @click="menuViolation=false">ตกลง</v-btn></v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
          <v-row class="justify-center mt-6">
            <v-btn color="primary" @click="updateListViolation()" :loading="loadingViolation">อัพเดท</v-btn>
          </v-row>
        </v-container>
          </v-layout>
          <div v-else>
             <v-layout child-flex class="pt-5">
                <v-container justify-center align-center>      
          <v-card class="card-mobile elevation-0 mb-3">
            <span class="textSR-mobile py-3 mb-3">ข้อมูลยานพาหนะ</span>
             <v-menu
                v-model="menu"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field placeholder="วัน เดือน ปี" outlined hide-details class="sl-mobile" v-model="dayformat" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
               <v-date-picker no-title range locale="th" :min="min" :max="maxSelectDate" v-model="date" @input="setTimeRange()" >
                  <v-spacer></v-spacer>
                  <v-btn outlined color="error" @click="cancle">ล้าง</v-btn>
                  <v-btn color="primary" @click="menu=false">ตกลง</v-btn></v-date-picker>
              </v-menu>
          </v-card>
                    
                      <v-row class="justify-center mt-6">
            <v-btn color="primary" @click="updateList()" :loading="loading">อัพเดท</v-btn>
          </v-row>
          </v-container>
          
          </v-layout>
          <v-layout child-flex class="pt-5">
            <v-container justify-center align-center>      
             <v-card class="card-mobile elevation-0 mb-3">
            <span class="textSR-mobile py-3 mb-3">ข้อมูลยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด</span>
              <v-menu
                v-model="menuViolation"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field placeholder="วัน เดือน ปี" outlined hide-details class="sl-mobile" v-model="dayformatViolation" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker no-title range locale="th" :min="minViolation" :max="maxSelectDateViolation" v-model="dateViolation" @input="setTimeRangeViolation()" >
                  <v-spacer></v-spacer>
                  <v-btn outlined color="error" @click="cancleViolation">ล้าง</v-btn>
                  <v-btn color="primary" @click="menuViolation=false">ตกลง</v-btn></v-date-picker>
              </v-menu>
          </v-card>       
            <v-row class="justify-center mt-6">
             <v-btn color="primary" @click="updateListViolation()" :loading="loadingViolation">อัพเดท</v-btn>
          </v-row>
          </v-container>
          </v-layout>
         </div>
        </v-container>
    </v-container>
    </v-content>
    
  </v-app>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
import headerbar from "../components/header-bar.vue";
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
    headerbar,
  },
   data() {
    return {
      loading:false,
      onProgress:false,
    drawer:true,
      menu:false,
      loadingViolation:false,
      menuViolation:false,
       dateViolation:[],
       date:[],
        min:'2022-08-01',
      maxSelectDateViolation: new Date().toISOString().substr(0, 10),
      minViolation:'2022-08-01',
      maxSelectDate: new Date().toISOString().substr(0, 10),
    }
   },
   methods:{      
    headerbar(drawer) {
      this.drawer = drawer;
    },
    cancle(){
       this.date = []
       this.min= '2022-08-01'
       this.maxSelectDate = new Date().toISOString().substr(0, 10)
       //this.menu=false
    },
        cancleViolation(){
       this.dateViolation = []
       this.minViolation= '2022-08-01'
       this.maxSelectDateViolation = new Date().toISOString().substr(0, 10)
       //this.menu=false
    },
    setTimeRange(){
      
      var now = new Date();
      var endDate = new Date(this.date[0]);
       endDate.setDate(endDate.getDate() + 6);
       now.setDate(now.getDate());
       this.min = this.date[0]
       if(now.getTime() < endDate.getTime()){
        
          this.maxSelectDate = now.toISOString().substr(0, 10)
       }else{
         this.maxSelectDate = endDate.toISOString().substr(0, 10)
       }
      //   let end = endDate.toISOString().substr(0, 10)
      //   let data = end.split("-");
      //   let year = parseInt(data[0])+543;
      //   return data[2]+"-"+data[1]+"-"+year.toString();
      //  this.maxSelectDate =
      },
    setTimeRangeViolation(){
      console.log("setTimeRangeViolation");
         var now = new Date();
      var endDate = new Date(this.dateViolation[0]);
       endDate.setDate(endDate.getDate() + 6);
       now.setDate(now.getDate());
       this.minViolation = this.dateViolation[0]
       if(now.getTime() < endDate.getTime()){
        
          this.maxSelectDateViolation = now.toISOString().substr(0, 10)
       }else{
         this.maxSelectDateViolation = endDate.toISOString().substr(0, 10)
       }
      },
      updateList(){
        if(this.date.length == 0){
          Toast.fire({
        icon: "error",
        title: "กรุณาเลือกวันที่",
      });
     return
    }
          let session_data = localStorage.getItem("session");
        let url = baseUrl.ipServer + "/date-record-insert";
        var payload = {
          "starttime":this.date[0],
          "endtime":this.date[1] ? this.date[1] : this.date[0],
          }
        this.axios.post(url,payload, { headers: { session: session_data } }).then((response) => {
          if(response.data.status_code == 200){
        this.loading = false
         this.date = []
        this.min = '2022-08-01'
        this.maxSelectDate =  new Date().toISOString().substr(0, 10),
         Toast.fire({
                     icon: "success",
                    title: "อัพเดทข้อมูล สำเร็จ",
                }) 
            this.$emit("submit");
          }else{
             this.date = []
        this.min = '2022-08-01'
        this.maxSelectDate =  new Date().toISOString().substr(0, 10),
            this.loading = false
             Toast.fire({
                     icon: "error",
                    title: "ไม่สามารถอัพเดทข้อมูลได้",
                }) 
          }
          }).catch((error) => {
            this.loading = false
             this.date = []
        this.min = '2022-08-01'
        this.maxSelectDate =  new Date().toISOString().substr(0, 10),
        console.log(error);
        this.onProgress = false
        if(error.response.data.message === 'session timeout'){
            this.$store.dispatch("logout");
            this.$router.push('/')
             Toast.fire({
              icon: "error",
              title: error.response.data.message,
            });

            return;
        }
        Toast.fire({
                     icon: "error",
                    title: "ไม่สามารถอัพเดทข้อมูลได้",
                }) 
      });
      },
      updateListViolation(){
 if(this.dateViolation.length == 0){
          Toast.fire({
        icon: "error",
        title: "กรุณาเลือกวันที่",
      });
     return
    }
          let session_data = localStorage.getItem("session");
        let url = baseUrl.ipServer + "/date-violation-insert";
        var payload = {
          "starttime":this.dateViolation[0],
          "endtime":this.dateViolation[1] ? this.dateViolation[1] : this.dateViolation[0],
          }
        this.axios.post(url,payload, { headers: { session: session_data } }).then((response) => {
          if(response.data.status_code == 200){
        this.loadingViolation = false
         this.dateViolation = []
        this.minViolation = '2022-08-01'
        this.maxSelectDateViolation =  new Date().toISOString().substr(0, 10),
         Toast.fire({
                     icon: "success",
                    title: "อัพเดทข้อมูล สำเร็จ",
                }) 
            this.$emit("submit");
          }else{
             this.dateViolation = []
        this.minViolation = '2022-08-01'
        this.maxSelectDateViolation =  new Date().toISOString().substr(0, 10),
            this.loadingViolation = false
             Toast.fire({
                     icon: "error",
                    title: "ไม่สามารถอัพเดทข้อมูลได้",
                }) 
          }
          }).catch((error) => {
            this.loadingViolation = false
             this.dateViolation = []
        this.minViolation = '2022-08-01'
        this.maxSelectDateViolation =  new Date().toISOString().substr(0, 10),
        console.log(error);
        if(error.response.data.message === 'session timeout'){
            this.$store.dispatch("logout");
            this.$router.push('/')
             Toast.fire({
              icon: "error",
              title: error.response.data.message,
            });

            return;
        }
        Toast.fire({
                     icon: "error",
                    title: "ไม่สามารถอัพเดทข้อมูลได้",
                }) 
      });
      },
      gobackpage(){
         this.$router.push({path:"/dashboard"});
      }
   },
   computed:{
        dayformat(){
     
      if(this.date.length === 0){
       
       console.log("null");
        return []

      }else{
        let data1 = this.date[0].split("-");
        let year1 = parseInt(data1[0])+543;
        if(this.date[1] !== undefined){
          let data2 = this.date[1].split("-");
          let year2 = parseInt(data2[0])+543;
          return data1[2]+"-"+data1[1]+"-"+year1.toString()+" ~ "+data2[2]+"-"+data2[1]+"-"+year2.toString()
        }
       
        return data1[2]+"-"+data1[1]+"-"+year1.toString();
      }
      
      
    },
    dayformatViolation(){
     
      if(this.dateViolation.length === 0){
        return []

      }else{
        let data1 = this.dateViolation[0].split("-");
        let year1 = parseInt(data1[0])+543;
        if(this.dateViolation[1] !== undefined){
          let data2 = this.dateViolation[1].split("-");
          let year2 = parseInt(data2[0])+543;
          return data1[2]+"-"+data1[1]+"-"+year1.toString()+" ~ "+data2[2]+"-"+data2[1]+"-"+year2.toString()
        }
       
        return data1[2]+"-"+data1[1]+"-"+year1.toString();
      }
      
      
    },
   }
}
</script>
<style scoped>
@import '../assets/css/system-configuration.css';
.sl {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  width: 300px;
}
.sl-mobile {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
}
.card-mobile {
  border-radius: 15px !important;
  font-weight: 700;
  font-size: 20px;
  color: #02754B;
  text-align: center;
}
.textSR {
  font-weight: 700;
  font-size: 20px;
  color: #02754B;
  text-align: center;
  background-color: white;
  width: 520px;
  display: block;
  border-radius: 15px;
}
.textSR-mobile {
  font-weight: 700;
  font-size: 20px;
  color: #02754B;
  text-align: center;
  background-color: white;
  display: block;
  border-radius: 15px;
}
</style>