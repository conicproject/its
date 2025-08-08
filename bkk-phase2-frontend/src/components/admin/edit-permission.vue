<template>
  <v-row justify="center">
    <v-dialog v-model="shower" scrollable persistent max-width="700px">
      <v-card>
        <v-card-title> เพิ่ม/แก้ไขข้อมูล ระดับการเข้าใช้งาน </v-card-title>
        <v-card-text>
          <div v-if="loading == true" class="text-center">
            <v-progress-circular indeterminate size="40"></v-progress-circular>
          </div>
          <v-container v-else>
            <v-row>
              <v-col>
                <v-text-field :rules="Rules" v-model="permissionName" label="ระดับ"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-list>
                  <v-list-item v-for="item in menu" :key="item.id">
                    <v-list-item-content>
                      <v-list-item-title>{{ item.id }}&nbsp;{{ item.name }}</v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-switch v-model="item.is_open" :value="item.id" inset></v-switch>
                      <!-- <v-switch v-model="item.is_open" inset></v-switch> -->
                    </v-list-item-action>
                  </v-list-item>
                </v-list>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="$emit('close')">Close</v-btn>
          <v-btn color="primary" text @click="confirm()">Submit</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
const baseUrl = require("../../../baseUrl.json");
import Swal from "sweetalert2/dist/sweetalert2.js";
const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});
export default {
  props: ["show", "dataItem", "keywordClick"],
  data() {
    return {
      permissionName: '',
      menu: [],
      loading: false,
    };
  },
  computed: {
    shower: {
      get() {
        if (this.show === true) {
          if (this.keywordClick == 'add') {

          } else {
            this.permissionName = this.dataItem.name

          }
        }
        return this.show;
      },
      set(value) {
        if (!value) {
          // console.log("show",this.dataItem);
        }
      },
    },
  },
  watch: {
    show: function (newVal, oldVal) { // watch it

      if (newVal == true) {
        this.getmenu()
      } else {
        this.permissionName = ''
        this.menu = []
      }
    }
  },
  methods: {
    confirm() {
      if (this.permissionName === '') {
        Toast.fire({
          icon: "error",
          title: "กรุณากรอกข้อมูลให้ครบ",
        })

        return
      }
      // let menu = this.menu.filter((item, _) => item.is_open == true).map((item, _) => (item.id))

      if (this.keywordClick == 'add') {
        let menu = this.menu.filter((item, _) => item.is_open != false).map((item, _) => (item.id))
        let data = {
          "name": this.permissionName,
          "menu": menu,
        }

        this.addItem(data)

      } else {
        let menu = this.menu.filter(function (item) {
 
            if (item.is_open !== false && item.is_open != null)
              return item.id;

        }).map((item, _) => (item.id))

        let data = {
          "id": this.dataItem.id,
          "name": this.permissionName,
          "menu": menu,
        }

        this.editItem(data)

      }
    },
    addItem(param) {
      this.loading = true
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/add-user-level";
      var payload = param
      this.axios.post(url, payload, { headers: { session: session_data } }).then((response) => {
        console.log(response);
        if (response.data.status_code == 200) {
          this.loading = false
          this.disableGroup = false
          Toast.fire({
            icon: "success",
            title: "เพิ่มข้อมูล สำเร็จ",
          })
          this.$emit("submit");
        } else {
          this.loading = false
          Toast.fire({
            icon: "error",
            title: "ไม่สามารถเพิ่มข้อมูลได้",
          })
        }
      }).catch((error) => {
        this.loading = false
        console.log(error);
        this.onProgress = false
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
          title: "ไม่สามารถเพิ่มข้อมูลได้",
        })
      });
    },
    editItem(param) {
      this.loading = true
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/edit-user-level";
      var payload = param
      console.log(payload);
      this.axios.post(url, payload, { headers: { session: session_data } }).then((response) => {
        if (response.data.status_code == 200) {
          this.loading = false
          this.disableGroup = false
          Toast.fire({
            icon: "success",
            title: "แก้ไขข้อมูล สำเร็จ",
          })
          this.$emit("submit");
        } else {
          this.loading = false
          Toast.fire({
            icon: "error",
            title: "ไม่สามารถแก้ไขข้อมูลได้",
          })
        }
      }).catch((error) => {
        this.loading = false
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
          icon: "error",
          title: "ไม่สามารถแก้ไขข้อมูลได้",
        })
      });
    },
    getmenu() {
      this.menu = []
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/get-menu";
      this.loading = true
      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {
          console.log("length", response);
          if (response.data.status_code == 200) {
            for (let i = 0; i < response.data.data.length; i++) {
              let data = {}
              data["id"] = response.data.data[i].id
              data["name"] = response.data.data[i].name
              console.log('is_open', data)
              if (this.keywordClick !== 'add') {


                if (this.dataItem.menu_id) {
                  let check = 0
                  for (let j = 0; j < this.dataItem.menu_id.length; j++) {

                    if (this.dataItem.menu_id[j] === response.data.data[i].id) {
                      data["is_open"] = response.data.data[i].id
                      check = 1
                    }
                  }

                  if (check == 0) {
                    data["is_open"] = false
                  }
                } else {
                  data["is_open"] = false
                }
                
                //  for(let j = 0 ; j< this.dataItem.menu_id.length; j++){
                //   if(this.dataItem.menu_id[j] === response.data.data[i].id){
                //     data["is_open"] = true
                //   }
                //  }
              } else {
                data["is_open"] = false
              }

              this.menu.push(data)
            }
            this.loading = false
          }
        }).catch((error) => {
          console.log(error);
          this.loading = false
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
  mounted() { },
};
</script>
<style scoped></style>