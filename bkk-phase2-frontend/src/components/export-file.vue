<template>
    <v-layout justify-end v-if="keypage !== 'card'">
            <v-speed-dial
      v-model="fab"
      :top="top"
      :bottom="bottom"
      :right="right"
      :left="left"
      :direction="direction"
      :open-on-hover="hover"
      :transition="transition"
      
    >
      <template v-slot:activator>
        <v-btn
         large
         class="elevation-0 border"
           v-model="fab"
        ><span class="pa-3">
          export
          </span>
        </v-btn>
      </template>
<v-card>
  <v-list class="pa-0" dense  >
    <v-list-item >     
        <v-list-item-title class="pointer"  @click="exportfile('pdf')">
           Export PDF
        </v-list-item-title> 
    </v-list-item>
    <!-- <download-excel
  class="btn btn-default"
  :data="json_data"
  :fields="json_fields"
  type="xlsx"
  :name="createname" 
  :header="header || ''"
> -->
  <v-list-item >     
        <v-list-item-title class="pointer" @click="exportExcel()">
           Export Excel
        </v-list-item-title> 
    </v-list-item>
<!-- </download-excel> -->
    
    <v-divider></v-divider>
  </v-list>
</v-card>
    </v-speed-dial>
            <!-- <v-btn large id="border">export</v-btn> -->

           <!-- <ag-grid-vue style="width: 500px; height: 500px;"
        class="ag-theme-alpine"
        :columnDefs="columnDefs"
        :rowData="rowData">
    </ag-grid-vue> -->
            </v-layout> 
            <v-layout justify-end v-else >
        <v-btn @click="exportfile('pdf')"
         large
         class="elevation-0 border"
           v-model="fab"
        ><span class="pa-3">
          Export PDF
          </span>
        </v-btn>
  </v-layout>    
</template>
<script>
import Vue from "vue";
import JsonExcel from "vue-json-excel";
import  * as XLSX from 'xlsx';
Vue.component("downloadExcel", JsonExcel);
// import { AgGridVue } from "ag-grid-vue";
export default {
  //   components: {
  //   AgGridVue,
  // },
  props:['keypage','json_data','json_fields','title','header'],
    data: function() {
    return {
       columnDefs: null,
      rowData: null,
       direction: 'top',
      fab: false,
      fling: false,
      hover: false,
      tabs: null,
      top: false,
      right: false,
      bottom: true,
      left: false,
      transition: 'slide-y-reverse-transition',
        exportF:[
          {
            i:1,
            type:"pdf",
            name:"Export PDF",
          },
          {
            i:2,
            type:"excel",
            name:"Export Excel",
          }
        ]
    }},
    methods:{
      
      createname(){
        //  let today = new Date();
        //  let name1 = this.title+'_'+today.getDate()+'-'+today.getMonth()+'-'+today.getFullYear()+".xls"
         let name = this.title+".xlsx"
      return name;
      },
      exportExcel(){
        //  const dataWS = XLSX.utils.json_to_sheet(this.json_data,{skipHeader:true})
        //  const wb = XLSX.utils.book_new()
        //  XLSX.utils.book_append_sheet(wb, dataWS)
        //  XLSX.writeFile(wb,this.createname())

         this.$emit('downloadEx')
       },
      exportfile(parameter){
        if(parameter === "pdf"){
          this.$emit('download')
        }
        
      }
    },
    mounted(){
    },
     beforeMount() {
    this.columnDefs = [
      { field: "make" },
      { field: "model" },
      { field: "price" },
    ];

    this.rowData = [
      { make: "Toyota", model: "Celica", price: 35000 },
      { make: "Ford", model: "Mondeo", price: 32000 },
      { make: "Porsche", model: "Boxster", price: 72000 },
    ];
  },
}
</script>
<style scoped lang="scss">
.pointer{
  cursor: pointer;
}

   @import "~ag-grid-community/styles/ag-grid.css";
   @import "~ag-grid-community/styles/ag-theme-alpine.css";


</style>