<template>
  <v-app id="bg" >
    <sidebar :sideNav="drawer"></sidebar> 
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-content class="pl-3"  >
      <v-container class="pl-1 pr-1">
        <v-chip large class="ma-2" color="#02754B" v-if="$vuetify.breakpoint.width > 1025">
          <span class="pl-5 pr-5 headertext">ค้นหาข้อมูลจุดต้นทาง/ปลายทางของยานพาหนะ</span>
        </v-chip>
         <v-chip large class="ma-2" color="#02754B" v-else>
          <span class="pl-5 pr-5 headertext-mobile">ค้นหาข้อมูลจุดต้นทาง/ปลายทาง<br/>ของยานพาหนะ</span>
        </v-chip>

        <v-container justify-center align-center class="search-vahicle pt-5" v-if="$vuetify.breakpoint.width > 1025">
            <!-- <v-row class="d-flex justify-center align-center">        
                <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 subheadertext">ค้นหาข้อมูลจุดต้นทาง/ปลายทางของยานพาหนะ</span>
        </v-chip>
        </v-row> -->
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
                  <v-text-field placeholder="วัน เดือน ปี พ.ศ."  outlined hide-details class="sl" v-model="dayformat" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker locale="th" :min="min" :max="maxSelectDate" v-model="date" @input="menu = false"></v-date-picker>
              </v-menu></v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="type" :items="listCarType" outlined hide-details label="ประเภทยานพาหนะ" class="sl"></v-select></v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="province" :items="listProvince" outlined hide-details label="จังหวัด" class="sl"></v-select></v-col>
          </v-row>
          <v-row class="justify-center mt-16">
            <v-btn color="primary" @click="confirm()">ตกลง</v-btn>
          </v-row>
        </v-container>
        <v-container justify-center align-center class="search-vahicle-mobile pt-5" v-else>
           <!-- <v-row class="d-flex justify-center align-center">        
                <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 subheadertext">ค้นหาข้อมูลจุดต้นทาง/ปลายทางของยานพาหนะ</span>
        </v-chip>
        </v-row> -->
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
                  <v-text-field placeholder="วัน เดือน ปี พ.ศ."  outlined hide-details class="sl" v-model="dayformat" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker locale="th" :min="min" :max="maxSelectDate" v-model="date" @input="menu = false"></v-date-picker>
              </v-menu></v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="type" :items="listCarType" outlined hide-details label="ประเภทยานพาหนะ" class="sl"></v-select></v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="province" :items="listProvince" outlined hide-details label="จังหวัด" class="sl"></v-select></v-col>
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
       province:"",
      type:"",
       listProvince:[],
      listCarType:[],
      min:'2022-08-01',
      menu:false,
      date:'',
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
      if(this.date === ""){
        return ""

      }
        let data = this.date.split("-");
        let year = parseInt(data[0])+543;
        return data[2]+"-"+data[1]+"-"+year.toString();
      
    },
  },
  methods:{

    confirm(){
      if(this.date === ""){
          Toast.fire({
        icon: "error",
        title: "กรุณากรอกข้อมูล",
      });
        return
         }
      let param = {
        date: this.date,
        page:1,
      }
      param["date"] = this.date,
      param['page'] = 1
      if(this.type !== '')param['vehicle_type'] = this.type
      if(this.province !== '')param['province'] = this.province

      this.$router.push({ path: "/origin-destination-detail",query:param});
      
   
    // var param ={
    //     'date':this.date
    //   }
    //  if(this.type){
    //     param["vehicle_type"] = this.type
    //   }
    //   if(this.province){
    //     param["province"] = this.province
    //   }
    //   param["page"] = 1
    //   this.$router.push( {path: '/origin-destination-detail',query:param});
    },
    headerbar(drawer){
      this.drawer = drawer;
    },
        getListProvince(){
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/provinces"
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
            this.listProvince = response.data.data
           
          }
          else{
            Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลจังหวัดได้',     
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
          title: 'ไม่สามารถดึงข้อมูลจังหวัดได้',     
        })

          });
              },
    getListCarType(){
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/vehicles-type"
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
            this.listCarType = response.data.data
           
          }else{
             Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลประเภทรถได้',     
        })
        }
      }).catch((error) => {
        if(error.response.data.message === 'session timeout'){
            this.$store.dispatch("logout");
            this.$router.push('/')
             Toast.fire({
              icon: "error",
              title: error.response.data.message,
            });

            return;
        }
      console.log(error);
     Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลประเภทรถได้',     
        })
      });
       
    },
  },
  mounted(){
    this.getListProvince()
    this.getListCarType()
  }

};
</script>
<style scoped>
@import "../assets/css/background.css";
/* .headertext{
  font-weight: 600;
  font-size: 24px;
  color: #FFFFFF;
} */
.subheadertext{
  font-weight: 600;
  font-size: 18px;
  color: #FFFFFF;
}
/* .headertext-mobile{
    font-weight: 600;
    font-size: 20px;
    color: #FFFFFF;
} */
.sl {background: rgba(255, 255, 255, 0.9);border-radius: 15px;}
.search-vahicle {width: 50%;}
.search-vahicle-mobile {width: 100%;}
</style>
