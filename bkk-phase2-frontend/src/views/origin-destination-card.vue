<template>
  <v-app id="bg" >
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="false">
      <v-progress-circular
        indeterminate
        size="64"
      ></v-progress-circular>
    </v-overlay>
    <v-content class="ps-16 pe-16 pb-16 pt-8" v-if="$vuetify.breakpoint.width > 1264">
     <v-container> 
      <v-chip @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
     <v-icon large color="red">mdi-chevron-left</v-icon>
         <span class="text-left headerback">Back</span>
    </v-chip> 
        <v-chip large class="ma-2" color="#02754B">
                  <span class="pl-5 pr-5 headertext">ค้นหาข้อมูลจุดต้นทาง/ปลายทางของยานพาหนะ</span>
                </v-chip>  
                  
    <v-layout >
      <v-flex xs12 lg6 >
        <v-card style="background: #9EC6FA;" id="borderblue" height="100%" class="d-flex align-center">
          <v-card-text class="pa-0 pt-5">
            <v-layout
              row
              wrap
              align-center
              justify-center
              fill-height
              class="ma-0"
            >
              <v-flex lg12 md12 xs12 class="text-center pa-2 ">
                <v-flex>
                  <img
                  :src="imageVehicle"
                  width="100%"
                  height="100%"
                 />
                </v-flex>  
                <v-flex>
                  <img
                  :src="video"
                  width="100%"
                  height="100%"
                  
                />
                </v-flex>
                <v-flex>
                  <img
                  :src="plate_pic"
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
               <v-card style="background: white" class="pa-3" id="borderflex" height="100%">
               <v-card-text class="pa-0">
                <v-layout>
              <v-flex lg12 md12 xs12 >
                <br/>
                  <v-row>
                    <v-col>
                        <span class="title-style">ทะเบียนยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{licensePlate}}</span></v-card>
                    </v-col>
                    <v-col><span class="title-style">จังหวัด</span>
                       <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{province}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>           
                        <span class="title-style">สียานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{color}}</span></v-card>
                    </v-col>
                    <v-col><span class="title-style">ประเภทยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{type}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col class="d-flex align-center">
                        <v-container>
                        <span class="title-style">วัน/เดือน/ปี</span>
                        <v-card  class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{date}}</span></v-card>
                    </v-container>
                    </v-col>
                    <v-col>
                        <v-row>
                            <v-col>
                            <span class="title-style">สถานที่เริ่มต้น</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{locationStart}}</span></v-card>
                       </v-col>
                        </v-row>
                         <v-row>
                            <v-col>
                            <span class="title-style">สถานที่ปลายทาง</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{locationEnd}}</span></v-card>
                            </v-col>
                        </v-row>
                    </v-col>
                    <v-col>
                        <v-row>
                            <v-col>
                            <span class="title-style">เวลาเริ่มต้น</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{timeStart}}</span></v-card>
                        </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                            <span class="title-style">เวลาปลายทาง</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{timeEnd}}</span></v-card>
                            </v-col>
                        </v-row>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-card class="elevation-0 pa-3" style="width:100% ;height:650px">
                    <viewmap  keyPage="card" :checkpoint="location"></viewmap>
                    </v-card>
                  </v-row>
                  <br/>
              </v-flex>
            </v-layout>
          </v-card-text>
               </v-card>
      </v-flex>
    </v-layout>
    <!-- <exportfile class="pt-6" :keypage="keypage" @download="generateReport"></exportfile> -->
    </v-container>
    </v-content>
    <v-content class="ps-1 pe-1 pb-1 pt-1" v-else>
      <v-container>  
        <v-chip large class="ma-2" color="#02754B">
                  <span class="pl-5 pr-5 headertext-mobile">ค้นหาข้อมูลจุดต้นทาง/ปลายทาง<br/>ของยานพาหนะ</span>
                </v-chip>     
    <v-layout row wrap align-center justify-center>
      <v-flex xs12 lg12 class="ma-5">
        <v-card style="background: #9EC6FA;" id="border" class="d-flex align-center" >
          <v-card-text class="pa-0">
            <v-layout
              row
              wrap
              align-center
              justify-center
              fill-height
              class="ma-0"
            >
              <v-flex lg6 md12 xs12 class="text-center pa-2 " >
                <v-flex>
                  <img
                  :src="imageVehicle"
                  width="100%"
                  height="100%"
                 
                />
                </v-flex>  
                <v-flex>
                  <!-- <viewvideo  :height="height" :installCheck='false'></viewvideo> -->
                  <img
                  :src="video"
                  width="100%"
                  height="100%"
                  
                />
                </v-flex>
                <v-flex>
                  <img
                  :src="plate_pic"
                  width="50%"
                  height="50%"
                  
                />
                </v-flex>            
              </v-flex>
              <v-flex lg6 md12 xs12 style="background: white" class="pa-3" id="borderflex-mobile">
                <br/>
                  <v-row>
                    <v-col>
                        <span class="title-style">ทะเบียนยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{licensePlate}}</span></v-card>
                    </v-col>
        
                  </v-row>
                    <v-row>
                    
                    <v-col><span class="title-style">จังหวัด</span>
                       <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{province}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>           
                        <span class="title-style">สียานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{color}}</span></v-card>
                    </v-col>
                   
                  </v-row>
                  <v-row>
                
                    <v-col><span class="title-style">ประเภทยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{type}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                   
                    <v-col><span class="title-style">วัน/เดือน/ปี</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{date}}</span></v-card>
                    </v-col>
                   
                  </v-row>
                  <v-row>
                    <v-col>
                        <span class="title-style">สถานที่เริ่มต้น</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{location}}</span></v-card>
                    </v-col>
                    
                  </v-row>
                  <v-row>
                    
                    <v-col>
                        <span class="title-style">เวลาเริ่มต้น</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{time}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                        <span class="title-style">สถานที่ปลายทาง</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{location}}</span></v-card>
                    </v-col>
                   
                  </v-row>
                  <v-row>
                    <v-col>
                        <span class="title-style">เวลาปลายทาง</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{time}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-card class="elevation-0 pa-3" style="width:100% ;height:650px">
                    <viewmap keyPage="card" :checkpoint="location"></viewmap>
                    </v-card>
                  </v-row>
                  <br/>
              </v-flex>
            </v-layout>
          </v-card-text>
        </v-card>
         
      </v-flex>
    </v-layout>
    <!-- <exportfile class="pt-6" :keypage="keypage" @download="generateReport"></exportfile> -->
    </v-container>
    </v-content>
    <blacklistpdf @onProgress="onloading"  :downloadpdf="downloadpdf" :title="titlepage" :data="dataCard"></blacklistpdf>
  </v-app>
</template>
<script>
  const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
// import adddetail from "../components/add-vehicle-detail.vue";
import exportfile from "../components/export-file.vue";
 //import viewvideo from "../components/view-video.vue";
import headerbar from "../components/header-bar.vue";
import viewmap from '@/components/map.vue'
import blacklistpdf from "./blacklistpdf.vue";
import fontTH from "../fontTH.js";
import { jsPDF } from "jspdf";
//import * as jsPDF from 'jspdf'
//import * as autoTable from 'jspdf-autotable'
import "jspdf-autotable";
import THSarabunNewBold from "../THSarabunNewBold.js";
export default {
  components: {
    sidebar,
    viewmap,
    // adddetail,
    exportfile,
    headerbar,
   // viewvideo,
    blacklistpdf,
  },
  data() {
    return {
      titlepage:"รายงาน ยานพาหนะที่กำหนด (Blacklist Report)",
      onProgress: false,
      downloadpdf:false,
      keypage:"card",
      drawer: true,
      height:"450rem",
      imageVehicle: '',
      licensePlate: '',
      province: '',
      color: '',
      type: '',
      location: '',
      date: '',
      time: '',
      plate_pic:'',
      video:'',
      id:'',
      dataCard:{},
      base64_plate_pic:'',
      base64_image_pic:''
    };
  },
  methods:{
    gobackpage(){
      let item = this.$route.query.queryPayload

      this.$router.push({path: "/origin-destination-detail", query:item});
    },
    getData(){
      // console.log("this.$route.params",this.$route);
      this.dataCard =  this.$route.query
      console.log("dataCard",this.dataCard);

      this.id = this.dataCard.id
      this.imageVehicle = this.dataCard.image_url
      this.licensePlate = this.dataCard.license
      this.province = this.dataCard.province
      this.color = this.dataCard.color
      this.type = this.dataCard.type
      this.location = this.dataCard.location
      this.date = this.dataCard.date
      this.time = this.dataCard.time
      this.plate_pic = this.dataCard.picture

      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/blacklist/"+this.id+"/report";
      this.onProgress = true
      this.axios.get(url, {headers: { session: session_data }})
      .then((response) => {
         console.log(response);
         
          if (response.status === 200) {
            this.onProgress =false
           this.dataCard["base64_image_pic"] = response.data.data.base64_image_pic ? response.data.data.base64_image_pic :''
           this.dataCard["base64_plate_pic"] = response.data.data.base64_plate_pic ? response.data.data.base64_plate_pic :''
           this.base64_image_pic = response.data.data.base64_image_pic ? response.data.data.base64_image_pic :''
           this.base64_plate_pic = response.data.data.base64_plate_pic ? response.data.data.base64_plate_pic :''
          }else{
            this.onProgress =false
          }
        })
        .catch((error) => {
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
        });
    },
    onloading(parameter){
      //this.onProgress = parameter;
    },
    generateReport(){
      console.log("generateReport");
      //  this.downloadpdf = !this.downloadpdf;
      //   this.onProgress = true

      let doc = new jsPDF({ orientation: "p", unit: "pt" });
      doc.addFileToVFS('THSarabunNew-bold.ttf', THSarabunNewBold.font);
      doc.addFileToVFS("THSarabunNew.ttf",fontTH.th);
      doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
      doc.addFont('THSarabunNew-bold.ttf', 'THSarabunNewBold', 'bold');
      
      doc.setLineWidth(1.5);
      doc.line(10, 835, 10, 10); // vertical line
      doc.setLineWidth(0.5);
      doc.line(10, 10, 585, 10);// horizontal line
      doc.setLineWidth(1.5);
      doc.line(585, 835, 585, 10); // vertical line
      doc.setLineWidth(0.5);
      doc.line(10, 835, 585, 835);// horizontal line
      doc.setFontSize(24);
      doc.setFont('THSarabunNewBold', 'bold')
      doc.text("รายงาน ยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจร", 150, 45);
       doc.text("ทางข้ามชนิดปุ่มกด", 250, 70);
      doc.setFont("THSarabunNew", "Bold");
      doc.setLineWidth(1.5);
      doc.line(50, 180, 50, 100); // vertical line
      doc.setLineWidth(0.5);
      doc.line(550, 100, 50, 100);// horizontal line
      doc.setLineWidth(1.5);
      doc.line(550, 180, 550, 100); // vertical line
      doc.setLineWidth(1.5);
      doc.line(380, 180, 380, 100); // vertical line
       doc.setLineWidth(0.5);
      doc.line(550, 180, 50, 180);// horizontal line
       doc.setFontSize(18);
      doc.text("user ที่ใช้งาน  "+this.licensePlate, 70, 120);
      doc.text("วันที่  "+this.province, 70, 140);
      doc.text("หน่วยงาน  "+this.type, 70, 160);

     // console.log(this.plate_pic);
      // let carSM = require(this.plate_pic);
      // let carXL = require("@/assets/img/carBL2.png");
      // var car1 = new Image();
      // var car2 = new Image();
      // car1.src = carSM;
      // car2.src = carXL;
    
  
      // console.log("car", carSM,car1);

      doc.addImage(this.base64_image_pic, "JPEG", 100, 230, 400, 200);
      doc.addImage(this.base64_plate_pic, "JPEG", 400, 80, 100, 50);

      doc.text("ทะเบียนยานพาหนะ  "+this.licensePlate, 200, 550);
      doc.text("จังหวัด  "+this.province, 200, 570);
      doc.text("ประเภทยานพาหนะ  "+this.type, 200, 590);
      doc.text("สียานพาหนะ  "+this.color, 200, 610);
      doc.text("สถานที่  "+this.location, 200, 630);
      doc.text("วันที่  "+this.date, 200, 650);
      doc.text("เวลา  "+this.time, 200, 670);
        
      
      doc.save(`รายงาน ยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด.pdf`);
    },
    
     headerbar(drawer){
      this.drawer = drawer;
    },
    getVideo(){
      let session_data = localStorage.getItem("session");
      let url =  baseUrl.ipServer + "/blacklist-playback?session=" + session_data + "&id=" + this.id
      // console.log('vdo', url)
      this.video = baseUrl.ipServer + "/blacklist-playback?session=" + session_data + "&id=" + this.id
    }
  },
  mounted() {
    this.getData();
    this.getVideo();
  },
};
</script>
<style>
@import '../assets/css/background.css';
.headerback{
 font-weight: 600;
  font-size: 24px;
   color: red;
}
#borderflex{
  border-radius: 0px 15px 15px 0px;
  
}
#borderblue{
  border-radius: 15px 0px 0px 15px;
  
}
#borderflex-mobile{
  border-radius: 0px 0px 15px 15px;
  
}
.title-style{
  color:#404040;
  font-weight: bold;
}
.text-style{
  color:#2463C1;
  font-weight: bold;
  font-size: 18px;
}
</style>
