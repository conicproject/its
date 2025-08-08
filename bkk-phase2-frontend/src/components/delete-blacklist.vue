<template>
  <v-row justify="center">
    <v-dialog scrollable persistent max-width="700px">
      <v-card>
        <v-card-title>
        แก้ไขข้อมูล
        </v-card-title>

        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="red" text @click="$emit('close')">Close</v-btn>
            <v-btn color="primary">Submit</v-btn>
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
 
    },
    mounted(){
      // this.getListColor();
      // this.getListProvince();
      // this.getListCarType();
     // console.log("test");
    }
}
</script>
<style>

</style>