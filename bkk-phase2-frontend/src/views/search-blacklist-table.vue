<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-content class="pl-3">
      <v-overlay :value="onProgress">

        <v-progress-circular indeterminate size="64"></v-progress-circular>
      </v-overlay>
      <v-container class="pl-1 pr-1">
        <v-chip :disabled="disableBack" @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
          <v-icon large color="red">mdi-chevron-left</v-icon>
          <span class="text-left headerback">Back</span>
        </v-chip>
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">ค้นหายานพาหนะที่กำหนด</span>
        </v-chip>
        <searchdetail :loading="onLoading" :header="headers" :dataTable="dataTable" :export="exportF"
          :dataFilter="dataFilter" :dataPath="dataPath" :queryPayload="queryPayload"></searchdetail>


        <div class="text-center">
          <v-pagination v-model="pagination.page" :length="pagination.total" :total-visible="pagination.visible"
            @input="next"></v-pagination>
        </div>
        <!-- <exportfile class="pt-4 pr-2" @downloadEx="genEX" :keypage="keypage" @download="generateReport"
          :json_data="json_data" :title="titletext"></exportfile> -->
      </v-container>
    </v-content>

    <!-- <searchreportpdf @onProgress="onloading" :downloadpdf="downloadpdf" :downloadexcel="downloadexcel"
      :headers="headers" :dataTableRe="dataTable"></searchreportpdf> -->

  </v-app>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
import searchdetail from "../components/search-detail-blacklist.vue";
import exportfile from "../components/export-file.vue";
import headerbar from "../components/header-bar.vue";
import searchreportpdf from "../formatExport/reportPDF.vue";
import { mapGetters } from "vuex";
import { jsPDF } from "jspdf";
//import * as jsPDF from 'jspdf'
//import * as autoTable from 'jspdf-autotable'
import "jspdf-autotable";
import fontTH from "../fontTH.js";
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
    searchdetail,
    exportfile,
    headerbar,
    searchreportpdf,
  },
  data() {
    return {
      disableBack: false,
      onLoading: false,
      dataPath: {},
      downloadexcel: false,
      checkPage: 'bl',
      queryPayload: {},
      titletext: "ข้อมูลยานพาหนะ",
      onProgress: false,
      downloadpdf: false,
      keypage: "allsensor",
      drawer: true,
      exportF: [
        {
          i: 1,
          name: "save as..",
        },
        {
          i: 2,
          name: "Export PDF",
        },
        {
          i: 3,
          name: "Export Excel",
        },
      ],
      headers: [
        {
          text: "ป้ายทะเบียนยานพาหนะ",
          align: "center",
          sortable: false,
          value: "picture",

        },
        {
          text: "จังหวัดของยานพาหนะ",
          align: "center",
          sortable: false,
          value: "province",

        },
        {
          text: "เลขทะเบียนยานพาหนะ",
          align: "center",
          sortable: false,
          value: "license",

        },
        {
          text: "ประเภทยานพาหนะ",
          align: "center",
          sortable: false,
          value: "type",

        },
        { text: "สียานพาหนะ", align: "center", sortable: false, value: "color" },
        { text: "วัน/เดือน/ปี", align: "center", sortable: false, value: "date" },
        { text: "เวลา", align: "center", sortable: false, value: "time" },
        { text: "สถานที่", align: "center", sortable: false, value: "location" },
        { text: "ทิศทางการจราจร", align: "center", sortable: false, value: "direction" },
        { text: "รายละเอียด", align: "center", sortable: false, value: "note" },
      ],
      dataTable: [],
      dataFilter: {
        date: '-',
      },
      pagination: {
        page: 1,
        total: 15,
        perPage: 20,
        visible: 7
      },
    };
  },
  computed: {

    headerTable() {
      return "color:#2962FF ;" + "font-weight: 600; font-size:15px;";
    },
  },
  methods: {

    next(page) {
      this.$route.query.page = page

      this.getData()
    },
    getData() {
   
      const data = this.$route.query;
      this.queryPayload = this.$route.query;
      this.dataPath = data
      this.$store.dispatch("setDataSearch", this.dataPath);
      this.onLoading = true
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/blacklist-search";
      this.axios
        .get(url, {
          headers: { session: session_data },
          params: data,
        })
        .then((response) => {

          if (response.status === 200) {
            this.onLoading = false
            this.dataTable = [];
            for (let i = 0; i < response.data.data.records.length; i++) {
              let data = {}
              let isPublic = 0
              let imgPlate = response.data.data.records[i]['plate_picture']

              if (baseUrl.pathImg === "110.171.165.57") {
                isPublic = 1
              }

              if (imgPlate !== "None" && imgPlate !== null) {
                imgPlate = imgPlate.replace('10.151.1.86', baseUrl.pathImg)
                if (isPublic === 1) {
                  imgPlate = imgPlate.replace('6120', baseUrl.pathImgPort)
                  imgPlate = imgPlate.replace('6040', baseUrl.pathImgPort)
                }
              }

              data["index"] = i + 1
              data["id"] = response.data.data.records[i]['id']
              data["blacklist_id"] = response.data.data.records[i]['blacklist_id']
              data["picture"] = imgPlate
              data["province"] = response.data.data.records[i]["province"]
              data["img_base64"] = require(`@/assets/img/carBL2.png`)
              data["image_url"] = response.data.data.records[i]["image_url"]
              data["license"] = response.data.data.records[i]["plate_no"]
              data["type"] = response.data.data.records[i]["type"]
              data["color"] = response.data.data.records[i]["color"]
              data["lat"] = response.data.data.records[i]["latitude"]
              data["lon"] = response.data.data.records[i]["longtitude"]
              data["date"] = response.data.data.records[i]["time"].substr(0, 10);
              data["time"] = response.data.data.records[i]["time"].substr(11, 5);
              data["location"] = response.data.data.records[i]["checkpoint"]
              data["direction"] = response.data.data.records[i]["direction"] === "inbound" ? "ขาเข้า" : response.data.data.records[i]["direction"] === "outbound" ? "ขาออก" : ""
              data["note"] = "Link"
              this.dataTable.push(data)
            }

            const dataQuery = this.$route.query
 
            this.dataFilter = {
              'total': response.data.total,
              'date': this.setFormatDate(dataQuery.startdate,dataQuery.enddate),
              'point': dataQuery.checkpoint || "-",
              'direction': dataQuery.direction === "inbound" ? "ขาเข้า" : dataQuery.direction === "outbound" ? "ขาออก" : "-",
              'province': dataQuery.province || "-",
              'carType': dataQuery.vehicle_type || "-",
              'color': dataQuery.vehicle_color || "-",
              'plate_no': dataQuery.plate_no || "-",
            }

            //pagination
            this.pagination.total = response.data.page_total
          } else {
            this.onLoading = false
            Toast.fire({
              icon: 'error',
              title: 'ไม่สามารถดูข้อมูลได้',
            })

          }
        })
        .catch((error) => {
          this.onLoading = false
          console.log(error);
          if (error.response.data.message === 'session timeout') {
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
            title: 'ไม่สามารถดูข้อมูลได้',
          })

        })
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
      let date = param.date.split("-");
      let month = date[1] === '01' ? monthNames[0] : date[1] === '02' ? monthNames[1] : date[1] === '03' ? monthNames[2] : date[1] === '04' ? monthNames[3] : date[1] === '05' ? monthNames[4] : date[1] === '06' ? monthNames[5] : date[1] === '07' ? monthNames[6] : date[1] === '08' ? monthNames[7] : date[1] === '09' ? monthNames[8] : date[1] === '10' ? monthNames[9] : date[1] === '11' ? monthNames[10] : date[1] === '12' ? monthNames[11] : "";
      return `${date[2]} ${month} ${date[0]}`;


    },
    gobackpage() {
      this.$router.push('/vehicle/search-blacklist');
    },
    headerbar(drawer) {
      this.drawer = drawer;
    },
    setFormatDate(start, end) {

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

      let start_date = start.split("-") || "";
      let month_start = start_date[1] === '01' ? monthNames[0] : start_date[1] === '02' ? monthNames[1] : start_date[1] === '03' ? monthNames[2] : start_date[1] === '04' ? monthNames[3] : start_date[1] === '05' ? monthNames[4] : start_date[1] === '06' ? monthNames[5] : start_date[1] === '07' ? monthNames[6] : start_date[1] === '08' ? monthNames[7] : start_date[1] === '09' ? monthNames[8] : start_date[1] === '10' ? monthNames[9] : start_date[1] === '11' ? monthNames[10] : start_date[1] === '12' ? monthNames[11] : "";
      let year_start = parseInt(start_date[0]) + 543;

      if (end) {
        let end_date = end.split("-") || "";
        //console.log(end_date);
        let month_end = end_date[1] === '01' ? monthNames[0] : end_date[1] === '02' ? monthNames[1] : end_date[1] === '03' ? monthNames[2] : end_date[1] === '04' ? monthNames[3] : end_date[1] === '05' ? monthNames[4] : end_date[1] === '06' ? monthNames[5] : end_date[1] === '07' ? monthNames[6] : end_date[1] === '08' ? monthNames[7] : end_date[1] === '09' ? monthNames[8] : end_date[1] === '10' ? monthNames[9] : end_date[1] === '11' ? monthNames[10] : end_date[1] === '12' ? monthNames[11] : "";
        let year_end = parseInt(start_date[0]) + 543;
        return `${start_date[2]} ${month_start} ${year_start.toString()} - ${end_date[2]} ${month_end} ${year_end.toString()}`;
      }


      return `${start_date[2]} ${month_start} ${year_start.toString()}`;
      // let dateformat = new Date(param).toLocaleDateString('th-TH', {year: 'numeric', month: 'long', day:'numeric'})



    },
  },
  mounted() {
    this.getData()
  },
};
</script>
<style>
@import "../assets/css/background.css";

.headerback {
  font-weight: 600;
  font-size: 24px;
  color: red;
}

head-table {
  color: #2962ff;
  font-weight: 600;
  font-size: 15px;
}

#bg-card {
  background: #f4f4f4;
  border-radius: 15px;
}

.text-style {
  color: #02754B;
  font-weight: 600;
  font-size: 20px;
}

.title-style {
  color: #404040;
  font-weight: 600;
  font-size: 16px;
}</style>
