<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer"></sidebar> 
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-content  class="pl-3"  >
      <v-container class="pl-1 pr-1">
        <v-chip large class="ma-2" color="#02754B" v-if="$vuetify.breakpoint.width > 1025">
          <span class="pl-5 pr-5 headertext">ค้นหาข้อมูลรถบรรทุกในช่วงเวลาที่ห้ามเดินรถ</span>
        </v-chip>
                <v-chip large class="ma-2" color="#02754B" v-else>
          <span class="pl-5 pr-5 headertext-mobile">ค้นหาข้อมูลรถบรรทุกในช่วงเวลา<br/>ที่ห้ามเดินรถ</span>
        </v-chip>

        <v-container justify-center align-center class="search-vahicle pt-5" v-if="$vuetify.breakpoint.width > 1025">
          <v-row>
            <v-col> <v-menu
                v-model="menu"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field hint="ช่วงเวลาที่ค้นหาข้อมูลสูงสุด 7 วัน" persistent-hint placeholder="วัน เดือน ปี พ.ศ."  outlined  class="input-adddata rounded-lg sl mb-2" v-model="dayformat" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker no-title range locale="th" :min="min" :max="maxSelectDate" v-model="date" @input="setTimeRange()" >
                  <v-spacer></v-spacer>
                  <v-btn outlined color="error" @click="cancle">ล้าง</v-btn>
                  <v-btn color="primary" @click="menu=false">ตกลง</v-btn></v-date-picker>
              </v-menu></v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="selectPoint" :items="listCheckPoint"  item-value="name" item-text="name"  outlined hide-details label="จุดติดตั้ง" class="sl"></v-select></v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="selectDirection" :items="direction" outlined hide-details label="ทิศทางการจราจร" class="sl"></v-select></v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="selectTime" :items="rangeTime" item-value="key" item-text="text"   outlined hide-details label="เลือกช่วงเวลา" class="sl"></v-select></v-col>
          </v-row>
          <v-row class="justify-center mt-16">
            <v-btn color="primary" @click="confirm()">ตกลง</v-btn>
          </v-row>
        </v-container>
        
        <v-container justify-center align-center class="search-vahicle-mobile pt-5" v-else>
          <v-row>
            <v-col><v-menu
                v-model="menu"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field hint="ช่วงเวลาที่ค้นหาข้อมูลสูงสุด 7 วัน" persistent-hint placeholder="วัน เดือน ปี พ.ศ."  outlined  class="input-adddata rounded-lg sl mb-2" v-model="dayformat" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker no-title range locale="th" :min="min" :max="maxSelectDate" v-model="date" @input="setTimeRange()" >
                  <v-spacer></v-spacer>
                  <v-btn outlined color="error" @click="cancle">ล้าง</v-btn>
                  <v-btn color="primary" @click="menu=false">ตกลง</v-btn></v-date-picker>
              </v-menu></v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="selectPoint" :items="listCheckPoint"  item-value="name" item-text="name"  outlined hide-details label="จุดติดตั้ง" class="sl"></v-select></v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="selectDirection" :items="direction" outlined hide-details label="ทิศทางการจราจร" class="sl"></v-select></v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="selectTime" item-value="key" item-text="text" :items="rangeTime" outlined hide-details label="เลือกช่วงเวลา" class="sl"></v-select></v-col>
          </v-row>
          <v-row class="justify-center mt-16">
            <v-btn color="primary" @click="confirm()">ตกลง</v-btn>
          </v-row>
        </v-container>
      </v-container>

      <div>
        
      </div>
    </v-content>

    
  </v-app>
</template>
<script>
  const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
import headerbar from "../components/header-bar.vue";
import { fa } from "vuetify/lib/locale";
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
   headerbar
  },
  data(){
    return {
      selectTime:"",
      rangeTime:[{
        key:"[6,10]",
        text:"06:00 น. - 10:00 น."},{
        key:"[15,21]",
        text:"15:00 น. - 21:00 น."}],
      min:'2022-08-01',
      menu:false,
      date:[],
      maxSelectDate: new Date().toISOString().substr(0, 10),
      drawer: true,
      direction:[
        "ขาเข้า","ขาออก"
      ],
      selectPoint:"",
      selectDirection:"",
      listCheckPoint:[]
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
  },
  methods:{
    setTitleFormat(e){
      console.log(e);
    },
        cancle(){
      this.date = []
       this.min= '2022-08-01'
       this.maxSelectDate = new Date().toISOString().substr(0, 10)
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
    confirm(){
     
      if(this.date.length == 0){
          Toast.fire({
        icon: "error",
        title: "กรุณาเลือกวันที่",
      });
     return
    }
    
    if(this.selectTime == ""){
          Toast.fire({
        icon: "error",
        title: "กรุณาเลือกช่วงเวลา",
      });
     return
    }
    

    var param ={
        'startdate':this.date[0],
        'enddate':this.date[1] ? this.date[1] : this.date[0],
        'timerange':this.selectTime
      }
      if(this.selectPoint !== ''){
        param["checkpoint"] = this.selectPoint
      }
      if(this.selectDirection !== ''){
        if(this.selectDirection === "ขาเข้า"){
          param["direction"] = "inbound"
        }else{
          param["direction"] = "outbound"
        }
      }
      // param["page"] = 1
      
      this.$router.push( {path: '/truck-all',query:param});
    },
    headerbar(drawer){
      this.drawer = drawer;
    },
        getListCheckPoint(){
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/checkpoints"
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
            this.listCheckPoint = response.data.data
          }else{
          Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลจุดติดตั้งได้',     
        })
          }
          }).catch((error) => {
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
                    icon: 'error',
                    title: 'ไม่สามารถดึงข้อมูลจุดติดตั้งได้',     
                  })
          });
    },
  },
  mounted(){
    this.getListCheckPoint()
  }
};
</script>
<style scoped>
@import "../assets/css/background.css";
.v-date-picker-header {
  display: none
}
.headertext{
  font-weight: 600;
  font-size: 24px;
  color: #FFFFFF;
}
.sl {background: rgba(255, 255, 255, 0.9);border-radius: 15px;}
.search-vahicle {width: 50%;}
.search-vahicle-mobile {width: 100%;}
.input-adddata {background-color: white; height: 56px;}
</style>
