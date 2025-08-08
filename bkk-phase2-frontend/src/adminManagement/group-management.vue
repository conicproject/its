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
    <v-content class="pl-3" >
      <v-container class="pl-1 pr-1">
                        <v-chip @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
     <v-icon large color="red">mdi-chevron-left</v-icon>
         <span class="text-left headerback">Back</span>
    </v-chip> 
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">จัดการกลุ่มผู้ใช้งาน</span>
        </v-chip>
        <v-container>
          <v-layout v-if="$vuetify.breakpoint.width > 1025">
            <v-flex lg5 md5 ><v-chip @click="addDepartment" class="mt-3 pl-10 pr-10 addbutton elevation-2" large dark color="green">เพิ่ม</v-chip></v-flex>
             <v-flex><v-chip large class="ma-2" color="#02754B">
            <span class="pl-5 pr-5 headertext">ข้อมูลกลุ่มผู้ใช้งาน</span>
        </v-chip></v-flex>  
            </v-layout>
                      <div v-else>
            <v-flex  ><v-chip @click="addDepartment" class="mt-3 pl-10 pr-10 addbutton elevation-2" large dark color="green">เพิ่ม</v-chip></v-flex>
             <v-flex><v-chip large class="ma-2" color="#02754B">
            <span class="pl-5 pr-5 headertext">ข้อมูลกลุ่มผู้ใช้งาน</span>
        </v-chip></v-flex>  
            </div>
          <v-layout child-flex class="pt-5" v-if="$vuetify.breakpoint.width > 1904">
            <v-data-table :headers="headers" :items="dataUserGroup" id="table-vehicle" :hide-default-footer="false"
              :items-per-page="20">
              <template v-slot:[`header.id`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.department_name`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.level`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- <template v-slot:[`header.description`]="{ header }">
                <span>{{ header.text }}</span>
              </template> -->
              <template v-slot:[`header.actions`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.id}}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.name }}</span></td>
                  <td class="text-center"><span style="font-size:20px;">{{ props.item.user_level_name }}</span></td>
                  <!-- <td class="text-center"><span style="font-size:20px;">{{ props.item.description }}</span></td> -->
                  <td class="text-center">
                    {{ props.item.actions }}

                    <v-icon small class="mr-2" :disabled="props.item.isEditable" @click="edit(props.item)">
                      mdi-pencil
                    </v-icon>
                    <v-icon small :disabled="props.item.isDeletable" @click="confirmdelete(props.item)">
                      mdi-delete
                    </v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>
                    <v-layout child-flex class="pt-5" v-else-if="$vuetify.breakpoint.width < 1904 && $vuetify.breakpoint.width > 1025">
            <v-data-table :headers="headers" :items="dataUserGroup" id="table-vehicle" :hide-default-footer="false"
              :items-per-page="20">
             <template v-slot:[`header.id`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.department_name`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.level`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- <template v-slot:[`header.description`]="{ header }">
                <span>{{ header.text }}</span>
              </template> -->
              <template v-slot:[`header.actions`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                
                  <td class="text-center">{{ props.item.id }}</td>
                  <td class="text-center">{{ props.item.name }}</td>
                  <td class="text-center">{{ props.item.user_level_name }}</td>
                   <!-- <td class="text-center">{{ props.item.description }}</td> -->
                  <td class="text-center">
                    {{ props.item.actions }}

                    <v-icon small class="mr-2" :disabled="props.item.isEditable" @click="edit(props.item)">
                      mdi-pencil
                    </v-icon>
                    <v-icon small :disabled="props.item.isDeletable" @click="confirmdelete(props.item)">
                      mdi-delete
                    </v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>
                    <v-layout child-flex class="pt-5" v-else>
            <v-data-table :headers="headers" :items="dataUserGroup" id="table-vehicle" :hide-default-footer="false"
              :items-per-page="20">
              <template v-slot:[`header.id`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.department_name`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.level`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- <template v-slot:[`header.description`]="{ header }">
                <span>{{ header.text }}</span>
              </template> -->
              <template v-slot:[`header.actions`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                 
                  <td class="text-center">{{ props.item.id }}</td>
                  <td class="text-center">{{ props.item.name }}</td>
                  <td class="text-center">{{ props.item.user_level_name }}</td>
                  <!-- <td class="text-center">{{ props.item.description }}</td> -->
                  <td class="text-center">
                   
                    <v-icon small class="mr-2" @click="edit(props.item)">
                      mdi-pencil
                    </v-icon>
                    <v-icon small @click="confirmdelete(props.item)">
                      mdi-delete
                    </v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>
        
        </v-container>
    </v-container>
      <edit :keywordClick="keywordClick" :show="openDialogEdit" @close="openDialogEdit = false" :dataItem="dataItem"  @submit="(openDialogEdit = false), getuserGroup()"></edit>
    </v-content>  
  </v-app>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
import sidebar from "../components/sidebar-new.vue";
import headerbar from "../components/header-bar.vue";
import edit from "../components/admin/edit-group.vue";
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
    edit
  },
     data() {
    return {
      dataItem:{},
      keywordClick:"",
      onProgress:false,
      dataUserGroup:[],
      drawer:true,
      openDialogEdit: false,
        headers: [
        {
          text: "ID",
          align: "center",
          sortable: false,
          value: "id",
        },
        {
          text: "ชื่อกลุ่ม",
          align: "center",
          sortable: false,
          value: "department_name",
        },
        {
          text: "ระดับผู้ใช้งาน",
          align: "center",
          sortable: false,
          value: "level",
        },
        // {
        //   text: "description",
        //   align: "center",
        //   sortable: false,
        //   value: "description",
        // },
        { text: "action", align: "center", sortable: false, value: "action" },
      ],
    }
   },
      methods: {
    headerbar(drawer) {
      this.drawer = drawer;
    },
    gobackpage() {
       this.$router.push({path:"/dashboard"});
    },
    addDepartment() {
      this.keywordClick = "add";
      this.openDialogEdit = true
    },
    getuserGroup() {
      this.onProgress = true;
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/list-user-group";
      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {
          if (response.data.status_code == 200) {
            this.onProgress = false;
            this.dataUserGroup = response.data.data;
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
    confirmdelete(item) {
      Swal.fire({
        title: "คุณต้องการลบกลุ่มผู้ใช้งานนี้ ?",
        showDenyButton: false,
        showCancelButton: true,
        confirmButtonText: "ลบ",
        cancelButtonText: `ยกเลิก`,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
          this.deleteItem(item);
        }
      });
    },
    deleteItem(param) {
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/del-user-group";
      var data = JSON.stringify({
        id: param.id,
      });
      var config = {
        method: "delete",
        url: url,
        headers: {
          session: session_data,
          "Content-Type": "application/json",
        },
        data: data,
      };
      this.axios(config)
        .then((response) => {
          if (response.data.status_code == 200) {
             this.getuserGroup();
            Toast.fire({
              icon: "success",
              title: "ลบข้อมูล สำเร็จ",
            });
   
          
          } else {
            Toast.fire({
              icon: "error",
              title: "ไม่สามารถลบข้อมูลได้",
            });
          }
        })
        .catch((error) => {
          console.log(error);
          // if (error.response.data.message === "session timeout") {
          //   this.$store.dispatch("logout");
          //   this.$router.push("/");
          //   Toast.fire({
          //     icon: "error",
          //     title: error.response.data.message,
          //   });

          //   return;
          // }
          Toast.fire({
            icon: "error",
            title: error,
          });
        });
    },
   },
   mounted(){
    this.getuserGroup()
   }
}
</script>
<style scoped>
@import '../assets/css/system-configuration.css';
</style>