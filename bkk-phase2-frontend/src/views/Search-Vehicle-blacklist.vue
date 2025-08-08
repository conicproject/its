<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer"></sidebar> 
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-content  class="pl-3" v-if="$vuetify.breakpoint.width > 1025">
      <v-container class="pl-1 pr-1">
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">ค้นหายานพาหนะที่กำหนด</span>
        </v-chip>
          <formsearch 
          class="search-vahicle pt-5"
          :listColor="listColor"
          :listCarType="listCarType"
          :listProvince="listProvince"
          :listCheckPoint="listCheckPoint"
          @confirm="confirm"
          ></formsearch>
          
      </v-container>

      <div>
        
      </div>
    </v-content>
    <v-content  class="pl-0 pb-16 pt-8" v-else>
      <v-container class="pl-1 pr-1">
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext-mobile">ค้นหายานพาหนะที่กำหนด</span>
        </v-chip>
          <formsearch 
          class="search-vahicle-mobile"
          :listColor="listColor"
          :listCarType="listCarType"
          :listProvince="listProvince"
          :listCheckPoint="listCheckPoint"
          @confirm="confirm"
          ></formsearch>
          
      </v-container>

      <div>
        
      </div>
    </v-content>
    
  </v-app>
</template>
<script>
  const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
import formsearch from "../components/form-search-vehicle.vue";
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
   formsearch,
   headerbar,
  },
  data(){
    return {
      drawer: true,
      listColor:[],
      listProvince:[],
      listCarType:[],
      listCheckPoint:[],
        }
  },
  methods:{
      getListColor(){
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/vehicles-color"
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
            this.listColor = response.data.data
          
          }else{
            Toast.fire({
              icon: 'error',
             title: 'ไม่สามารถดึงข้อมูลสีรถได้',     
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
             title: 'ไม่สามารถดึงข้อมูลสีรถได้',     
            })
      });
    },
    getListProvince(){
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/provinces"
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
            this.listProvince = response.data.data
            
          }else{
            Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลจังหวัดได้',     
        })

         // this.$router.push('/error')
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
          title: 'ไม่สามารถดึงข้อมูลประเภทรถได้',     
        })
      });
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
    confirm(carType,color,point,province,direction,date,license){
      // console.log(carType,color,point,province,direction,date,license);
        if(date === []){
          Toast.fire({
        icon: "error",
        title: "กรุณากรอกข้อมูล",
      });
        }else{
      // var param ={
      //   'date':date
      // }
      var param ={
       'startdate':date[0],
        'enddate':date[1] ? date[1] : date[0],
      }
      if(license){
        param["plate_no"] = license
      }
      if(carType){
        param["vehicle_type"] = carType
      }
      if(color){
        param["vehicle_color"] = color
      }
      if(point){
        param["checkpoint"] = point
      }
      if(province){
        param["province"] = province
      }
      if(direction){
        if(direction === "ขาเข้า"){
          param["direction"] = "inbound"
        }else{
          param["direction"] = "outbound"
        }
        
      }
      param["page"] = 1

        this.$router.push( {path: '/search-blacklist-table',query:param});
    }
    },
    headerbar(drawer){
      console.log("hhh",drawer);
      this.drawer = drawer;
    }
  },
  mounted(){
    this.getListCheckPoint();
   this.getListCarType();
    this.getListColor();
    this.getListProvince();  
  }
};
</script>
<style scoped>
@import "../assets/css/background.css";
.headertext{
  font-weight: 600;
  font-size: 24px;
  color: #FFFFFF;
}
.sl {background: rgba(255, 255, 255, 0.9);border-radius: 15px; width: 300px;}
.search-vahicle {width: 50%;}
.search-vahicle-mobile {width: 100%;}
</style>
