<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-overlay :value="onProgress">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
    <v-content class="pl-3">
      <v-container class="pl-1 pr-1">
        <v-chip @click="gobackpage()" large class="ma-2 pl-0" color="transparent">
          <v-icon large color="red">mdi-chevron-left</v-icon>
          <span class="text-left headerback">Back</span>
        </v-chip>
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">จัดการผู้ใช้งาน</span>
        </v-chip>
        <v-container>
          <v-layout v-if="$vuetify.breakpoint.width > 1025">
            <v-flex lg5 md5
              ><v-chip @click="addUser" class="mt-3 pl-10 pr-10 addbutton elevation-2" large dark color="green"
                >เพิ่ม</v-chip
              ></v-flex
            >
            <v-flex
              ><v-chip large class="ma-2" color="#02754B">
                <span class="pl-5 pr-5 headertext">ข้อมูลผู้ใช้งาน</span>
              </v-chip></v-flex
            >
          </v-layout>
          <div v-else>
            <v-flex
              ><v-chip @click="addUser" class="mt-3 pl-10 pr-10 addbutton elevation-2" large dark color="green"
                >เพิ่ม</v-chip
              ></v-flex
            >
            <v-flex
              ><v-chip large class="ma-2" color="#02754B">
                <span class="pl-5 pr-5 headertext">ข้อมูลผู้ใช้งาน</span>
              </v-chip></v-flex
            >
          </div>
          <v-layout child-flex class="pt-5" v-if="$vuetify.breakpoint.width > 1904">
            <v-data-table
              :headers="headers"
              :items="dataUser"
              id="table-vehicle"
              :hide-default-footer="false"
              :items-per-page="20"
            >
              <template v-slot:[`header.id`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.name`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.email`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.phone`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.department`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.address`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.group_id`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.is_super_user`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                  <td class="text-center">
                    <span style="font-size:20px;">{{ props.item.id }}</span>
                  </td>
                  <td class="text-center">
                    <span style="font-size:20px;">{{ props.item.name }}</span>
                  </td>
                  <td class="text-center">
                    <span style="font-size:20px;">{{ props.item.EMAIL }}</span>
                  </td>
                  <td class="text-center">
                    <span style="font-size:20px;">{{ props.item.PHONE }}</span>
                  </td>
                  <td class="text-center">
                    <span style="font-size:20px;">{{ props.item.HOME_ADDRESS }}</span>
                  </td>
                  <td class="text-center">
                    <span style="font-size:20px;">{{ props.item.DEPARTMENT_NAME }}</span>
                  </td>
                  <td class="text-center">
                    <span style="font-size:20px;">{{ props.item.group_id }}</span>
                  </td>
                  <td class="text-center">
                    <v-icon small class="mr-2" v-if="props.item.is_super_user === 1">
                      mdi-check-bold
                    </v-icon>
                  </td>
                  <td class="text-center">
                    {{ props.item.actions }}

                    <v-icon v-if="props.item.id !== 1" small class="mr-2" :disabled="props.item.isEditable" @click="edit(props.item)">
                      mdi-pencil
                    </v-icon>
                    <v-icon v-if="props.item.id !== 1" small :disabled="props.item.isDeletable" @click="confirmdelete(props.item)">
                      mdi-delete
                    </v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>
          <v-layout child-flex class="pt-5" v-else-if="$vuetify.breakpoint.width < 1904 && $vuetify.breakpoint.width > 1025">
            <v-data-table
              :headers="headers"
              :items="dataUser"
              id="table-vehicle"
              :hide-default-footer="false"
              :items-per-page="20"
            >
              <template v-slot:[`header.id`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.name`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.email`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.phone`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.department`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.address`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.group_id`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <template v-slot:[`header.is_super_user`]="{ header }">
                <span>{{ header.text }}</span>
              </template>
              <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
              <template v-slot:item="props">
                <tr>
                  <td class="text-center">{{ props.item.id }}</td>
                  <td class="text-center">{{ props.item.name }}</td>
                  <td class="text-center">{{ props.item.EMAIL }}</td>
                  <td class="text-center">{{ props.item.PHONE }}</td>
                  <td class="text-center">{{ props.item.HOME_ADDRESS }}</td>
                  <td class="text-center">{{ props.item.DEPARTMENT_NAME }}</td>
                  <td class="text-center">{{ props.item.group_id }}</td>
                  <td class="text-center">
                    <v-icon small class="mr-2" v-if="props.item.is_super_user === 1">
                      mdi-check-bold
                    </v-icon>
                  </td>
                  <td class="text-center">
                    {{ props.item.actions }}

                    <v-icon v-if="props.item.id !== 1" small class="mr-2" :disabled="props.item.isEditable" @click="edit(props.item)">
                      mdi-pencil
                    </v-icon>
                    <v-icon v-if="props.item.id !== 1" small :disabled="props.item.isDeletable" @click="confirmdelete(props.item)">
                      mdi-delete
                    </v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-layout>
          <v-data-table
            :headers="headers"
            :items="dataUser"
            id="table-vehicle"
            :hide-default-footer="false"
            :items-per-page="20"
            v-else
          >
            <template v-slot:[`header.id`]="{ header }">
              <span>{{ header.text }}</span>
            </template>
            <template v-slot:[`header.name`]="{ header }">
              <span>{{ header.text }}</span>
            </template>
            <template v-slot:[`header.email`]="{ header }">
              <span>{{ header.text }}</span>
            </template>
            <template v-slot:[`header.phone`]="{ header }">
              <span>{{ header.text }}</span>
            </template>
            <template v-slot:[`header.department`]="{ header }">
              <span>{{ header.text }}</span>
            </template>
            <template v-slot:[`header.address`]="{ header }">
              <span>{{ header.text }}</span>
            </template>
            <template v-slot:[`header.group_id`]="{ header }">
              <span>{{ header.text }}</span>
            </template>
            <template v-slot:[`header.is_super_user`]="{ header }">
              <span>{{ header.text }}</span>
            </template>
            <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
            <template v-slot:item="props">
              <tr>
                <!-- <td class="text-center">{{ props.item.id }}</td> -->
                <td class="text-center">{{ props.item.id }}</td>
                <td class="text-center">{{ props.item.name }}</td>
                <td class="text-center">{{ props.item.EMAIL }}</td>
                <td class="text-center">{{ props.item.PHONE }}</td>
                <td class="text-center">{{ props.item.HOME_ADDRESS }}</td>
                <td class="text-center">{{ props.item.DEPARTMENT_NAME }}</td>
                <td class="text-center">{{ props.item.group_id }}</td>
                <td class="text-center">
                  <v-icon small class="mr-2" v-if="props.item.is_super_user === 1">
                    mdi-check-bold
                  </v-icon>
                </td>

                <td class="text-center">
                  <v-icon v-if="props.item.id !== 1" small class="mr-2" :disabled="props.item.isEditable" @click="edit(props.item)">
                    mdi-pencil
                  </v-icon>
                  <v-icon v-if="props.item.id !== 1" small :disabled="props.item.isDeletable" @click="confirmdelete(props.item)">
                    mdi-delete
                  </v-icon>
                </td>
              </tr>
            </template>
          </v-data-table>
        </v-container>
      </v-container>
      <edit
        :show="openDialogEdit"
        @close="openDialogEdit = false"
        @submit="(openDialogEdit = false), getUsers()"
        :dataItem="dataItem"
        :keywordClick="keywordClick"
        :length="dataUser.length"
      ></edit>
    </v-content>
  </v-app>
</template>
<script>
const baseUrl = require("../../baseUrl.json");
import sidebar from "../components/sidebar-new.vue";
import headerbar from "../components/header-bar.vue";
import edit from "../components/admin/edit-user.vue";
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
    edit,
  },
  data() {
    return {
      onProgress:false,
      dataItem: {},
      keywordClick: "",
      dataUser: [],
      openDialogEdit: false,
      headers: [
        {
          text: "ID",
          align: "center",
          sortable: false,
          value: "id",
        },
        {
          text: "ชื่อ",
          align: "center",
          sortable: false,
          value: "name",
        },
        {
          text: "อีเมล",
          align: "center",
          sortable: false,
          value: "email",
        },
        { text: "โทรศัพท์", align: "center", sortable: false, value: "phone" },
        { text: "ที่อยู่", align: "center", sortable: false, value: "address" },
        { text: "หน่วยงาน", align: "center", sortable: false, value: "department" },
        { text: "กลุ่มผู้ใช้งาน", align: "center", sortable: false, value: "group_id" },
        { text: "super admin", align: "center", sortable: false, value: "is_super_user" },
        { text: "action", align: "center", sortable: false, value: "actions" },
      ],
      drawer: true,
      onProgress: false,
    };
  },
  methods: {
    gobackpage() {
       this.$router.push({path:"/dashboard"});
    },
    headerbar(drawer) {
      this.drawer = drawer;
    },
    addUser() {
      this.keywordClick = "add";

      this.openDialogEdit = true;
    },
    edit(param) {
      this.keywordClick = "edit";
      this.dataItem = param;
      this.openDialogEdit = true;
    },
    getUsers() {
      this.onProgress = true;
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/list-user";
      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {
          if (response.data.status_code == 200) {
            this.onProgress = false;
            this.dataUser = response.data.data;
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
    confirmdelete(item) {
      Swal.fire({
        title: "คุณต้องการลบผู้ใช้งานนี้ ?",
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
      let url = baseUrl.ipServer + "/del-user";
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
             this.getUsers();
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
  mounted() {
    this.getUsers();
  },
};
</script>
<style scoped>
@import "../assets/css/system-configuration.css";
</style>
