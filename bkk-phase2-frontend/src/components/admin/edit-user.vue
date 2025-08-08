<template>
  <v-row justify="center">
    <v-dialog v-model="shower" scrollable persistent max-width="700px">
      <v-form ref="form">
      <v-card>        
        <v-card-title> เพิ่ม/แก้ไขข้อมูล ผู้ใช้งาน </v-card-title>
        <v-card-text v-if="$vuetify.breakpoint.width > 754">
          <v-container>
            <v-row>
              <v-col>
                <v-text-field  label="ชื่อ"  :rules="nameRules" v-model="name"></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                
                  @click:append="showPassword1 = !showPassword1"
                  :type="showPassword1 ? 'text' : 'password'"
                  :append-icon="showPassword1 ? 'mdi-eye' : 'mdi-eye-off'"
                  label="รหัสผ่าน"
                  :rules="passwordRules"
                  v-model="password"
                ></v-text-field>
               
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                 <v-text-field
               
                  label="อีเมล"             
                  :rules="emailRules"
                  required
                  v-model="email"
                ></v-text-field>
              </v-col>
              <!-- <v-col>
                <v-text-field
                autocomplete="off"
                :rules="passwordRules"
                  @click:append="showPassword2 = !showPassword2"
                  :type="showPassword2 ? 'text' : 'password'"
                  :append-icon="showPassword2 ? 'mdi-eye' : 'mdi-eye-off'"
                  label="ยืนยันรหัสผ่าน"
                  v-model="confirmpassword"
                ></v-text-field>
              </v-col> -->
            </v-row>
            <v-row>
              <v-col>
                <v-text-field label="ที่อยู่" v-model="address"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  required
                  :rules="phoneRules"
                  :counter="10"
                  label="เบอร์โทรศัพท์"
                  v-model="phoneNumber"
                ></v-text-field>
              </v-col>
              <v-col>
                <v-checkbox
                
               v-model="is_super_user"
               label="super admin"
              :value="is_super_user"
              hide-details
            ></v-checkbox>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-select :items="listGroupName" :disabled="disableGroup" :rules="departmentRules" label="หน่วยงาน" v-model="institute" @change="changeDepartment(institute)"></v-select>
              </v-col>
      
              <v-col>
                <v-select :items="listGroupId" item-text="name" item-value="id" autocomplete="off" :rules="groupRules"  label="กลุ่มผู้ใช้งาน" v-model="group"></v-select>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
          <v-card-text v-else>
          <v-container>
            <v-row>
                <v-text-field label="ชื่อ"  :rules="nameRules" v-model="name"></v-text-field>  
            </v-row>
            <v-row>
             <v-text-field
                  @click:append="showPassword1 = !showPassword1"
                  :type="showPassword1 ? 'text' : 'password'"
                  :append-icon="showPassword1 ? 'mdi-eye' : 'mdi-eye-off'"
                  label="รหัสผ่าน"
                  :rules="passwordRules"
                  v-model="password"
                ></v-text-field>
            
            </v-row>
            <v-row>
               <v-text-field
                  label="อีเมล"
                 
                  :rules="emailRules"
                  required
                  v-model="email"
                ></v-text-field>
                
                <!-- <v-text-field
                autocomplete="off"
                :rules="passwordRules"
                  @click:append="showPassword2 = !showPassword2"
                  :type="showPassword2 ? 'text' : 'password'"
                  :append-icon="showPassword2 ? 'mdi-eye' : 'mdi-eye-off'"
                  label="ยืนยันรหัสผ่าน"
                  v-model="confirmpassword"
                ></v-text-field> -->
              
            </v-row>
            <v-row>     
                <v-text-field label="ที่อยู่" v-model="address"></v-text-field>      
            </v-row>
            <v-row>         
                <v-text-field
                  required
                  :rules="phoneRules"
                  :counter="10"
                  label="เบอร์โทรศัพท์"
                  v-model="phoneNumber"
                ></v-text-field>        
            </v-row>
             <v-row>
               <v-checkbox
               
              v-model="is_super_user"
              label="super admin"
              :value="is_super_user"
              hide-details
            ></v-checkbox>
            </v-row>
            <v-row>
                 <v-select :items="listGroupName" :disabled="disableGroup" :rules="departmentRules" label="หน่วยงาน" v-model="institute" @change="changeDepartment(institute)"></v-select>
            </v-row>
            <v-row>
             <v-select :items="listGroupId" item-text="name" item-value="id" autocomplete="off" :rules="groupRules"  label="กลุ่มผู้ใช้งาน" v-model="group"></v-select>
            </v-row>
          </v-container> 
        </v-card-text>       
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="close()">Close</v-btn>
          <v-btn color="primary" text @click="confirm()" :loading="loading">Submit</v-btn>
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
  props: ["show", "dataItem","keywordClick","length"],
  data() {
    return {
      groupDic:{},
      listGroupName:[],
      listGroupId:[],
      showPassword1: false,
      showPassword2: false,
      email: '',
      phoneNumber:'',
      institute:'',
      disableGroup:false,
      is_super_user:false,
     loading:false,
      address:'',
      name:'',
      surname:'',
      username:'',
      password:'',
      confirmpassword:'',
      group:'',
            select: null,
      items: [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4',
      ],
      emailRules: [
        (v) =>
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
            v
          ) || "อีเมลไม่ถูกต้อง",
      ],
      phoneRules: [    
         v => !isNaN(parseFloat(v)) && v >= 0 && v <= 999999999 || 'Phone Number must be valid',
        
      ],
      passwordRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        
      ],
      nameRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
       
      ],
      departmentRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
       
      ],
      groupRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        
      ],
        addressRules: [
         v => !!v || 'กรุณากรอกข้อมูล',
        
      ],
        positionRules: [
        v => !!v || 'กรุณากรอกข้อมูล',
        
      ],
    };
  },
  computed: {
    shower: {
      get() {
        if (this.show === true) {
          
            if(this.keywordClick == 'edit'){
          this.disableGroup = true
          this.email = this.dataItem.EMAIL ||''
          this.phoneNumber = this.dataItem.PHONE || ''
          this.is_super_user = this.dataItem.is_super_user === 1 ? true : false
          this.institute = this.dataItem.DEPARTMENT_NAME || ''
          this.address  = this.dataItem.HOME_ADDRESS || ''
          this.name = this.dataItem.name || ''
          this.group = this.dataItem.group_id || ''
       
        }else{
          this.email = ''
          this.phoneNumber = ''
          this.institute = ''
          this.is_super_user = false
          this.address  =''
          this.name = ''
          this.surname = ''
          this.username = ''
          this.password = ''
          this.confirmpassword = ''
          this.group = ''
        }
        return this.show
      }else{
          this.email = ''
          this.phoneNumber = ''
          this.institute = ''
          this.is_super_user = ''
          this.address  =''
          this.name = ''
          this.surname = ''
          this.username = ''
          this.password = ''
          this.confirmpassword = ''
          this.group = ''
      }
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
        this.$refs.form.reset()
        this.$refs.form.resetValidation()
       if(this.keywordClick == 'edit'){
         this.changeDepartment(this.dataItem.DEPARTMENT_NAME)
       }else{
         this.getdepartment()
       }
       }
        }
  },
  methods: {
    close(){
      
      this.$refs.form.reset()
      this.$refs.form.resetValidation()
      this.disableGroup =false
      this.$emit('close')
    },
    confirm(){
      if(this.name === '' || this.institute === '' || this.group  === ''){
                    Toast.fire({
                     icon: "error",
                    title: "กรุณากรอกข้อมูลให้ครบ",
                })
                console.log(this.name,this.institute,this.password,this.group);
        return
      }
      // if(this.password !== this.confirmpassword){
      //   Toast.fire({
      //                icon: "error",
      //               title: "password ไม่ตรงกัน",
      //           })
      //   return
      // }
      if(this.keywordClick == 'add'){ 
        if(this.password === ''){
          Toast.fire({
                     icon: "error",
                    title: "กรุณากรอก password",
                })
          return
        }
       let data = {
          'email': this.email,
          'phone': this.phoneNumber,
          'address':this.address,
          'name':this.name,
          'password':this.password,
          'group':this.group,
          'is_super_user':this.is_super_user == true? 1: 0,
          'department_name':this.institute,
        }
         
         this.addItem(data)
         
    }else{

          let data = {}
          console.log(this.password);
          if(this.password !== ''){
           data = {    
              'id':this.dataItem.id,
              'email': this.email,
              'phone': this.phoneNumber,
              'password': this.password,
              'address':this.address,
              'name':this.name,
              'group':this.group,
              'is_super_user':this.is_super_user == true? 1: 0,
              'department_name':this.institute,
            }  
          }else{
            data = {    
              'id':this.dataItem.id,
              'email': this.email,
              'phone': this.phoneNumber,
              'address':this.address,
              'name':this.name,
              'group':this.group,
              'is_super_user':this.is_super_user == true? 1: 0,
              'department_name':this.institute,
            } 
          }
          this.editItem(data)
           
    }
    },
    addItem(param){
      this.loading = true
        let session_data = localStorage.getItem("session");
        let url = baseUrl.ipServer + "/add-user";
        var payload = param
        this.axios.post(url,payload, { headers: { session: session_data } }).then((response) => {
          console.log(response);
          if(response.data.status_code == 200){
            this.loading = false
         this.$refs.form.reset()
         this.$refs.form.resetValidation()  
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
         let url = baseUrl.ipServer + "/edit-user";
        var payload = param
        console.log(payload);
        this.axios.post(url,payload, { headers: { session: session_data } }).then((response) => {
          if(response.data.status_code == 200){
            //this.loading = false
            this.$refs.form.reset()
            this.$refs.form.resetValidation() 
            this.disableGroup =false
            Toast.fire({
                     icon: "success",
                    title: "แก้ไขข้อมูล สำเร็จ",
                }) 
            this.$emit("submit");
          }else{
            //this.loading = false
             Toast.fire({
                     icon: "error",
                    title: "ไม่สามารถแก้ไขข้อมูลได้",
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
                    title: "ไม่สามารถแก้ไขข้อมูลได้",
                }) 
      });
      },
      getdepartment(){
        this.listGroupId = []
        let session_data = localStorage.getItem("session");
         let url = baseUrl.ipServer + "/get-department-group";
          
        this.axios.get(url,{ headers: { session: session_data } }).then((response) => {
           
          this.groupDic = response.data.data
          console.log(this.group);
          this.listGroupName = Object.keys(response.data.data)
          for (const [key, value] of Object.entries(response.data.data[this.listGroupName[0]])) {
          
            this.listGroupId.push({'name':key,'id':value})
           }
          });
      },
      changeDepartment(param){       
        this.listGroupId = []
         for (const [key, value] of Object.entries(this.groupDic[param])) {
            console.log(key, value);
            this.listGroupId.push({'name':key,'id':value})
           }
      }
  },
  mounted() {
    this.getdepartment()
  },
};
</script>
<style scoped>
</style>