<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="onProgress">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
    <v-main class="pl-3">
      <v-container class="pl-1 pr-1">
        <v-layout v-if="$vuetify.breakpoint.width > 1025">
          <v-chip
            @click="gobackpage()"
            large
            class="ma-2 pl-0"
            color="transparent"
          >
            <v-icon large color="red">mdi-chevron-left</v-icon>
            <span class="text-left headerback">Back</span>
          </v-chip>
          <v-chip large class="ma-2" color="#02754B">
            <span class="pl-5 pr-5 headertext">ค้นหาข้อมูลยานพาหนะ</span>
          </v-chip>
        </v-layout>
        <v-layout v-else>
          <v-chip
            @click="gobackpage()"
            large
            class="ma-2 pl-0"
            color="transparent"
          >
            <v-icon large color="red">mdi-chevron-left</v-icon>
            <span class="text-left headerback">Back</span>
          </v-chip>
          <v-chip large class="ma-2" color="#02754B">
            <span class="pl-5 pr-5 headertext-mobile">ค้นหาข้อมูลยานพาหนะ</span>
          </v-chip>
        </v-layout>
        <adddetail class="pt-5" :dataCard="dataCard"></adddetail>
        <exportfile
          class="pt-6"
          :keypage="keypage"
          @download="generateReport"
        ></exportfile>
      </v-container>
      <!-- <blacklistpdf @onProgress="onloading"  :downloadpdf="downloadpdf" :title="titlepage" :data="dataCard"></blacklistpdf> -->
    </v-main>
  </v-app>
</template>
<script>
const baseUrl = require("../../baseUrl.json");
import { mapGetters } from "vuex";
import sidebar from "../components/sidebar-new.vue";
import adddetail from "../components/add-vehicle-detail.vue";
import exportfile from "../components/export-file.vue";
// import viewvideo from "../components/view-video.vue";
import headerbar from "../components/header-bar.vue";
import blacklistpdf from "./blacklistpdf.vue";
import fontTH from "../fontTH.js";
import { jsPDF } from "jspdf";

//import * as jsPDF from 'jspdf'
//import * as autoTable from 'jspdf-autotable'
import "jspdf-autotable";
import THSarabunNewBold from "../THSarabunNewBold.js";
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
  },
  data() {
    return {
      titlepage: "รายงาน ยานพาหนะ",
      onProgress: false,
      downloadpdf: false,
      keypage: "card",
      drawer: true,
      dataCard: {},
    };
  },
  computed: {
    ...mapGetters(["dataSearch"]),
  },
  methods: {
    onloading(parameter) {
      this.onProgress = parameter;
    },
    generateReport() {
      console.log("generateReport", this.dataCard);
      let doc = new jsPDF({ orientation: "p", unit: "pt" });
      doc.addFileToVFS("THSarabunNew-bold.ttf", THSarabunNewBold.font);
      doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);
      doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
      doc.addFont("THSarabunNew-bold.ttf", "THSarabunNewBold", "bold");

      doc.setLineWidth(1.5);
      doc.line(10, 835, 10, 10); // vertical line
      doc.setLineWidth(0.5);
      doc.line(10, 10, 585, 10); // horizontal line
      doc.setLineWidth(1.5);
      doc.line(585, 835, 585, 10); // vertical line
      doc.setLineWidth(0.5);
      doc.line(10, 835, 585, 835); // horizontal line
      doc.setFontSize(24);
      doc.setFont("THSarabunNewBold", "bold");
      doc.text("รายงานยานพาหนะ", 200, 45);
      doc.setFont("THSarabunNew", "Bold");
      doc.setLineWidth(1.5);
      doc.line(50, 150, 50, 60); // vertical line
      doc.setLineWidth(0.5);
      doc.line(550, 60, 50, 60); // horizontal line
      doc.setLineWidth(1.5);
      doc.line(550, 150, 550, 60); // vertical line
      doc.setLineWidth(1.5);
      doc.line(380, 150, 380, 60); // vertical line
      doc.setLineWidth(0.5);
      doc.line(550, 150, 50, 150); // horizontal line
      doc.setFontSize(18);
      doc.text("user ที่ใช้งาน  " + this.dataCard.user, 70, 90);
      doc.text("วันที่  " + this.dataCard.report_date, 70, 110);
      doc.text("หน่วยงาน " + this.dataCard.department, 70, 130);

      let carSM = require("@/assets/img/carBL.png");
      let carXL = require("@/assets/img/carBL2.png");
      var car1 = new Image();
      var car2 = new Image();
      car1.src = carSM;
      car2.src = carXL;

      // console.log("logo", this.imgURL);
      doc.addImage(this.dataCard.overview_base64, "JPEG", 100, 180, 400, 200);
      doc.addImage(this.dataCard.plate_base64, "JPEG", 400, 80, 100, 50);

      doc.text("ทะเบียนยานพาหนะ " + this.dataCard.plate_no, 200, 500);
      doc.text("จังหวัด " + this.dataCard.province, 200, 520);
      doc.text("ประเภทยานพาหนะ " + this.dataCard.type, 200, 540);
      doc.text("สียานพาหนะ " + this.dataCard.color, 200, 560);
      doc.text("สถานที่ " + this.dataCard.checkpoint, 200, 580);
      doc.text("วันที่ " + this.dataCard.date, 200, 600);
      doc.text("เวลา " + this.dataCard.time, 200, 620);

      doc.save(`รายงานยานพาหนะ.pdf`);
    },
    headerbar(drawer) {
      this.drawer = drawer;
    },
    gobackpage() {
      let params = this.dataSearch;
      this.$router.push({ path: "/search-vehicle-detail", query: params });
    },
    setDateReport(param) {
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
      let date = param.split("-");
      let month =
        date[1] === "01"
          ? monthNames[0]
          : date[1] === "02"
          ? monthNames[1]
          : date[1] === "03"
          ? monthNames[2]
          : date[1] === "04"
          ? monthNames[3]
          : date[1] === "05"
          ? monthNames[4]
          : date[1] === "06"
          ? monthNames[5]
          : date[1] === "07"
          ? monthNames[6]
          : date[1] === "08"
          ? monthNames[7]
          : date[1] === "09"
          ? monthNames[8]
          : date[1] === "10"
          ? monthNames[9]
          : date[1] === "11"
          ? monthNames[10]
          : date[1] === "12"
          ? monthNames[11]
          : "";
      return `${date[2]} ${month} ${date[0]}`;
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
      let date = param.split("T")[0].split("-");
      let time = param.split("T")[1];
      let month =
        date[1] === "01"
          ? monthNames[0]
          : date[1] === "02"
          ? monthNames[1]
          : date[1] === "03"
          ? monthNames[2]
          : date[1] === "04"
          ? monthNames[3]
          : date[1] === "05"
          ? monthNames[4]
          : date[1] === "06"
          ? monthNames[5]
          : date[1] === "07"
          ? monthNames[6]
          : date[1] === "08"
          ? monthNames[7]
          : date[1] === "09"
          ? monthNames[8]
          : date[1] === "10"
          ? monthNames[9]
          : date[1] === "11"
          ? monthNames[10]
          : date[1] === "12"
          ? monthNames[11]
          : "";
      return `${date[2]} ${month} ${date[0]}`;
    },
    setTimeReport(param) {
      let time = param.split("T")[1].split(":");
      return `${time[0]}:${time[1]}`;
    },
    getData() {
      let dataCard = this.$route.query;

      
      this.getVehicleDetail(dataCard)
    },
    getVehicleDetail(data){
  
      this.onProgress = true;


      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/vehicle-report-detail";

      this.axios
        .post(url, data, {
          headers: { session: session_data }
        })
        .then((response) => {
          
          let isPublic = 0
          if(baseUrl.pathImg === "110.171.165.57"){
            isPublic = 1
          }
          const records = response.data.data.records

          records["report_time"] = this.setTimeReport(
            records.report_date
          );
          records["report_date"] = this.setDateReportNew(
            records.report_date
          );
          records["date"] = this.setDateReport(records.date);
          records["time"] = records.time;
          records["image_url"] = records.image_url;
          records["plate_picture"] = records.picture;
          records["overview_base64"] = records.img_overview_base64;
          records["plate_base64"] = records.img_base64;
          records['checkpoint'] = records.location;
          records['plate_no'] = records.license;
          // const records = response.data.data.records
          this.dataCard = records
        })
        .catch((error) => {
          console.log(error);
          Toast.fire({
            icon: "error",
            title: "การเชื่อมต่อมีปัญหา กรุณาโหลดใหม่อีกครั้ง",
          });
        })
        .finally(() => {
          this.onProgress = false;
        });
    },
    getImageReport(data) {
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/vehicle/" + data.id + "/report";
      console.log("getImageReport", url);
      this.axios
        .get(url, {
          headers: { session: session_data },
        })
        .then((response) => {
          console.log(response);
          if (response.data.status_code === 200) {
            let dataCard = response.data.data;
            let isPublic = 0
            if(baseUrl.pathImg === "110.171.165.57"){
              isPublic = 1
            }

            if(response.data.data.image_url !== "None" && response.data.data.image_url !== null){
              response.data.data.image_url = response.data.data.image_url.replace('10.151.1.86', baseUrl.pathImg)
              if(isPublic === 1){
                response.data.data.image_url = response.data.data.image_url.replace('6120', baseUrl.pathImgPort)
                response.data.data.image_url = response.data.data.image_url.replace('6040', baseUrl.pathImgPort)
              }
            }

            if(response.data.data.plate_picture !== "None" && response.data.data.plate_picture !== null){
              response.data.data.plate_picture = response.data.data.plate_picture.replace('10.151.1.86', baseUrl.pathImg)
              if(isPublic === 1){
                response.data.data.plate_picture = response.data.data.plate_picture.replace('6120', baseUrl.pathImgPort)
                response.data.data.plate_picture = response.data.data.plate_picture.replace('6040', baseUrl.pathImgPort)
              }
            }

            dataCard["report_time"] = this.setTimeReport(
              response.data.data.report_date
            );
            dataCard["report_date"] = this.setDateReportNew(
              response.data.data.report_date
            );
            dataCard["date"] = this.setDateReportNew(response.data.data.time);
            dataCard["time"] = this.setTimeReport(response.data.data.time);
            dataCard["lat"] = data.lat;
            dataCard["lon"] = data.lon;

            dataCard["image_url"] = response.data.data.image_url;
            dataCard["plate_picture"] = response.data.data.plate_picture;
            this.dataCard = dataCard;
          } else {
            Toast.fire({
              icon: "error",
              title: "ไม่สามารถดึงข้อมูลประเภทรถได้",
            });
          }
        })
        .catch((error) => {
          console.log(error);
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
            title: "ไม่สามารถดึงข้อมูลประเภทรถได้",
          });
        });
    },
  },
  mounted() {
    this.getData();
  },
};
</script>
<style>
@import "../assets/css/background.css";

#borderflex {
  border-radius: 0px 15px 15px 0px;
}
#borderflex-mobile {
  border-radius: 0px 0px 15px 15px;
}
.headerback {
  font-weight: 600;
  font-size: 24px;
  color: red;
}
.title-style {
  color: #404040;
  font-weight: bold;
}
.text-style {
  color: #2463c1;
  font-weight: bold;
}
</style>
