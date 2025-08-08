<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="onProgress">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
    <v-content class="pl-3" v-if="$vuetify.breakpoint.width > 754">
      <v-container class="pl-1 pr-1">
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">รายงานผลข้อมูลจราจรของ กทม.</span>
        </v-chip>

        <v-container d-flex flex-column justify-center align-center>
          <v-row>
            <v-col class="d-flex justify-end"><span class="textSR py-3">รายวัน</span></v-col>
            <v-col @click="changeSelect('day')">
              <v-menu v-model="menu" :close-on-content-click="false" :nudge-right="40" transition="scale-transition"
                offset-y min-width="auto">
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field placeholder="วัน เดือน ปี" :disabled="disable.day" outlined hide-details class="sl"
                    v-model="dayformat" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker locale="th" :min="min" :max="maxSelectDate" v-model="date"
                  @input="menu = false"></v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="d-flex justify-end"><span class="textSR py-3">รายสัปดาห์</span></v-col>
            <v-col @click="changeSelect('week')">
              <v-menu v-model="menuWeek" :close-on-content-click="false" :nudge-right="40" transition="scale-transition"
                offset-y min-width="auto">
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field placeholder="วัน เดือน ปี" :disabled="disable.week" outlined hide-details class="sl"
                    v-model="weekRange" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker locale="th" :min="min" :max="maxWeekRange" :allowed-dates="allowedDates" v-model="week"
                  @input="menuWeek = false"></v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="d-flex justify-end"><span class="textSR py-3">รายเดือน</span></v-col>
            <v-col @click="changeSelect('month')">
              <v-menu v-model="menuMonth" :close-on-content-click="false" :nudge-right="40" transition="scale-transition"
                offset-y min-width="auto">
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field placeholder="เดือน ปี" :disabled="disable.month" outlined hide-details class="sl"
                    v-model="monthformat" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker locale="th" :min="min" :max="maxMonthRange" type="month" v-model="month"
                  @input="menuMonth = false"></v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="d-flex justify-end"><span class="textSR py-3">รายปี</span></v-col>
            <v-col @click="changeSelect('year')">
              <v-select placeholder="ปี" :disabled="disable.year" v-model="selectYear" :items="years" outlined
                hide-details class="sl"></v-select>
            </v-col>
          </v-row>
          <v-row class="justify-center mt-16">
            <v-btn class="mr-4" color="primary" @click="confirm()">Export</v-btn>
            <v-btn color="primary" @click="exportExcel()">Export Excel</v-btn>
          </v-row>

        </v-container>

      </v-container>

      <div></div>

    </v-content>
    <v-content class="pl-3" v-else>
      <v-container class="pl-1 pr-1">
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext-mobile">รายงานผลข้อมูลจราจรของ กทม.</span>
        </v-chip>

        <v-container justify-center align-center>
          <v-card class="card-mobile elevation-0 mb-3" @click="changeSelect('day')">
            <span class="textSR-mobile py-3 mb-3">รายวัน</span>
            <v-menu v-model="menu" :close-on-content-click="false" :nudge-right="40" transition="scale-transition"
              offset-y min-width="auto">
              <template v-slot:activator="{ on, attrs }">
                <v-text-field placeholder="วัน เดือน ปี" :disabled="disable.day" outlined hide-details class="sl-mobile"
                  v-model="dayformat" readonly v-bind="attrs" v-on="on"></v-text-field>
              </template>
              <v-date-picker locale="th" :min="min" :max="maxSelectDate" v-model="date"
                @input="menu = false"></v-date-picker>
            </v-menu>
          </v-card>
          <v-card class="card-mobile elevation-0 mb-3" @click="changeSelect('week')">
            <span class="textSR-mobile py-3 mb-3">รายสัปดาห์</span>
            <v-menu v-model="menuWeek" :close-on-content-click="false" :nudge-right="40" transition="scale-transition"
              offset-y min-width="auto">
              <template v-slot:activator="{ on, attrs }">
                <v-text-field placeholder="วัน เดือน ปี" :disabled="disable.week" outlined hide-details class="sl-mobile"
                  v-model="weekRange" readonly v-bind="attrs" v-on="on"></v-text-field>
              </template>
              <v-date-picker locale="th" :min="min" :max="maxWeekRange" :allowed-dates="allowedDates" v-model="week"
                @input="menuWeek = false"></v-date-picker>
            </v-menu>
          </v-card>
          <v-card class="card-mobile elevation-0 mb-3" @click="changeSelect('month')">
            <span class="textSR-mobile py-3 mb-3">รายเดือน</span>
            <v-menu v-model="menuMonth" :close-on-content-click="false" :nudge-right="40" transition="scale-transition"
              offset-y min-width="auto">
              <template v-slot:activator="{ on, attrs }">
                <v-text-field placeholder="เดือน ปี" :disabled="disable.month" outlined hide-details class="sl-mobile"
                  v-model="monthformat" readonly v-bind="attrs" v-on="on"></v-text-field>
              </template>
              <v-date-picker locale="th" :min="min" :max="maxMonthRange" type="month" v-model="month"
                @input="menuMonth = false"></v-date-picker>
            </v-menu>
          </v-card>
          <v-card class="card-mobile elevation-0 mb-3" @click="changeSelect('year')">
            <span class="textSR-mobile py-3 mb-3">รายปี</span>
            <v-select placeholder="ปี" :disabled="disable.year" v-model="selectYear" :items="years" outlined hide-details
              class="sl-mobile"></v-select>
          </v-card>

          <v-row class="justify-center mt-10">
            <v-btn class="mr-4" color="primary" @click="confirm()">Export</v-btn>
            <v-btn color="primary" @click="exportExcel()">Export Excel</v-btn>
          </v-row>
        </v-container>
      </v-container>

      <div></div>
    </v-content>

    <datePDF :downloadpdf="openDatePDF" :dataExport="dataExport" :date="dateReport" @closePDF="close('d')"></datePDF>
    <weekPDF :downloadpdf="openWeekPDF" :dataExport="dataExport" :date="dateReport" @closePDF="close('w')"></weekPDF>
    <monthPDF :downloadpdf="openMonthPDF" :dataExport="dataExport" :date="dateReport" :checkMonth="checkMonthReport"
      @closePDF="close('m')"></monthPDF>
    <yearPDF :downloadpdf="openYearPDF" :dataExport="dataExport" :date="dateReport" @closePDF="close('y')"></yearPDF>

  </v-app>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
import headerbar from "../components/header-bar.vue";
import Swal from "sweetalert2/dist/sweetalert2.js";
import datePDF from "../formatExport/adminDatePDF.vue"
import weekPDF from "../formatExport/adminWeekPDF.vue"
import monthPDF from "../formatExport/adminMonthPDF.vue"
import yearPDF from "../formatExport/adminYearPDF.vue"
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import loginVue from './login.vue';

am4core.useTheme(am4themes_animated);
const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});
export default {
  components: {
    sidebar,
    headerbar,
    datePDF,
    weekPDF,
    monthPDF,
    yearPDF,
  },
  data() {
    return {
      success: false,
      onProgress: false,
      onProgressDay: false,
      onProgressWeek: false,
      onProgressMonth: false,
      onProgressYear: false,
      checkMonthReport: 0,
      dateReport: "",
      textDate: "",
      openDatePDF: false,
      openMonthPDF: false,
      openWeekPDF: false,
      openYearPDF: false,
      min: '2022-08-01',
      allowedDates: (val) => new Date(val).getDay() === 1,
      drawer: true,
      opendatepicker: false,
      date: "",
      menu: false,
      week: "",
      menuWeek: false,
      menuMonth: false,
      month: "",
      selectYear: "",
      menuTimeStart: false,
      menuTimeEnd: false,
      timeStart: "",
      timeEnd: "",
      selected: true,
      unselect: true,
      disable: [
        {
          name: "day",
          value: false
        },
        {
          name: "week",
          value: false
        },
        {
          name: "month",
          value: false
        },
        {
          name: "year",
          value: false
        },
        {
          name: "time",
          value: false
        }
      ],
      disable: {
        day: false,
        week: true,
        month: true,
        year: true,
        startRange: true,
        endRange: true
      },
      dataExport: [],

      new_report_direction: {},
      testYear: false,

    };
  },
  computed: {
    timeStartformat() {
      if (this.timeStart === "") {
        return ""

      }
      let data = this.timeStart.split("-");
      let year = parseInt(data[0]) + 543;
      return data[2] + "-" + data[1] + "-" + year.toString();

    },
    timeEndformat() {
      if (this.timeStart === "") {
        return ""

      }
      var endDate = new Date(this.timeStart);
      endDate.setDate(endDate.getDate() + 6)
      this.timeEnd = endDate.toISOString().substr(0, 10)
      let end = endDate.toISOString().substr(0, 10)
      let data = end.split("-");
      let year = parseInt(data[0]) + 543;
      return data[2] + "-" + data[1] + "-" + year.toString();

    },
    dayformat() {
      if (this.date === "") {
        return ""

      }
      let data = this.date.split("-");
      let year = parseInt(data[0]) + 543;
      return data[2] + "-" + data[1] + "-" + year.toString();

    },
    monthformat() {
      if (this.month === "") {
        return ""

      }
      let data = this.month.split("-");
      let year = parseInt(data[0]) + 543;
      return data[1] + "-" + year.toString();

    },
    maxSelectDate() {
      var endDate = new Date();
      endDate.setDate(endDate.getDate() - 1);
      return endDate.toISOString().substr(0, 10);
    },
    weekRange() {
      if (this.week === "") {
        return ""
      } else {
        let data1 = this.week.split("-");
        let year1 = parseInt(data1[0]) + 543;
        var endDate = new Date(this.week);
        endDate.setDate(endDate.getDate() + 6);
        let week2 = endDate.toISOString().substr(0, 10)
        let data2 = week2.split("-");
        let year2 = parseInt(data2[0]) + 543;
        return data1[2] + "-" + data1[1] + "-" + year1.toString() + " ~ " + data2[2] + "-" + data2[1] + "-" + year2.toString();
      }
    },
    maxDateEnd() {

      if (this.timeStart === "") {
        var endDate = new Date();
        endDate.setDate(endDate.getDate() - 7);
        return endDate.toISOString().substr(0, 10);
      } else {
        var endDate = new Date(this.timeStart);
        endDate.setDate(endDate.getDate() + 6);
        return endDate.toISOString().substr(0, 10);
      }
    },
    minSelectRange() {
      return this.timeStart
    },
    maxDateStart() {
      var endDate = new Date();
      endDate.setDate(endDate.getDate() - 7);
      return endDate.toISOString().substr(0, 10);
    },
    maxWeekRange() {
      var endDate = new Date();
      endDate.setDate(endDate.getDate() - 6);
      return endDate.toISOString().substr(0, 10);

    },
    maxMonthRange() {
      var endDate = new Date();
      endDate.setDate(endDate.getDate());
      return endDate.toISOString().substr(0, 10);

    },
    years() {
      const year = (new Date().getFullYear()) + 543

      return Array.from({ length: year - 2564 }, (value, index) => 2565 + index);
    },
  },
  methods: {
    close(param) {
      this.onProgress = false

      this.$router.go();
    },

    changeSelect(param) {
      //console.log("changeSelect",param);
      if (param === "day") {
        this.disable.day = false;
        this.disable.week = true;
        this.disable.month = true;
        this.disable.year = true;
        this.disable.startRange = true;
        this.disable.endRange = true;

        this.week = ""
        this.month = ""
        this.year = ""
        this.time = ""
      } else if (param === "week") {
        this.disable.day = true;
        this.disable.week = false;
        this.disable.month = true;
        this.disable.year = true;
        this.disable.startRange = true;
        this.disable.endRange = true;
        this.date = ""
        this.month = ""
        this.year = ""
        this.time = ""
      } else if (param === "month") {
        this.disable.day = true;
        this.disable.week = true;
        this.disable.month = false;
        this.disable.year = true;
        this.disable.startRange = true;
        this.disable.endRange = true;
        this.date = ""
        this.week = ""
        this.year = ""
        this.time = ""
      }
      else if (param === "year") {
        this.disable.day = true;
        this.disable.week = true;
        this.disable.month = true;
        this.disable.year = false;
        this.disable.startRange = true;
        this.disable.endRange = true;
        this.date = ""
        this.week = ""
        this.month = ""

        this.time = ""
      }
      else if (param === "range") {
        this.disable.day = true;
        this.disable.week = true;
        this.disable.month = true;
        this.disable.year = true;
        this.disable.startRange = false;
        this.disable.endRange = true;
        this.date = ""
        this.week = ""
        this.month = ""
        this.year = ""
      } else if (param === "rangeEnd") {
        //console.log(this.timeStart);
        if (this.timeStart !== "") {
          this.disable.day = true;
          this.disable.week = true;
          this.disable.month = true;
          this.disable.year = true;
          this.disable.startRange = false;
          this.disable.endRange = false;
          this.date = ""
          this.week = ""
          this.month = ""
          this.year = ""
        }
      }

    },
    dateSelect() {
      this.menu = false;
      this.disable.Week = true
      this.disable.Month = true
      this.disable.Year = true
      this.disable.Time = true
    },
    maxStart() {
      var endDate = new Date();
      endDate.setDate(endDate.getDate() - 1);
      return endDate.toISOString().substr(0, 10);
    },
    isValidHttpUrl(string) {
      let url;
      try {
        url = new URL(string);
      } catch (_) {
        return false;
      }
      return url.protocol === "http:" || url.protocol === "https:";
    },
    async exportExcel() {
      if (this.date == "" && this.week == "" && this.month == "" && this.selectYear == "" && this.timeStart == "" && this.timeEnd == "") {
        Toast.fire({
          icon: "error",
          title: "กรุณากรอกข้อมูล",
        });
        return
      }
      let settime = this.timeStart + "," + this.timeEnd;
      let paramType = !this.disable.day ? "day" : !this.disable.week ? "week" : !this.disable.month ? "month" : !this.disable.year ? "year" : !this.disable.startRange ? "range" : "";
      let year = parseInt(this.selectYear - 543)
      let paramDate = this.date !== "" ? this.date : this.week !== "" ? this.week : this.month !== "" ? this.month : this.selectYear !== "" ? year : this.timeStart !== "" && this.timeEnd !== "" ? settime : "";
      this.textDate = this.date !== "" ? this.date : this.week !== "" ? this.week : this.month !== "" ? this.month : this.selectYear !== "" ? year : this.timeStart !== "" && this.timeEnd !== "" ? settime : "";
      if (paramType !== undefined && paramDate !== undefined) {
        let typeExport = paramType == "day" ? "daily-excel" : paramType
        typeExport = paramType == "week" ? "weekly-excel" : typeExport
        typeExport = paramType == "month" ? "monthly-excel" : typeExport
        typeExport = paramType == "year" ? "yearly-excel" : typeExport

        const url = `${baseUrl.imgServer}/media/${typeExport}/${paramDate}.xlsx`;

        window.open(url, '_blank', 'noreferrer');
      }
    },
    async confirm() {
      if (this.date == "" && this.week == "" && this.month == "" && this.selectYear == "" && this.timeStart == "" && this.timeEnd == "") {
        Toast.fire({
          icon: "error",
          title: "กรุณากรอกข้อมูล",
        });
        return
      }
      let settime = this.timeStart + "," + this.timeEnd;
      let paramType = !this.disable.day ? "day" : !this.disable.week ? "week" : !this.disable.month ? "month" : !this.disable.year ? "year" : !this.disable.startRange ? "range" : "";
      let year = parseInt(this.selectYear - 543)
      let paramDate = this.date !== "" ? this.date : this.week !== "" ? this.week : this.month !== "" ? this.month : this.selectYear !== "" ? year : this.timeStart !== "" && this.timeEnd !== "" ? settime : "";
      this.textDate = this.date !== "" ? this.date : this.week !== "" ? this.week : this.month !== "" ? this.month : this.selectYear !== "" ? year : this.timeStart !== "" && this.timeEnd !== "" ? settime : "";

      if (paramType !== undefined && paramDate !== undefined) {
        let param = { type: paramType, date: paramDate }

        // report New version 

        let typeExport = paramType == "day" ? "daily" : paramType
        typeExport = paramType == "week" ? "weekly" : typeExport
        typeExport = paramType == "month" ? "monthly" : typeExport
        typeExport = paramType == "year" ? "yearly" : typeExport

        const url = `${baseUrl.imgServer}/media/${typeExport}/${paramDate}.pdf`;
        console.log('url :>> ', url);
        window.open(url, '_blank', 'noreferrer');



        // report old version
        // this.onProgress = true
        // let res = await this.getDataExport(param)

        // if(res.status === 'success'){

        //   if(paramType == 'day'){
        //     this.openDatePDF = !this.openDatePDF
        //   }else if(paramType == 'week'){
        //     this.openWeekPDF =!this.openWeekPDF
        //   }else if(paramType == 'month'){
        //     this.openMonthPDF = !this.openMonthPDF
        //   }else if(paramType == 'year'){
        //     this.openYearPDF = !this.openYearPDF
        //   }

        // }

      }


    },
    async getDataExport(param) {
      return new Promise((resolve, reject) => {
        this.setDateReport(param)
        if (param.type == 'day') {
          var type_key = 'time'
        } else if (param.type == 'week' || param.type == 'month') {
          var type_key = 'date'
        } else if (param.type == 'year') {
          var type_key = 'month'
        }
        let session_data = localStorage.getItem("session");
        let url = baseUrl.ipServer + "/report-bkk";
        this.axios
          .get(url, {
            headers: { session: session_data },
            params: param,
          })
          .then((response) => {
            if (response.status === 200) {
              this.dataExport = []
              console.log(response.data);
              let res = response.data.data
              for (let i = 0; i < res.length; i++) {
                let data = {}
                data["checkpoint_name"] = res[i].checkpoint.short_name
                data["checkpoint_id"] = res[i].checkpoint.id
                data["road_name"] = res[i].checkpoint.road

                const carTypeHeader = [
                  'รถยนต์ส่วนบุคคล', 'รถจักรยานยนต์', 'รถโดยสาร',
                  'รถบรรทุก', 'รถบรรทุกขนาดเล็ก', 'รถตู้', 'รถสามล้อเครื่อง',
                  'รถ SUV', 'อื่นๆ', 'pcu', 'total'
                ]
                const carType_violation = [
                  'รถยนต์ส่วนบุคคล', 'รถจักรยานยนต์', 'รถโดยสาร',
                  'รถบรรทุก', 'รถบรรทุกขนาดเล็ก', 'รถตู้', 'รถสามล้อเครื่อง',
                  'รถ SUV', 'อื่นๆ'
                ]

                const type_data = [
                  'ปริมาณยานพาหนะทั้งหมด', 'ปริมาณยานพาหนะฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด'
                ]
                const ReportDataExtractTime = res[i].report.inbound[carTypeHeader[0]]['data']

                let header = {}
                let formatDate
                let headerTable = []

                for (let i = 0; i < ReportDataExtractTime.length; i++) {
                  //console.log( "report",ReportDataExtractTime[i][type_key]);
                  if (type_key == 'month') {
                    formatDate = this.settextMonth(ReportDataExtractTime[i][type_key])
                  }
                  else {
                    formatDate = ReportDataExtractTime[i][type_key]
                  }
                  header["text"] = formatDate
                  headerTable.push(formatDate)

                }

                //headerTable = ['TYPE'].concat(headerTable)

                headerTable.push('ALL')
                //headerTable.push('PCU')
                data["headerTable"] = headerTable
                var total_volume_in = 0
                var total_volume_out = 0
                let dataInbound = []
                var count1 = 0;
                let dataOutbound = []
                var count2 = 0;
                if (param.type == 'week') {
                  for (const carType of carTypeHeader) {
                    const data = res[i].report.inbound[carType]['data']
                    const total = res[i].report.inbound[carType]['total']
                    total_volume_in = res[i].report.inbound['total']['total']
                    const pcu = res[i].report.inbound[carType]['pcu']

                    let extract_data = {}
                    extract_data['type'] = carType

                    for (let i = 0; i < data.length; i++) {
                      extract_data["_" + data[i]["days"]] = data[i]["volume"]

                    }

                    extract_data['all'] = total
                    extract_data['pcu'] = pcu
                    extract_data['id'] = count1++
                    dataInbound.push(extract_data)
                  }
                  for (const carType of carTypeHeader) {
                    const data = res[i].report.outbound[carType]['data']
                    const total = res[i].report.outbound[carType]['total']
                    total_volume_out = res[i].report.outbound['total']['total']
                    const pcu = res[i].report.outbound[carType]['pcu']

                    let extract_data = {}
                    extract_data['type'] = carType
                    extract_data['id'] = count2++
                    for (let i = 0; i < data.length; i++) {
                      extract_data["_" + data[i]["days"]] = data[i]["volume"]
                    }
                    extract_data['all'] = total
                    extract_data['pcu'] = pcu
                    dataOutbound.push(extract_data)
                  }
                } else if (param.type == 'month') {
                  for (const carType of carTypeHeader) {
                    const data = res[i].report.inbound[carType]['data']
                    const total = res[i].report.inbound[carType]['total']
                    total_volume_in = res[i].report.inbound['total']['total']
                    const pcu = res[i].report.inbound[carType]['pcu']

                    let extract_data = {}
                    extract_data['type'] = carType
                    let key_date;
                    for (let i = 0; i < data.length; i++) {
                      if (String(data[i]["date"]).search("T") == -1) {
                        key_date = "-"
                      } else {
                        key_date = data[i]["date"].split("T")[0].split("-")[2]
                      }



                      extract_data["_" + key_date] = data[i]["volume"]

                    }

                    extract_data['all'] = total
                    extract_data['pcu'] = pcu
                    extract_data['id'] = count1++
                    dataInbound.push(extract_data)
                  }
                  for (const carType of carTypeHeader) {
                    const data = res[i].report.outbound[carType]['data']
                    const total = res[i].report.outbound[carType]['total']
                    total_volume_out = res[i].report.outbound['total']['total']
                    const pcu = res[i].report.outbound[carType]['pcu']

                    let extract_data = {}
                    extract_data['type'] = carType
                    extract_data['id'] = count2++

                    for (let i = 0; i < data.length; i++) {
                      let key_date;
                      if (String(data[i]["date"]).search("T") == -1) {
                        key_date = "-"
                      } else {
                        key_date = data[i]["date"].split("T")[0].split("-")[2]
                      }

                      extract_data["_" + key_date] = data[i]["volume"]
                    }
                    extract_data['all'] = total
                    extract_data['pcu'] = pcu
                    dataOutbound.push(extract_data)
                  }
                }
                else {

                  for (const carType of carTypeHeader) {
                    const data = res[i].report.inbound[carType]['data']
                    const total = res[i].report.inbound[carType]['total']
                    total_volume_in = res[i].report.inbound['total']['total']
                    const pcu = res[i].report.inbound[carType]['pcu']

                    let extract_data = {}
                    extract_data['type'] = carType
                    for (let i = 0; i < data.length; i++) {
                      extract_data["_" + i] = data[i]["volume"]
                    }

                    extract_data['all'] = total
                    extract_data['pcu'] = pcu
                    extract_data['id'] = count1++
                    dataInbound.push(extract_data)
                  }

                  for (const carType of carTypeHeader) {
                    const data = res[i].report.outbound[carType]['data']
                    const total = res[i].report.outbound[carType]['total']
                    total_volume_out = res[i].report.outbound['total']['total']
                    const pcu = res[i].report.outbound[carType]['pcu']

                    let extract_data = {}
                    extract_data['type'] = carType
                    extract_data['id'] = count2++
                    for (let i = 0; i < data.length; i++) {
                      extract_data["_" + i] = data[i]["volume"]
                    }
                    extract_data['all'] = total
                    extract_data['pcu'] = pcu
                    dataOutbound.push(extract_data)
                  }
                }

                let dataChart = []
                let dataCat = []
                let lineChart = []
                for (let j = 0; j < res[i].car_type.volume.length; j++) {
                  dataChart.push(res[i].car_type.volume[j].volume)
                  dataCat.push(res[i].car_type.volume[j].car_type)
                }

                if (param.type == 'day') {
                  let inbound_report = res[i].report_quarter_hour.inbound
                  let quater_data_in = [{ 'type': '00-15' }, { 'type': '15-30' }, { 'type': '30-45' }, { 'type': '45-00' }, { 'type': 'total' }]
                  let total_quarter = [0, 0, 0, 0, 0]
                  for (let j = 0; j < inbound_report.length; j++) {

                    quater_data_in[4]["_" + j] = inbound_report[j].total
                    total_quarter[4] += inbound_report[j].total

                    for (let z = 0; z < inbound_report[j].data.length; z++) {
                      quater_data_in[z]["_" + j] = inbound_report[j].data[z].volume
                      total_quarter[z] += inbound_report[j].data[z].volume
                    }
                  }

                  for (let all_index = 0; all_index < total_quarter.length; all_index++) {
                    quater_data_in[all_index]['all'] = total_quarter[all_index]
                  }

                  let outbound_report = res[i].report_quarter_hour.outbound
                  let quater_data_out = [{ 'type': '00-15' }, { 'type': '15-30' }, { 'type': '30-45' }, { 'type': '45-00' }, { 'type': 'total' }]
                  let total_quarter_out = [0, 0, 0, 0, 0]
                  for (let j = 0; j < outbound_report.length; j++) {

                    quater_data_out[4]["_" + j] = outbound_report[j].total
                    total_quarter_out[4] += outbound_report[j].total

                    for (let z = 0; z < outbound_report[j].data.length; z++) {
                      quater_data_out[z]["_" + j] = outbound_report[j].data[z].volume
                      total_quarter_out[z] += outbound_report[j].data[z].volume
                    }
                  }

                  for (let all_index = 0; all_index < total_quarter_out.length; all_index++) {
                    quater_data_out[all_index]['all'] = total_quarter_out[all_index]
                  }

                  data["quaterInbound"] = quater_data_in
                  data["quaterOutbound"] = quater_data_out
                }
                else {

                  let inbound_report = res[i].report_direction.inbound
                  let new_report_direction = []
                  let array_inbound_volume_mean = []
                  let array_outbound_volume_mean = []
                  let array_inbound_volume = []
                  let array_outbound_volume = []
                  for (let j = 0; j < res[i].report_direction.inbound.data.length; j++) {
                    array_inbound_volume.push(Math.floor(inbound_report.data[j].volume))
                    array_outbound_volume.push(Math.floor(inbound_report.data[j].volume))
                    array_inbound_volume_mean.push(Math.floor(inbound_report.data[j].volume_mean))
                    array_outbound_volume_mean.push(Math.floor(inbound_report.data[j].volume_mean))
                  }
                  array_inbound_volume[inbound_report.data.length] = Math.floor(inbound_report.total.volume || 0)
                  array_outbound_volume[inbound_report.data.length] = Math.floor(inbound_report.total.volume || 0)
                  array_inbound_volume_mean[inbound_report.data.length] = Math.floor(inbound_report.total.volume_mean || 0)
                  array_outbound_volume_mean[inbound_report.data.length] = Math.floor(inbound_report.total.volume_mean || 0)
                  new_report_direction = {
                    "volume_inbound": array_inbound_volume,
                    "volume_outbound": array_outbound_volume,
                    "volume_mean_inbound": array_inbound_volume_mean,
                    "volume_mean_volume_outbound": array_outbound_volume_mean
                  }

                  data["dataDirection"] = new_report_direction
                }

                let report_rush_in_normal = res[i].report_rush_hour
                let dataRush = []
                if (param.type == 'month' || param.type == 'year') {

                  var count1 = 0;
                  for (const carType of carTypeHeader) {
                    const data = report_rush_in_normal.inbound[carType]['data']
                    const data_out = report_rush_in_normal.outbound[carType]['data']
                    const total = report_rush_in_normal.inbound[carType]['total']
                    const total_out = report_rush_in_normal.outbound[carType]['total']
                    let extract_data = {}

                    extract_data['type'] = carType
                    for (let i = 0; i < data.length; i++) {
                      extract_data["in_" + i] = data[i]
                      extract_data["out_" + i] = data_out[i]
                    }
                    extract_data['in_all'] = total
                    extract_data['out_all'] = total_out
                    extract_data['id'] = count1++
                    dataRush.push(extract_data)
                  }
                  //console.log(dataRushInbound);
                }


                if (param.type == 'year') {

                  let dataYear = []
                  let dataYear_in = []
                  let dataYear_out = []
                  var count1 = 0;
                  var count1_in = 0;
                  var count1_out = 0;
                  for (const carType of carTypeHeader) {
                    const data = res[i].report.inbound[carType]['data']
                    const total = res[i].report.inbound[carType]['total']
                    const data_out = res[i].report.outbound[carType]['data']
                    const total_out = res[i].report.outbound[carType]['total']
                    let extract_data = {}
                    let extract_data_in = {}
                    let extract_data_out = {}
                    extract_data['type'] = carType
                    extract_data_in['type'] = carType
                    extract_data_out['type'] = carType
                    for (let i = 0; i < data.length; i++) {
                      extract_data["in_" + i] = data[i]["volume"]
                      extract_data["out_" + i] = data_out[i]["volume"]
                      extract_data_in["all_" + i] = data[i]["volume"]
                      extract_data_out["all_" + i] = data_out[i]["volume"]
                    }
                    extract_data['in_all'] = total
                    extract_data['out_all'] = total_out
                    extract_data['id'] = count1++

                    extract_data_in['all_all'] = total
                    extract_data_out['all_all'] = total_out
                    extract_data_in['id'] = count1_in++
                    extract_data_out['id'] = count1_out++


                    dataYear.push(extract_data)
                    dataYear_in.push(extract_data_in)
                    dataYear_out.push(extract_data_out)
                  }
                  //console.log(dataRushInbound);
                  data["dataYear"] = dataYear
                  data["dataYear_in"] = dataYear_in
                  data["dataYear_out"] = dataYear_out
                }

                let graph = res[i].graph
                let apex_line = [{ name: "ขาเข้า", data: [] }, { name: "ขาออก", data: [] }]
                let apex_cat_ = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                let month_raw1 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
                let apex_cat = []
                let array_in = []
                let array_out = []
                for (let index = 0; index < graph.inbound.length; index++) {
                  apex_line[0]['data']
                  if (param.type == 'week') {
                    //apex_cat.push(graph.outbound[index].date)
                    apex_cat = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]
                  } else if (param.type == 'day') {
                    apex_cat.push(graph.outbound[index].time)
                    array_in.push(graph.inbound[index].volume)
                    array_out.push(graph.outbound[index].volume)
                  } else if (param.type == 'month') {
                    let date = graph.outbound[index].date.split('T')[0].split("-")

                    apex_cat = month_raw1
                  } else if (param.type == 'year') {
                    apex_cat.push(graph.outbound[index].month)
                    array_in.push(graph.inbound[index].volume)
                    array_out.push(graph.outbound[index].volume)
                  }




                }
                if (param.type == 'week') {
                  let jj = 0
                  for (let ii = 0; ii < 7; ii++) {
                    if (graph.inbound[jj]) {
                      if (apex_cat_[ii] == graph.inbound[jj].days) {
                        array_in.push(graph.inbound[jj].volume)
                        array_out.push(graph.outbound[jj].volume)
                        jj++
                      } else {
                        array_in.push(0)
                        array_out.push(graph.outbound[jj].volume)
                      }
                    } else {
                      array_in.push(0)
                      array_out.push(0)
                    }
                  }
                } else if (param.type == 'month') {
                  let j = 0
                  for (let i = 0; i < 31; i++) {
                    let a;
                    if (!graph.inbound[j]) {
                      a = "00"
                    } else {
                      a = graph.inbound[j].date.split('T')[0].split("-")[2]
                    }

                    if (month_raw1[i] === a) {

                      array_in.push(graph.inbound[j].volume)
                      array_out.push(graph.outbound[j].volume)
                      console.log("b ", a);
                      // if (graph_violation.inbound.length < j)
                      j++
                    } else {
                      array_in.push(0)
                      array_out.push(0)

                    }
                  }
                }
                apex_line[0].data = array_in
                apex_line[1].data = array_out

                data["dataInbound"] = dataInbound
                data["dataOutbound"] = dataOutbound
                data["categories"] = dataCat
                data["dataChart"] = dataChart
                data["dataPieChart"] = res[i].car_type.volume
                data["dataLineChart"] = lineChart
                data["dataRush"] = dataRush
                data["apex_cat"] = apex_cat
                data["apex_line"] = apex_line


                //---------------------------violation data
                let dataInbound_violation = []
                var count1_violation = 0;
                let dataOutbound_violation = []
                var count2_violation = 0;
                var total_volume_in_violation = 0
                var total_volume_out_violation = 0
                let array_pie_in = []
                let array_pie_out = []
                if (param.type == 'week') {
                  for (const carType of carTypeHeader) {
                    const data_violation = res[i].violation.report.inbound[carType]['data']
                    const total_violation = res[i].violation.report.inbound[carType]['total']
                    total_volume_in_violation = res[i].violation.report.inbound['total']['total']
                    const pcu_violation = res[i].violation.report.inbound[carType]['pcu']
                    let total_pie = {}
                    //  total_pie["car_type"] = carType
                    //  total_pie["volume"] = res[i].violation.report.inbound[carType]['total']
                    if (carType !== "total" && carType !== "pcu") {
                      array_pie_in.push(res[i].violation.report.inbound[carType]['total'])
                    }

                    let extract_data = {}
                    extract_data['type'] = carType

                    for (let i = 0; i < data_violation.length; i++) {
                      extract_data["_" + data_violation[i]["days"]] = data_violation[i]["volume"]

                    }

                    extract_data['all'] = total_violation
                    extract_data['pcu'] = pcu_violation
                    extract_data['id'] = count1_violation++
                    dataInbound_violation.push(extract_data)
                  }
                  for (const carType of carTypeHeader) {
                    const data_violation = res[i].violation.report.outbound[carType]['data']
                    const total_violation = res[i].violation.report.outbound[carType]['total']
                    total_volume_out_violation = res[i].violation.report.outbound['total']['total']
                    const pcu_violation = res[i].violation.report.outbound[carType]['pcu']
                    let total_pie = {}
                    //  total_pie["car_type"] = carType
                    //  total_pie["volume"] = res[i].violation.report.outbound[carType]['total']
                    if (carType !== "total" && carType !== "pcu") {
                      array_pie_out.push(res[i].violation.report.outbound[carType]['total'])
                    }
                    let extract_data = {}
                    extract_data['type'] = carType
                    extract_data['id'] = count2_violation++
                    for (let i = 0; i < data_violation.length; i++) {
                      extract_data["_" + data_violation[i]["days"]] = data_violation[i]["volume"]
                    }
                    extract_data['all'] = total_violation
                    extract_data['pcu'] = pcu_violation
                    dataOutbound_violation.push(extract_data)
                  }
                } else if (param.type == 'month') {
                  for (const carType of carTypeHeader) {
                    const data_violation = res[i].violation.report.inbound[carType]['data']
                    const total_violation = res[i].violation.report.inbound[carType]['total']
                    total_volume_in_violation = res[i].violation.report.inbound['total']['total']
                    const pcu_violation = res[i].violation.report.inbound[carType]['pcu']
                    let total_pie = {}
                    //  total_pie["car_type"] = carType
                    //  total_pie["volume"] = res[i].violation.report.inbound[carType]['total']
                    if (carType !== "total" && carType !== "pcu") {
                      array_pie_in.push(res[i].violation.report.inbound[carType]['total'])
                    }
                    let extract_data = {}
                    extract_data['type'] = carType
                    let key_date;
                    for (let i = 0; i < data_violation.length; i++) {
                      if (String(data_violation[i]["date"]).search("T") == -1) {
                        key_date = "-"
                      } else {
                        key_date = data_violation[i]["date"].split("T")[0].split("-")[2]
                      }

                      extract_data["_" + key_date] = data_violation[i]["volume"]

                    }

                    extract_data['all'] = total_violation
                    extract_data['pcu'] = pcu_violation
                    extract_data['id'] = count1_violation++
                    dataInbound_violation.push(extract_data)
                  }
                  for (const carType of carTypeHeader) {
                    const data_violation = res[i].violation.report.outbound[carType]['data']
                    const total_violation = res[i].violation.report.outbound[carType]['total']
                    total_volume_out_violation = res[i].violation.report.outbound['total']['total']
                    const pcu_violation = res[i].violation.report.outbound[carType]['pcu']
                    let total_pie = {}
                    total_pie["car_type"] = carType
                    total_pie["volume"] = res[i].violation.report.outbound[carType]['total']
                    if (carType !== "total" && carType !== "pcu") {
                      array_pie_out.push(res[i].violation.report.outbound[carType]['total'])
                    }
                    let extract_data = {}
                    extract_data['type'] = carType
                    extract_data['id'] = count2_violation++
                    let key_date;
                    for (let i = 0; i < data_violation.length; i++) {

                      if (String(data_violation[i]["date"]).search("T") == -1) {
                        key_date = "-"
                      } else {
                        key_date = data_violation[i]["date"].split("T")[0].split("-")[2]
                      }

                      extract_data["_" + key_date] = data_violation[i]["volume"]
                    }
                    extract_data['all'] = total_violation
                    extract_data['pcu'] = pcu_violation
                    dataOutbound_violation.push(extract_data)
                  }
                }
                else {

                  for (const carType of carTypeHeader) {
                    const data_violation = res[i].violation.report.inbound[carType]['data']
                    const total_violation = res[i].violation.report.inbound[carType]['total']
                    total_volume_in_violation = res[i].violation.report.inbound['total']['total']
                    let total_pie = {}
                    total_pie["car_type"] = carType
                    console.log("carType", carType);
                    total_pie["volume"] = res[i].violation.report.inbound[carType]['total']
                    if (carType !== "total" && carType !== "pcu") {
                      array_pie_in.push(res[i].violation.report.inbound[carType]['total'])
                    }
                    const pcu_violation = res[i].violation.report.inbound[carType]['pcu']

                    let extract_data = {}
                    extract_data['type'] = carType
                    for (let i = 0; i < data_violation.length; i++) {
                      extract_data["_" + i] = data_violation[i]["volume"]
                    }

                    extract_data['all'] = total_violation
                    extract_data['pcu'] = pcu_violation
                    extract_data['id'] = count1_violation++
                    dataInbound_violation.push(extract_data)

                  }

                  for (const carType of carTypeHeader) {
                    const data_violation = res[i].violation.report.outbound[carType]['data']
                    const total_violation = res[i].violation.report.outbound[carType]['total']
                    total_volume_out_violation = res[i].violation.report.outbound['total']['total']
                    const pcu_violation = res[i].violation.report.outbound[carType]['pcu']
                    let total_pie = {}
                    total_pie["car_type"] = carType
                    total_pie["volume"] = res[i].violation.report.outbound[carType]['total']
                    if (carType !== "total" && carType !== "pcu") {
                      array_pie_out.push(res[i].violation.report.outbound[carType]['total'])
                    }
                    let extract_data = {}
                    extract_data['type'] = carType
                    extract_data['id'] = count2_violation++
                    for (let i = 0; i < data_violation.length; i++) {
                      extract_data["_" + i] = data_violation[i]["volume"]
                    }
                    extract_data['all'] = total_violation
                    extract_data['pcu'] = pcu_violation
                    dataOutbound_violation.push(extract_data)
                  }
                }


                let dataChart_violation = []
                let dataCat_violation = []
                let lineChart_violation = []
                for (let j = 0; j < res[i].violation.car_type.volume.length; j++) {
                  dataChart_violation.push(res[i].violation.car_type.volume[j].volume)
                  dataCat_violation.push(res[i].violation.car_type.volume[j].car_type)
                }

                if (param.type == 'day') {
                  let inbound_report = res[i].violation.report_quarter_hour.inbound
                  let quater_data_in_violation = [{ 'type': '00-15' }, { 'type': '15-30' }, { 'type': '30-45' }, { 'type': '45-00' }, { 'type': 'total' }]
                  let total_quarter = [0, 0, 0, 0, 0]
                  for (let j = 0; j < inbound_report.length; j++) {

                    quater_data_in_violation[4]["_" + j] = inbound_report[j].total
                    total_quarter[4] += inbound_report[j].total

                    for (let z = 0; z < inbound_report[j].data.length; z++) {
                      quater_data_in_violation[z]["_" + j] = inbound_report[j].data[z].volume
                      total_quarter[z] += inbound_report[j].data[z].volume
                    }
                  }

                  for (let all_index = 0; all_index < total_quarter.length; all_index++) {
                    quater_data_in_violation[all_index]['all'] = total_quarter[all_index]
                  }

                  let outbound_report_violation = res[i].violation.report_quarter_hour.outbound
                  let quater_data_out_violation = [{ 'type': '00-15' }, { 'type': '15-30' }, { 'type': '30-45' }, { 'type': '45-00' }, { 'type': 'total' }]
                  let total_quarter_out = [0, 0, 0, 0, 0]
                  for (let j = 0; j < outbound_report_violation.length; j++) {

                    quater_data_out_violation[4]["_" + j] = outbound_report_violation[j].total
                    total_quarter_out[4] += outbound_report_violation[j].total

                    for (let z = 0; z < outbound_report_violation[j].data.length; z++) {
                      quater_data_out_violation[z]["_" + j] = outbound_report_violation[j].data[z].volume
                      total_quarter_out[z] += outbound_report_violation[j].data[z].volume
                    }
                  }

                  for (let all_index = 0; all_index < total_quarter_out.length; all_index++) {
                    quater_data_out_violation[all_index]['all'] = total_quarter_out[all_index]
                  }

                  data["quaterInbound_violation"] = quater_data_in_violation
                  data["quaterOutbound_violation"] = quater_data_out_violation
                }
                else {
                  let inbound_report = res[i].violation_report_direction.inbound
                  let new_report_direction_violation = []
                  let array_inbound_volume_mean = []
                  let array_outbound_volume_mean = []
                  let array_inbound_volume = []
                  let array_outbound_volume = []
                  for (let j = 0; j < inbound_report.data.length; j++) {
                    array_inbound_volume.push(Math.floor(inbound_report.data[j].volume))
                    array_outbound_volume.push(Math.floor(inbound_report.data[j].volume))
                    array_inbound_volume_mean.push(Math.floor(inbound_report.data[j].volume_mean))
                    array_outbound_volume_mean.push(Math.floor(inbound_report.data[j].volume_mean))
                  }
                  array_inbound_volume[inbound_report.data.length] = Math.floor(inbound_report.total.volume || 0)
                  array_outbound_volume[inbound_report.data.length] = Math.floor(inbound_report.total.volume || 0)
                  array_inbound_volume_mean[inbound_report.data.length] = Math.floor(inbound_report.total.volume_mean || 0)
                  array_outbound_volume_mean[inbound_report.data.length] = Math.floor(inbound_report.total.volume_mean || 0)
                  new_report_direction_violation = {
                    "volume_inbound": array_inbound_volume,
                    "volume_outbound": array_outbound_volume,
                    "volume_mean_inbound": array_inbound_volume_mean,
                    "volume_mean_volume_outbound": array_outbound_volume_mean
                  }

                  data["dataDirection_violation"] = new_report_direction_violation
                }

                let report_rush_in_violation = res[i].violation_report_rush_hour
                let dataRush_violation = []
                if (param.type == 'month' || param.type == 'year') {

                  var count1 = 0;
                  for (const carType of carTypeHeader) {
                    const data = report_rush_in_violation.inbound[carType]['data']
                    const data_out = report_rush_in_violation.outbound[carType]['data']
                    const total = report_rush_in_violation.inbound[carType]['total']
                    const total_out = report_rush_in_violation.outbound[carType]['total']
                    let extract_data = {}

                    extract_data['type'] = carType
                    for (let i = 0; i < data.length; i++) {
                      extract_data["in_" + i] = data[i]
                      extract_data["out_" + i] = data_out[i]
                    }
                    extract_data['in_all'] = total
                    extract_data['out_all'] = total_out
                    extract_data['id'] = count1++
                    dataRush_violation.push(extract_data)
                  }
                  //console.log(dataRushInbound);
                }


                if (param.type == 'year') {

                  let dataYear_violation_in = []
                  let dataYear_violation_out = []
                  var count1 = 0; var count2 = 0;

                  for (const carType of carTypeHeader) {
                    const data = res[i].violation.report.inbound[carType]['data']
                    const total = res[i].violation.report.inbound[carType]['total']
                    const data_out = res[i].violation.report.outbound[carType]['data']
                    const total_out = res[i].violation.report.outbound[carType]['total']
                    let extract_data_in = {}
                    let extract_data_out = {}
                    extract_data_in['type'] = carType
                    extract_data_out['type'] = carType
                    for (let i = 0; i < data.length; i++) {
                      extract_data_in["all_" + i] = data[i]["volume"]
                      extract_data_out["all_" + i] = data_out[i]["volume"]
                    }
                    extract_data_in['all_all'] = total
                    extract_data_out['all_all'] = total_out
                    extract_data_in['id'] = count1++
                    extract_data_out['id'] = count2++
                    dataYear_violation_in.push(extract_data_in)
                    dataYear_violation_out.push(extract_data_out)
                  }
                  //console.log(dataRushInbound);
                  data["dataYear_violation_in"] = dataYear_violation_in
                  data["dataYear_violation_out"] = dataYear_violation_out

                }

                let graph_violation = res[i].violation.graph
                let apex_line_in_violation = [{ name: "ปริมาณยานพาหนะทั้งหมด", data: [] }, { name: "ปริมาณยานพาหนะฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด", data: [] }]
                let apex_line_out_violation = [{ name: "ปริมาณยานพาหนะทั้งหมด", data: [] }, { name: "ปริมาณยานพาหนะฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด", data: [] }]
                let apex_cat_violation = []
                let apex_cat_violation_ = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                let month_raw = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
                let array_in_violation = []
                let array_out_violation = []

                for (let index = 0; index < graph_violation.inbound.length; index++) {
                  apex_line[0]['data']
                  if (param.type == 'week') {
                    apex_cat_violation = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]
                  } else if (param.type == 'day') {
                    apex_cat_violation.push(graph_violation.outbound[index].time)

                    array_in_violation.push(graph_violation.inbound[index].volume)
                    array_out_violation.push(graph_violation.outbound[index].volume)

                  } else if (param.type == 'month') {

                    let date = graph_violation.outbound[index].date.split('T')[0].split("-")
                    apex_cat_violation = month_raw


                  } else if (param.type == 'year') {
                    apex_cat_violation.push(graph_violation.outbound[index].month)

                    array_in_violation.push(graph_violation.inbound[index].volume)
                    array_out_violation.push(graph_violation.outbound[index].volume)

                  }



                }
                if (param.type == 'week') {
                  let jj = 0
                  let graph_violation_ = res[i].violation.graph

                  for (let ii = 0; ii < 7; ii++) {
                    console.log(graph_violation_.inbound[jj]);
                    if (graph_violation_.inbound[jj]) {
                      if (apex_cat_violation_[ii] === graph_violation_.inbound[jj].days) {
                        array_in_violation.push(graph_violation_.inbound[jj].volume)
                        array_out_violation.push(graph_violation_.outbound[jj].volume)
                        jj++
                      } else {
                        array_in_violation.push(0)
                        array_out_violation.push(graph_violation_.outbound[jj].volume)
                      }
                    } else {
                      array_in_violation.push(0)
                      array_out_violation.push(0)
                    }
                  }
                } else if (param.type == 'month') {
                  let j = 0
                  for (let i = 0; i < 31; i++) {
                    let a;
                    if (!graph_violation.inbound[j]) {
                      a = "00"
                    } else {
                      a = graph_violation.inbound[j].date.split('T')[0].split("-")[2]
                    }
                    console.log(month_raw[i], a);
                    if (month_raw[i] === a) {

                      array_in_violation.push(graph_violation.inbound[j].volume)
                      array_out_violation.push(graph_violation.outbound[j].volume)

                      // if (graph_violation.inbound.length < j)
                      j++
                    } else {
                      array_in_violation.push(0)
                      array_out_violation.push(0)
                      console.log(array_in_violation);
                    }
                  }
                }

                apex_line_in_violation[0].data = array_in
                apex_line_in_violation[1].data = array_in_violation
                apex_line_out_violation[0].data = array_out
                apex_line_out_violation[1].data = array_out_violation

                console.log("apex_line_in_violation", apex_line_in_violation);

                data["dataInbound_violation"] = dataInbound_violation
                data["dataOutbound_violation"] = dataOutbound_violation
                data["categories_violation"] = carType_violation
                data["dataChart_violation"] = dataChart_violation
                data["dataPieChart_violation"] = res[i].violation.car_type.volume
                data["PieChart_in_violation"] = array_pie_in
                data["PieChart_out_violation"] = array_pie_out
                data["dataLineChart_violation"] = lineChart_violation
                data["dataRush_violation"] = dataRush_violation
                data["apex_cat_violation"] = apex_cat_violation
                data["apex_line_in_violation"] = apex_line_in_violation
                data["apex_line_out_violation"] = apex_line_out_violation
                data["percent_violation_in"] = ((total_volume_in_violation / total_volume_in) * 100).toFixed(2)
                data["percent_violation_out"] = ((total_volume_out_violation / total_volume_out) * 100).toFixed(2)
                data["categories_all_v"] = type_data
                data["PieChart_all_in_violation"] = [total_volume_in, total_volume_in_violation]
                data["PieChart_all_out_violation"] = [total_volume_out, total_volume_out_violation]
                this.dataExport.push(data)
              }


              console.log(this.dataExport);
              resolve({
                status: "success",
              });


            }

          }).catch((error) => {
            console.log(error);
            this.onProgress = false
            this.onProgressDay = false
            this.onProgressWeek = false
            this.onProgressMonth = false
            this.onProgressYear = false
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
              icon: "error",
              title: "Cannot connet API",
            });
          });
      });
    },
    settextMonth(param) {
      let month = param == 1 ? 'ม.ค.' :
        param == 2 ? 'ก.พ.' :
          param == 3 ? 'มี.ค.' :
            param == 4 ? 'เม.ษ.' :
              param == 5 ? 'พ.ค.' :
                param == 6 ? 'มิ.ย.' :
                  param == 7 ? 'ก.ค.' :
                    param == 8 ? 'ส.ค.' :
                      param == 9 ? 'ก.ย.' :
                        param == 10 ? 'ต.ค.' :
                          param == 11 ? 'พ.ย.' : 'ธ.ค.'

      return month
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

      if (param.type === 'day') {
        let date = param.date.split("-") || [];
        let month = date[1] === '01' ? monthNames[0] : date[1] === '02' ? monthNames[1] : date[1] === '03' ? monthNames[2] : date[1] === '04' ? monthNames[3] : date[1] === '05' ? monthNames[4] : date[1] === '06' ? monthNames[5] : date[1] === '07' ? monthNames[6] : date[1] === '08' ? monthNames[7] : date[1] === '09' ? monthNames[8] : date[1] === '10' ? monthNames[9] : date[1] === '11' ? monthNames[10] : date[1] === '12' ? monthNames[11] : "";
        let year = parseInt(date[0]) + 543;
        this.dateReport = `${date[2]} ${month} ${year.toString()}`;
      } else if (param.type === 'week') {
        var endDate = new Date(param.date);
        let date1 = param.date.split("-") || [];
        let year1 = parseInt(date1[0]) + 543;
        endDate.setDate(endDate.getDate() + 6);
        let week2 = endDate.toISOString().substr(0, 10)
        let date2 = week2.split("-");
        let year2 = parseInt(date2[0]) + 543;
        let month1 = date1[1] === '01' ? monthNames[0] : date1[1] === '02' ? monthNames[1] : date1[1] === '03' ? monthNames[2] : date1[1] === '04' ? monthNames[3] : date1[1] === '05' ? monthNames[4] : date1[1] === '06' ? monthNames[5] : date1[1] === '07' ? monthNames[6] : date1[1] === '08' ? monthNames[7] : date1[1] === '09' ? monthNames[8] : date1[1] === '10' ? monthNames[9] : date1[1] === '11' ? monthNames[10] : date1[1] === '12' ? monthNames[11] : "";
        let month2 = date2[1] === '01' ? monthNames[0] : date2[1] === '02' ? monthNames[1] : date2[1] === '03' ? monthNames[2] : date2[1] === '04' ? monthNames[3] : date2[1] === '05' ? monthNames[4] : date2[1] === '06' ? monthNames[5] : date2[1] === '07' ? monthNames[6] : date2[1] === '08' ? monthNames[7] : date2[1] === '09' ? monthNames[8] : date2[1] === '10' ? monthNames[9] : date2[1] === '11' ? monthNames[10] : date2[1] === '12' ? monthNames[11] : "";
        this.dateReport = date1[2] + " " + month1 + " " + year1.toString() + " - " + date2[2] + " " + month2 + " " + year2.toString()
      } else if (param.type === 'month') {
        let date = param.date.split("-") || [];
        let month = date[1] === '01' ? monthNames[0] : date[1] === '02' ? monthNames[1] : date[1] === '03' ? monthNames[2] : date[1] === '04' ? monthNames[3] : date[1] === '05' ? monthNames[4] : date[1] === '06' ? monthNames[5] : date[1] === '07' ? monthNames[6] : date[1] === '08' ? monthNames[7] : date[1] === '09' ? monthNames[8] : date[1] === '10' ? monthNames[9] : date[1] === '11' ? monthNames[10] : date[1] === '12' ? monthNames[11] : "";
        let year = parseInt(date[0]) + 543;
        this.dateReport = `${month} ${year.toString()}`;
        this.checkMonthReport = date[1] == '02' ? 2 :
          date[1] == '04' ||
            date[1] == '06' ||
            date[1] == '09' ||
            date[1] == '11' ? 1 : 0
      } else if (param.type === 'range') {
        let date = param.date.split(",") || [];

        let date1 = date[0].split("-") || [];
        let year1 = parseInt(date1[0]) + 543;
        let date2 = date[1].split("-");
        let year2 = parseInt(date2[0]) + 543;
        this.dateReport = date1[2] + "-" + date1[1] + "-" + year1.toString() + " ~ " + date2[2] + "-" + date2[1] + "-" + year2.toString()
        console.log("datereport", this.dateReport);
      } else {
        let year = parseInt(param.date) + 543
        this.dateReport = year;
      }
    },
    headerbar(drawer) {
      this.drawer = drawer;
    },
    async genChartLineApex(cat, data) {
      return new Promise(async (resolve, reject) => {
        var options = {
          chart: {
            height: 200,
            type: "line",
            animations: {
              enabled: false,
            },
            stacked: false,
            toolbar: {
              show: false,
            },
            zoom: {
              enabled: true,
            },
          },
          markers: {
            size: 4,
          },
          plotOptions: {
            bar: {
              horizontal: false,
              borderRadius: 10,
            },
          },
          dataLabels: {
            enabled: false,
            style: {
              colors: ["#000"],
            },
            offsetX: 0,
            offsetY: -10,
            background: {
              enabled: false,
            },
          },
          colors: ["#008000", "#d4a823", "#f92525"],
          series: data,
          xaxis: {
            categories: cat,
          },
          yaxis: {
            title: {
              text: "$ (thousands)",
            },
          },
          fill: {
            opacity: 1,
          },
          tooltip: {
            y: {
              formatter: function (val) {
                return "$ " + val + " thousands";
              },
            },
          },
        };
        var chart = new ApexCharts(document.querySelector("#chartLine"), options);
        chart.render().then(() => {
          chart.dataURI().then(({ imgURI, blob }) => {
            //Here shows error
            console.log(imgURI)
            this.imgURI = imgURI;
          });
        });
        resolve({
          status: "success",
        });
      });
    },
    async genChartPieApex(cat, data) {
      return new Promise(async (resolve, reject) => {
        var options = {
          chart: {
            type: "pie",
            width: "300",
            animations: {
              enabled: false,
            },

          },
          legend: {
            show: false,
            labels: {

              colors: "#ffff",
              useSeriesColors: false,
            },
          },
          series: data,
          labels: cat,
        };

        var chart = new ApexCharts(document.querySelector("#chartLine"), options);
        chart.render().then(() => {
          chart.dataURI().then(({ imgURI, blob }) => {
            //Here shows error
            //this.imgPie = imgURI;
            console.log("PIE", imgURI);
            // if(this.exportAdmin === true){
            //   this.genPDFAdmin();
            // }else{
            //   this.genPDF();
            // }
          });
          resolve({
            status: "success",
          });
        });


      });
    },
    async genChartPie(data) {

      return new Promise(async (resolve, reject) => {

        var chart = am4core.create("chartPie", am4charts.PieChart);
        data[0].color = am4core.color("#ED1C24")
        data[1].color = am4core.color("#235789")
        data[2].color = am4core.color("#F1D302")
        data[3].color = am4core.color("#020100")
        data[4].color = am4core.color("#eb8334")
        data[5].color = am4core.color("#34eb4c")
        data[6].color = am4core.color("#34e8eb")
        data[7].color = am4core.color("#9634eb")
        data[8].color = am4core.color("#eb34cc")
        chart.data = data
        //console.log(this.dataExport.dataPieChart);
        var pieSeries = chart.series.push(new am4charts.PieSeries());
        pieSeries.dataFields.value = "volume";
        pieSeries.dataFields.category = "car_type";
        pieSeries.slices.template.propertyFields.fill = "color";

        chart.legend = new am4charts.Legend();
        pieSeries.hiddenInLegend = true;
        var options = chart.exporting.getFormatOptions("png");
        options.keepTainted = false;
        chart.exporting.setFormatOptions("png", options);

        //chart.exporting.export("png");
        this.imgPie = await chart.exporting.getImage("png");

        resolve({
          status: "success",
        });

        // });
        // });
      })
    },
    async genChartBar(data) {
      return new Promise(async (resolve, reject) => {

        var chart = am4core.create("chartBar", am4charts.XYChart);
        data[0].color = am4core.color("#ED1C24")
        data[1].color = am4core.color("#235789")
        data[2].color = am4core.color("#F1D302")
        data[3].color = am4core.color("#020100")
        data[4].color = am4core.color("#eb8334")
        data[5].color = am4core.color("#34eb4c")
        data[6].color = am4core.color("#34e8eb")
        data[7].color = am4core.color("#9634eb")
        data[8].color = am4core.color("#eb34cc")
        // Add data
        chart.data = data
        // Create axes
        let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
        categoryAxis.dataFields.category = "car_type";
        // categoryAxis.renderer.grid.template.location = 0;
        // categoryAxis.renderer.minGridDistance = 200;

        let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

        // Create series
        var series = chart.series.push(new am4charts.ColumnSeries());
        series.dataFields.valueY = "volume";
        series.dataFields.categoryX = "car_type";
        series.columns.template.propertyFields.fill = "color";
        //series.name = "volume";


        var options = chart.exporting.getFormatOptions("png");
        options.keepTainted = true;
        chart.exporting.setFormatOptions("png", options);
        this.imgBar = await chart.exporting.getImage("png");

        resolve({
          status: "success",
        });

      });


    },
    async genChartBarApex(cat, data) {

      return new Promise(async (resolve, reject) => {
        let img = '';
        var options = {
          series: [{
            data: data
          }],
          chart: {
            height: 350,
            type: 'bar',
            events: {
              click: function (chart, w, e) {
                // console.log(chart, w, e)
              }
            }
          },
          // colors: colors,
          plotOptions: {
            bar: {
              columnWidth: '45%',
              distributed: true,
            }
          },
          dataLabels: {
            enabled: false
          },
          legend: {
            show: false
          },
          xaxis: {
            categories: cat,
            labels: {
              style: {
                // colors: colors,
                fontSize: '12px'
              }
            }
          }
        };

        var chart = new ApexCharts(document.querySelector("#chartBar"), options);
        chart.render().then(() => {
          chart.dataURI().then(({ imgURI, blob }) => {
            //Here shows error
            img = imgURI;
            console.log(img);
            resolve({
              status: "success",
              data: img
            });
          });

        });


      });
    },
  },
  mounted() {

    // let car_type ={
    //             "volume": [
    //                 {
    //                     "car_type": "รถ SUV",
    //                     "volume": 51298
    //                 },
    //                 {
    //                     "car_type": "รถจักรยานยนต์",
    //                     "volume": 352490
    //                 },
    //                 {
    //                     "car_type": "รถตู้",
    //                     "volume": 1154
    //                 },
    //                 {
    //                     "car_type": "รถบรรทุก",
    //                     "volume": 14621
    //                 },
    //                 {
    //                     "car_type": "รถบรรทุกขนาดเล็ก",
    //                     "volume": 0
    //                 },
    //                 {
    //                     "car_type": "รถยนต์ส่วนบุคคล",
    //                     "volume": 112547
    //                 },
    //                 {
    //                     "car_type": "รถสามล้อเครื่อง",
    //                     "volume": 5505
    //                 },
    //                 {
    //                     "car_type": "รถโดยสาร",
    //                     "volume": 4892
    //                 },
    //                 {
    //                     "car_type": "อื่นๆ",
    //                     "volume": 3823
    //                 }
    //             ],
    //             "percent": [
    //                 {
    //                     "car_type": "รถ SUV",
    //                     "percent": 9.389563084582578
    //                 },
    //                 {
    //                     "car_type": "รถจักรยานยนต์",
    //                     "percent": 64.51961268830195
    //                 },
    //                 {
    //                     "car_type": "รถตู้",
    //                     "percent": 0.2112276462943642
    //                 },
    //                 {
    //                     "car_type": "รถบรรทุก",
    //                     "percent": 2.676221331429722
    //                 },
    //                 {
    //                     "car_type": "รถบรรทุกขนาดเล็ก",
    //                     "percent": 0.0
    //                 },
    //                 {
    //                     "car_type": "รถยนต์ส่วนบุคคล",
    //                     "percent": 20.60055277945564
    //                 },
    //                 {
    //                     "car_type": "รถสามล้อเครื่อง",
    //                     "percent": 1.0076327494371535
    //                 },
    //                 {
    //                     "car_type": "รถโดยสาร",
    //                     "percent": 0.8954295023154504
    //                 },
    //                 {
    //                     "car_type": "อื่นๆ",
    //                     "percent": 0.6997602181831494
    //                 }
    //             ]
    //         }


    //         let apex_pie = []
    //         let apex_cat = []

    //         for (let index = 0; index < car_type.volume.length; index++) {

    //           //console.log(car_type.volume[index])  
    //           apex_pie.push(car_type.volume[index].volume)
    //           apex_cat.push(car_type.volume[index].car_type)
    //          //s apex_pie.push(car_type.volume[index].volume)


    //         }
    //console.log(car_type.volume);

    // console.log(apex_cat,apex_pie);
    //this.genChartPieApex(apex_cat,apex_pie)

    // this.genChartPie(car_type.volume)
    // this.genChartBarApex(apex_cat,apex_pie)
  }
};
</script>
<style scoped>
@import "../assets/css/background.css";

/* .headertext {
  font-weight: 600;
  font-size: 24px;
  color: #ffffff;
} */
.sltime {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  width: 150px;
}

.sl {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  width: 300px;
}

.sl-mobile {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
}

.textSR {
  font-weight: 700;
  font-size: 20px;
  color: #02754B;
  text-align: center;
  background-color: white;
  width: 200px;
  display: block;
  border-radius: 15px;
}

.textSR-mobile {
  font-weight: 700;
  font-size: 20px;
  color: #02754B;
  text-align: center;
  background-color: white;
  display: block;
  border-radius: 15px;
}

.card-mobile {
  border-radius: 15px !important;
  font-weight: 700;
  font-size: 20px;
  color: #02754B;
  text-align: center;
}

/* .headertext-mobile{
    font-weight: 600;
    font-size: 18px;
    color: #FFFFFF;
} */
</style>
