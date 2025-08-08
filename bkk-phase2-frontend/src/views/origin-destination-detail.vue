<template>
  <v-app id="bg" >
     <sidebar :sideNav="drawer" ></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="onProgress">
      <v-progress-circular
        indeterminate
        size="64"
      ></v-progress-circular>
    </v-overlay>
    <v-content class="pl-3" >
      <v-container class="pl-1 pr-1">
        <v-chip :disabled="disableBack" @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
     <v-icon large color="red">mdi-chevron-left</v-icon>
         <span class="text-left headerback">Back</span>
    </v-chip>
        <v-chip v-if="$vuetify.breakpoint.width > 750" large class="ma-2" color="#02754B">
          <span  class="pl-5 pr-5 headertext">ข้อมูลแสดงจุดต้นทาง/ปลายทางของยานพาหนะ</span>
        </v-chip>  
        <v-chip v-else large class="ma-2" color="#02754B">
         <span  class="pl-5 pr-5 headertext-mobile">ข้อมูลแสดงจุดต้นทาง/ปลายทาง<br/>ของยานพาหนะ</span>
        </v-chip>      
          <v-container  v-if="$vuetify.breakpoint.width > 1904">
                  <v-layout justify-center class="pb-3">
        <v-flex >
          <v-card height="100%" class="elevation-0 pa-3 text-center" id="bg-card"><span class="text-style">{{dataFilter.date}}</span></v-card>
        </v-flex>
        
        
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex lg6>
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col height="100%"  class="pr-0"><span class="title-style">จังหวัด:</span></v-col>
              <v-col height="100%"  class="pr-0"><span class="text-style">{{dataFilter.province}}</span></v-col>
              <!-- <v-divider vertical class="ma-2"></v-divider>
              <v-col height="100%"  class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col height="100%" cols="2" class="text-right"><span class="text-style"></span></v-col
              ><v-col height="100%" cols="2" class="text-right">
                <span class="title-style">คัน</span>
              </v-col> -->
            </v-row>
          </v-card>
        </v-flex>
        <v-flex lg6 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col height="100%" class="pr-0"><span class="title-style">ประเภทยานพาหนะ:</span></v-col>
              <v-col height="100%"  class="pr-0"><span class="text-style">{{dataFilter.vehicle_type}}</span></v-col>
              <!-- <v-divider vertical class="ma-2"></v-divider>
              <v-col height="100%" class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col height="100%" cols="2" class="text-right"> <span class="text-style"></span></v-col>
              <v-col height="100%" cols="2" class="text-right">
                <span class="title-style">คัน</span>
              </v-col> -->
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>

      <v-layout child-flex class="pt-3">
      <v-data-table 
      :headers="headers" 
      :items="dataTable" 
      id="table-vehicle" 
      :hide-default-footer="true"
      loading-text="Loading"
      :loading="loading"
      :items-per-page="20"
      >
        <!-- <template v-slot:[`header.id`]="{ header }">
          <span>{{ header.text }}</span>
        </template> -->
        <template v-slot:[`header.picLicense`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.license`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.province`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.type`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.color`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.date`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.destination`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
         <template v-slot:[`header.note`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
        <template v-slot:item="props">
          <tr>
            <td class="text-center"><span style="font-size:20px;">{{ props.item.index}}</span></td>
            <!-- <td class="text-center"><img width="50" :src="props.item.picture"></td> -->
            <td class="text-center"><span style="font-size:20px;">{{ props.item.plate_no }}</span></td>
            <td class="text-center"><span style="font-size:20px;">{{ props.item.province }}</span></td>
            <td class="text-center"><span style="font-size:20px;">{{ props.item.type }}</span></td>
            <td class="text-center"><span style="font-size:20px;">{{ props.item.color }}</span></td>
            <td class="text-center"><span style="font-size:20px;">{{ props.item.date }}</span></td>
            <td class="text-center"><span style="font-size:20px; color:green;">{{ props.item.time }}</span> ครั้ง</td>
            <td  class="text-center">
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
        <v-flex >
          <v-card class="elevation-0 pa-3 text-center" id="bg-card"><span class="text-style">{{dataFilter.date}}</span></v-card>
        </v-flex>
        
        
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex lg6>
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col  class="pr-0"><span class="title-style">จังหวัด:</span></v-col>
              <v-col  class="pr-0"><span class="text-style">{{dataFilter.province}}</span></v-col>
              <!-- <v-divider vertical class="ma-2"></v-divider>
              <v-col cols="2" class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col cols="2" class="text-right"> <span class="text-style"></span></v-col
              ><v-col class="text-right">
                <span class="title-style">คัน</span>
              </v-col> -->
            </v-row>
          </v-card>
        </v-flex>
        <v-flex lg6 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col  class="pr-0"><span class="title-style">ประเภทยานพาหนะ:</span></v-col>
              <v-col  class="pr-0"><span class="text-style">{{dataFilter.vehicle_type}}</span></v-col>
              <!-- <v-divider vertical class="ma-2"></v-divider>
              <v-col class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col cols="2" class="text-right"> <span class="text-style"></span></v-col>
              <v-col cols="2" class="text-right">
                <span class="title-style">คัน</span>
              </v-col> -->
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>

       <v-layout child-flex class="pt-3" >
      <v-data-table 
      :headers="headers" 
      :items="dataTable" 
      id="table-vehicle" 
      :hide-default-footer="true"
      loading-text="Loading"
      :loading="loading"
      :items-per-page="20"
      >
        <!-- <template v-slot:[`header.id`]="{ header }">
          <span>{{ header.text }}</span>
        </template> -->
        <template v-slot:[`header.picLicense`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.license`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.province`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.type`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.color`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.date`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.destination`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.note`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
        <template v-slot:item="props">
          <tr>
            <td class="text-center">{{ props.item.index}}</td>
             <!-- <td class="text-center"><img width="50" :src="props.item.picture"></td> -->
            <td class="text-center">{{ props.item.plate_no }}</td>
            <td class="text-center">{{ props.item.province }}</td>
            <td class="text-center">{{ props.item.type }}</td>
            <td class="text-center">{{ props.item.color }}</td>
            <td class="text-center">{{ props.item.date }}</td>
            <td class="text-center"><span style="color:green">{{ props.item.time }}</span> ครั้ง</td>
            <td  class="text-center">
                <v-btn text small @click="link(props.item)">
                  <v-icon>mdi-information-outline</v-icon>
                </v-btn>
            </td>
          </tr>
        </template>
      </v-data-table>
    </v-layout>
    </v-container>
    <v-container  v-else>
            <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3 text-center" id="bg-card"><span class="text-style">{{dataFilter.date}}</span></v-card>
        </v-flex>
      </v-layout>
      
     
      <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3" id="bg-card">
           <v-row>
              <v-col class="pr-0"><span class="title-style">จังหวัด:</span></v-col>
              <v-col class="pr-0"><span class="text-style">{{dataFilter.province}}</span></v-col>
              <!-- <v-divider vertical class="ma-2"></v-divider>
              <v-col cols="2" class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col cols="2" class="text-right"> <span class="text-style"></span></v-col
              ><v-col class="text-right">
                <span class="title-style">คัน</span>
              </v-col> -->
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3" id="bg-card">
            <v-row>
              <v-col class="pr-0"><span class="title-style">ประเภทยานพาหนะ:</span></v-col>
              <v-col class="pr-0"><span class="text-style">{{dataFilter.vehicle_type}}</span></v-col>
              <!-- <v-divider vertical class="ma-2"></v-divider>
              <v-col class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col cols="2" class="text-right"> <span class="text-style"></span></v-col>
              <v-col cols="2" class="text-right">
                <span class="title-style">คัน</span>
              </v-col> -->
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>

              <v-layout child-flex class="pt-3">
      <v-data-table 
      :headers="headers" 
      :items="dataTable" 
      id="table-vehicle" 
      :hide-default-footer="true"
      loading-text="Loading"
      :loading="loading"
      :items-per-page="20"
      >
        <!-- <template v-slot:[`header.id`]="{ header }">
          <span>{{ header.text }}</span>
        </template> -->
        <template v-slot:[`header.picLicense`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.license`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.province`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.type`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.color`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.date`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.destination`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
         <template v-slot:[`header.note`]="{ header }">
          <span>{{ header.text }}</span>
        </template>

        <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
        <template v-slot:item="props">
          <tr>
            <td class="text-center">{{ props.item.index }}</td>
            <!-- <td class="text-center"><img width="50" :src="props.item.picture"></td> -->
            <td class="text-center">{{ props.item.plate_no }}</td>
            <td class="text-center">{{ props.item.province }}</td>
            <td class="text-center">{{ props.item.type }}</td>
            <td class="text-center">{{ props.item.color }}</td>
            <td class="text-center">{{ props.item.date }}</td>
            <td class="text-center"><span style="color:green">{{ props.item.time }}</span> ครั้ง</td>
            <td  class="text-center">
                <v-btn text small @click="link(props.item)">
                  <v-icon>mdi-information-outline</v-icon>
                </v-btn>
            </td>
          </tr>
        </template>
      </v-data-table>
    </v-layout>
    </v-container>
    <v-pagination class="pt-3" v-model="pagination.page" :length="pagination.total" :total-visible="pagination.visible"  @input="next"></v-pagination>
     <v-layout>
         <!-- <exportfile class="pt-6 pr-3" @downloadEx="genEX" :keypage="keypage" @download="generateReport"  :title="titletext"></exportfile> -->
     </v-layout>
        </v-container>
      
    </v-content>

    <!-- <searchOriginDespdf :downloadpdf="downloadpdf" :downloadexcel="downloadexcel"></searchOriginDespdf> -->
  </v-app>
</template>
<script>
  const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
// import searchdetail from "../components/search-detail-table.vue";
import exportfile from "../components/export-file.vue";
import headerbar from "../components/header-bar.vue";
import searchOriginDespdf from "../formatExport/reportOriginDesPDF.vue";
import Swal from "sweetalert2/dist/sweetalert2.js";
const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});

import "jspdf-autotable";
import fontTH from "../fontTH.js";
export default {
  components: {
    sidebar,
    searchOriginDespdf,
    exportfile,
    headerbar,
  },
  data() {
    return {
      pagination: {
        page: 1,
        total: 15,
        perPage: 20,
        visible:7
      },

      titletext:"รถบรรทุกในช่วงเวลาที่ห้ามเดินรถ",
      downloadpdf:false,
      onProgress: false,
      downloadexcel:false,
      keypage:"allsensor",
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
          text: "ลำดับ",
          align: "center",
          sortable: false,
          value: "id",
          
        },
        //  {
        //   text: "ป้ายทะเบียนยานพาหนะ",
        //   align: "center",
        //   sortable: false,
        //   value: "picLicense",
        // },
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
        { text: "destination", align: "center", sortable: false, value: "time" },
        { text: "รายละเอียด", align: "center", sortable: false, value: "note" },
      ],
      dataTable: [],
      disableBack:false,
      loading: false,
      dataFilter:{}
    };
  },
  computed: {
    headerTable() {
      return "color:#2962FF ;" + "font-weight: 600; font-size:15px;";
    },
  },
  methods: {
    genEX(){
      this.downloadexcel = !this.downloadexcel
    },
    generateReport(){
      this.downloadpdf = !this.downloadpdf
    },
    gobackpage(){
      this.$router.push("/origin-destination");
    },

    next (page){
     
      this.$route.query.page = page
      this.dataTable = [];
      this.getDataDestination()
    },
    headerbar(drawer){
      console.log("hhh",drawer);
      this.drawer = drawer;
    },
    link(item) {
        // const dataQuery = this.$route.query
        //       let param ={
        //          'date': dataQuery.date,
        //          'time': dataQuery.date,
        //          'point': dataQuery.checkpoint || "-",
        //          'direction' : dataQuery.direction === "inbound" ? "ขาเข้า" : dataQuery.direction === "outbound"? "ขาออก":"-",
        //          'province': dataQuery.province || "-",
        //          'carType': dataQuery.vehicle_type || "-",
        //          'color': dataQuery.vehicle_color || "-",
        //          'plate_no': dataQuery.plate_no || "-",
        //       }
        
        item['date_payload'] = this.$route.query.date
        item['provine_payload'] = this.$route.query.province
        item['vehicle_type_payload'] = this.$route.query.vehicle_type
  
          this.$router.push({path:'/origin-destination-detail-table', query:item});
    
        
      },

      getDataDestination(){
       
         const data_query = this.$route.query;
     
         let session_data = localStorage.getItem("session");
         let url = baseUrl.ipServer + "/vehicle-destination-times";
         this.loading = true
         this.axios
        .get(url, {
          headers: { session: session_data },
          params: data_query,
        })
         .then((response) => {
          if (response.status === 200) {
            this.loading = false
            this.dataTable = [];
            for (let i = 0; i < response.data.data.records.length; i++) {
              let data = {}
               data["index"] = i + 1
              data["plate_no"] = response.data.data.records[i]['plate_no']
              data["province"] = response.data.data.records[i]["province"]
              data["type"] = response.data.data.records[i]["type"]
              data["color"] = response.data.data.records[i]["color"]
              // data["time"] = response.data.data.records[i]["times"]
              data["time"] = response.data.data.records[i]["times"] - 1
              data["date"] =  this.setDateReport(data_query.date)
              this.dataTable.push(data)
            }

             
            this.dataFilter = {         
              'date': this.setDateReport(data_query.date),
              'province': data_query.province || "-",
              'vehicle_type': data_query.vehicle_type || "-",
            }

            console.log(this.dataFilter);

            //pagination
            this.pagination.total = response.data.page_total
          }
          else {
             this.loading = false
             Toast.fire({
          icon: 'error',
          title: 'Cannot connet API',     
        })
          }
        })
        .catch((error) => {
           this.loading = false
        //   if(error.response.data.message === 'session timeout'){
        //     this.$store.dispatch("logout");
        //     this.$router.push('/')
        //      Toast.fire({
        //       icon: "error",
        //       title: error.response.data.message,
        //     });

        //     return;
        // }
        console.log(error);
           Toast.fire({
          icon: 'error',
          title: 'Cannot connet API',     
        })
      })
      

 


  },
 
        setDateReport(param) {
     console.log(param);
      if(param !== {}){
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
      
      let date = param.split("-") || "";
      let month = date[1] === '01' ? monthNames[0] : date[1] === '02' ? monthNames[1] : date[1] === '03' ? monthNames[2] : date[1] === '04' ? monthNames[3] : date[1] === '05' ? monthNames[4] : date[1] === '06' ? monthNames[5] : date[1] === '07' ? monthNames[6] : date[1] === '08' ? monthNames[7] : date[1] === '09' ? monthNames[8] : date[1] === '10' ? monthNames[9] : date[1] === '11' ? monthNames[10] : date[1] === '12' ? monthNames[11] : "";    
      let year = parseInt(date[0])+543;
     
      // let dateformat = new Date(param).toLocaleDateString('th-TH', {year: 'numeric', month: 'long', day:'numeric'})
      console.log(`${date[2]}   ${month} ${year.toString()}`);
      return `${date[2]} ${month} ${year.toString()}`;
     
    }
    },

  },
  mounted() {
   this.getDataDestination()
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
.headerback{
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
    font-size: 15px;
    color: #FFFFFF;
} */
#table-vehicle table thead tr th:nth-child(1){background-color: #02754B; color: white; font-size: 18px; min-width:150px;}
#table-vehicle table thead tr th:nth-child(2){background-color: #02754B; color: white; font-size: 18px; min-width:150px;}
#table-vehicle table thead tr th:nth-child(3){background-color: #02754B; color: white; font-size: 18px; min-width:100px;}
#table-vehicle table thead tr th:nth-child(4){background-color: #02754B; color: white; font-size: 18px; min-width:150px;}
#table-vehicle table thead tr th:nth-child(5){background-color: #02754B; color: white; font-size: 18px; min-width:100px;}
#table-vehicle table thead tr th:nth-child(6){background-color: #02754B; color: white; font-size: 18px; min-width:150px;}
#table-vehicle table thead tr th:nth-child(7){background-color: #02754B; color: white; font-size: 18px; min-width:100px;}
#table-vehicle table thead tr th:nth-child(8){background-color: #02754B; color: white; font-size: 18px; min-width:100px;}
#table-vehicle table thead tr th:nth-child(9){background-color: #02754B; color: white; font-size: 18px; min-width:100px;}
#table-vehicle table thead tr th:nth-child(10){background-color: #02754B; color: white; font-size: 18px; min-width:100px;}
#table-vehicle table thead tr th:nth-child(11){background-color: #02754B; color: white; font-size: 18px; min-width:100px;}
#table-vehicle table thead tr th:nth-child(12){background-color: #02754B; color: white; font-size: 18px; min-width:100px;}
#table-vehicle table thead tr th:nth-child(13){background-color: #02754B; color: white; font-size: 18px; min-width:100px;}
#table-vehicle table thead tr th:nth-child(14)
  {background-color: #02754B; color: white; font-size: 18px;}

  #table-vehicle table tbody tr:nth-child(odd) {background-color: #ddf1fc;}

</style>
