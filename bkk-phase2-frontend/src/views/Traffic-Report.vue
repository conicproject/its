<template>
  <v-app id="bg" >
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-content  class="pl-3" >
      <v-container class="pl-1 pr-1">
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">รายงานข้อมูลจราจร</span>
        </v-chip>
        <v-container d-flex flex-column justify-center align-center v-if="$vuetify.breakpoint.width > 754">
                  <v-row>
            <v-col class="d-flex justify-end"><span class="textSR py-3">ชนิดข้อมูล</span></v-col>
            <v-col >
           <v-select placeholder="เลือกชนิดข้อมูล" item-value="key" item-text="name" v-model="selectData" :items="items_selectData" outlined hide-details class="sl"></v-select>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="d-flex justify-end"><span class="textSR py-3">รายวัน</span></v-col>
            <v-col  @click="changeSelect('day')">
              <v-menu
                v-model="menu"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field placeholder="วัน เดือน ปี" :disabled="disable.day" outlined hide-details class="sl" v-model="dayformat" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker locale="th" :min="min" :max="maxSelectDate" v-model="date" @input="menu = false"></v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="d-flex justify-end"><span class="textSR py-3">รายสัปดาห์</span></v-col>
            <v-col  @click="changeSelect('week')">
              <v-menu
                v-model="menuWeek"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                   placeholder="วัน เดือน ปี"
                   :disabled="disable.week"
                    outlined
                    hide-details
                    class="sl"
                    v-model="weekRange"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker locale="th" :min="min" :max="maxWeekRange" :allowed-dates="allowedDates" v-model="week" @input="menuWeek = false"></v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="d-flex justify-end"><span class="textSR py-3">รายเดือน</span></v-col>
            <v-col @click="changeSelect('month')">
              <v-menu
                v-model="menuMonth"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field  placeholder="เดือน ปี"  :disabled="disable.month" outlined hide-details class="sl" v-model="monthformat" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker locale="th" :min="min" :max="maxMonthRange" type="month" v-model="month" @input="menuMonth = false"></v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="d-flex justify-end"><span class="textSR py-3">รายปี</span></v-col>
            <v-col @click="changeSelect('year')" >
              <v-select placeholder="ปี" :disabled="disable.year"  v-model="selectYear" :items="years" outlined hide-details class="sl"></v-select>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="d-flex justify-end"><span class="textSR py-3">ตามช่วงเวลา</span></v-col>
            <v-col  @click="changeSelect('range')">
              <v-menu
                v-model="menuTime"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                   placeholder="ช่วงวัน เดือน ปี"
                   :disabled="disable.startRange"
                    outlined
                    hide-details
                    class="sl"
                    v-model="timeStartformat"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker no-title range locale="th" :min="min"  v-model="timeStart" :max="maxDateStart" @input="setTimeRange()">
                  <v-spacer></v-spacer>
                  <v-btn outlined color="error" @click="cancle">ล้าง</v-btn>
                  <v-btn color="primary" @click="menuTime=false">ตกลง</v-btn>
                  </v-date-picker></v-menu></v-col>
            
          </v-row>
          <v-row class="justify-center mt-16">
            <v-btn color="primary" @click="confirm()">ตกลง</v-btn>
          </v-row>
        </v-container>
        <v-container justify-center align-center v-else>
                 <v-card  class="card-mobile elevation-0 mb-3" >
            <span class="textSR-mobile py-3 mb-3">ชนิดข้อมูล</span>
            <div ><v-select placeholder="เลือกชนิดข้อมูล" item-value="key" item-text="name" v-model="selectData" :items="items_selectData" outlined hide-details class="sl-mobile"></v-select></div>
          </v-card>
          <v-card class="card-mobile elevation-0 mb-3" @click="changeSelect('day')">
            <span class="textSR-mobile py-3 mb-3">รายวัน</span>
              <v-menu
                v-model="menu"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field placeholder="วัน เดือน ปี" :disabled="disable.day" outlined hide-details class="sl-mobile" v-model="dayformat" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker locale="th" :min="min" :max="maxSelectDate" v-model="date" @input="menu = false"></v-date-picker>
              </v-menu>
          </v-card>
          <v-card class="card-mobile elevation-0 mb-3" @click="changeSelect('week')">
            <span class="textSR-mobile py-3 mb-3">รายสัปดาห์</span>
             <v-menu
                v-model="menuWeek"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                   placeholder="วัน เดือน ปี"
                   :disabled="disable.week"
                    outlined
                    hide-details
                    class="sl-mobile"
                    v-model="weekRange"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker locale="th" :min="min" :max="maxWeekRange" :allowed-dates="allowedDates" v-model="week" @input="menuWeek = false"></v-date-picker>
              </v-menu>
          </v-card>
          <v-card class="card-mobile elevation-0 mb-3" @click="changeSelect('month')">
            <span class="textSR-mobile py-3 mb-3">รายเดือน</span>
            <v-menu
                v-model="menuMonth"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field  placeholder="เดือน ปี"  :disabled="disable.month" outlined hide-details class="sl-mobile" v-model="monthformat" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker locale="th" :min="min" :max="maxMonthRange" type="month" v-model="month" @input="menuMonth = false"></v-date-picker>
              </v-menu>
          </v-card>
          <v-card  class="card-mobile elevation-0 mb-3" @click="changeSelect('year')">
            <span class="textSR-mobile py-3 mb-3">รายปี</span>
             <v-select placeholder="ปี" :disabled="disable.year"  v-model="selectYear" :items="years" outlined hide-details class="sl-mobile"></v-select>
          </v-card>
          <v-card class="card-mobile elevation-0" @click="changeSelect('range')">
            <span class="textSR-mobile py-3 mb-3">ตามช่วงเวลา</span>
            
            <!-- <v-col class="pr-0 pb-0"   @click="changeSelect('range')"> -->
              <v-menu
                v-model="menuTime"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                   placeholder="ช่วงวัน เดือน ปี"
                   :disabled="disable.startRange"
                    outlined
                    hide-details
                    class="sl-mobile"
                    v-model="timeStartformat"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker no-title range locale="th" :min="min"  v-model="timeStart" :max="maxDateStart" @input="setTimeRange()">
                  <v-spacer></v-spacer>
                  <v-btn outlined color="error" @click="cancle">ล้าง</v-btn>
                  <v-btn color="primary" @click="menuTime=false">ตกลง</v-btn>
                  </v-date-picker></v-menu>
            
            <!-- <v-col class="pl-0 pb-0"  @click="changeSelect('rangeEnd')"> -->
          </v-card>
          <v-row class="justify-center mt-10">
            <v-btn color="primary" @click="confirm()">ตกลง</v-btn>
          </v-row>
        </v-container>
      </v-container>
    </v-content>

    
  </v-app>
</template>
<script>
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
        selectData: 0,
       items_selectData: [
        {
          key: 0,
          name: "ข้อมูลจราจร",
        },
        {
          key: 1,
          name: "ข้อมูลยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด",
        },
      ],
      min:'2022-08-01',
      allowedDates: (val) => new Date(val).getDay() === 1,
      drawer: true,
      opendatepicker: false,
      date: "",
      menu: false,
      week: '',
      menuWeek: false,
      menuMonth: false,
      month:"",
      selectYear:"",
      menuTime: false,
    maxDateStart:new Date().toISOString().substr(0, 10),
      timeStart: [],
      timeEnd: "",
      selected:true,
      unselect:true,
      disable:[
        {
          name:"day",
          value:false
        },
         {
          name:"week",
          value:false
        },
         {
          name:"month",
          value:false
        },
         {
          name:"year",
          value:false
        },
         {
          name:"time",
          value:false
        }
],
      disable:{
        day : false,
      week : true,
      month : true,
      year : true,
      startRange :true,
      endRange :true}
    };
  },
  computed: {
    timeStartformat(){
      if(this.timeStart.length === 0){
          return []

      }
       let data1 = this.timeStart[0].split("-");
        let year1 = parseInt(data1[0])+543;
        if(this.timeStart[1] !== undefined){
          var endDate = new Date(this.timeStart[0]);
          var endDate_2 = new Date(this.timeStart[1]);
          if(endDate.getTime() == endDate_2.getTime()){
            this.timeStart.splice(1, 1);
            return data1[2]+"-"+data1[1]+"-"+year1.toString();
          }
          let data2 = this.timeStart[1].split("-");
          let year2 = parseInt(data2[0])+543;
          return data1[2]+"-"+data1[1]+"-"+year1.toString()+" ~ "+data2[2]+"-"+data2[1]+"-"+year2.toString()
        }
       
        return data1[2]+"-"+data1[1]+"-"+year1.toString();
    },
    timeEndformat(){
      if(this.timeStart === ""){
        return ""

      }
      var endDate = new Date(this.timeStart);
       endDate.setDate(endDate.getDate() + 14)
       this.timeEnd = endDate.toISOString().substr(0, 10)
        let end = endDate.toISOString().substr(0, 10)
        let data = end.split("-");
        let year = parseInt(data[0])+543;
        return data[2]+"-"+data[1]+"-"+year.toString();
      
    },
    dayformat(){
      if(this.date === ""){
        return ""

      }
        let data = this.date.split("-");
        let year = parseInt(data[0])+543;
        return data[2]+"-"+data[1]+"-"+year.toString();
      
    },
    monthformat(){
      if(this.month === ""){
        return ""

      }
        let data = this.month.split("-");
        let year = parseInt(data[0])+543;
        return data[1]+"-"+year.toString();
      
    },
    maxSelectDate() {
       var endDate  = new Date();
      endDate.setDate(endDate.getDate() - 1);
      return endDate.toISOString().substr(0, 10);
    },
    weekRange() {
      if(this.week === ""){
        return ""
      }else{
        let data1 = this.week.split("-");
        let year1 = parseInt(data1[0])+543;
        var endDate = new Date(this.week);
        endDate.setDate(endDate.getDate() + 6);
        let week2 = endDate.toISOString().substr(0, 10)
        let data2 = week2.split("-");
        let year2 = parseInt(data2[0])+543;
        return data1[2]+"-"+data1[1]+"-"+year1.toString() + " ~ " +data2[2]+"-"+data2[1]+"-"+year2.toString();
      }
    },
    maxDateEnd(){
      
       if(this.timeStart === ""){
         var endDate  = new Date();
         endDate.setDate(endDate.getDate() - 7);
        return endDate.toISOString().substr(0, 10);
       }else{
         var endDate  = new Date(this.timeStart);
         endDate.setDate(endDate.getDate() + 6);
        return endDate.toISOString().substr(0, 10);
       }
    },
    minSelectRange(){ 
      return this.timeStart
    },
    maxWeekRange(){
       var endDate  = new Date();
      endDate.setDate(endDate.getDate() - 6);
      return endDate.toISOString().substr(0, 10);

    },
    maxMonthRange(){
       var endDate  = new Date();
      endDate.setDate(endDate.getDate());
      return endDate.toISOString().substr(0, 10);

    },
    years() {
      console.log("year");
      const year = (new Date().getFullYear())+543
      return Array.from({ length: year - 2564 }, (value, index) => 2565 + index);
    },
  },
  methods: {
    cancle(){
      this.timeStart = []
       this.min= '2022-08-01'
       this.maxDateStart = new Date().toISOString().substr(0, 10)
       //this.menuTime=false
    },
  setTimeRange(){
      console.log(this.timeStart);
      var now = new Date();
      var endDate = new Date(this.timeStart[0]);
       
       endDate.setDate(endDate.getDate() + 14);
       now.setDate(now.getDate());
       this.min = this.timeStart[0]
       
       if(now.getTime() < endDate.getTime()){
          this.maxDateStart = now.toISOString().substr(0, 10)
          //console.log(now.getTime()< endDate.getTime());
       }
       else{
         this.maxDateStart = endDate.toISOString().substr(0, 10)
       }
      //   let end = endDate.toISOString().substr(0, 10)
      //   let data = end.split("-");
      //   let year = parseInt(data[0])+543;
      //   return data[2]+"-"+data[1]+"-"+year.toString();
      //  this.maxSelectDate =
      },
    changeSelect(param){
      //console.log("changeSelect",param);
     if(param === "day"){
       this.disable.day = false;
       this.disable.week = true;
       this.disable.month = true;
       this.disable.year = true;
       this.disable.startRange = true;
       this.disable.endRange = true;
       
      this.week = ""
      this.month = ""
      this.year = ""
      this.time = ""
     }else if(param === "week"){
      this.disable.day = true;
       this.disable.week = false;
       this.disable.month = true;
       this.disable.year = true;
       this.disable.startRange = true;
       this.disable.endRange = true;
       this.date = ""
      this.month = ""
      this.year = ""
      this.time = ""
     }else if(param === "month"){
      this.disable.day = true;
       this.disable.week = true;
       this.disable.month = false;
       this.disable.year = true;
       this.disable.startRange = true;
       this.disable.endRange = true;
       this.date = ""
      this.week = ""
      this.year = ""
      this.time = ""
     }
     else if(param === "year"){
      this.disable.day = true;
       this.disable.week = true;
       this.disable.month = true;
       this.disable.year = false;
       this.disable.startRange = true;
       this.disable.endRange = true;
       this.date = ""
      this.week = ""
      this.month = ""
     
      this.time = ""
     }
     else if(param === "range"){
      this.disable.day = true;
       this.disable.week = true;
       this.disable.month = true;
       this.disable.year = true;
       this.disable.startRange = false;
       this.disable.endRange = true;
       this.date = ""
       this.week = ""
      this.month = ""
      this.year = ""
     }else if(param === "rangeEnd"){
      //console.log(this.timeStart);
      if(this.timeStart !== ""){
        this.disable.day = true;
       this.disable.week = true;
       this.disable.month = true;
       this.disable.year = true;
       this.disable.startRange = false;
       this.disable.endRange = false;
       this.date = ""
       this.week = ""
      this.month = ""
      this.year = ""
      }
     }
     
    },
    dateSelect(){
      this.menu = false;
      this.disable.Week = true
      this.disable.Month = true
      this.disable.Year = true
      this.disable.Time = true
    },
    maxStart(){
      var endDate  = new Date();
      endDate.setDate(endDate.getDate() - 1);
      return endDate.toISOString().substr(0, 10);
    },
    confirm() {
     
      if(this.date == "" && this.week == "" && this.month == "" && this.selectYear == "" && this.timeStart.length === 0){
        Toast.fire({
        icon: "error",
        title: "กรุณากรอกข้อมูล",
      });
      return
      }
       let settime
      if(this.timeStart[1] !== undefined){
         settime = this.timeStart[0] + "," + this.timeStart[1];
      }else{
       // settime = this.timeStart[0]
       if(this.disable.startRange == false){
        console.log(this.disable);
        Toast.fire({
        icon: "error",
        title: "กรุณากรอกข้อมูลให้ครบ",
      });
      return
       }
      }
        
        let paramType = !this.disable.day ? "day" : !this.disable.week ? "week" : !this.disable.month ? "month" : !this.disable.year ? "year" : !this.disable.startRange ? "range" : "";
        let year = parseInt(this.selectYear-543)
        let paramDate = this.date !== "" ? this.date : this.week !== "" ? this.week : this.month !== "" ? this.month : this.selectYear !== "" ? year: this.timeStart.length !== 0 ? settime : "";
        let checkpoint = "34"
        if(paramType == 'range'){
          if(this.timeStart.length === 0){
            Toast.fire({
              icon: "error",
              title: "กรุณากรอกข้อมูล",
            });
            return
          }       
        }
        if (paramType !== undefined && paramDate !== undefined) {
          let param = { type: paramType , date: paramDate,checkpoint:checkpoint ,
         typeData:this.selectData
          } 
          this.$router.push({ path: "/traffic-report",query:param});
        }
       
      
    },
    headerbar(drawer) {
      this.drawer = drawer;
    },
  },
  mounted(){
    console.log(new Date());
  }
};
</script>
<style scoped>
@import "../assets/css/background.css";
.v-date-picker-title__date {
    font-size: 12px !important;
    text-align: left;
    font-weight: 500;
    position: relative;
    overflow: hidden;
    padding-bottom: 8px;
    margin-bottom: -8px;
}
.v-input{
  font-size: 20px;
  line-height: 1.5rem;
}
.v-select__selections {
    align-items: center;
    display: flex;
    flex: 1 1;
    flex-wrap: wrap;
    line-height: 20px;
}
.headertext {
  font-weight: 600;
  font-size: 24px;
  color: #ffffff;
}
.sltime {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  width: 150px;
}
.sl {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  width: 300px;
}
.sl-mobile {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
}
.textSR {
  font-weight: 700;
  font-size: 20px;
  color: #02754B;
  text-align: center;
  background-color: white;
  width: 200px;
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
.card-mobile {
  border-radius: 15px !important;
  font-weight: 700;
  font-size: 20px;
  color: #02754B;
  text-align: center;
}
</style>
