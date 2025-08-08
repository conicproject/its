<template>
  <v-row justify="center">
    <v-dialog v-model="shower" scrollable persistent max-width="700px">
       <v-form ref="form">
      <v-card>
        <v-card-title> เพิ่ม/แก้ไขข้อมูล ถนน </v-card-title>
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
                <v-text-field label="ไอดีถนน" :rules="Rules" v-model="dataItem.road_id"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field label="รหัสถนน" :rules="Rules" v-model="dataItem.road_code"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field label="ชื่อถนน" :rules="Rules" v-model="dataItem.road_name"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col >
                <v-text-field label="From section" :rules="Rules" v-model="dataItem.from_section"></v-text-field>
              </v-col> 
              </v-row>
               <v-row>
              <v-col >
                <v-text-field label="To section" :rules="Rules" v-model="dataItem.to_section"></v-text-field>
              </v-col> 
              </v-row>
                  <!-- <v-row>
              <v-col >
                <v-select label="ถนน"></v-select>
              </v-col></v-row>       -->
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="$emit('close')">Close</v-btn>
          <v-btn color="primary" @click="confirm()" text>Submit</v-btn>
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
      dataItem:{},
      loading:false,
      color: "",
      province: "",
      type: "",
      note: "",
      license: "",
      drawer: true,
      listColor: [],
      listProvince: [],
      listCarType: [],
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
             console.log(this.dataItem,this.keywordClick);
       if(newVal == true){
       if(this.keywordClick == 'edit'){
        this.dataItem = this.data
       }else{
         this.$refs.form.resetValidation()
          this.dataItem = { 
              road_id:'',
              road_code:'',
              road_name:'',
              from_section:'',
              to_section:''
              }
       }
       }else{
      
        this.dataItem = { 
              road_id:'',
              road_code:'',
              road_name:'',
              from_section:'',
              to_section:''
              }
       }
       }
        
  },
  methods: {
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
        let url = baseUrl.ipServer + "/add-road";
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
         let url = baseUrl.ipServer + "/edit-road";
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