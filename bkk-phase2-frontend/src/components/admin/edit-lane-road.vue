<template>
  <v-row justify="center">
    <v-dialog v-model="shower" scrollable persistent max-width="700px">
       <v-form ref="form">
      <v-card>
        <v-card-title> เพิ่ม/แก้ไขข้อมูล เลนถนน </v-card-title>
        <v-card-text>
          <div v-if="loading == true" class="text-center">
             <v-progress-circular
        indeterminate
        size="40"
      ></v-progress-circular>
          </div>
          <v-container v-else>
            <v-row>
              <v-col>
                <v-text-field label="ไอดีเลนถนน" :rules="Rules" v-model="dataItem.lane_id"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field label="รหัสเลนถนน" :rules="Rules" v-model="dataItem.lane_code"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col >
                <v-text-field label="ชื่อเลนถนน" :rules="Rules" v-model="dataItem.lane_name"></v-text-field>
              </v-col> </v-row>
              <v-row>
              <v-col >
                <v-select :items="direction" :rules="Rules" label="ทิศทางการจราจร" item-text="name" item-value="key" v-model="dataItem.road_direction"></v-select>
              </v-col> </v-row>
              <v-row>
              <v-col >
                <v-select label="ถนน" :rules="Rules" :items="listRoad" item-text="road_name" item-value="road_id" v-model="dataItem.road_id"></v-select>
              </v-col> 
              </v-row>
              <v-row>
              <v-col >
                <v-select label="กล้อง" :rules="Rules" :items="listCamera" item-text="camera_name" item-value="camera_id" v-model="dataItem.camera_id"></v-select>
              </v-col>
              </v-row>
              <v-row>
               <v-col >
                <v-select label="จุดติดตั้ง" :rules="Rules" :items="listCheckPoint" item-text="name" item-value="id" v-model="dataItem.checkpoint_id"></v-select>
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
       </v-form>
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
  props: ["show", "data","keywordClick"],
  data() {
    return {
      loading:false,
      dataItem:{},
      direction:[
        {name:"ขาเข้า",
        key:"inbound"},{name:"ขาออก",key:"outbound"}
      ],
      color: "",
      province: "",
      type: "",
      note: "",
      license: "",
      drawer: true,
      listRoad: [],
      listCamera: [],
      listCheckPoint: [],
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
            console.log(this.keywordClick); 
       if(newVal == true){
        this.getListRoad()
        this.getListCamera()
        this.getListCheckPoint()
      
       if(this.keywordClick == 'edit'){
        this.dataItem = this.data

       }else{
         this.$refs.form.resetValidation()
          this.dataItem = { 
              lane_id: '',
              lane_code: '', 
              lane_name: '', 
              road_id: '',
              camera_id: '', 
              checkpoint_id: ''
              }
       }
       }else{
        
        this.dataItem = { 
              lane_id: '',
              lane_code: '', 
              lane_name: '', 
              road_id: '',
              camera_id: '', 
              checkpoint_id: ''
              }
       }
       }
        
  },
  methods: {
    getListRoad(){
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/list-road"
       this.loading = true
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
             this.loading = false
            this.listRoad = response.data.data
          }else{
          Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลถนนได้',     
        })
          }
          }).catch((error) => {
          console.log(error);
           this.loading = false
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
                    title: 'ไม่สามารถดึงข้อมูลถนนได้',     
                  })
          });
    },
    getListCamera(){
let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/list-cameras"
       this.loading = true
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
             this.loading = false
            this.listCamera = response.data.data
          }else{
          Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลกล้องได้',     
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
                    icon: 'error',
                    title: 'ไม่สามารถดึงข้อมูลกล้องได้',     
                  })
          });
    },
        getListCheckPoint(){
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/get-checkpoints"
       this.loading = true
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
             this.loading = false
            this.listCheckPoint = response.data.data
          }else{
          Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลจุดติดตั้งได้',     
        })
          }
          }).catch((error) => {
          console.log(error);
           this.loading = false
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
                    title: 'ไม่สามารถดึงข้อมูลจุดติดตั้งได้',     
                  })
          });
    },
          confirm(){
      
      for (const [key, value] of Object.entries(this.dataItem)) {
        
        if(value === ''){
          console.log(key,value);
          Toast.fire({
                     icon: "error",
                    title: "กรุณากรอกข้อมูลให้ครบ",
          })
               
        return
        }
      
      }
      if(this.keywordClick == 'add'){ 
       
         this.addItem(this.dataItem)
         
    }else{

          this.editItem(this.dataItem)
           
    }
    },
      addItem(param){
        this.loading = true
        let session_data = localStorage.getItem("session");
        let url = baseUrl.ipServer + "/add-lane";
        var payload = param
        this.axios.post(url,payload, { headers: { session: session_data } }).then((response) => {
          console.log(response);
          if(response.data.status_code == 200){
        this.loading = false
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
         let url = baseUrl.ipServer + "/edit-lane";
        var payload = param
        console.log(payload);
        this.axios.patch(url,payload, { headers: { session: session_data } }).then((response) => {
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
  },
  mounted() {},
};
</script>
<style scoped>
</style>