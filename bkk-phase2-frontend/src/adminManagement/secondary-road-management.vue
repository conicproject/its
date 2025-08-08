<template>
  <v-app id="bg" >
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="onProgress">
      <v-progress-circular
        indeterminate
        size="64"
      ></v-progress-circular>
    </v-overlay>
    <v-content class="pl-3" >
      <v-container class="pl-1 pr-1">
                        <v-chip @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
     <v-icon large color="red">mdi-chevron-left</v-icon>
         <span class="text-left headerback">Back</span>
    </v-chip> 
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">จัดการถนน</span>
        </v-chip>
        <v-container>
          <v-layout v-if="$vuetify.breakpoint.width > 1025">
            <v-flex lg5 md5 >
              <v-chip @click="addRoad" class="mt-3 pl-10 pr-10 addbutton elevation-2" large dark color="green">เพิ่ม</v-chip>
              </v-flex>
             <v-flex>
              <v-chip large class="ma-2" color="#02754B">
            <span class="pl-5 pr-5 headertext">ข้อมูลถนน</span>
        </v-chip>
        </v-flex>  
            </v-layout>
                      <div v-else>
            <v-flex lg5 md5 >
              <v-chip @click="addRoad" class="mt-3 pl-10 pr-10 addbutton elevation-2" large dark color="green">เพิ่ม</v-chip>
              </v-flex>
             <v-flex>
              <v-chip large class="ma-2" color="#02754B">
            <span class="pl-5 pr-5 headertext">ข้อมูลถนน</span>
        </v-chip>
        </v-flex>  
            </div>
          <v-layout child-flex class="pt-5" v-if="$vuetify.breakpoint.width > 1904">
            <v-data-table :headers="headers" :items="listRoad" id="table-vehicle" :hide-default-footer="false"
              :items-per-page="20">
              <template v-slot:[`header.road_id`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.road_code`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.road_name`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.form_section`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.to_section`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.actions`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.road_id }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.road_code }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.road_name }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.from_section }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.to_section }}</span></td>
                  <td class="text-center">
                    <v-icon small class="mr-2" :disabled="props.item.isEditable" @click="edit(props.item)">
                      mdi-pencil
                    </v-icon>
                    <v-icon small >
                      mdi-delete
                    </v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>

          <v-layout child-flex class="pt-5" v-else-if="$vuetify.breakpoint.width < 1904 && $vuetify.breakpoint.width > 1025">
            <v-data-table :headers="headers" :items="listRoad" id="table-vehicle" :hide-default-footer="false"
              :items-per-page="20">
             <template v-slot:[`header.road_id`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.road_code`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.road_name`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.form_section`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.to_section`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.actions`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                 
                  <td class="text-center">{{ props.item.road_id }}</td>
                  <td class="text-center">{{ props.item.road_code }}</td>
                  <td class="text-center">{{ props.item.road_name }}</td>
                  <td class="text-center">{{ props.item.from_section }}</td>
                  <td class="text-center">{{ props.item.to_section }}</td>
                  <td class="text-center">
                    <v-icon small class="mr-2" :disabled="props.item.isEditable" @click="edit(props.item)">
                      mdi-pencil
                    </v-icon>
                    <v-icon small >
                      mdi-delete
                    </v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>

          <v-layout child-flex class="pt-5" v-else>
            <v-data-table :headers="headers" :items="listRoad" id="table-vehicle" :hide-default-footer="false"
              :items-per-page="20">
              <template v-slot:[`header.road_id`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.road_code`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.road_name`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.form_section`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.to_section`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.actions`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                  <td class="text-center">{{ props.item.road_id }}</td>
                  <td class="text-center">{{ props.item.road_code }}</td>
                  <td class="text-center">{{ props.item.road_name }}</td>
                  <td class="text-center">{{ props.item.from_section }}</td>
                  <td class="text-center">{{ props.item.to_section }}</td>
                  <td class="text-center">                 
                    <v-icon small class="mr-2"  @click="edit(props.item)">
                      mdi-pencil
                    </v-icon>
                    <v-icon small >
                      mdi-delete
                    </v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>
        </v-container>
    </v-container>
      <edit :keywordClick="keywordClick" :show="openDialogEdit" @close="openDialogEdit = false" :data="dataItem" @submit="(openDialogEdit = false), getListRoad()"></edit>
    </v-content> 
  </v-app>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
import headerbar from "../components/header-bar.vue";
import edit from "../components/admin/edit-secound-road.vue";
export default {
      components: {
    sidebar,
    headerbar,
    edit
  },
   data() {
    return {
      keywordClick:'',
      onProgress:false,
      listRoad:[],
      drawer:true,
      openDialogEdit : false,
        headers: [
        {
          text: "ID",
          align: "center",
          sortable: false,
          value: "road_id",
        },
        {
          text: "รหัสถนน",
          align: "center",
          sortable: false,
          value: "road_code",
        },
        {
          text: "ชื่อถนน",
          align: "center",
          sortable: false,
          value: "road_name",
        },
        { text: "form section", align: "center", sortable: false, value: "from_section" },
        { text: "to section", align: "center", sortable: false, value: "to_section" },
        { text: "action", align: "center", sortable: false, value: "action" },
      ],
    }
   },
   methods: {
    headerbar(drawer) {
      this.drawer = drawer;
    },
    gobackpage() {
      
    },
    addRoad() {
      this.keywordClick = "add";
      this.openDialogEdit = true
    },
    getListRoad(){
      this.onProgress = true;
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/list-road";
      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {
          if (response.data.status_code == 200) {
            this.onProgress = false;
            this.listRoad = response.data.data;
          } else {
            this.onProgress = false;
            Toast.fire({
              icon: "error",
              title: response.data.message,
            });
          }
        })
        .catch((error) => {
          console.log(error);
          this.onProgress = false;
          if (error.response.data.message === "session timeout") {
            this.$store.dispatch("logout");
            this.$router.push("/");
            Toast.fire({
              icon: "error",
              title: error.response.data.message,
            });

            return;
          }
        });
    },
        edit(param) {
      this.keywordClick = "edit";
      this.dataItem = param;
      this.openDialogEdit = true;
    },
   },
   mounted(){
    this.getListRoad()
   }
}
</script>
<style scoped>
@import '../assets/css/system-configuration.css';
</style>