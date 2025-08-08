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
          <v-container  v-if="$vuetify.breakpoint.width > 1024">
        <v-layout  class="pb-3">
        <v-flex lg4 >
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row
              ><v-col >
                <span class="title-style">เลขทะเบียนยานพาหนะ:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.plate_no}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
        <v-flex lg4 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col >
                <span class="title-style">จังหวัด:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.province}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
        <v-flex lg4 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
           <v-row>
              <v-col height="100%"  class="pr-0"><span class="title-style">ประเภทยานพาหนะ:</span></v-col>
              <v-col height="100%"  class="pr-0"><span class="text-style">{{dataFilter.vehicle_type}}</span></v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
       
      <v-layout class="pb-3">
       
        <v-flex lg4 >
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
             <v-row>
              <v-col  class="pr-0"><span class="title-style">สียานพาหนะ:</span></v-col>
              <v-col  class="pr-0"><span class="text-style">{{dataFilter.vehicle_color}}</span></v-col>
            </v-row>
          </v-card>
        </v-flex>
         <v-flex lg4 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col height="100%"  class="pr-0"><span class="title-style">วัน/เดือน/ปี:</span></v-col>
              <v-col height="100%" class="pr-0"><span class="text-style">{{dataFilter.date}}</span></v-col>
            </v-row>
          </v-card>
        </v-flex>
        <v-flex lg4 class="pl-3">
          <v-card height="100%" class="elevation-0 pa-3" id="bg-card">
            <v-row>
              <v-col height="100%" class="pr-0"><span class="title-style">destination:</span></v-col>
              <v-col height="100%" class="pr-0"><span class="text-style">{{dataFilter.destination }}</span><span class="title-style"> ครั้ง</span></v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout child-flex class="pt-3">
      <v-data-table 
      :headers="headers" 
      :items="dataTable" 
      id="table-vehicle" 
      :hide-default-footer="false"
      loading-text="Loading"
      :loading="loading"
      :items-per-page="20"
      >
        <template v-slot:[`header.plate_picture`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.timeStart`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.locationStart`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.directionStart`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.timeEnd`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.locationEnd`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.directionEnd`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.timeAll`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
         <template v-slot:[`header.note`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
        <template v-slot:item="props">
          <tr>
            <td class="text-center"><img width="50" :src="props.item.plate_picture"></td>
            <td class="text-center"><span style="font-size:20px;">{{ props.item.start_time }}</span></td>
            <td class="text-center"><span style="font-size:20px;">{{ props.item.origin }}</span></td>
            <td class="text-center"><span style="font-size:20px;">{{ props.item.origin_direction }}</span></td>
            <td class="text-center"><span style="font-size:20px;">{{ props.item.end_time }}</span></td>
            <td class="text-center"><span style="font-size:20px;">{{ props.item.destination }}</span></td>
            <td class="text-center"><span style="font-size:20px;">{{ props.item.destination_direction }}</span></td>
            <td  class="text-center"><span style="font-size:20px;">{{props.item.diff_time}}</span></td>
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
    <v-container v-else-if="$vuetify.breakpoint.width < 1024 && $vuetify.breakpoint.width > 750">
    <v-layout justify-center class="pb-3">
        <v-flex lg6 >
          <v-card class="elevation-0 pa-3" id="bg-card">
            <v-row
              ><v-col >
                <span class="title-style">เลขทะเบียนยานพาหนะ:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.plate_no}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
        <v-flex lg6 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col >
                <span class="title-style">จังหวัด:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.province}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex lg6>
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col class="pr-0"><span class="title-style">ประเภทยานพาหนะ:</span></v-col>
              <v-col  class="pr-0"><span class="text-style">{{dataFilter.vehicle_type}}</span></v-col>
            </v-row>
          </v-card>
        </v-flex>
        <v-flex lg6 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col class="pr-0"><span class="title-style">สียานพาหนะ:</span></v-col>
              <v-col class="pr-0"><span class="text-style">{{dataFilter.vehicle_color}}</span></v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex lg6>
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col  class="pr-0"><span class="title-style">วัน/เดือน/ปี:</span></v-col>
              <v-col  class="pr-0"><span class="text-style">{{dataFilter.date}}</span></v-col>
            </v-row>
          </v-card>
        </v-flex>
        <v-flex lg6 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col  class="pr-0"><span class="title-style">destination:</span></v-col>
              <v-col  class="pr-0"><span class="text-style">{{dataFilter.destination}}</span><span class="title-style"> ครั้ง</span></v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
       <v-layout child-flex class="pt-3" >
      <v-data-table 
      :headers="headers" 
      :items="dataTable" 
      id="table-vehicle" 
      :hide-default-footer="false"
      loading-text="Loading"
      :loading="loading"
      :items-per-page="20"
      >
        <template v-slot:[`header.plate_picture`]="{ header }" min-width="100px">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.timeStart`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.locationStart`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.directionStart`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.timeEnd`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.locationEnd`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.directionEnd`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.timeAll`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.note`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
        <template v-slot:item="props">
          <tr>
            <td class="text-center"><img width="50" :src="props.item.plate_picture"></td>
            <td class="text-center">{{ props.item.start_time }}</td>
            <td class="text-center">{{ props.item.origin }}</td>
            <td class="text-center">{{ props.item.origin_direction }}</td>
            <td class="text-center">{{ props.item.end_time }}</td>
            <td class="text-center">{{ props.item.destination }}</td>
            <td class="text-center">{{ props.item.destination_direction}}</td>
            <td  class="text-center">{{props.item.diff_time}}</td>
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
          <v-card class="elevation-0 pa-3 text-center" id="bg-card"><span class="text-style">-</span></v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3" id="bg-card" >
            <v-row
              ><v-col >
                <span class="title-style">เลขทะเบียนยานพาหนะ:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.plate_no}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3" id="bg-card">
            <v-row>
              <v-col >
                <span class="title-style">จังหวัด:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.province}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3" id="bg-card">
            <v-row>
              <v-col >
                <span class="title-style">ประเภทยานพาหนะ:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.vehicle_type}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3" id="bg-card">
            <v-row>
              <v-col >
                <span class="title-style">สียานพาหนะ:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.vehicle_color}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3" id="bg-card">
            <v-row>
              <v-col >
                <span class="title-style">วัน/เดือน/ปี:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.date}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
       <v-flex>
          <v-card class="elevation-0 pa-3" id="bg-card">
            <v-row>
              <v-col >
                <span class="title-style">destination:</span> </v-col
              ><v-col>
                <v-col  class="pr-0"><span class="text-style">{{dataFilter.destination}}</span><span class="title-style"> ครั้ง</span></v-col>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
              <v-layout child-flex class="pt-3">
      <v-data-table 
      :headers="headers" 
      :items="dataTable" 
      id="table-vehicle" 
      :hide-default-footer="false"
      loading-text="Loading"
      :loading="loading"
      :items-per-page="20"
      >
        <template v-slot:[`header.plate_picture`]="{ header }" >
          <span>{{ header.text }}</span>
        </template>
        
<template v-slot:[`header.timeStart`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.locationStart`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.directionStart`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.timeEnd`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.locationEnd`]="{ header }">
          <span>{{ header.text}}</span>
        </template>
        <template v-slot:[`header.directionEnd`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
        <template v-slot:[`header.timAll`]="{ header }">
          <span>{{ header.text }}</span>
        </template>
         <template v-slot:[`header.note`]="{ header }">
          <span>{{ header.text }}</span>
        </template>

        <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
        <template v-slot:item="props">
          <tr>
            <td class="text-center"><img width="50" :src="props.item.plate_picture"></td>
            <td class="text-center">{{ props.item.start_time }}</td>
            <td class="text-center">{{ props.item.origin }}</td>
            <td class="text-center">{{ props.item.origin_direction}}</td>
            <td class="text-center">{{ props.item.end_time }}</td>
            <td class="text-center">{{ props.item.destination }}</td>
            <td class="text-center">{{ props.item.destination_direction }}</td>
            <td  class="text-center">{{props.item.diff_time}}</td>
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
    <!-- <v-pagination class="pt-3" v-model="pagination.page" :length="pagination.total" :total-visible="pagination.visible" ></v-pagination> -->
     <v-layout>
         <exportfile class="pt-6 pr-3" @downloadEx="genEX" :keypage="keypage" @download="generateReport"  :title="titletext"></exportfile>
     </v-layout>
        </v-container>
      <detail :show="opendetail" @close="opendetail=false" :data="detailData" :dataFilter="dataFilter" :base64_plate_pic="base64_plate_pic" :base64_image_pic="base64_image_pic" :reportOther="reportOther"></detail>
    </v-content>
    
    <searchOriginDespdf :downloadpdf="downloadpdf" :downloadexcel="downloadexcel" :dataTableRe="dataReport"></searchOriginDespdf>
  </v-app>
</template>
<script>
  const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
// import searchdetail from "../components/search-detail-table.vue";
import exportfile from "../components/export-file.vue";
import headerbar from "../components/header-bar.vue";
import searchOriginDespdf from "../formatExport/reportOriginDesPDF.vue";
import detail from "../components/origin-destination-detail.vue";

import "jspdf-autotable";
import fontTH from "../fontTH.js";
export default {
  components: {
    sidebar,
    searchOriginDespdf,
    exportfile,
    headerbar,
    detail
  },
  data() {
    return {
      pagination: {
        page: 1,
        total: 15,
        perPage: 20,
        visible:7
      },
      opendetail:false,
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
          value: "plate_picture",
        },
        { text: "เวลาเริ่มต้น", align: "center", sortable: false, value: "timeStart" },
        { text: "สถานที่เริ่มต้น", align: "center", sortable: false, value: "locationStart" },
        { text: "ทิศทางการจราจร", align: "center", sortable: false, value: "directionStart" },
         { text: "เวลาปลายทาง", align: "center", sortable: false, value: "timeEnd" },
        { text: "สถานที่ปลายทาง", align: "center", sortable: false, value: "locationEnd" },
        { text: "ทิศทางการจราจร", align: "center", sortable: false, value: "directionEnd" },
        { text: "เวลาที่ใช้ในการเดินทางจากจุดเริ่มต้นถึงจุดปลายทาง", align: "center", sortable: false, value: "timeAll" },
         { text: "รายละเอียด", align: "center", sortable: false, value: "note" },
      ],
      dataTable: [
        {
          id:'',
          locationStart:'data',
          directionStart:'data',
          timeStart:'data',
          locationEnd:'data',
          directionEnd:'data',
          timeAll:'data',
          note:'link',
        }
      ],
      disableBack:false,
      loading: false,
      dataFilter:{},
      detailData:{},
      dataReport:[],
      base64_plate_pic:'',
      base64_image_pic:'',
      reportOther:{}
    };
  },
  computed: {
    headerTable() {
      return "color:#2962FF ;" + "font-weight: 600; font-size:15px;";
    },
  },
  methods: {
       async getReport(){
       return new Promise(async(resolve, reject) => {
       let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/vehicle-destination-list/report";
      let data = {
        date:this.$route.query["date_payload"],
        plate_no:this.$route.query["plate_no"],
        province:this.$route.query["province"],
        vehicle_type:this.$route.query["type"],
        vehicle_color:this.$route.query["color"],
      }
      this.dataReport = []
      this.axios.get(url, {headers: { session: session_data },params: data})
      .then((response) => {
        //  console.log(response);
        let isPublic = 0
        let checkImgIsvalid = 0
        if(baseUrl.pathImg === "110.171.165.57"){
          isPublic = 1
        }
        
          if (response.status === 200) {
             
             for (let i = 0; i < response.data.data.records.length-1; i++) {
            let data = {}
                          var start = new Date(response.data.data.records[i]["start_time"]);
              var end = new Date(response.data.data.records[i]["end_time"]);
              var diffMs = (end - start); // milliseconds between now & Christmas
              var diffDays = Math.floor(diffMs / 86400000); // days
              var diffHrs = Math.floor((diffMs % 86400000) / 3600000); // hours
              var diffMins = Math.round(((diffMs % 86400000) % 3600000) / 60000); // minutes

              
              let checkimage = response.data.data.records[i]["image_url"].includes("http:")         
              

              

              

              data["index"] = i + 1
              data["destination"] = response.data.data.records[i]['destination']
              data["destination_direction"] = response.data.data.records[i]["destination_direction"]
              data["destination_lat"] = response.data.data.records[i]['destination_lat']
              data["destination_long"] = response.data.data.records[i]["destination_long"]
              data["diff_time"] = diffHrs + " ชม. " + diffMins + " น"
              data["end_time"] = response.data.data.records[i]["end_time"].substr(11, 8) || 'None'
              data["id"] = response.data.data.records[i]["id"]
              data["image_url"] = response.data.data.records[i]["image_url"]
              data["latitude"] = response.data.data.records[i]["latitude"]
              data["longtitude"] = response.data.data.records[i]['longtitude']
              data["origin"] = response.data.data.records[i]['origin']
              data["origin_direction"] = response.data.data.records[i]["original_direction"]
              data["plate_picture"] = response.data.data.records[i]['plate_picture']
              data["start_time"] =response.data.data.records[i]["start_time"].substr(11, 8) || 'None'
              data["base64_plate_pic"] = response.data.data.records[i]['base64_plate_pic'] ?'data:image/png;base64,'+response.data.data.records[i]['base64_plate_pic'] : ''
              data["base64_image_pic"] = response.data.data.records[i]['base64_image_pic'] ?'data:image/png;base64,'+response.data.data.records[i]['base64_image_pic'] : ''
              data["user"] = response.data.data.records[i]["user"]
              data["report_date"] = this.setDateReport(response.data.data.records[i]["report_date"].substr(0, 10))
              data["department"] = response.data.data.records[i]["department"]

              this.dataReport.push(data)
             }
            
            resolve({
          status: "success",
        });
       
          }else{
            Toast.fire({
          icon: 'error',
          title: 'Cannot connet API',     
        })
          }

            resolve({
          status: "error",
        });

        
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
          resolve({
          status: "error",
        });
        });

           })
    },
   async genEX(){
     let res = await this.getReport()
         if(res.status === "success"){
         this.downloadexcel = !this.downloadexcel
      }
 
    },
    async generateReport(){
     let res = await this.getReport()
         if(res.status === "success"){
        this.downloadpdf = !this.downloadpdf
      }
 
     
      
     
    },
    gobackpage(){
       let payload = {}
        payload['date'] = this.$route.query.date_payload
        if(this.$route.query.province)
        payload['province'] = this.$route.query.province
        if(this.$route.query.vehicle_type_payload)
        payload['vehicle_type'] = this.$route.query.vehicle_type_payload
        payload['page'] = 1
      this.$router.push({path:"/origin-destination-detail", query:payload});
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
    getData() {
      
      let data = {}
      data["date"] = this.$route.query["date_payload"]
      data["plate_no"] =  this.$route.query["plate_no"]
      data["province"] =  this.$route.query["province"]
      data["vehicle_type"] =  this.$route.query["type"]
      data["time"] =  this.$route.query["time"]
      data["vehicle_color"] =  this.$route.query["color"]
     // delete data.queryPayload;
     // data["date"] = this.$route.query.queryPayload.date
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/vehicle-destination-list/list";
      this.loading = true
      this.axios
        .get(url, {
          headers: { session: session_data },
          params: data,
        })
        .then((response) => {
          if (response.status === 200) {
            this.loading = false
            this.dataTable = [];
            let isPublic = 0

            if(baseUrl.pathImg === "110.171.165.57"){
              isPublic = 1
            }
            for (let i = 0; i < response.data.data.records.length-1; i++) {
              let data = {}
              var start = new Date(response.data.data.records[i]["start_time"]);
var end = new Date(response.data.data.records[i]["end_time"]);
var diffMs = (end - start); // milliseconds between now & Christmas
var diffDays = Math.floor(diffMs / 86400000); // days
var diffHrs = Math.floor((diffMs % 86400000) / 3600000); // hours
var diffMins = Math.round(((diffMs % 86400000) % 3600000) / 60000); // minutes

              if(response.data.data.records[i]["plate_picture"] !== "None" && response.data.data.records[i]["plate_picture"] !== null){
                response.data.data.records[i]["plate_picture"] = response.data.data.records[i]["plate_picture"].replace('10.151.1.86', baseUrl.pathImg)
                response.data.data.records[i]["plate_picture"] = response.data.data.records[i]["plate_picture"].replace('10.151.1.71', baseUrl.pathImg)
                if(isPublic === 1){
                  response.data.data.records[i]["plate_picture"] = response.data.data.records[i]["plate_picture"].replace('6120', baseUrl.pathImgPort)
                  response.data.data.records[i]["plate_picture"] = response.data.data.records[i]["plate_picture"].replace('6040', baseUrl.pathImgPort)
                }
              }

              if(response.data.data.records[i]["image_url"] !== "None" && response.data.data.records[i]["image_url"] !== null){
                response.data.data.records[i]["image_url"] = response.data.data.records[i]["image_url"].replace('10.151.1.86', baseUrl.pathImg)
                response.data.data.records[i]["image_url"] = response.data.data.records[i]["image_url"].replace('10.151.1.71', baseUrl.pathImg)

                if(isPublic === 1){
                  response.data.data.records[i]["image_url"] = response.data.data.records[i]["image_url"].replace('6120', baseUrl.pathImgPort)
                  response.data.data.records[i]["image_url"] = response.data.data.records[i]["image_url"].replace('6040', baseUrl.pathImgPort)
                }
              }

              data["index"] = i + 1
              data["destination"] = response.data.data.records[i]['destination']
              data["destination_direction"] = response.data.data.records[i]["destination_direction"]
              data["destination_lat"] = response.data.data.records[i]['destination_lat']
              data["destination_long"] = response.data.data.records[i]["destination_long"]
              data["diff_time"] = diffHrs + " ชม. " + diffMins + " น"
              data["end_time"] = response.data.data.records[i]["end_time"].substr(11, 8) || 'None'
              data["id"] = response.data.data.records[i]["id"]
              data["image_url"] = response.data.data.records[i]["image_url"]
              data["latitude"] = response.data.data.records[i]["latitude"]
              data["longtitude"] = response.data.data.records[i]['longtitude']
              data["origin"] = response.data.data.records[i]['origin']
              data["origin_direction"] = response.data.data.records[i]["original_direction"]
              data["plate_picture"] = response.data.data.records[i]['plate_picture']
              data["start_time"] = response.data.data.records[i]["start_time"].substr(11, 8) || 'None'
              data["date_payload"] = this.$route.query["date_payload"]
             
              this.dataTable.push(data)
            }
             this.dataFilter = {         
              'date': this.$route.query.date|| "-",
              'province': this.$route.query.province || "-",
              'vehicle_type': this.$route.query.type || "-",
              'vehicle_color': this.$route.query.color || "-",
              'plate_no': this.$route.query.plate_no || "-",
              'destination': this.$route.query.time|| "-",
            }
            //pagination
            this.pagination.total = response.data.page_total
            // console.log( this.dataTable);
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
        });
    },
    next (page){
      //  console.log(this.$route.query.page)
      this.$route.query.page = page
     
      this.getData()
    },
    headerbar(drawer){
      console.log("hhh",drawer);
      this.drawer = drawer;
    },
    async link(item) {
        let result = await this.getReport()
         console.log(result);
            this.reportOther = {}

         for(let i = 0 ; i < this.dataReport.length ;i++){
          console.log(this.dataReport[i]);
          if(this.dataReport[i]['id'] === item['id']){
            
            this.reportOther["base64_plate_pic"] = this.dataReport[i]['base64_plate_pic']
            this.reportOther["base64_image_pic"] = this.dataReport[i]['base64_image_pic']
            this.reportOther["user"] = this.dataReport[i]['user']
            this.reportOther["department"] = this.dataReport[i]['department']
            this.reportOther["report_date"] = this.dataReport[i]['report_date']
          }
         }

        this.opendetail = true
        this.detailData = item
       
      
        
      },

      


 


  },
  mounted() {
   this.getData()
   
   
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
#table-vehicle table thead tr th:nth-child(1){background-color: #02754B; color: white; font-size: 18px;min-width:70px;}

 #table-vehicle table thead tr th:nth-child(2){background-color: #02754B; color: white; font-size: 18px;min-width:100px;}
  #table-vehicle table thead tr th:nth-child(3){background-color: #02754B; color: white; font-size: 18px;min-width:100px;}
  #table-vehicle table thead tr th:nth-child(4){background-color: #02754B; color: white; font-size: 18px;min-width:150px;}
  #table-vehicle table thead tr th:nth-child(5){background-color: #02754B; color: white; font-size: 18px;min-width:120px;}
  #table-vehicle table thead tr th:nth-child(6){background-color: #02754B; color: white; font-size: 18px;min-width:150px;}
  #table-vehicle table thead tr th:nth-child(7){background-color: #02754B; color: white; font-size: 18px;min-width:150px;}
   #table-vehicle table thead tr th:nth-child(8){background-color: #02754B; color: white; font-size: 18px;min-width:250px;}
  #table-vehicle table thead tr th:nth-child(9){background-color: #02754B; color: white; font-size: 18px;min-width:100px;}
   #table-vehicle table thead tr th:nth-child(10){background-color: #02754B; color: white; font-size: 18px;min-width:100px;}
  #table-vehicle table thead tr th:nth-child(11){background-color: #02754B; color: white; font-size: 18px;min-width:100px;}
   #table-vehicle table thead tr th:nth-child(12){background-color: #02754B; color: white; font-size: 18px;min-width:100px;}
  #table-vehicle table thead tr th:nth-child(13){background-color: #02754B; color: white; font-size: 18px;min-width:100px;}
  #table-vehicle table thead tr th:nth-child(14)
  {background-color: #02754B; color: white; font-size: 18px;min-width:150px;}

  #table-vehicle table tbody tr:nth-child(odd) {background-color: #ddf1fc;}

</style>
