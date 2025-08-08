<template>
  <v-app id="bg" >
    <sidebar :sideNav="drawer"></sidebar>
    <headerbar @close="headerbar" class="nav-header"></headerbar>
    <v-content class="pl-3" >
      <v-container class="pl-1 pr-1">
        <v-chip large class="ma-2" color="#02754B">
          <span class="pl-5 pr-5 headertext">เพิ่มข้อมูลยานพาหนะที่กำหนด</span>
        </v-chip>

        <v-container v-if="$vuetify.breakpoint.width > 650" class="justify-center pl-5 pr-5 pt-5">
          <v-form>
            <v-row>
              <v-col>
                <span class="title-style">ทะเบียนยานพาหนะ</span>
                <v-text-field v-model="license" outlined hide-details class="input-adddata rounded-lg" placeholder="เลขทะเบียนยานพาหนะ"> </v-text-field>
              </v-col>
              <v-col
                ><span class="title-style">จังหวัด</span>
                <v-select   class="input-adddata rounded-lg" v-model="province" :items="listProvince" outlined hide-details   placeholder="เลือกจังหวัด"></v-select>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <span class="title-style">สียานพาหนะ</span>
                <v-select   class="input-adddata rounded-lg" v-model="color" :items="listColor" outlined hide-details   placeholder="เลือกสียานพาหนะ"></v-select>
              </v-col>
              <v-col><span class="title-style">ประเภทยานพาหนะ</span>
                <v-select   class="input-adddata rounded-lg" v-model="carType" :items="listCarType" outlined hide-details  placeholder="เลือกประเภทยานพาหนะ"></v-select>
              </v-col>
            </v-row>
            <v-row>
              <v-col
                ><v-text-field
                v-model="note"
                  outlined
                  placeholder="เพิ่มข้อมูลป้ายทะเบียนยานพาหนะที่กำหนด"
                  class="input-adddata rounded-lg"
                  persistent-hint
                  hide-details
                ></v-text-field
              ></v-col>
            </v-row>
            <v-row class="mt-7">
              <v-col class="d-flex justify-center"
                ><v-btn class="mr-1" style="background: red; color: white; border: unset;" outlined @click="fn_clear()">ล้าง</v-btn><v-btn color="primary"  @click="fn_save()">บันทึกข้อมูล</v-btn></v-col
              >
              <!-- <v-col class="d-flex justify-center"><v-btn color="primary" class="rounded-pill"  @click="confirm()">ค้นหาข้อมูล</v-btn></v-col> -->
              <!-- <v-col class="d-flex justify-center"><v-btn color="primary" class="rounded-pill" @click="fn_delete()">ลบข้อมูล</v-btn></v-col> -->
            </v-row>
          </v-form>
        </v-container>
        <v-container  v-else >
          <v-form>
            <v-row>
              <v-col>
                <span class="title-style">ทะเบียนยานพาหนะ</span>
                <v-text-field v-model="license" outlined hide-details class="input-adddata rounded-lg" placeholder="เลขทะเบียนยานพาหนะ"> </v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <span class="title-style">จังหวัด</span>
                <v-select   class="input-adddata rounded-lg" v-model="province" :items="listProvince" outlined hide-details   placeholder="เลือกจังหวัด"></v-select>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <span class="title-style">สียานพาหนะ</span>
                <v-select   class="input-adddata rounded-lg" v-model="color" :items="listColor" outlined hide-details   placeholder="เลือกสียานพาหนะ"></v-select>
              </v-col>
            </v-row>
            <v-row>
              <v-col
                ><span class="title-style">ประเภทยานพาหนะ</span>
                <v-select   class="input-adddata rounded-lg" v-model="carType" :items="listCarType" outlined hide-details  placeholder="เลือกประเภทยานพาหนะ"></v-select>
              </v-col>
            </v-row>
            <v-row>
              <v-col
                >
                <v-text-field
                v-model="note"
                  outlined
                  placeholder="เพิ่มข้อมูลป้ายทะเบียนยานพาหนะที่กำหนด"
                  class="input-adddata rounded-lg"
                  persistent-hint
                  hide-details
                ></v-text-field
                
              ></v-col>
            </v-row>

            <v-row class="mt-7">
              <v-col class="d-flex justify-center"
                ><v-btn color="red"  class="mr-1" outlined @click="fn_clear()">ล้าง</v-btn><v-btn color="primary"  @click="fn_save()">บันทึกข้อมูล</v-btn></v-col
              >
              <!-- <v-col class="d-flex justify-center"><v-btn color="primary" class="rounded-pill"  @click="confirm()">ค้นหาข้อมูล</v-btn></v-col> -->
              <!-- <v-col class="d-flex justify-center"><v-btn color="primary" class="rounded-pill" @click="fn_delete()">ลบข้อมูล</v-btn></v-col> -->
            </v-row>
          </v-form>
        </v-container>
      </v-container>
    </v-content>

  </v-app>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
import { mapGetters } from "vuex";
import sidebar from "../components/sidebar-new.vue";
import Swal from "sweetalert2/dist/sweetalert2.js";
import headerbar from "../components/header-bar.vue";

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
  },
  data() {
    return {
      color:"",
      province:"",
      carType:"",
      note:"",
      license:"",
      drawer: true,
      listColor:[],
      listProvince:[],
      listCarType:[],
      listCheckPoint:[],
    };
  },
  computed:{
    //...mapGetters(["dataProvince","dataColor","dataCarType"]),
  },
  methods: {
    fn_clear(){
       this.color=""
          this.province=""
          this.carType=""
          this.note=""
          this.license=""
    },
    getListColor(){
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/vehicles-color"
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
            this.listColor = response.data.data
           
          }else{
            Toast.fire({
              icon: 'error',
             title: 'ไม่สามารถดึงข้อมูลสีรถได้',     
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
             title: 'ไม่สามารถดึงข้อมูลสีรถได้',     
            })
      });
    },
    getListProvince(){
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/provinces"
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
            this.listProvince = response.data.data
           
          }
          else{
            Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลจังหวัดได้',     
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
          title: 'ไม่สามารถดึงข้อมูลจังหวัดได้',     
        })

          });
              },
    getListCarType(){
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/vehicles-type"
        this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          if(response.status === 200){
            this.listCarType = response.data.data
           
          }else{
             Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลประเภทรถได้',     
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
          title: 'ไม่สามารถดึงข้อมูลประเภทรถได้',     
        })
      });
    },

    fn_save() {
      //console.log("save");
      if(this.license === ""){
        Toast.fire({
        icon: "error",
        title: "กรุณากรอกเลขทะเบียนยานพาหนะ",
      });
      }else{
      
    var payload = {
            "license_plate": this.license,
            "province": this.province,
            "color": this.color,
            "type": this.carType,
            "note": this.note
        }
          let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/blacklist"
        this.axios.post(url,payload,{headers:{session:session_data}})
        .then((response) => {
        if(response.status === 200){
          console.log(response);
          this.color=""
          this.province=""
          this.carType=""
          this.note=""
          this.license=""
          Toast.fire({
        icon: "success",
        title: "บันทึกข้อมูลสำเร็จ",
      });
     this.$router.push('/vehicle/list-blacklist')
        }else{
          Toast.fire({
        icon: "error",
        title: "ไม่สามารถบันทึกข้อมูลได้",
      });
        }
      }).catch((error) => {
         if(error.response.data.message === 'session timeout'){
            this.$store.dispatch("logout");
            this.$router.push('/')
        }
         Toast.fire({
        icon: "error",
        title: "ไม่สามารถบันทึกข้อมูลได้",
      });
      });
        
    }

      
    },
    headerbar(drawer) {
      
      this.drawer = drawer;
    },
    confirm() {
      this.$router.push({ path: "/add-vehicle-detail" });
    },
  },
  mounted(){
    this.getListCarType();
    this.getListColor();
    this.getListProvince();  
  }
};
</script>
<style>
@import "../assets/css/background.css";
.headertext {
  font-weight: 600;
  font-size: 24px;
  color: #ffffff;
}
.input-keydata {
  background-color: white;
}
.input-adddata {
  background-color: white;
}
.title-style{
  color:#404040;
  font-weight: bold;
  font-size: 18px;
}
</style>
