<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="onProgress">
      <v-progress-circular
        indeterminate
        size="64"
      ></v-progress-circular>
    </v-overlay>
    <v-content  class="pl-3" >
      <v-container class="pl-1 pr-1">
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">ข้อมูลยานพาหนะที่กำหนด</span>
        </v-chip>
        <v-container>
          <v-layout child-flex class="pt-5" v-if="$vuetify.breakpoint.width > 1904">
            <v-data-table :headers="headers" :items="desserts" id="table-vehicle" :hide-default-footer="true" :items-per-page="20">
              <!-- <template v-slot:[`header.id`]="{ header }">
                <span>{{ header.text }}</span>
              </template> -->
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
              <!-- <template v-slot:[`header.time`]="{ header }">
                <span>{{ header.text }}</span>
              </template> -->

              <template v-slot:[`header.note`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.actions`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                  <!-- <td class="text-center"><span style="font-size:20px;">{{ props.item.id }}</span></td> -->
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.license }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.province }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.type }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.color }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.date }}</span></td>
                  <!-- <td class="text-center"><span style="font-size:20px;">{{ props.item.time }}</span></td> -->
                  <td class="text-center">
                    
                      <!-- <v-icon>more_vert</v-icon> -->
                     <span style="font-size:20px;"> {{ props.item.note }}</span>
                    
                  </td>
                  <td class="text-center">
                    {{ props.item.actions }}

                    <v-icon small class="mr-2" :disabled="props.item.isEditable" @click="edit(props.item)">
                      mdi-pencil
                    </v-icon>
                    <v-icon small :disabled="props.item.isDeletable" @click="deleteblacklistfunction(props.item)">
                      mdi-delete
                    </v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>
          <v-layout child-flex class="pt-5" v-else-if="$vuetify.breakpoint.width < 1904 && $vuetify.breakpoint.width > 1025">
            <v-data-table :headers="headers" :items="desserts" id="table-vehicle" :hide-default-footer="true" :items-per-page="20">
              <!-- <template v-slot:[`header.id`]="{ header }">
                <span>{{ header.text }}</span>
              </template> -->
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
              <!-- <template v-slot:[`header.time`]="{ header }">
                <span>{{ header.text }}</span>
              </template> -->

              <template v-slot:[`header.note`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.actions`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                  <!-- <td class="text-center">{{ props.item.id }}</td> -->
                  <td class="text-center">{{ props.item.license }}</td>
                  <td class="text-center">{{ props.item.province }}</td>
                  <td class="text-center">{{ props.item.type }}</td>
                  <td class="text-center">{{ props.item.color }}</td>
                  <td class="text-center">{{ props.item.date }}</td>
                  <!-- <td class="text-center">{{ props.item.time }}</td> -->
                  <td class="text-center">
                    
                      <!-- <v-icon>more_vert</v-icon> -->
                      {{ props.item.note }}
                    
                  </td>
                  <td class="text-center">
                    {{ props.item.actions }}

                    <v-icon small class="mr-2" :disabled="props.item.isEditable" @click="edit(props.item)">
                      mdi-pencil
                    </v-icon>
                    <v-icon small :disabled="props.item.isDeletable" @click="deleteblacklistfunction(props.item)">
                      mdi-delete
                    </v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>
          <v-layout child-flex class="pt-5" v-else>
            <v-data-table :headers="headers" :items="desserts" id="table-vehicle" :hide-default-footer="true" :items-per-page="20">
              <!-- <template v-slot:[`header.id`]="{ header }">
                <span>{{ header.text }}</span>
              </template> -->
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
              <!-- <template v-slot:[`header.time`]="{ header }">
                <span>{{ header.text }}</span>
              </template> -->

              <template v-slot:[`header.note`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.actions`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                  <!-- <td class="text-center">{{ props.item.id }}</td> -->
                  <td class="text-center">{{ props.item.license }}</td>
                  <td class="text-center">{{ props.item.province }}</td>
                  <td class="text-center">{{ props.item.type }}</td>
                  <td class="text-center">{{ props.item.color }}</td>
                  <td class="text-center">{{ props.item.date }}</td>
                  <!-- <td class="text-center">{{ props.item.time }}</td> -->
                  <td class="text-center">
                    
                      <!-- <v-icon>more_vert</v-icon> -->
                      {{ props.item.note }}
                    
                  </td>
                  <td class="text-center">
                    {{ props.item.actions }}

                    <v-icon small class="mr-2" :disabled="props.item.isEditable" @click="edit(props.item)">
                      mdi-pencil
                    </v-icon>
                    <v-icon small :disabled="props.item.isDeletable" @click="deleteblacklistfunction(props.item)">
                      mdi-delete
                    </v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>
         <!-- <exportfile class="pt-6"  @downloadEx="genEX" :keypage="keypage" @download="generateReport" :json_data="json_data" :title="titletext"></exportfile> -->
        </v-container>
        <v-pagination v-model="pagination.page" :length="pagination.total" :total-visible="pagination.visible" @input="next"></v-pagination>
    </v-container>
      <edit :show="openDialogEdit" @closeEdit="closeEdit()" :dataItem="dataItem"></edit>
    </v-content>

     <!-- <searchblacklistpdf @onProgress="onloading"  :downloadpdf="downloadpdf" :downloadexcel="downloadexcel" :dataTableRe="desserts"></searchblacklistpdf> -->
  </v-app>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
import headerbar from "../components/header-bar.vue";
import edit from "../components/edit.vue";
// import deleteblacklist from "../components/delete-blacklist.vue";
import exportfile from "../components/export-file.vue";
import searchblacklistpdf from "../formatExport/reportBlacklistPDF.vue";
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
    headerbar,
    // deleteblacklist,
    edit,
    exportfile,
    searchblacklistpdf,
  },
  data() {
    return {
            pagination: {
        page: 1,
        total: 15,
        perPage: 20,
        visible:7
      },
      downloadpdf:false,
      titletext:"ข้อมูลยานพาหนะที่กำหนด",
      onProgress: false,
      downloadexcel:false,
      keypage:"allsensor",
      dataItem: {},
      openDialogEdit: false,
      openDialogDelete: false,
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
        //   color: "red",
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
        // { text: "เวลา", align: "center", sortable: false, value: "time" },
        { text: "หมายเหตุ", align: "center", sortable: false, value: "note" },
        { text: "แก้ไข/ลบ", align: "center", sortable: false, value: "actions" },
      ],
      desserts: [],

    };
  },
  computed: {
    headerTable() {
      return "color:#2962FF ;" + "font-weight: 600; font-size:15px;";
    },
  },
  methods: {

    headerbar(drawer) {
      this.drawer = drawer;
    }, 
    deleteblacklistfunction(item) {
     
          Swal.fire({
      title: 'หากข้อมูลนี้ถูกลบ จะมีผลกับข้อมูลยานพาหนะที่กำหนด',
      showDenyButton: false,
      showCancelButton: true,
      confirmButtonText: 'ลบ',
      cancelButtonText: `ยกเลิก`,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
    }).then((result) => {
      /* Read more about isConfirmed, isDenied below */
      if (result.isConfirmed) {
        this.deleteItem(item)
         
      } 
    })
    },
    deleteItem(item){
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/blacklist/"+item.id;
      this.axios
        .delete(url, {
          headers: { session: session_data },
        })
        .then((response) => {
           if (response.status === 200) {
            this.getBlacklistData()
            Toast.fire({
              icon: 'error',
             title: 'ลบข้อมูลสำเร็จ',     
            })}
           else{Toast.fire({
              icon: 'error',
             title: 'ไม่สามารถลบข้อมูลได้',     
            })}
        });
    },
        edit(parameter) {
      this.openDialogEdit = true;
      this.dataItem = parameter;
    },
    closeEdit(){
      console.log("dddd");
      this.openDialogEdit = false;
      this.getBlacklistData()
    },
        next (page){
      console.log(page);
      this.$route.query.page = page
    
      this.getBlacklistData()
    },
     getBlacklistData() {

      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/blacklists?&page="+this.pagination.page;
      this.axios
        .get(url, {
          headers: { session: session_data },
        })
        .then((response) => {
          if (response.status === 200) {
            this.desserts = [];
            const res_data_array = response.data.data

            for (let index = 0; index < res_data_array.length; index++) {
              let data = {}
              data['id'] = res_data_array[index].id
              data['license'] = res_data_array[index].license_plate
              data['province'] = res_data_array[index].province
              data['type'] = res_data_array[index].type
              data['color'] = res_data_array[index].color
              data['date'] = res_data_array[index].date ? this.setDateReport(res_data_array[index].date.substr(0, 10)): ""
              data['note'] = res_data_array[index].note

              this.desserts.push(data)
            }
             this.pagination.total = response.data.page_total
          }else{
            Toast.fire({
              icon: 'error',
             title: 'ไม่สามารถดูข้อมูลได้',     
            })
          }
        }).catch((error)=>{
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
      let date = param.split("-");
      let month = date[1] === '01' ? monthNames[0] : date[1] === '02' ? monthNames[1] : date[1] === '03' ? monthNames[2] : date[1] === '04' ? monthNames[3] : date[1] === '05' ? monthNames[4] : date[1] === '06' ? monthNames[5] : date[1] === '07' ? monthNames[6] : date[1] === '08' ? monthNames[7] : date[1] === '09' ? monthNames[8] : date[1] === '10' ? monthNames[9] : date[1] === '11' ? monthNames[10] : date[1] === '12' ? monthNames[11] : "";
      return `${date[2]} ${month} ${date[0]}`;


    },
  },
  mounted() {
    this.getBlacklistData()
  },
};
</script>
<style>
@import "../assets/css/background.css";
#borderflex {
  border-radius: 0px 15px 15px 0px;
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
#table-vehicle table thead tr th:nth-child(1),
#table-vehicle table thead tr th:nth-child(2),
#table-vehicle table thead tr th:nth-child(3),
#table-vehicle table thead tr th:nth-child(4),
#table-vehicle table thead tr th:nth-child(5),
#table-vehicle table thead tr th:nth-child(6),
#table-vehicle table thead tr th:nth-child(7),
#table-vehicle table thead tr th:nth-child(8),
#table-vehicle table thead tr th:nth-child(9) {
  background-color: #02754B;
  color: white; 
  font-size: 18px;
}

#table-vehicle table tbody tr:nth-child(odd) {
  background-color: #ddf1fc;
}
</style>
