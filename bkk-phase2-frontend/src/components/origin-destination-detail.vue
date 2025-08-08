<template>
    <v-row justify="center">
        <v-dialog  v-model="shower" scrollable persistent max-width="1200px">
            <v-card>
                <v-card-title>
                    รายละเอียด
                    <v-spacer></v-spacer><v-btn text fab @click="$emit('close')"><v-icon>mdi-close-thick</v-icon></v-btn>
                </v-card-title>
               <v-card-text>
     <v-container v-if="$vuetify.breakpoint.width > 1264">  
    <v-layout >
      <v-flex xs12 lg6 >
        <v-card style="background: white;" id="borderblue" height="100%" class="d-flex align-start">
          <v-card-text class="pa-0 pt-0">
            <v-layout
              row
              wrap
              align-center
              justify-center
              fill-height
              class="ma-0"
            >
              <v-flex lg12 md12 xs12 class="text-center ">
                <v-flex>
                  <!-- <img
                  :src="imageVehicle"
                  width="100%"
                  height="100%"
                 /> -->
                <img
                  :src="data.image_url"
                  width="100%"
                  height="100%"
                 />
                </v-flex>  
                <!-- <v-flex>
                  <img
                  :src="video"
                  width="100%"
                  height="100%"
                  
                />
                </v-flex> -->
                <!-- <v-flex>
                  <img
                  :src="plate_pic"
                  width="50%"
                  height="50%"
                  
                />
                </v-flex>             -->
              </v-flex>
            </v-layout>
              </v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs12 lg6 >
               <v-card style="background: white" class="pl-3 pr-3" id="borderflex" height="100%">
               <v-card-text class="pa-0">
                <v-layout>
              <v-flex lg12 md12 xs12 >
                  <v-row>
                    <v-col cols="7" >
                        <img
                  :src="data.plate_picture"
                  width="100%"
                  height="150px"  
                />
                    </v-col>
                    <v-col class="pa-0">
                    <v-col> 
                        <span class="title-style">ทะเบียนยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.plate_no}}</span></v-card>
                    </v-col>
                    <v-col class="pt-0"><span class="title-style">จังหวัด</span>
                       <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.province}}</span></v-card>
                    </v-col>
                   </v-col>
                  </v-row>
                  <v-row>
                    <v-col class="pt-0">           
                        <span class="title-style">สียานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.vehicle_color}}</span></v-card>
                    </v-col>
                    <v-col class="pt-0"><span class="title-style">ประเภทยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.vehicle_type}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col class="d-flex align-center pt-0">
                        <v-container>
                        <span class="title-style">วัน/เดือน/ปี</span>
                        <v-card  class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.date}}</span></v-card>
                    </v-container>
                    </v-col>
                    <v-col  class="pt-0">
                        <v-row class="pa-0">
                            <v-col >
                            <span class="title-style">สถานที่เริ่มต้น</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{data.origin}}</span></v-card>
                       </v-col>
                        </v-row>
                         <v-row class="pa-0">
                            <v-col class="pt-0">
                            <span class="title-style">สถานที่ปลายทาง</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{data.destination}}</span></v-card>
                            </v-col>
                        </v-row>
                    </v-col>
                    <v-col  class="pt-0">
                        <v-row  class="pa-0">
                            <v-col >
                            <span class="title-style">เวลาเริ่มต้น</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{data.start_time}}</span></v-card>
                        </v-col>
                        </v-row>
                        <v-row class="pa-0">
                            <v-col class="pt-0">
                            <span class="title-style">เวลาปลายทาง</span>
                             <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{data.end_time}}</span></v-card>
                            </v-col>
                        </v-row>
                    </v-col>
                  </v-row>
                  <br/>
              </v-flex>
            </v-layout>
          </v-card-text>
               </v-card>
      </v-flex>
    </v-layout>
    <v-layout>
         <v-row>
                    <v-card class="elevation-0 pa-3" style="width:100% ;height:650px">
                    <viewmap  keyPage="destination" :lat="data.latitude" :lon="data.longtitude" :destination_lat="data.destination_lat" :destination_lon="data.destination_long"></viewmap>
                    </v-card>
                  </v-row>
    </v-layout>
    <exportfile class="pt-6" :keypage="keypage" @download="report"></exportfile>
    </v-container>
         <v-container v-else-if="$vuetify.breakpoint.width < 1264 && $vuetify.breakpoint.width > 750">  
    <v-layout row wrap align-center justify-center>
      <v-flex xs12 lg12 class="ma-5">
        <v-card style="background: white;" id="border" class="d-flex align-center" >
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
                  <!-- <img
                  :src="imageVehicle"
                  width="100%"
                  height="100%"
                 /> -->
                <img
                  :src="data.image_url"
                  width="100%"
                  height="100%"
                 />
                </v-flex>         
              </v-flex>
              <v-flex lg6 md12 xs12 style="background: white" class="pa-3" id="borderflex-mobile">
                <br/>
                <v-row>
                    <v-col cols="7" >
                        <img
                  :src="data.plate_picture"
                  width="100%"
                  height="150px"  
                />
                    </v-col>
                    <v-col class="pa-0">
                    <v-col> 
                        <span class="title-style">ทะเบียนยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.plate_no}}</span></v-card>
                    </v-col>
                    <v-col class="pt-0"><span class="title-style">จังหวัด</span>
                       <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.province}}</span></v-card>
                    </v-col>
                   </v-col>
                  </v-row>
                   <v-row>
                    <v-col class="pt-0">           
                        <span class="title-style">สียานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.vehicle_color}}</span></v-card>
                    </v-col>
                    <v-col class="pt-0"><span class="title-style">ประเภทยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.vehicle_type}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col class="d-flex align-center pt-0">
                        <v-container>
                        <span class="title-style">วัน/เดือน/ปี</span>
                        <v-card  class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.date}}</span></v-card>
                    </v-container>
                    </v-col>
                    <v-col  class="pt-0">
                        <v-row class="pa-0">
                            <v-col >
                            <span class="title-style">สถานที่เริ่มต้น</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{data.origin}}</span></v-card>
                       </v-col>
                        </v-row>
                         <v-row class="pa-0">
                            <v-col class="pt-0">
                            <span class="title-style">สถานที่ปลายทาง</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{data.destination}}</span></v-card>
                            </v-col>
                        </v-row>
                    </v-col>
                    <v-col  class="pt-0">
                        <v-row  class="pa-0">
                            <v-col >
                            <span class="title-style">เวลาเริ่มต้น</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{data.start_time}}</span></v-card>
                        </v-col>
                        </v-row>
                        <v-row class="pa-0">
                            <v-col class="pt-0">
                            <span class="title-style">เวลาปลายทาง</span>
                             <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{data.end_time}}</span></v-card>
                            </v-col>
                        </v-row>
                    </v-col>
                  </v-row>
                  <br/>
              </v-flex>
            </v-layout>
            <v-layout>
                 <v-row>
                    <v-card class="elevation-0 pa-3" style="width:100% ;height:650px">
                    <viewmap keyPage="destination" :lat="data.latitude" :lon="data.longtitude" :destination_lat="data.destination_lat" :destination_lon="data.destination_long"></viewmap>
                    </v-card>
                  </v-row>
            </v-layout>
          </v-card-text>
        </v-card>
         
      </v-flex>
    </v-layout>
    <exportfile class="pt-6" :keypage="keypage" @download="report"></exportfile>
    </v-container>

      <v-container v-else>  
    <v-layout row wrap align-center justify-center>
      <v-flex xs12 lg12 >
        <v-card style="background: white;" id="border" class="pa-0 d-flex align-center" >
          <v-card-text class="pa-0">
            <v-layout
              row
              wrap
              align-center
              justify-center
              fill-height
              class="ma-0"
            >
              <v-flex lg6 md12 xs12 class="text-center" >
               <v-flex>
                  <!-- <img
                  :src="imageVehicle"
                  width="100%"
                  height="100%"
                 /> -->
                <img
                  :src="data.image_url"
                  width="100%"
                  height="100%"
                 />
                </v-flex>         
              </v-flex>
              <v-flex lg6 md12 xs12 style="background: white" class="pa-3" id="borderflex-mobile">
                <v-row>
                 <!-- <img
                  :src="plate_pic"
                  width="50%"
                  height="50%"
                  
                /> -->
                <img
                  :src="data.plate_picture"
                  width="100%"
                  height="100%"  
                />
                </v-row>
                  <v-row>
                    <v-col>
                        <span class="title-style">ทะเบียนยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.plate_no}}</span></v-card>
                    </v-col>
        
                  </v-row>
                    <v-row>
                    
                    <v-col><span class="title-style">จังหวัด</span>
                       <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.province}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>           
                        <span class="title-style">สียานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.vehicle_color}}</span></v-card>
                    </v-col>
                   
                  </v-row>
                  <v-row>
                
                    <v-col><span class="title-style">ประเภทยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.vehicle_type}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                   
                    <v-col><span class="title-style">วัน/เดือน/ปี</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{dataFilter.date}}</span></v-card>
                    </v-col>
                   
                  </v-row>
                  <v-row>
                    <v-col>
                        <span class="title-style">สถานที่เริ่มต้น</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{data.origin}}</span></v-card>
                    </v-col>
                    
                  </v-row>
                  <v-row>
                    
                    <v-col>
                        <span class="title-style">เวลาเริ่มต้น</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{data.start_time}}</span></v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                        <span class="title-style">สถานที่ปลายทาง</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{data.destination}}</span></v-card>
                    </v-col>
                   
                  </v-row>
                  <v-row>
                    <v-col>
                        <span class="title-style">เวลาปลายทาง</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style d-inline-block text-truncate">{{data.end_time}}</span></v-card>
                    </v-col>
                  </v-row>
                  <br/>
              </v-flex>
            </v-layout>
            <v-layout>
                 <v-row>
                    <v-card class="elevation-0 pa-3" style="width:100% ;height:450px">
                    <viewmap keyPage="destination" :lat="data.latitude" :lon="data.longtitude" :destination_lat="data.destination_lat" :destination_lon="data.destination_long" ></viewmap>
                    </v-card>
                  </v-row>
            </v-layout>
          </v-card-text>
        </v-card>
         
      </v-flex>
    </v-layout>
    <exportfile class="pt-6" :keypage="keypage" @download="report"></exportfile>
    </v-container>
</v-card-text>   
            </v-card>
        </v-dialog>
    </v-row>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
import Swal from "sweetalert2/dist/sweetalert2.js";
import viewmap from '@/components/map.vue'
import exportfile from "@/components/export-file.vue";
import fontTH from "../fontTH.js";
import { jsPDF } from "jspdf";
//import * as jsPDF from 'jspdf'
//import * as autoTable from 'jspdf-autotable'
import "jspdf-autotable";
import THSarabunNewBold from "../THSarabunNewBold.js";
  const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});
export default {
    components:{
        viewmap,
        exportfile
    },
    props: ['show','data','dataFilter','base64_plate_pic','base64_image_pic','reportOther'],
    data() {
    return {
      keypage:"card",
      color:"",
      province:"",
      type:"",
      note:"",
      license:"",
      drawer: true,
      listColor:[],
      listProvince:[],
      listCarType:[],
      listCheckPoint:[],
      
    };
  },
    computed:{
        shower :{
            get() {
                if(this.show === true){
                //  console.log("show",this.dataItem);
                 //this.getImageReport()
                
                }
                return this.show
            },
            set (value) {
                if (!value) {
                // console.log("show",this.dataItem);
                }
            }
        },
    },
    methods:{
    report(){
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
      doc.text("รายงาน ข้อมูลแสดงจุดต้นทาง/ปลายทางของยานพาหนะ", 120, 55);
    //doc.text("ทางข้ามชนิดปุ่มกด", 250, 70);
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
      doc.text("user ที่ใช้งาน  "+this.reportOther.user, 70, 120);
      doc.text("วันที่  "+this.reportOther.report_date, 70, 140);
      doc.text("หน่วยงาน  "+this.reportOther.department, 70, 160);

     // console.log(this.plate_pic);
      // let carSM = require(this.plate_pic);
      // let carXL = require("@/assets/img/carBL2.png");
      // var car1 = new Image();
      // var car2 = new Image();
      // car1.src = carSM;
      // car2.src = carXL;
    
  
     

      doc.addImage(this.reportOther.base64_image_pic, "JPEG", 100, 230, 400, 200);
      doc.addImage(this.reportOther.base64_plate_pic, "JPEG", 400, 115, 100, 50);

      doc.text("ทะเบียนยานพาหนะ  "+this.dataFilter.plate_no, 200, 550);
      doc.text("จังหวัด  "+this.dataFilter.province, 200, 570);
      doc.text("ประเภทยานพาหนะ  "+this.dataFilter.vehicle_type, 200, 590);
      doc.text("สียานพาหนะ  "+this.dataFilter.vehicle_color, 200, 610);
      doc.text("วันที่  "+this.dataFilter.date, 200, 630);
      doc.text("สถานที่เริ่มต้น  "+this.data.origin, 200, 650);
      doc.text("เวลาเริ่มต้น  "+this.data.start_time, 200, 670);
      doc.text("สถานที่ปลายทาง  "+this.data.destination, 200, 690);
      doc.text("เวลาปลายทาง   "+this.data.end_time, 200, 710);
      
        
      
      doc.save(`รายงาน ข้อมูลแสดงจุดต้นทาง/ปลายทางของยานพาหนะ.pdf`);
    },
    getImageReport(){
      console.log("dats",this.data);
       let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/vehicle-destination-list/report";
      let data = {
        date:this.data.date_payload,
        plate_no:this.dataFilter.plate_no,
        province:this.dataFilter.province,
        vehicle_type:this.dataFilter.vehicle_type,
        vehicle_color:this.dataFilter.vehicle_color,
      }
      this.axios.get(url, {headers: { session: session_data },params: data})
      .then((response) => {
         console.log(response);
         
          if (response.status === 200) {
           
           
          }else{
           
          }
        })
    }
    },
    mounted(){
     
    }
}
</script>
<style>

</style>