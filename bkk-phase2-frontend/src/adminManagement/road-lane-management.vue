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
          <span class="pl-5 pr-5 headertext">จัดการเลนถนน</span>
        </v-chip>
        <v-container>
          <v-layout v-if="$vuetify.breakpoint.width > 1025">
            <v-flex lg5 md5 >
              <v-chip @click="addLane" class="mt-3 pl-10 pr-10 addbutton elevation-2" large dark color="green">เพิ่ม</v-chip>
              </v-flex>
             <v-flex><v-chip large class="ma-2" color="#02754B">
            <span class="pl-5 pr-5 headertext">ข้อมูลเลนถนน</span>
        </v-chip></v-flex>  
            </v-layout>
            <div v-else>
            <v-flex lg5 md5 >
              <v-chip @click="addLane" class="mt-3 pl-10 pr-10 addbutton elevation-2" large dark color="green">เพิ่ม</v-chip>
              </v-flex>
             <v-flex><v-chip large class="ma-2" color="#02754B">
            <span class="pl-5 pr-5 headertext">ข้อมูลเลนถนน</span>
        </v-chip></v-flex>  
            </div>
          <v-layout child-flex class="pt-5" v-if="$vuetify.breakpoint.width > 1904">
            <v-data-table :headers="headers" :items="listLane" id="table-vehicle" :hide-default-footer="false"
              :items-per-page="20">
              <template v-slot:[`header.id`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.name`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.lanename`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.direction`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.roadcode`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.cameraname`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.checkpoint`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.actions`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.lane_id }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.lane_code }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.lane_name }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.road_direction }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.road_id }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.camera_id }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.checkpoint_id }}</span></td>
                  <td class="text-center">
                    <v-icon small :disabled="props.item.isEditable" @click="edit(props.item)">
                      mdi-pencil
                    </v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>

          <v-layout child-flex class="pt-5" v-else-if="$vuetify.breakpoint.width < 1904 && $vuetify.breakpoint.width > 1025">
            <v-data-table :headers="headers" :items="listLane" id="table-vehicle" :hide-default-footer="false"
              :items-per-page="20">
              <template v-slot:[`header.id`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.name`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.lanename`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.direction`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.roadcode`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.cameraname`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
               <template v-slot:[`header.checkpoint`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.actions`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                  <td class="text-center">{{ props.item.lane_id }}</td>
                  <td class="text-center">{{ props.item.lane_code }}</td>
                  <td class="text-center">{{ props.item.lane_name }}</td>
                  <td class="text-center">{{ props.item.road_direction }}</td>
                  <td class="text-center">{{ props.item.road_id }}</td>
                  <td class="text-center">{{ props.item.camera_id }}</td>
                  <td class="text-center">{{ props.item.checkpoint_id }}</td>
                  <td class="text-center">
                    <v-icon small :disabled="props.item.isEditable" @click="edit(props.item)">
                      mdi-pencil
                    </v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>

          <v-layout child-flex class="pt-5" v-else>
            <v-data-table :headers="headers" :items="listLane" id="table-vehicle" :hide-default-footer="false"
              :items-per-page="20">
              <template v-slot:[`header.id`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.name`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.lanename`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.direction`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.roadcode`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.cameraname`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
               <template v-slot:[`header.checkpoint`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.actions`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                  <td class="text-center">{{ props.item.lane_id }}</td>
                  <td class="text-center">{{ props.item.lane_code }}</td>
                  <td class="text-center">{{ props.item.lane_name }}</td>
                  <td class="text-center">{{ props.item.road_direction }}</td>
                  <td class="text-center">{{ props.item.road_id }}</td>
                  <td class="text-center">{{ props.item.camera_id }}</td>
                  <td class="text-center">{{ props.item.checkpoint_id }}</td>
                  <td class="text-center">
                   
                    <v-icon small @click="edit(props.item)">
                      mdi-pencil
                    </v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>
        </v-container>
    </v-container>
      <edit :keywordClick="keywordClick" :show="openDialogEdit" @close="openDialogEdit = false" :data="dataItem" @submit="(openDialogEdit = false), getListLane()"></edit>
    </v-content>
  </v-app>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
import headerbar from "../components/header-bar.vue";
import edit from "../components/admin/edit-lane-road.vue";
export default {
      components: {
    sidebar,
    headerbar,
    edit

  },
     data() {
    return {
      keywordClick:'',
      dataItem:{},
      listLane:[],
      drawer:true,
      onProgress:false,
      openDialogEdit : false,
        headers: [
        {
          text: "ID",
          align: "center",
          sortable: false,
          value: "id",
        },
        {
          text: "รหัสเลนถนน",
          align: "center",
          sortable: false,
          value: "name",
        },
        {
          text: "ชื่อเลนถนน",
          align: "center",
          sortable: false,
          value: "lanename",
        },
        { text: "ทิศทางการจราจร", align: "center", sortable: false, value: "direction" },
        { text: "รหัสถนน", align: "center", sortable: false, value: "roadcode" },
        { text: "รหัสกล้อง", align: "center", sortable: false, value: "cameraname" },
        { text: "จุดติดตั้ง", align: "center", sortable: false, value: "checkpoint" },
        { text: "action", align: "center", sortable: false, value: "action" },
      ],
    }
   }, 
   methods: {
            edit(param) {
      this.keywordClick = "edit";
      this.dataItem = param;
      this.openDialogEdit = true;
    },
            headerbar(drawer) {
      this.drawer = drawer;
    },
    gobackpage() {
       this.$router.push({path:"/dashboard"});
    },
    addLane() {
     
      this.keywordClick = "add";
      this.openDialogEdit = true
    },
        getListLane(){
      this.onProgress = true;
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/list-lane";
      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {
          if (response.data.status_code == 200) {
            this.onProgress = false;
            this.listLane = response.data.data;
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
    
    }
   },
   mounted(){
    this.getListLane()
   }
}
</script>
<style scoped>
@import '../assets/css/system-configuration.css';
</style>