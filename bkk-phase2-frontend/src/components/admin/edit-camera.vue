<template>
  <v-row justify="center">
    <v-dialog v-model="shower" scrollable persistent max-width="700px">
       <v-form ref="form">
      <v-card>
        <v-card-title> เพิ่ม/แก้ไขข้อมูล กล้อง </v-card-title>
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
                <v-text-field label="ไอดีกล้อง" :rules="Rules" v-model="dataItem.camera_id"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field label="ชื่อกล้อง" :rules="Rules" v-model="dataItem.camera_name"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col >
                <v-text-field label="รหัสกล้อง" :rules="Rules" v-model="dataItem.camera_code"></v-text-field>
              </v-col> </v-row>
                            <v-row>
              <v-col>
                <v-text-field label="รหัสกล้องกทม" :rules="Rules" v-model="dataItem.bma_code"></v-text-field>
              </v-col>
          
            </v-row>
   
            <v-row v-if="$vuetify.breakpoint.width > 754">
              <v-col>
                <v-text-field label="ยี่ห้อ" :rules="Rules" v-model="dataItem.brand"></v-text-field>
              </v-col>
              <v-col>
                <v-text-field label="รุ่น"  v-model="dataItem.model"></v-text-field>
              </v-col>
            </v-row>
            <v-row v-else>
              <v-col>
                <v-text-field label="ยี่ห้อ" :rules="Rules" v-model="dataItem.brand"></v-text-field>
             
                <v-text-field label="รุ่น"  v-model="dataItem.model"></v-text-field>
              </v-col>
            </v-row>
                <v-row v-if="$vuetify.breakpoint.width > 754">
              
              <v-col>
                <v-text-field label="serial" v-model="dataItem.serial"></v-text-field>
                
              </v-col>
              <v-col>
                <v-text-field label="IP" :rules="Rules" v-model="dataItem.ip"></v-text-field>
              </v-col>
            </v-row>
                <v-row v-else>
              <v-col>
                
              
                <v-text-field label="serial" v-model="dataItem.serial"></v-text-field>
                <v-text-field label="IP" :rules="Rules" v-model="dataItem.ip"></v-text-field>
              </v-col>
            </v-row>
              <v-row v-if="$vuetify.breakpoint.width > 754">
              <v-col >
                <v-select :rules="Rules" v-model="dataItem.checkpoint_id" :items="listCheckPoint" item-value="id" item-text="name" label="จุดติดตั้ง"></v-select>
              </v-col>
              <v-col >
                 
                <v-checkbox
                
              v-model="dataItem.is_sample"
               label="is sample"
              :value="dataItem.is_sample"
              hide-details
            ></v-checkbox>
              
                <!-- <v-text-field label="is sample" :rules="Rules" v-model="dataItem.is_sample"></v-text-field> -->
              </v-col>
               </v-row>
              <v-row v-else>
              <v-col >
                <v-select :rules="Rules" v-model="dataItem.checkpoint_id" :items="listCheckPoint" item-value="id" item-text="name" label="จุดติดตั้ง"></v-select>
             
               <v-checkbox
                
              v-model="dataItem.is_sample"
               label="is sample"
              :value="dataItem.is_sample"
              hide-details
            ></v-checkbox>
              </v-col>
               </v-row>
               <v-row v-if="$vuetify.breakpoint.width > 754">
              <v-col >
                <v-text-field label="HLS" :rules="Rules" v-model="dataItem.hls"></v-text-field>
              </v-col>
              <v-col>
                <v-text-field label="Type" :rules="Rules" v-model="dataItem.type"></v-text-field>
              </v-col>
               </v-row>
              <v-row v-else>
              <v-col >
                <v-text-field label="HLS" :rules="Rules" v-model="dataItem.hls"></v-text-field>
             
                <v-text-field label="Type" :rules="Rules" v-model="dataItem.type"></v-text-field>
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
             
       if(newVal == true){
        this.getListCheckPoint()
      console.log(this.keywordClick);
       if(this.keywordClick == 'edit'){
        this.dataItem = this.data
        //this.data.checkpoint_id = parseInt(this.data.checkpoint_id)
        // this.data = { 
        //       bma_code: this.dataItem.bma_code,
        //       brand: this.dataItem.bma_code, 
        //       camera_code: this.dataItem.bma_code, 
        //       camera_name: this.dataItem.bma_code, 
        //       checkpoint_id: this.dataItem.bma_code, 
        //       hls: this.dataItem.bma_code,
        //       id: '',
        //       ip: '',
        //       is_sample: '',
        //       model: '', 
        //       serial: '', 
        //       type: ''
         //     }
         console.log(this.dataItem);
       }else{
         this.$refs.form.resetValidation()
          this.dataItem = { 
              bma_code: '',
              brand: '', 
              camera_code: '', 
              camera_name: '', 
              checkpoint_id: '', 
              hls: '',
              camera_id: '',
              ip: '',
              is_sample: '',
              model: '', 
              serial: '', 
              type: ''
              }
       }
       }else{
        
         this.dataItem = { 
              bma_code: '',
              brand: '', 
              camera_code: '', 
              camera_name: '', 
              checkpoint_id: '', 
              hls: '',
              camera_id: '',
              ip: '',
              is_sample: '',
              model: '', 
              serial: '', 
              type: ''
              }
       }
       }
        
  },
  methods: {
    getListCheckPoint(){
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/get-checkpoints"
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
            this.listCheckPoint = response.data.data
          }else{
          Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลจุดติดตั้งได้',     
        })
          }
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
                    title: 'ไม่สามารถดึงข้อมูลจุดติดตั้งได้',     
                  })
          });
    },
      confirm(){
        console.log(this.dataItem);
      for (const [key, value] of Object.entries(this.dataItem)) {
        if(key !== 'model' && key !== 'serial'){
        if(value === ''){
          console.log(key,value);
          Toast.fire({
                     icon: "error",
                    title: "กรุณากรอกข้อมูลให้ครบ",
          })
               
        return
        }
        }
      }
      if(this.keywordClick == 'add'){ 
        this.dataItem.is_sample  =  this.dataItem.is_sample == true ? 1 :0
         this.addItem(this.dataItem)
         
    }else{

       this.dataItem.is_sample  =  this.dataItem.is_sample == true ? 1 :0
         
          this.editItem(this.dataItem)
           
    }
    },
      addItem(param){
        this.loading = true
        let session_data = localStorage.getItem("session");
        let url = baseUrl.ipServer + "/add-camera";
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
         let url = baseUrl.ipServer + "/edit-camera";
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
  },
  mounted() {},
};
</script>
<style scoped>
</style>