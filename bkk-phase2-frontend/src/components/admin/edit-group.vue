<template>
  <v-row justify="center">
    <v-dialog v-model="shower" scrollable persistent max-width="700px">
      <v-card>
        <v-card-title> เพิ่ม/แก้ไขข้อมูล กลุ่มผู้ใช้งาน</v-card-title>
        <v-card-text>
          <div v-if="loading == true" class="text-center">
             <v-progress-circular
        indeterminate
        size="40"
      ></v-progress-circular>
          </div>
          <v-container v-else>
            <v-row v-if="keywordClick == 'add'">
              <v-col >
                <v-select :rules="Rules"   v-model="selectDepartment" :items="listDepartment" item-value="id" item-text="department_name" label="หน่วยงาน" ></v-select>
              </v-col></v-row>
            <v-row>
              <v-col>
                <v-text-field v-model="groupName" label="ชื่อกลุ่ม" :rules="nameRules"></v-text-field>
              </v-col>
            </v-row>
              <v-row>
              <v-col >
                <v-select  :rules="Rules" v-model="selectLevel" :items="listUserLevel" item-value="id" item-text="level_name" label="ระดับผู้ใช้งาน" ></v-select>
              </v-col>
              </v-row>
              <!-- <v-row>
              <v-col>
                <v-text-field v-model="description" label="คำอธิบาย" ></v-text-field>
              </v-col>
            </v-row> -->

          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="$emit('close')">Close</v-btn>
          <v-btn color="primary" text @click="confirm()" >Submit</v-btn>
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
  props: ["show", "dataItem","keywordClick"],
  data() {
    return {

        nameRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        // v => /[0-9]{3}-[0-9]{2}-[0-9]{3}/ || 'Phone Number must be valid'
      ],
      listUserLevel:[],
      listDepartment:[],
      selectDepartment:'',
      selectLevel:'',
      groupName:'',
      description:null,
      loading:false,
                  Rules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        // v => /[0-9]{3}-[0-9]{2}-[0-9]{3}/ || 'Phone Number must be valid'
      ],
    };
  },
  computed: {
    shower: {
      get() {
        if (this.show === true) {
          //  console.log("show",this.dataItem);
          if(this.keywordClick == 'add'){
            this.groupName = ''
        this.selectDepartment = ''
        this.selectLevel = ''
        this.description = ''
          }else{
             this.groupName = this.dataItem.name
        this.selectDepartment = this.dataItem.name
        this.selectLevel = this.dataItem.user_level_id
        this.description = this.dataItem.description
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
  watch:{
      show:function(newVal, oldVal) { // watch it
             
       if(newVal == true){
        this.getUsersLevel()
        this.getDepartment()
        this.groupName = this.dataItem.name
        this.selectDepartment = this.dataItem.name
        this.selectLevel = this.dataItem.user_level_id
        this.description = this.dataItem.description
       }else{
        this.groupName = ''
        this.selectDepartment = ''
        this.selectLevel = ''
        this.description = ''
       }
        }
  },
  methods: {
  confirm(){
      if(this.groupName === '' || this.selectLevel === ''){
          Toast.fire({
                     icon: "error",
                    title: "กรุณากรอกข้อมูลให้ครบ",
                })
                console.log(this.name,this.institute,this.password,this.group);
        return
      }
      if(this.keywordClick == 'add'){ 
        if(this.selectDepartment === ''){
          Toast.fire({
                     icon: "error",
                    title: "กรุณากรอกข้อมูลให้ครบ",
                })
          return
        }
       let data = {
            "name" : this.groupName,
            "department_id":this.selectDepartment,
            "user_level_id":this.selectLevel}
         
         this.addItem(data)
         
    }else{

           let data = {    
              'id':this.dataItem.id,
              'name': this.groupName,
              'user_level_id': this.selectLevel,
            }  
         
          this.editItem(data)
           
    }
    },
      addItem(param){
        this.loading = true
        let session_data = localStorage.getItem("session");
        let url = baseUrl.ipServer + "/add-user-group";
        var payload = param
        this.axios.post(url,payload, { headers: { session: session_data } }).then((response) => {
          console.log(response);
          if(response.data.status_code == 200){
        this.loading = false
         this.disableGroup =false
         Toast.fire({
                     icon: "success",
                    title: "เพิ่มข้อมูล สำเร็จ",
                }) 
            this.$emit("submit");
          }else{
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
                     icon: "error",
                    title: "ไม่สามารถเพิ่มข้อมูลได้",
                }) 
      });
      },
      editItem(param){
        this.loading = true
        let session_data = localStorage.getItem("session");
         let url = baseUrl.ipServer + "/edit-user-group";
        var payload = param
        console.log(payload);
        this.axios.post(url,payload, { headers: { session: session_data } }).then((response) => {
          if(response.data.status_code == 200){
            this.loading = false
            this.disableGroup =false
            Toast.fire({
                     icon: "success",
                    title: "แก้ไขข้อมูล สำเร็จ",
                }) 
            this.$emit("submit");
          }else{
            this.loading = false
             Toast.fire({
                     icon: "error",
                    title: "ไม่สามารถแก้ไขข้อมูลได้",
                }) 
          }
          }).catch((error) => {
            this.loading = false
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
                     icon: "error",
                    title: "ไม่สามารถแก้ไขข้อมูลได้",
                }) 
      });
      },
      getUsersLevel(){
        let session_data = localStorage.getItem("session");
         let url = baseUrl.ipServer + "/get-user-level";
         this.loading = true
        this.axios.get(url, { headers: { session: session_data } }).then((response) => {
        if (response.data.status_code === 200) {
           this.loading = false
          this.listUserLevel = response.data.data
          
        }}).catch((error) => {
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
      },
      getDepartment() {
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/get-department";
      this.loading = true
      this.axios
        .get(url, { headers: { session: session_data } })
        .then((response) => {
          if (response.data.status_code == 200) {
           this.loading = false
            this.listDepartment = response.data.data;
          } 
        })
        .catch((error) => {
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
    },

  },
};
</script>
<style scoped>
</style>