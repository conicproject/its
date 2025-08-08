<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="loading">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
    <v-content class="ps-16 pe-16 pb-16 pt-8" v-if="$vuetify.breakpoint.width > 1025">
      <v-container class="pl-16">
        <v-layout>
          <v-chip @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
            <v-icon large color="red">mdi-chevron-left</v-icon>
            <span class="text-left headerback">Back</span>
          </v-chip>
          <v-chip large class="ma-2" color="#02754B">
            <span class="pl-5 pr-5 headertext">ค้นหาข้อมูลรถบรรทุกในช่วงเวลาที่ห้ามเดินรถ</span>
          </v-chip>

        </v-layout>
        <!-- <adddetail :dataCard="dataCard"></adddetail> -->

        <v-layout>
          <v-flex xs12 lg6>
            <v-card style="background: #9EC6FA;" id="borderblue" height="100%" class="d-flex align-center">
              <v-card-text class="pa-0 pt-5">
                <v-layout row wrap align-center justify-center fill-height class="ma-0">
                  <v-flex lg12 md12 xs12 class="text-center pa-2 ">
                    <v-flex>
                      <img :src="imageVehicle" width="100%" height="100%" />
                    </v-flex>
                    <!-- <v-flex>
                  <img
                  :src="video"
                  width="100%"
                  height="100%"
                  
                />
                </v-flex> -->
                    <v-flex>
                      <img :src="plate_pic" width="50%" height="50%" />
                    </v-flex>
                  </v-flex>
                </v-layout>
              </v-card-text>
            </v-card>
          </v-flex>
          <v-flex xs12 lg6>
            <v-card style="background: white" class="pa-3" id="borderflex" height="100%">
              <v-card-text class="pa-0">
                <v-layout>
                  <v-flex lg12 md12 xs12>
                    <br />
                    <v-row>
                      <v-col>
                        <span class="title-style">ทะเบียนยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span
                            class="text-style d-inline-block text-truncate">{{ licensePlate }}</span></v-card>
                      </v-col>
                      <v-col><span class="title-style">จังหวัด</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span
                            class="text-style d-inline-block text-truncate">{{ province }}</span></v-card>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <span class="title-style">สียานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span
                            class="text-style d-inline-block text-truncate">{{ color }}</span></v-card>
                      </v-col>
                      <v-col><span class="title-style">ประเภทยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span
                            class="text-style d-inline-block text-truncate">{{ type }}</span></v-card>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <span class="title-style">สถานที่</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span
                            class="text-style d-inline-block text-truncate">{{ location }}</span></v-card>
                      </v-col>
                      <v-col><span class="title-style">วัน/เดือน/ปี</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span
                            class="text-style d-inline-block text-truncate">{{ date }}</span></v-card>
                      </v-col>
                      <v-col>
                        <span class="title-style">เวลา</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span
                            class="text-style d-inline-block text-truncate">{{ time }}</span></v-card>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-card class="elevation-0 pa-3" style="width:100% ;height:650px">
                        <viewmap :lat="lat" :lon="lon" keyPage="card" :checkpoint="location"></viewmap>
                      </v-card>
                    </v-row>
                    <br />
                  </v-flex>
                </v-layout>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
        <exportfile class="pt-6" :keypage="keypage" @download="generateReport"></exportfile>
      </v-container>
    </v-content>
    <v-content class="ps-1 pe-1 pb-1 pt-1" v-else>
      <v-container class="pl-1">
        <!-- <v-layout> -->
        <v-chip @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
          <v-icon large color="red">mdi-chevron-left</v-icon>
          <span class="text-left headerback">Back</span>
        </v-chip>
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext-mobile">ค้นหาข้อมูลรถบรรทุกในช่วงเวลา<br />ที่ห้ามเดินรถ</span>
        </v-chip>
        <!-- </v-layout>    -->
        <!-- <adddetail :dataCard="dataCard"></adddetail> -->
        <v-layout row wrap align-center justify-center>
          <v-flex xs12 lg12 class="ma-5">
            <v-card style="background: #9EC6FA;" id="border" class="d-flex align-center">
              <v-card-text class="pa-0">
                <v-layout row wrap align-center justify-center fill-height class="ma-0">
                  <v-flex lg6 md12 xs12 class="text-center pa-2 ">
                    <v-flex>
                      <img :src="imageVehicle" width="100%" height="100%" />
                    </v-flex>

                    <!-- <viewvideo  :height="height" :installCheck='false'></viewvideo> -->

                    <v-flex>
                      <img :src="plate_pic" width="50%" height="50%" />
                    </v-flex>
                  </v-flex>
                  <v-flex lg6 md12 xs12 style="background: white" class="pa-3" id="borderflex-mobile">
                    <br />
                    <v-row>
                      <v-col>
                        <span class="title-style">ทะเบียนยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{ licensePlate
                        }}</span></v-card>
                      </v-col>
                      <v-col><span class="title-style">จังหวัด</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{ province
                        }}</span></v-card>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <span class="title-style">สียานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{ color
                        }}</span></v-card>
                      </v-col>
                      <v-col><span class="title-style">ประเภทยานพาหนะ</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{ type
                        }}</span></v-card>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <span class="title-style">สถานที่</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{ location
                        }}</span></v-card>
                      </v-col>
                      <v-col><span class="title-style">วัน/เดือน/ปี</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{ date
                        }}</span></v-card>
                      </v-col>
                      <v-col>
                        <span class="title-style">เวลา</span>
                        <v-card class="elevation-0 pa-2" color="#DCF3FF"><span class="text-style">{{ time
                        }}</span></v-card>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-card class="elevation-0 pa-3" style="width:100% ;height:650px">
                        <viewmap :lat="lat" :lon="lon" keyPage="card" :checkpoint="location"></viewmap>
                      </v-card>
                    </v-row>
                    <br />
                  </v-flex>
                </v-layout>
              </v-card-text>
            </v-card>

          </v-flex>
        </v-layout>
        <exportfile class="pt-6" :keypage="keypage" @download="generateReport"></exportfile>
        <!-- <blacklistpdf @onProgress="onloading"  :downloadpdf="downloadpdf" :title="titlepage" :downloadexcel="downloadexcel"></blacklistpdf> -->
      </v-container>
    </v-content>
  </v-app>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
import adddetail from "../components/add-vehicle-detail.vue";
import exportfile from "../components/export-file.vue";
// import viewvideo from "../components/view-video.vue";
import headerbar from "../components/header-bar.vue";
import blacklistpdf from "./blacklistpdf.vue";
import fontTH from "../fontTH.js";
import { jsPDF } from "jspdf";
import "jspdf-autotable";
import THSarabunNewBold from "../THSarabunNewBold.js";
import viewmap from '@/components/map.vue'
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
    adddetail,
    exportfile,
    headerbar,
    blacklistpdf,
    viewmap,
  },
  data() {
    return {
      titlepage: "รายงาน รถบรรทุกเดินรถในช่วงเวลาที่ห้ามเดินรถ",
      onProgress: false,
      downloadpdf: false,
      keypage: "card",
      drawer: true,
      imageVehicle: '',
      licensePlate: '',
      province: '',
      color: '',
      type: '',
      location: '',
      date: '',
      time: '',
      plate_pic: '',
      video: '',
      id: '',
      lat: '',
      lon: '',
      dataCard: {},
      base64_plate_pic: '',
      base64_image_pic: '',
      loading: false,
      report_time: '',
      report_date: '',
      user: ''
    };
  },
  methods: {

    generateReport() {

      let doc = new jsPDF({ orientation: "p", unit: "pt" });
      doc.addFileToVFS('THSarabunNew-bold.ttf', THSarabunNewBold.font);
      doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
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
      doc.text("รายงาน รถบรรทุกเดินรถในช่วงเวลาที่ห้ามเดินรถ", 100, 45);
      doc.setFont("THSarabunNew", "Bold");
      doc.setLineWidth(1.5);
      doc.line(50, 150, 50, 60); // vertical line
      doc.setLineWidth(0.5);
      doc.line(550, 60, 50, 60);// horizontal line
      doc.setLineWidth(1.5);
      doc.line(550, 150, 550, 60); // vertical line
      doc.setLineWidth(1.5);
      doc.line(380, 150, 380, 60); // vertical line
      doc.setLineWidth(0.5);
      doc.line(550, 150, 50, 150);// horizontal line
      doc.setFontSize(18);
      doc.text("user ที่ใช้งาน  " + this.user, 70, 90);
      doc.text("วันที่  " + this.report_date, 70, 110);
      doc.text("หน่วยงาน  " + this.department, 70, 130);

      doc.addImage(this.base64_image_pic, "JPEG", 100, 180, 400, 200);
      doc.addImage(this.base64_plate_pic, "JPEG", 400, 80, 100, 50);


      doc.text("ทะเบียนยานพาหนะ  " + this.province, 200, 500);
      doc.text("จังหวัด  " + this.province, 200, 520);
      doc.text("ประเภทยานพาหนะ  " + this.type, 200, 540);
      doc.text("สียานพาหนะ  " + this.color, 200, 560);
      doc.text("สถานที่  " + this.location, 200, 580);
      doc.text("วันที่  " + this.date, 200, 600);
      doc.text("เวลา  " + this.time, 200, 620);


      doc.save(`รถบรรทุกเดินรถในช่วงเวลาที่ห้ามเดินรถ.pdf`);

    },
    headerbar(drawer) {

      this.drawer = drawer;
    },
    getData() {

      this.dataCard = this.$route.query;
      this.id = this.dataCard.id;
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/truck/" + this.id + "/report";
      this.loading = true;
      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {

          if (response.status === 200) {
            let isPublic = baseUrl.pathImg === "110.171.165.57" ? 1 : 0
            let resData = response.data.data
            // console.table(resData)

            // if (resData.plate_picture !== "None" && resData.plate_picture !== null) {
            //   resData.plate_picture = resData.plate_picture.replace('10.151.1.86', baseUrl.pathImg)
            //   if (isPublic === 1) {
            //     resData.plate_picture = resData.plate_picture.replace('6120', baseUrl.pathImgPort)
            //     resData.plate_picture = resData.plate_picture.replace('6040', baseUrl.pathImgPort)
            //   }
            // }

            // if (resData.image_url !== "None" && resData.image_url !== null) {
            //   resData.image_url = resData.image_url.replace('10.151.1.86', baseUrl.pathImg)
            //   if (isPublic === 1) {
            //     resData.image_url = resData.image_url.replace('6120', baseUrl.pathImgPort)
            //     resData.image_url = resData.image_url.replace('6040', baseUrl.pathImgPort)
            //   }
            // }

            this.loading = false;
            this.province = resData.province
            this.color = resData.color;
            this.licensePlate = resData.plate_no;
            this.location = resData.checkpoint
            this.type = resData.type
            this.date = this.setDateReportNew(resData.time)
            this.time = this.setTimeReport(resData.time)
            this.report_time = this.setTimeReport(resData.report_date)
            this.report_date = this.setDateReportNew(resData.report_date)
            this.user = resData.user
            this.department = resData.department
            // this.imageVehicle =
            //   resData.image_url ? resData.image_url : "";
            // this.plate_pic = resData.plate_picture
            //   ? resData.plate_picture
            //   : "";
            this.imageVehicle = isPublic == 1 ? resData.net_image : resData.bma_image
            this.plate_pic = isPublic == 1 ? resData.net_plate : resData.bma_plate
            this.base64_image_pic = resData.base64_image_pic
              ? resData.base64_image_pic
              : "";
            this.base64_plate_pic = resData.base64_plate_pic
              ? resData.base64_plate_pic
              : "";
            this.lat = resData.latitude;
            this.lon = resData.longtitude;
          } else {
            this.loading = false;
            Toast.fire({
              icon: "error",
              title: response.data.message,
            });
          }
        })
        .catch((error) => {
          console.log(error);
          this.loading = false;
          if (error.response.data.message === "session timeout") {
            this.$store.dispatch("logout");
            this.$router.push("/");

            Toast.fire({
              icon: "error",
              title: error.response.data.message,
            });

            return;
          }
          Toast.fire({
            icon: "error",
            title: "ไม่สามารถดูข้อมูลได้",
          });
        });
    },
    setDateReportNew(param) {
      let monthNames = [
        "มกราคม",
        "กุมภาพันธ์",
        "มีนาคม",
        "เมษายน",
        "พฤษภาคม",
        "มิถุนายน",
        "กรกฎาคม",
        "สิงหาคม",
        "กันยายน",
        "ตุลาคม",
        "พฤศจิกายน",
        "ธันวาคม",
      ];
      let date = param.split("T")[0].split("-")
      let time = param.split("T")[1]
      let month = date[1] === '01' ? monthNames[0] : date[1] === '02' ? monthNames[1] : date[1] === '03' ? monthNames[2] : date[1] === '04' ? monthNames[3] : date[1] === '05' ? monthNames[4] : date[1] === '06' ? monthNames[5] : date[1] === '07' ? monthNames[6] : date[1] === '08' ? monthNames[7] : date[1] === '09' ? monthNames[8] : date[1] === '10' ? monthNames[9] : date[1] === '11' ? monthNames[10] : date[1] === '12' ? monthNames[11] : "";
      return `${date[2]} ${month} ${date[0]}`;


    },
    setTimeReport(param) {
      let time = param.split("T")[1].split(":")
      return `${time[0]}:${time[1]}`;
    },
    gobackpage() {
      const data = this.$route.query;
      delete data.id;
      this.$router.push({ path: "/truck-all", query: data });
    }
  },
  mounted() {
    this.getData()
  },
};
</script>
<style>
@import '../assets/css/background.css';

#borderflex {
  border-radius: 0px 15px 15px 0px;

}

#borderflex-mobile {
  border-radius: 0px 0px 15px 15px;

}

.title-style {
  color: #404040;
  font-weight: bold;
}

.text-style {
  color: #2463C1;
  font-weight: bold;
}

.headerback {
  font-weight: 600;
  font-size: 24px;
  color: red;
}</style>
