<template>
  <v-row justify="center">
    <v-dialog v-model="shower" scrollable persistent max-width="700px">
      <v-form ref="form">
      <v-card>
        <v-card-title> เพิ่ม/แก้ไขข้อมูล จุดติดตั้ง </v-card-title>
        <v-card-text v-if="$vuetify.breakpoint.width > 754">
          <div v-if="loading == true" class="text-center">
             <v-progress-circular
        indeterminate
        size="40"
      ></v-progress-circular>
          </div>
          <v-container v-else>
            <v-row>
              <v-col>
                <v-text-field label="ไอดีจุดติดตั้ง" :rules="Rules" v-model="dataItem.checkpoint_id"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field label="ชื่อจุดติดตั้งภาษาไทย" :rules="Rules" v-model="dataItem.checkpoint_nameth"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col >
                <v-text-field label="ชื่อย่อภาษาไทย" :rules="Rules" v-model="dataItem.checkpoint_nickname"></v-text-field>
              </v-col> </v-row>
                            <v-row>
              <v-col>
                <v-text-field label="ชื่อจุดติดตั้งภาษาอังกฤษ" :rules="Rules" v-model="dataItem.checkpoint_name"></v-text-field>
              </v-col>
          
            </v-row>
            <v-row>
                        <v-col>
                <v-text-field label="ละติจูด" :rules="Rules" v-model="dataItem.latitude"></v-text-field>
              </v-col>
                  <v-col>
                <v-text-field label="ลองจิจูด" :rules="Rules" v-model="dataItem.longtitude"></v-text-field>
              </v-col>    
              </v-row>
            <v-row>
              <v-col>
                <v-text-field label="จำกัดความเร็ว" :rules="Rules" v-model="dataItem.speedlimit"></v-text-field>
              </v-col>
              <v-col>
                <v-text-field label="road_condition_id"  v-model="dataItem.road_condition_id"></v-text-field>
              </v-col>
              <v-col>
                 <v-select :rules="Rules" v-model="dataItem.district_id" :items="listDistrict" item-value="id" item-text="name" label="เขต"></v-select>
              </v-col>
            </v-row>
                <v-row>
              <v-col>
                <!-- <v-text-field label="road_id" :rules="Rules" v-model="dataItem.road_id"></v-text-field> -->
                 <v-select :rules="Rules" v-model="dataItem.road_id" :items="listRoad" item-value="road_id" item-text="road_name" label="ถนน"></v-select>
              </v-col>
              <v-col>
                <v-text-field label="project_id" :rules="Rules" v-model="dataItem.project_id"></v-text-field>
              </v-col>
            </v-row>
             <v-row>
              <v-col>
                <v-text-field label="Checkpoint_code" :rules="Rules" v-model="dataItem.checkpoint_code"></v-text-field>
              </v-col>
            </v-row>
             <v-row>
              <v-col>
                <v-text-field label="Area_code" :rules="Rules" v-model="dataItem.area_code"></v-text-field>
              </v-col>
            </v-row>

          </v-container>
        </v-card-text>
        <v-card-text v-else>
          <div v-if="loading == true" class="text-center">
             <v-progress-circular
        indeterminate
        size="40"
      ></v-progress-circular>
          </div>
          <v-container v-else>
             <v-row>
              <v-col>
                <v-text-field label="ไอดีจุดติดตั้ง" :rules="Rules" v-model="dataItem.checkpoint_id"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field label="ชื่อจุดติดตั้งภาษาไทย" :rules="Rules" v-model="dataItem.checkpoint_nameth"></v-text-field>
             </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field label="ชื่อย่อภาษาไทย" :rules="Rules" v-model="dataItem.checkpoint_nickname"></v-text-field>
              </v-col>
              </v-row>
                            <v-row>
              <v-col>
                <v-text-field label="ชื่อจุดติดตั้งภาษาอังกฤษ" :rules="Rules" v-model="dataItem.checkpoint_name"></v-text-field>
              </v-col>
          
            </v-row>
            <v-row>
                 
               <v-col>    
                <v-text-field label="ละติจูด" :rules="Rules" v-model="dataItem.latitude"></v-text-field>
              </v-col>
               <v-col>
                <v-text-field label="ลองจิจูด" :rules="Rules" v-model="dataItem.longtitude"></v-text-field>
              </v-col>
      
              </v-row>
                          <v-row>
              <v-col>
                 <v-text-field label="จำกัดความเร็ว" :rules="Rules" v-model="dataItem.speedlimit"></v-text-field>
             </v-col>
            </v-row>
                          <v-row>
          
               <v-col>
                <v-text-field label="road_condition_id"  v-model="dataItem.road_condition_id"></v-text-field>
             </v-col>
               <v-col>
                <v-select :rules="Rules" v-model="dataItem.district_id" :items="listDistrict" item-value="id" item-text="name" label="เขต"></v-select>
              </v-col>
   
            </v-row>
              <v-row>
              <v-col>
               <v-select :rules="Rules" v-model="dataItem.road_id" :items="listRoad" item-value="road_id" item-text="road_name" label="ถนน"></v-select>
               </v-col>
               <v-col>
               <v-text-field label="project_id" :rules="Rules" v-model="dataItem.project_id"></v-text-field>
               </v-col>
              </v-row>
              
             <v-row>
              <v-col>
                <v-text-field label="Checkpoint_code" :rules="Rules" v-model="dataItem.checkpoint_code"></v-text-field>
            </v-col>
            </v-row>
            <v-row>
             <v-col>
                <v-text-field label="Area_code" :rules="Rules" v-model="dataItem.area_code"></v-text-field>
              </v-col>
            </v-row>

          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="close()">Close</v-btn>
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
import loginVue from '../../views/login.vue';
const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});
export default {
  props: ["show", "dataCheck","keywordClick"],
  data() {
    return {
      listDistrict:[],
      listRoad:[],
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
            emailRules: [
        (v) => !!v || "กรุณากรอกข้อมูล",
        (v) =>
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
            v
          ) || "อีเมลไม่ถูกต้อง",
      ],
      Rules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        // v => /[0-9]{3}-[0-9]{2}-[0-9]{3}/ || 'Phone Number must be valid'
      ],
            thaiNameRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        // v => /[0-9]{3}-[0-9]{2}-[0-9]{3}/ || 'Phone Number must be valid'
      ],
            engNameRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        // v => /[0-9]{3}-[0-9]{2}-[0-9]{3}/ || 'Phone Number must be valid'
      ],
            latRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        // v => /[0-9]{3}-[0-9]{2}-[0-9]{3}/ || 'Phone Number must be valid'
      ],
            lonRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        // v => /[0-9]{3}-[0-9]{2}-[0-9]{3}/ || 'Phone Number must be valid'
      ],
            addressRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        // v => /[0-9]{3}-[0-9]{2}-[0-9]{3}/ || 'Phone Number must be valid'
      ],
            limitRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        // v => /[0-9]{3}-[0-9]{2}-[0-9]{3}/ || 'Phone Number must be valid'
      ],
            zoneRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        // v => /[0-9]{3}-[0-9]{2}-[0-9]{3}/ || 'Phone Number must be valid'
      ],
            roadIdRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        // v => /[0-9]{3}-[0-9]{2}-[0-9]{3}/ || 'Phone Number must be valid'
      ],
            checkpointCodeRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        // v => /[0-9]{3}-[0-9]{2}-[0-9]{3}/ || 'Phone Number must be valid'
      ],
            areaCodeRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        // v => /[0-9]{3}-[0-9]{2}-[0-9]{3}/ || 'Phone Number must be valid'
      ],
    };
  },
  computed: {
    shower: {
      get() {
        if (this.show === true) {
         if(this.keywordClick !== 'edit'){
            this.dataItem = { 
              checkpoint_id: '',
              checkpoint_code: '',
               checkpoint_name: '', 
               speedlimit: '', 
               latitude: '', 
               longtitude: '', 
               road_id: '',
               district_id: '',
               road_condition_id: '',
               checkpoint_nameth: '',
               checkpoint_nickname: '', 
               area_code: '', 
               project_id: ''
              }
       
         }else{
         this.dataItem = this.dataCheck
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
        this.getDistrict()
        this.getRoad()
        this.$refs.form.resetValidation()
        
       if(this.keywordClick == 'edit'){
        this.dataItem = this.dataCheck
        this.dataItem = this.dataCheck

         console.log(this.dataItem);
       }else{
         this.dataItem = { 
              checkpoint_id: '',
              checkpoint_code: '',
               checkpoint_name: '', 
               speedlimit: '', 
               latitude: '', 
               longtitude: '', 
               road_id: '',
               district_id: '',
               road_condition_id: '',
               checkpoint_nameth: '',
               checkpoint_nickname: '', 
               area_code: '', 
               project_id: ''
              }
       }
       }
        }
  },
  methods: {
    close(){
       //this.$refs.form.reset()
        this.$refs.form.resetValidation()
      this.$emit('close')
    },
      confirm(){
      for (const [key, value] of Object.entries(this.dataItem)) {
        if(key !== 'road_condition_id'){
        if(value === ''){
          console.log(value);
          Toast.fire({
                     icon: "error",
                    title: "กรุณากรอกข้อมูลให้ครบ",
          })
               
        return
        }
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
        let url = baseUrl.ipServer + "/add-checkpoint";
        var payload = param
        this.axios.post(url,payload, { headers: { session: session_data } }).then((response) => {
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
         let url = baseUrl.ipServer + "/edit-checkpoint";
        var payload = param
        console.log(param);
        this.axios.post(url,payload, { headers: { session: session_data } }).then((response) => {
          if(response.data.status_code == 200){
            this.loading = false
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
      getDistrict(){
        let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/get-district"
       this.loading = true
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
             this.loading = false
            this.listDistrict = response.data.data
          }else{
          Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลDistrictได้',     
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
                    title: 'ไม่สามารถดึงข้อมูลจุดติดตั้งได้',     
                  })
          });
      },
      getRoad(){
        let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/get-road"
       this.loading = true
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
             this.loading = false
            this.listRoad = response.data.data
          }else{
          Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลRoadได้',     
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
                    title: 'ไม่สามารถดึงข้อมูลจุดติดตั้งได้',     
                  })
          });
      },
  },
  mounted() {},
};
</script>
<style scoped>
</style>