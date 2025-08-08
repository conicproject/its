<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-main class="pl-3">
      <v-overlay :value="onProgress">
        <v-progress-circular indeterminate size="64"></v-progress-circular>
      </v-overlay>
      <v-container class="pl-1 pr-1">
        <v-chip :disabled="disableBack" @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
          <v-icon large color="red">mdi-chevron-left</v-icon>
          <span class="text-left headerback">Back</span>
        </v-chip>
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">ค้นหายานพาหนะ</span>
        </v-chip>
        <searchdetail :header="headers" :dataTable="dataTable" :export="exportF" :dataFilter="dataFilter"
          :dataPath="dataPath" :loading="onLoading"></searchdetail>

        <div class="text-center">
          <v-pagination v-model="pagination.page" :length="pagination.total" :total-visible="pagination.visible"
            @input="next"></v-pagination>
        </div>
        <exportfile class="pt-4 pr-2" @downloadEx="genEX" :keypage="keypage" @download="generateReport"
          :title="titletext"></exportfile>
      </v-container>

      <!-- <download-excel
  class="btn btn-default"
  :data="json_data"
  :fields="json_fields"
  type="xlsx"
  name="filename.xls"
>
  Download CSV (you can customize this with html code!)
</download-excel> -->
    </v-main>
    <searchreportpdf :downloadpdf="downloadpdf" :downloadexcel="downloadexcel" :headers="headers" :dataTableRe="dataTable"
      :loading="onLoading"></searchreportpdf>
  </v-app>
</template>
<script>
const baseUrl = require("../../baseUrl.json");
const vehicleType = require("../data/vehicleType.json");
import sidebar from "../components/sidebar-new.vue";
import searchdetail from "../components/search-detail-table.vue";
import exportfile from "../components/export-file.vue";
import headerbar from "../components/header-bar.vue";
import searchreportpdf from "../formatExport/reportPDF.vue";
import "jspdf-autotable";

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
      dataTableReport: [
        {
          picture: "",
          province: "data",
          license: "data",
          type: "data",
          color: "data",
          date: "data",
          time: "data",
          location: "data",
          direction: "data",
          note: "link",
        },
      ],
      dataPath: {},
      downloadexcel: false,

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
        {
          text: "สียานพาหนะ",
          align: "center",
          sortable: false,
          value: "color",
        },
        {
          text: "วัน/เดือน/ปี",
          align: "center",
          sortable: false,
          value: "date",
        },
        { text: "เวลา", align: "center", sortable: false, value: "time" },
        {
          text: "สถานที่",
          align: "center",
          sortable: false,
          value: "location",
        },
        {
          text: "ทิศทางการจราจร",
          align: "center",
          sortable: false,
          value: "direction",
        },
        { text: "รายละเอียด", align: "center", sortable: false, value: "note" },
      ],
      dataTable: [
        // {
        //   picture:'',
        //   province:'data',
        //   license:'data',
        //   type:'data',
        //   color:'data',
        //   date:'data',
        //   time:'data',
        //   location:'data',
        //   direction:'data',
        //   note:'link',
        // }
      ],
      dataFilter: {},
      pagination: {
        page: 1,
        total: 15,
        perPage: 20,
        visible: 7,
      },
      disableBack: false,
      onLoading: false,
    };
  },
  computed: {
    headerTable() {
      return "color:#2962FF ;" + "font-weight: 600; font-size:15px;";
    },
  },
  methods: {
    genEX() {
      this.downloadexcel = !this.downloadexcel;
    },
    generateReport() {
      this.downloadpdf = !this.downloadpdf;
    },
    gobackpage() {
      this.$router.push("/vehicle/search");
    },
    getData() {
      const data = this.$route.query;
      data["total"] = this.dataFilter["total"] ? this.dataFilter["total"] : 0;
      this.dataPath = data;
      this.$store.dispatch("setDataSearch", this.dataPath);
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/v2/vehicle-search";
      this.onLoading = true;
      this.axios
        .get(url, {
          headers: { session: session_data },
          params: data,
        })
        .then((response) => {
          if (response.status === 200) {
            const dataQuery = this.$route.query;

            this.onLoading = false;
            this.dataTable = [];
            let provinceTh = "-"
            let vehicleTypeTH = "-";

            let blankImg =
              "data:image/png;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==";
            for (let i = 0; i < response.data.data.records.length; i++) {
              let dataRes = response.data.data.records[i];
              let data = {};
              let isPublic = 0;
              let checkImgIsvalid = 0;
              if (baseUrl.pathImg === "110.171.165.57") {
                isPublic = 1;
              }

              // add province name in filter head
              if (dataQuery.province && i === 0) {
                provinceTh = dataRes["province"]
              }

              let checkimage =
                response.data.data.records[i]["image_url"].includes("http:");
              if (
                response.data.data.records[i]["image_url"] !== "None" &&
                dataRes["image_url"] !== null
              ) {
                response.data.data.records[i]["image_url"] =
                  response.data.data.records[i]["image_url"].replace(
                    "10.151.1.86",
                    baseUrl.pathImg
                  );
                if (isPublic === 1) {
                  response.data.data.records[i]["image_url"] =
                    response.data.data.records[i]["image_url"].replace(
                      "6120",
                      baseUrl.pathImgPort
                    );
                  response.data.data.records[i]["image_url"] =
                    response.data.data.records[i]["image_url"].replace(
                      "6040",
                      baseUrl.pathImgPort
                    );
                }
              }

              if (
                response.data.data.records[i]["plate_picture"] !== "None" &&
                dataRes["plate_picture"] !== null
              ) {
                response.data.data.records[i]["plate_picture"] =
                  response.data.data.records[i]["plate_picture"].replace(
                    "10.151.1.86",
                    baseUrl.pathImg
                  );
                if (isPublic === 1) {
                  response.data.data.records[i]["plate_picture"] =
                    response.data.data.records[i]["plate_picture"].replace(
                      "6120",
                      baseUrl.pathImgPort
                    );
                  response.data.data.records[i]["plate_picture"] =
                    response.data.data.records[i]["plate_picture"].replace(
                      "6040",
                      baseUrl.pathImgPort
                    );
                }
              }

              data["index"] = i + 1;
              data["id"] = response.data.data.records[i]["id"];
              data["picture"] = response.data.data.records[i]["plate_picture"];
              data["province"] = response.data.data.records[i]["province"];

              if (isPublic === 0) {
                data["img_base64"] = dataRes["base64_plate_pic"]
                  ? "data:image/png;base64," + dataRes["base64_plate_pic"]
                  : "";
              } else {
                data["img_base64"] = dataRes["base64_plate_pic"]
                  ? "data:image/png;base64," + dataRes["base64_plate_pic"]
                  : "";
              }
              if (checkimage !== true) {
                data["img_base64"] = blankImg;
              }
              data["image_url"] = response.data.data.records[i]["image_url"];
              data["license"] = response.data.data.records[i]["plate_no"];
              data["type"] = response.data.data.records[i]["type"];
              data["color"] = response.data.data.records[i]["color"];
              data["lat"] = response.data.data.records[i]["latitude"];
              data["lon"] = response.data.data.records[i]["longtitude"];
              data["date"] = response.data.data.records[i]["time"].substr(
                0,
                10
              );
              data["time"] = response.data.data.records[i]["time"].substr(
                11,
                5
              );
              data["location"] = response.data.data.records[i]["checkpoint"];
              data["direction"] =
                response.data.data.records[i]["direction"] === "inbound"
                  ? "ขาเข้า"
                  : response.data.data.records[i]["direction"] === "outbound"
                    ? "ขาออก"
                    : "";
              data["note"] = "Link";
              this.dataTable.push(data);
            }


            // change vehicle type en to th name
            if (dataQuery.vehicle_type) {
              vehicleTypeTH = vehicleType
                .filter((obj) => obj.en === dataQuery.vehicle_type)
                .map((obj) => obj.th)[0];
            }

            this.dataFilter = {
              total: response.data.total,
              date: this.setFormatDate(dataQuery.startdate, dataQuery.enddate),
              point: dataQuery.checkpoint || "-",
              direction:
                dataQuery.direction === "inbound"
                  ? "ขาเข้า"
                  : dataQuery.direction === "outbound"
                    ? "ขาออก"
                    : "-",
              province: provinceTh,
              carType: vehicleTypeTH,
              color: dataQuery.vehicle_color || "-",
              plate_no: dataQuery.plate_no || "-",
              pointName: dataQuery.pointName || "-",
            };
            // console.log("data",this.dataTable);
            //pagination
            this.pagination.total = response.data.page_total;
          } else {
            this.onLoading = false;
            // this.$router.push("/error");
            Toast.fire({
              icon: "error",
              title: "Cannot connet API",
            });
          }
        })
        .catch((error) => {
          this.onLoading = false;
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
            title: "Cannot connet API",
          });
        });
    },
    next(page) {
      this.$route.query.page = page;

      this.getList(true, page)
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
      let month_start =
        start_date[1] === "01"
          ? monthNames[0]
          : start_date[1] === "02"
            ? monthNames[1]
            : start_date[1] === "03"
              ? monthNames[2]
              : start_date[1] === "04"
                ? monthNames[3]
                : start_date[1] === "05"
                  ? monthNames[4]
                  : start_date[1] === "06"
                    ? monthNames[5]
                    : start_date[1] === "07"
                      ? monthNames[6]
                      : start_date[1] === "08"
                        ? monthNames[7]
                        : start_date[1] === "09"
                          ? monthNames[8]
                          : start_date[1] === "10"
                            ? monthNames[9]
                            : start_date[1] === "11"
                              ? monthNames[10]
                              : start_date[1] === "12"
                                ? monthNames[11]
                                : "";
      let year_start = parseInt(start_date[0]) + 543;

      if (end) {
        let end_date = end.split("-") || "";
        //console.log(end_date);
        let month_end =
          end_date[1] === "01"
            ? monthNames[0]
            : end_date[1] === "02"
              ? monthNames[1]
              : end_date[1] === "03"
                ? monthNames[2]
                : end_date[1] === "04"
                  ? monthNames[3]
                  : end_date[1] === "05"
                    ? monthNames[4]
                    : end_date[1] === "06"
                      ? monthNames[5]
                      : end_date[1] === "07"
                        ? monthNames[6]
                        : end_date[1] === "08"
                          ? monthNames[7]
                          : end_date[1] === "09"
                            ? monthNames[8]
                            : end_date[1] === "10"
                              ? monthNames[9]
                              : end_date[1] === "11"
                                ? monthNames[10]
                                : end_date[1] === "12"
                                  ? monthNames[11]
                                  : "";
        let year_end = parseInt(start_date[0]) + 543;
        return `${start_date[2]} ${month_start} ${year_start.toString()} - ${end_date[2]
          } ${month_end} ${year_end.toString()}`;
      }

      return `${start_date[2]} ${month_start} ${year_start.toString()}`;
      // let dateformat = new Date(param).toLocaleDateString('th-TH', {year: 'numeric', month: 'long', day:'numeric'})
    },
    setDataFilter() {
      const filter = localStorage.getItem('vehicleFilter')
      const param = localStorage.getItem('vehicleParam')

      const filter_parse = JSON.parse(filter)
      const param_parse = JSON.parse(param)
      const { startdate, enddate, plate_no, direction } = param_parse
      // console.log(JSON.parse(filter));
      // console.log(JSON.parse(param));
      this.dataFilter = {
        'total': filter_parse.total,
        'date': this.setFormatDate(startdate, enddate),
        'pointName': filter_parse["checkpoint"]["short_name"],
        'direction': direction || "-",
        'province': filter_parse["province"]["name"],
        'carType': filter_parse["type"]["name"],
        'color': filter_parse["color"]["name"],
        'plate_no': plate_no || "-",
      }
    },
    getList(isPagination, next = 1) {
      const param = localStorage.getItem('vehicleParam')
      const filter = localStorage.getItem('vehicleFilter')
      const filter_parse = JSON.parse(filter)
      let params = JSON.parse(param)
      params["total"] = filter_parse.total
      if (isPagination) {
        params["page"] = next
      }

      this.dataPath = params

      this.$store.dispatch("setDataSearch", this.dataPath);
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/v3/vehicle-search";
      this.onLoading = true;
      // console.log("params", params)
      // return
      this.dataTable = [];
      this.axios
        .get(url, {
          headers: { session: session_data },
          params: params,
        })
        .then((response) => {
          if (response.status === 200) {
            const records = response.data.data.records
            for (let i = 0; i < records.length; i++) {
              const record = records[i]
              let data = {};
              let isPublic = 0;
              let splitDate = record["time"].split("T")[1].split(":");

              if (baseUrl.pathImg === "110.171.165.57") {
                isPublic = 1;
              }

              data["index"] = i + 1;
              data["id"] = record["id"];
              data["picture"] = isPublic == 1 ? record["NET_PLATE_PIC_URL"] : record["BMA_PLATE_PIC_URL"]
              data["province"] = record["province"];
              data["image_url"] = isPublic == 1 ? record["NET_IMAGE_PATH"] : record["BMA_IMAGE_PATH"]
              data["license"] = record["plate_no"];
              data["type"] = record["type"];
              data["color"] = record["color"];
              data["lat"] = record["latitude"];
              data["lon"] = record["longtitude"];
              data["date"] = record["time"].substr(
                0,
                10
              );
              data["time"] = record["time"].substr(
                11,
                5
              );
              data["location"] = record["checkpoint"];
              data["direction"] =
                record["direction"] === "inbound"
                  ? "ขาเข้า"
                  : record["direction"] === "outbound"
                    ? "ขาออก"
                    : "";
              data["note"] = "Link";

              this.dataTable.push(data);
            }

            //pagination
            this.pagination.total = response.data.page_total
            this.pagination.page = params["page"]
            this.onLoading = false
            localStorage.setItem('vehicleParam', JSON.stringify(params))
          }
        })
        .catch((error) => {
          this.onLoading = false;
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
            title: "Cannot connet API",
          });
        });
    }
  },
  mounted() {
    this.setDataFilter()
    this.getList()
    // this.getData();
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

.head-table {
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
}
</style>
