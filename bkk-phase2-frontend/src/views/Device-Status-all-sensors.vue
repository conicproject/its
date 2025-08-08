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
    <v-content  class="ps-16 pe-16 pb-16 pt-8"  v-if="$vuetify.breakpoint.width > 1025">
      <v-container class="pl-16">
        <v-chip @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
     <v-icon large color="red">mdi-chevron-left</v-icon>
         <span class="text-left headerback">Back</span>
    </v-chip> 
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">รายงานสถานะอุปกรณ์</span>
        </v-chip>
      
        <v-layout>
          <v-flex class="pa-3">
             <span class="text-left headerpage">All Sensors</span>
          </v-flex>
          <!-- <v-btn id="container3" v-scroll-to="{ el: '#container1' }">ทำงาน(Up)</v-btn> -->
        </v-layout>
       
  <v-simple-table v-if="dataOffline.length >0"  class="table-scroll small-first-col">
     
    <template v-slot:default>
        <thead>
        <tr>
            <th class="text-center">
           
          </th>
          <th class="text-center">
            ไม่ทำงาน(Down)
          </th>
          <th class="text-center">
            
          </th>
          
        </tr>
      </thead>
      <thead>
        <tr>
          <th width="40%"  class="text-center">
            อุปกรณ์
          </th>
          <th width="30%" class="text-center">
            IP Address
          </th>
          <th width="30%" class="text-center">
            จุดติดตั้ง
          </th>
        </tr>
      </thead>

      <tbody class="body-half-screen">
        <tr
          v-for="item in dataOffline"
          :key="item.name"
        >
          <td class="text-center">{{ item.name }}</td>
          <td class="text-center">{{ item.ip }}</td>
          <td class="text-center">{{ item.checkpoint }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>

  <v-simple-table v-else class="table-scroll small-first-col">
    <template v-slot:default>
      <thead>
        <tr>
            <th class="text-center">
           
          </th>
          <th class="text-center">
            ไม่ทำงาน(Down)
          </th>
          <th class="text-center">
            
          </th>
          
        </tr>
      </thead>
      <thead>
        <tr>
          <th width="40%"  class="text-center">
            อุปกรณ์
          </th>
          <th width="30%" class="text-center">
            IP Address
          </th>
          <th width="30%" class="text-center">
            จุดติดตั้ง
          </th>
        </tr>
      </thead>
      <tbody class="body-half-screen">
        <tr
         
        >
          <td class="text-center"></td>
          <td class="text-center">ไม่มีข้อมูล</td>
          <td class="text-center"></td>
        </tr>
      </tbody>

    </template>
  </v-simple-table>
<br/><br/>
<!-- <v-layout justify-end class="pb-3"><v-btn id="container1" v-scroll-to="{ el: '#container3' }">ไม่ทำงาน(down)</v-btn></v-layout> -->
  <v-simple-table ref="up" v-if="dataOnline.length >0" class="table-scroll small-first-col">
    <template v-slot:default>
        <thead>
        <tr>
            <th width="40%" class="text-center">
           
          </th>
          <th width="30%" class="text-center">
            ทำงาน(Up)
          </th>
          <th width="30%" class="text-center">
            
          </th>
          
        </tr>
      </thead>
      <thead>
        <tr>
          <th class="text-center">
            อุปกรณ์
          </th>
          <th class="text-center">
            IP Address
          </th>
          <th class="text-center">
            จุดติดตั้ง
          </th>
        </tr>
      </thead>
      <tbody class="body-half-screen">
        <tr
          v-for="item in dataOnline"
          :key="item.name"
        >
          <td class="text-center">{{ item.name }}</td>
          <td class="text-center">{{ item.ip }}</td>
          <td class="text-center">{{ item.checkpoint }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>

  <v-simple-table v-else class="table-scroll small-first-col">
    <template v-slot:default>
      <thead>
        <tr>
            <th class="text-center">
           
          </th>
          <th class="text-right">
            ทำงาน(Up)
          </th>
          <th class="text-center">
            
          </th>
          
        </tr>
      </thead>
      <thead>
        <tr>
          <th width="40%"  class="text-center">
            อุปกรณ์
          </th>
          <th width="30%" class="text-center">
            IP Address
          </th>
          <th width="30%" class="text-center">
            จุดติดตั้ง
          </th>
        </tr>
      </thead>
      <tbody class="body-half-screen">
        <tr
         
        >
          <td class="text-center"></td>
          <td class="text-center">ไม่มีข้อมูล</td>
          <td class="text-center"></td>
        </tr>
      </tbody>

    </template>
  </v-simple-table>

  <!-- <exportfile class="pt-6"  :keypage="keypage" @download="generateReport" :json_data="json_data" :title="titletext" :dataOn="dataOnline" :dataOff="dataOffline"></exportfile> -->
   <!-- <v-btn >download</v-btn> -->
      </v-container>
    </v-content>
    <v-content class="pa-1" v-else>
      <v-container class="pl-1 pr-1">
        <v-chip @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
     <v-icon large color="red">mdi-chevron-left</v-icon>
         <span class="text-left headerback">Back</span>
    </v-chip> 
       <v-chip large class="ma-2" color="#02754B">
          <span class="pl-3 pr-3 headertext-mobile">รายงานสถานะอุปกรณ์</span>
        </v-chip>
       
            <v-layout>
          <v-flex class="pa-3">
             <span class="text-left headerpage">All Sensors</span>
          </v-flex>
          <!-- <v-btn  id="container4" v-scroll-to="{ el: '#container2' }">ทำงาน(Up)</v-btn> -->
        </v-layout>
         <v-simple-table class="table-scroll small-first-col" v-if="dataOffline.length >0">
    <template v-slot:default>
        <thead>
        <tr>
            <th class="text-center">
           
          </th>
          <th class="text-right">
            ไม่ทำงาน(Down)
          </th>
          <th class="text-center">
            
          </th>
          
        </tr>
      </thead>
      <thead>
        <tr>
          <th width="40%"  class="text-center">
            อุปกรณ์
          </th>
          <th width="30%" class="text-center">
            IP Address
          </th>
          <th width="30%" class="text-center">
            จุดติดตั้ง
          </th>
        </tr>
      </thead>
      <tbody class="body-half-screen">
        <tr
          v-for="item in dataOffline"
          :key="item.name"
        >
          <td class="text-center">{{ item.name }}</td>
          <td class="text-center">{{ item.ip }}</td>
          <td class="text-center">{{ item.checkpoint }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>

  <v-simple-table v-else class="table-scroll small-first-col">
    <template v-slot:default>
      <thead>
        <tr>
            <th class="text-center">
           
          </th>
          <th class="text-center">
            ไม่ทำงาน(Down)
          </th>
          <th class="text-center">
            
          </th>
          
        </tr>
      </thead>
      <thead>
        <tr>
          <th width="40%"  class="text-center">
            อุปกรณ์
          </th>
          <th width="30%" class="text-center">
            IP Address
          </th>
          <th width="30%" class="text-center">
            จุดติดตั้ง
          </th>
        </tr>
      </thead>
      <tbody class="body-half-screen">
        <tr
         
        >
          <td class="text-center"></td>
          <td class="text-center">ไม่มีข้อมูล</td>
          <td class="text-center"></td>
        </tr>
      </tbody>

    </template>
  </v-simple-table>
<br/><br/>
<!-- <v-layout justify-end class="pb-3"><v-btn id="container2" v-scroll-to="{ el: '#container4' }">ไม่ทำงาน(down)</v-btn></v-layout> -->
  <v-simple-table  class="table-scroll small-first-col" v-if="dataOnline.length >0">
    <template v-slot:default>
        <thead>
        <tr>
            <th width="40%" class="text-center">
           
          </th>
          <th width="30%" class="text-center">
            ทำงาน(Up)
          </th>
          <th width="30%" class="text-center">
            
          </th>
          
        </tr>
      </thead>
      <thead>
        <tr>
          <th class="text-center">
            อุปกรณ์
          </th>
          <th class="text-center">
            IP Address
          </th>
          <th class="text-center">
            จุดติดตั้ง
          </th>
        </tr>
      </thead>
      <tbody class="body-half-screen">
        <tr
          v-for="item in dataOnline"
          :key="item.name"
        >
          <td class="text-center">{{ item.name }}</td>
          <td class="text-center">{{ item.ip }}</td>
          <td class="text-center">{{ item.checkpoint }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
  <v-simple-table v-else class="table-scroll small-first-col">
    <template v-slot:default>
      <thead>
        <tr>
            <th class="text-center">
           
          </th>
          <th class="text-center">
            ทำงาน(Up)
          </th>
          <th class="text-center">
            
          </th>
          
        </tr>
      </thead>
      <thead>
        <tr>
          <th width="40%"  class="text-center">
            อุปกรณ์
          </th>
          <th width="30%" class="text-center">
            IP Address
          </th>
          <th width="30%" class="text-center">
            จุดติดตั้ง
          </th>
        </tr>
      </thead>
      <tbody class="body-half-screen">
        <tr
         
        >
          <td class="text-center"></td>
          <td class="text-center">ไม่มีข้อมูล</td>
          <td class="text-center"></td>
        </tr>
      </tbody>

    </template>
  </v-simple-table>

         <!-- <exportfile class="pt-6" :keypage="keypage" @download="generateReport" :json_data="json_data" :title="titletext" :dataOn="dataOnline" :dataOff="dataOffline"></exportfile> -->
         <!-- <v-btn @click="generateReport">download</v-btn> -->
      </v-container>

      <div>
        
      </div>
    </v-content>
    <!-- <sensorpdf  :downloadpdf="downloadpdf" :downloadexcel="downloadexcel" :dataOn="dataOnline" :dataOff="dataOffline"></sensorpdf> -->
  </v-app>
</template>
<script>
  const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
import headerbar from "../components/header-bar.vue";
import exportfile from "../components/export-file.vue";
import sensorpdf from "../formatExport/DeviceAllSensorPDF.vue";
import fontTH from "../fontTH.js";
import { jsPDF } from "jspdf";
import Swal from "sweetalert2/dist/sweetalert2.js";
const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});
//import * as jsPDF from 'jspdf'
//import * as autoTable from 'jspdf-autotable'
import "jspdf-autotable";

export default {
  components: {
    sidebar,
   exportfile,
   headerbar,
   sensorpdf,
  },
  data(){
    return {
      downloadexcel:false,
                  columns: [
        { title: "อุปกรณ์", dataKey: "col1" },
        { title: "IP Adress", dataKey: "col2" },
        { title: "จุดติดตั้ง", dataKey: "col3" },
      ],
      rows: [
        {
          col1: "data",
          col2: "data",
          col3: "data",
        },
         {
          col1: "data",
          col2: "data",
          col3: "data",
        },
        {
          col1: "data",
          col2: "data",
          col3: "data",
        },
      ],
      titletext:"All sensor",
       keypage:"allsensor",
      onProgress: false,
      downloadpdf:false,
      drawer: true,
      dataOnline:[],
      dataOffline:[],
    }
  },
  methods:{

     generateReport(){
      console.log("generateReport");
       this.downloadpdf = !this.downloadpdf;

      
    },
   
    headerbar(drawer){
      console.log("hhh",drawer);
      this.drawer = drawer;
    },
    gobackpage(){
        let path = localStorage.getItem('activepath') === 'null' ?'/device-status':localStorage.getItem('activepath');
      console.log(path);
      this.$router.push(path);
    },

    getDataAllSensor(){
      let session_data = localStorage.getItem("session");
      this.onProgress = true;
    
     let url = this.$route.query.checkpoint === undefined ? baseUrl.ipServer + "/devices-status/all-sensors" : baseUrl.ipServer + "/device-status/all-sensors/"+this.$route.query.checkpoint
  
     //let url = baseUrl.ipServer + "/devices-status/all-sensors" 
     console.log(url);
      this.axios.get(url,{headers:{session:session_data}})
      .then((response) => {
          if(response.data.status_code === 200){
           
           let res = response.data.data
           this.dataOnline = res.online
           this.dataOffline = res.offline
           this.onProgress = false;
          }else{
           
           Toast.fire({
          icon: 'error',
          title: 'Cannot connet API',     
        })
            this.onProgress = false;
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
          title: 'Cannot connet API',     
        })
        this.onProgress = false;
      });
    }
  },
  mounted() {
   this.getDataAllSensor()
   
  },
};
</script>
<style scoped>
@import "../assets/css/background.css";
.headerback{
 font-weight: 600;
  font-size: 24px;
    color: red;
}
.headertext{
  font-weight: 600;
  font-size: 24px;
  color: #FFFFFF;
}
.headerpage{
  font-weight: 600;
  font-size: 24px;
  color: #02754B;
}
.headertext-mobile{
  font-weight: 600;
  font-size: 18px;
  color: #FFFFFF;
}

.sl {background: rgba(255, 255, 255, 0.9);border-radius: 15px;}
.search-vahicle {width: 50%;}

.table-scroll{
  /*width:100%; */
  display: block;
  empty-cells: show;
  
  /* Decoration */
  border-spacing: 0;
  border: 0px solid;
}

.table-scroll thead{
  background-color: #f1f1f1;  
  position:relative;
  display: block;
  width:100%;
  overflow-y: scroll;
}

.table-scroll tbody{
  /* Position */
  display: block; position:relative;
  width:100%; overflow-y:scroll;
  /* Decoration */
  border-top: 1px solid rgba(0,0,0,0.2);
}

.table-scroll tr{
  width: 100%;
  display:flex;
}

.table-scroll td,.table-scroll th{
  flex-basis:33%;
  flex-grow:2;
  display: block;
  padding: 1rem;
  text-align:left;
}


.table-scroll.small-first-col td:first-child,
.table-scroll.small-first-col th:first-child{
  flex-basis:20%;
  /* flex-grow:1; */
}

.table-scroll tbody tr:nth-child(2n){
  background-color: rgba(255, 255, 255, 0.9);
}

.body-half-screen{
  max-height: 50vh;
}

.small-col{
  flex-basis:10%;
  }
</style>
