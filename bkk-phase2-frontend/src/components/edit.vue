<template>
    <v-row justify="center">
        <v-dialog  v-model="shower" scrollable persistent max-width="700px">
            <v-card>
                <v-card-title>
                แก้ไขข้อมูล
                </v-card-title>
                <v-card-text>
                     <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="license"
                      label="ทะเบียนยานพาหนะ"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                    :items="listProvince"
                      v-model="province"
                      label="จังหวัด"
                    ></v-select>
                    
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                    :items="listCarType"
                      v-model="type"
                      label="ประเภทยานพาหนะ"
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                    :items="listColor"
                      v-model="color"
                      label="สียานพาหนะ"
                    ></v-select>
                  </v-col>
                  <!-- <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="dataItem.date"
                      label="วัน/เดือน/ปี"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="dataItem.time"
                      label="เวลา"
                    ></v-text-field>
                  </v-col> -->
                  <v-col>
                    <v-text-field
                      v-model="note"
                      label="หมายเหตุ"
                    ></v-text-field>
                    </v-col>
                </v-row>
              </v-container>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="red" text @click="$emit('closeEdit')">Close</v-btn>
                    <v-btn color="primary" text @click="editItem()">Submit</v-btn>
                    
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
  import Swal from "sweetalert2/dist/sweetalert2.js";
  const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});
export default {
    props: ['show','dataItem'],
    data() {
    return {
      color:"",
      province:"",
      type:"",
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
        shower :{
            get() {
                if(this.show === true){
                //  console.log("show",this.dataItem);
                this.color=this.dataItem.color
          this.province=this.dataItem.province
          this.type=this.dataItem.type
          this.note=this.dataItem.note
          this.license=this.dataItem.license
                }
                return this.show
            },
            set (value) {
                if (!value) {
                // console.log("show",this.dataItem);
                }
            }
        },
    },
    methods:{
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

         // this.$router.push('/error')
          }
          }).catch((error) => {
          console.log(error);
          //this.$router.push('/error')
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
     Toast.fire({
          icon: 'error',
          title: 'ไม่สามารถดึงข้อมูลประเภทรถได้',     
        })
      });
    },
          editItem(){      
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
            "type": this.type,
            "note": this.note
        }
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/blacklist/"+this.dataItem.id
        this.axios.patch(url,payload,{headers:{session:session_data}})
        .then((response) => {
        if(response.status === 200){
          this.color=""
          this.province=""
          this.carType=""
          this.note=""
          this.license=""
          Toast.fire({
        icon: "success",
        title: "แก้ไขข้อมูลสำเร็จ",
        })
        this.$emit('closeEdit')
        //this.$router.go()
        }else{

          Toast.fire({
        icon: "error",
        title: "ไม่สามารถแก้ไขข้อมูลได้",
      });
        }
      }).catch((error) => {
        console.log(error);
        Toast.fire({
        icon: "error",
        title: "ไม่สามารถแก้ไขข้อมูลได้",
      });
      });
    }
      }
    },
    mounted(){
      this.getListColor();
      this.getListProvince();
      this.getListCarType();
     // console.log("test");
    }
}
</script>
<style>

</style>