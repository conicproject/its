<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="onProgress">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
    <v-content class="pl-3">
      <v-container class="pl-1 pr-1">
        <v-chip :disabled="disableBack" @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
          <v-icon large color="red">mdi-chevron-left</v-icon>
          <span class="text-left headerback">Back</span>
        </v-chip>
        <v-chip large class="ma-2" color="#02754B" v-if="$vuetify.breakpoint.width > 1024">
          <span class="pl-5 pr-5 headertext">ค้นหารถบรรทุกในช่วงเวลาที่ห้ามเดินรถ</span>
        </v-chip>
        <v-chip large class="ma-2" color="#02754B" v-else>
          <span class="pl-5 pr-5 headertext-mobile">ค้นหารถบรรทุกในช่วงเวลาที่ห้ามเดินรถ</span>
        </v-chip>
        <v-container v-if="$vuetify.breakpoint.width > 1904">
          <v-layout justify-center class="pb-3">
            <v-flex lg6>
              <v-card height="100%" class="elevation-0 pa-3 text-center" id="bg-card"><span class="text-style">{{
                this.dateHead }}</span></v-card>
            </v-flex>
            <v-flex lg6 class="pl-3">
              <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
                <v-row><v-col cols="4">
                    <span class="title-style">จุดติดตั้ง:</span> </v-col><v-col>
                    <span class="text-style">{{ this.checkpoint }}</span>
                  </v-col>
                </v-row>
              </v-card>
            </v-flex>
          </v-layout>
          <v-layout justify-center class="pb-3">
            <v-flex lg6>
              <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
                <v-row>
                  <v-col cols="5">
                    <span class="title-style">ทิศทางการจราจร:</span> </v-col><v-col>
                    <span class="text-style">{{ this.direction }}</span>
                  </v-col>
                </v-row>
              </v-card>
            </v-flex>
            <v-flex lg6 class="pl-3">
              <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
                <v-row>
                  <v-col cols="4">
                    <span class="title-style">ช่วงเวลา:</span> </v-col><v-col>
                    <span class="text-style">{{ this.rangetime }}</span>
                  </v-col>
                </v-row>
              </v-card>
            </v-flex>
          </v-layout>
          <v-layout child-flex class="pt-3">
            <v-data-table :headers="headers" :items="dataTable" id="table-vehicle" :hide-default-footer="true"
              loading-text="Loading" :loading="loading" :items-per-page="20">
              <!-- <template v-slot:[`header.id`]="{ header }">
          <span>{{ header.text }}</span>
        </template> -->
              <template v-slot:[`header.picLicense`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.license`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.province`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.type`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.color`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.date`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.time`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.location`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.direction`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.note`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                  <!-- <td class="text-center"><span style="font-size:20px;">{{ props.item.id}}</span></td> -->
                  <td class="text-center"><img width="50" :src="props.item.picture"></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.license }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.province }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.type }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.color }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.date }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.time }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.location }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.direction }}</span></td>
                  <td class="text-center">
                    <v-btn text small @click="link(props.item)">
                      <v-icon>mdi-information-outline</v-icon>
                    </v-btn>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>
        </v-container>
        <v-container v-else-if="$vuetify.breakpoint.width < 1904 && $vuetify.breakpoint.width > 750">
          <v-layout justify-center class="pb-3">
            <v-flex lg6>
              <v-card class="elevation-0 pa-3 text-center" id="bg-card"><span class="text-style">{{ this.dateHead
              }}</span></v-card>
            </v-flex>
            <v-flex lg6 class="pl-3">
              <v-card class="elevation-0 pa-3" id="bg-card">
                <v-row><v-col cols="4">
                    <span class="title-style">จุดติดตั้ง:</span> </v-col><v-col>
                    <span class="text-style">{{ this.checkpoint }}</span>
                  </v-col>
                </v-row>
              </v-card>
            </v-flex>
          </v-layout>
          <v-layout justify-center class="pb-3">
            <v-flex lg6>
              <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
                <v-row>
                  <v-col cols="5">
                    <span class="title-style">ทิศทางการจราจร:</span> </v-col><v-col>
                    <span class="text-style">{{ this.direction }}</span>
                  </v-col>
                </v-row>
              </v-card>
            </v-flex>


            <v-flex lg6 class="pl-3">
              <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
                <v-row>
                  <v-col cols="4">
                    <span class="title-style">ช่วงเวลา:</span> </v-col><v-col>
                    <span class="text-style">{{ this.rangetime }}</span>
                  </v-col>
                </v-row>
              </v-card>
            </v-flex>
          </v-layout>

          <v-layout child-flex class="pt-3">
            <v-data-table :headers="headers" :items="dataTable" id="table-vehicle" :hide-default-footer="true"
              loading-text="Loading" :loading="loading" :items-per-page="20">
              <!-- <template v-slot:[`header.id`]="{ header }">
          <span>{{ header.text }}</span>
        </template> -->
              <template v-slot:[`header.picLicense`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.license`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.province`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.type`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.color`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.date`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.time`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.location`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.direction`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.note`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                  <!-- <td class="text-center">{{ props.item.id}}</td> -->
                  <td class="text-center"><img width="50" :src="props.item.picture"></td>
                  <td class="text-center">{{ props.item.license }}</td>
                  <td class="text-center">{{ props.item.province }}</td>
                  <td class="text-center">{{ props.item.type }}</td>
                  <td class="text-center">{{ props.item.color }}</td>
                  <td class="text-center">{{ props.item.date }}</td>
                  <td class="text-center">{{ props.item.time }}</td>
                  <td class="text-center">{{ props.item.location }}</td>
                  <td class="text-center">{{ props.item.direction }}</td>
                  <td class="text-center">
                    <v-btn text small @click="link(props.item)">
                      <v-icon>mdi-information-outline</v-icon>
                    </v-btn>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>
        </v-container>

        <v-container v-else>
          <v-layout justify-center class="pb-3">
            <v-flex>
              <v-card class="elevation-0 pa-3 text-center" id="bg-card"><span class="text-style">{{ this.dateHead
              }}</span></v-card>
            </v-flex>
          </v-layout>
          <v-layout justify-center class="pb-3">
            <v-flex>
              <v-card class="elevation-0 pa-3" id="bg-card">
                <v-row><v-col cols="4">
                    <span class="title-style">จุดติดตั้ง:</span> </v-col><v-col>
                    <span class="text-style">{{ this.checkpoint }}</span>
                  </v-col>
                </v-row>
              </v-card>
            </v-flex>
          </v-layout>
          <v-layout justify-center class="pb-3">
            <v-flex>
              <v-card class="elevation-0 pa-3" id="bg-card">
                <v-row>
                  <v-col cols="5">
                    <span class="title-style">ทิศทางการจราจร:</span> </v-col><v-col>
                    <span class="text-style">{{ this.direction }}</span>
                  </v-col>
                </v-row>
              </v-card>
            </v-flex>
          </v-layout>
          <v-layout justify-center class="pb-3">
            <v-flex>
              <v-card class="elevation-0 pa-3" id="bg-card">
                <v-row>
                  <v-col cols="4">
                    <span class="title-style">ช่วงเวลา:</span> </v-col><v-col>
                    <span class="text-style">{{ this.rangetime }}</span>
                  </v-col>
                </v-row>
              </v-card>
            </v-flex>
          </v-layout>

          <v-layout child-flex class="pt-3">
            <v-data-table :headers="headers" :items="dataTable" id="table-vehicle" :hide-default-footer="true"
              loading-text="Loading" :loading="loading" :items-per-page="20">
              <!-- <template v-slot:[`header.id`]="{ header }">
          <span>{{ header.text }}</span>
        </template> -->
              <template v-slot:[`header.picLicense`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.license`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.province`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.type`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.color`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.date`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.time`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.location`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.direction`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.note`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                  <!-- <td class="text-center">{{ props.item.id }}</td> -->
                  <td class="text-center"><img width="50" :src="props.item.picture"></td>
                  <td class="text-center">{{ props.item.license }}</td>
                  <td class="text-center">{{ props.item.province }}</td>
                  <td class="text-center">{{ props.item.type }}</td>
                  <td class="text-center">{{ props.item.color }}</td>
                  <td class="text-center">{{ props.item.date }}</td>
                  <td class="text-center">{{ props.item.time }}</td>
                  <td class="text-center">{{ props.item.location }}</td>
                  <td class="text-center">{{ props.item.direction }}</td>
                  <td class="text-right">
                    <v-btn text small @click="link(props.item)">
                      <v-icon>mdi-information-outline</v-icon>
                    </v-btn>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>
        </v-container>
        <v-pagination class="pt-3" v-model="pagination.page" :length="pagination.total"
          :total-visible="pagination.visible"
          @input="next"></v-pagination>
        <v-layout>
          <!-- <exportfile class="pt-6 pr-3" @downloadEx="genEX" :keypage="keypage" @download="generateReport" :title="titletext"></exportfile> -->
        </v-layout>
      </v-container>

    </v-content>

    <!-- <searchtruckpdf :downloadpdf="downloadpdf" :downloadexcel="downloadexcel" :dataTableRe="dataTable"></searchtruckpdf> -->
  </v-app>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
// import searchdetail from "../components/search-detail-table.vue";
import exportfile from "../components/export-file.vue";
import headerbar from "../components/header-bar.vue";
import searchtruckpdf from "../formatExport/reportTruckPDF.vue";
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
    searchtruckpdf,
    exportfile,
    headerbar,
  },
  data() {
    return {
      pagination: {
        page: 1,
        total: 15,
        perPage: 20,
        visible: 7
      },

      titletext: "รถบรรทุกในช่วงเวลาที่ห้ามเดินรถ",
      dateHead: "",
      onProgress: false,
      downloadpdf: false,
      downloadexcel: false,
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
        // {
        //   text: "ลำดับ",
        //   align: "center",
        //   sortable: false,
        //   value: "id",

        // },
        {
          text: "ป้ายทะเบียนยานพาหนะ",
          align: "center",
          sortable: false,
          value: "picLicense",
        },
        {
          text: "เลขทะเบียนยานพาหนะ",
          align: "center",
          sortable: false,
          value: "license",
        },
        {
          text: "จังหวัด",
          align: "center",
          sortable: false,
          value: "province",
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
      disableBack: false,
      loading: false,
      rangetime: '',
      checkpoint: '',
      direction: ''
    };
  },
  computed: {
    headerTable() {
      return "color:#2962FF ;" + "font-weight: 600; font-size:15px;";
    },
  },
  methods: {
    next(page) {
      this.getDataTruck(page)
    },
    genEX() {

      this.downloadexcel = !this.downloadexcel;
    },
    generateReport() {
      this.downloadpdf = !this.downloadpdf
    },
    gobackpage() {
      this.$router.push("/vehicle/list-truck");
    },

    headerbar(drawer) {

      this.drawer = drawer;
    },
    link(item) {
      const data = this.$route.query;
      data['id'] = item.id
      this.$router.push({ path: "/truck-detail", query: data });
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
        let month_end = end_date[1] === '01' ? monthNames[0] : end_date[1] === '02' ? monthNames[1] : end_date[1] === '03' ? monthNames[2] : end_date[1] === '04' ? monthNames[3] : end_date[1] === '05' ? monthNames[4] : end_date[1] === '06' ? monthNames[5] : end_date[1] === '07' ? monthNames[6] : end_date[1] === '08' ? monthNames[7] : end_date[1] === '09' ? monthNames[8] : end_date[1] === '10' ? monthNames[9] : end_date[1] === '11' ? monthNames[10] : end_date[1] === '12' ? monthNames[11] : "";
        let year_end = parseInt(start_date[0]) + 543;
        return `${start_date[2]} ${month_start} ${year_start.toString()} - ${end_date[2]} ${month_end} ${year_end.toString()}`;
      }


      return `${start_date[2]}  ${month_start} ${year_start.toString()}`;

    },
    getDataTruck(page = 1) {
      this.loading = true
      let data = this.$route.query;
      data["page"] = page
      
      this.dataTable = []
      // data.push(obj)
      this.dateHead = this.setFormatDate(data.startdate, data.enddate)
      this.direction = data.direction === "inbound" ? "ขาเข้า" : data.direction === "outbound" ? "ขาออก" : "-"
      this.checkpoint = data.checkpoint || "-"
      this.rangetime = data.timerange === "[6,10]" ? "06:00 น. - 10:00 น." : data.timerange === "[15,21]" ? "15:00 น. - 21:00 น." : "-"

      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/truck-search";
      this.axios
        .get(url, {
          headers: { session: session_data },
          params: data,
        })
        .then((response) => {
          if (response.status === 200) {
            this.disableBack = false
            this.dataTable = [];
            let isPublic = baseUrl.pathImg === "110.171.165.57" ? 1 : 0

            for (let i = 0; i < response.data.data.records.length; i++) {
              let resData = response.data.data.records[i]
              // if (resData['plate_picture'] !== "None" && resData['plate_picture'] !== null) {
              //   resData['plate_picture'] = resData['plate_picture'].replace('10.151.1.86', baseUrl.pathImg)
              //   if (isPublic === 1) {
              //     resData['plate_picture'] = resData['plate_picture'].replace('6120', baseUrl.pathImgPort)
              //     resData['plate_picture'] = resData['plate_picture'].replace('6040', baseUrl.pathImgPort)
              //   }
              // }

              let data = {}
              data["index"] = i + 1
              data['id'] = resData['id']
              data['pass_id'] = resData['pass_id']
              data["picture"] = isPublic == 1 ? resData["net_plate"] : resData["bma_plate"]
              data["province"] = resData["province"]
              data["image_url"] = isPublic == 1 ? resData["net_image"] : resData["bma_image"]
              data["license"] = resData["plate_no"]
              data["type"] = resData["type"]
              data["color"] = resData["color"]
              data["lat"] = resData["latitude"]
              data["lon"] = resData["longtitude"]
              data["date"] = this.setFormatDate(resData["time"].substr(0, 10))
              data["time"] = resData["time"].substr(11, 5);
              data["location"] = resData["checkpoint"]
              data["direction"] = resData["direction"] === "inbound" ? "ขาเข้า" : resData["direction"] === "outbound" ? "ขาออก" : ""
              data["rtsp_url"] = resData["rtsp_url"]
              data["note"] = "Link"
              this.dataTable.push(data)
            }


            //pagination

            this.pagination.total = response.data.page_total
            this.loading = false
          } else {
            this.loading = false
            this.disableBack = false
            Toast.fire({
              icon: 'error',
              title: 'Cannot connet API',
            })
          }
        })
        .catch((error) => {
          this.loading = false
          this.disableBack = false
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
            title: 'Cannot connet API',
          })
        });
    },



  },
  mounted() {
    this.getDataTruck()
  },
};
</script>
<style>
@import "../assets/css/background.css";

.head-table {
  color: #2962ff;
  font-weight: 600;
  font-size: 15px;
}

.headerback {
  font-weight: 600;
  font-size: 24px;
  color: red;
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
}

/* .headertext-mobile{
    font-weight: 600;
    font-size: 20px;
    color: #FFFFFF;
} */
#table-vehicle table thead tr th:nth-child(1),
#table-vehicle table thead tr th:nth-child(2),
#table-vehicle table thead tr th:nth-child(3),
#table-vehicle table thead tr th:nth-child(4),
#table-vehicle table thead tr th:nth-child(5),
#table-vehicle table thead tr th:nth-child(6),
#table-vehicle table thead tr th:nth-child(7),
#table-vehicle table thead tr th:nth-child(8),
#table-vehicle table thead tr th:nth-child(9),
#table-vehicle table thead tr th:nth-child(10),
#table-vehicle table thead tr th:nth-child(11) {
  background-color: #02754B;
  color: white;
  font-size: 18px;
}

#table-vehicle table tbody tr:nth-child(odd) {
  background-color: #ddf1fc;
}
</style>
