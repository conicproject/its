<template>
    <div>
      <vue-html2pdf
        :show-layout="false"
        :float-layout="true"
        :enable-download="false"
        :preview-modal="false"
        :paginate-elements-by-height="1400"
        filename="test"
        :pdf-quality="2"
        :manual-pagination="false"
        pdf-format="a3"
        pdf-orientation="landscape"
        pdf-content-width="100%"
       
        ref="html2Pdf"
        :pdf-margin="10"
      >
        <section slot="pdf-content">
          <div id="chartLine" style="width: 100%; height: 500px;"></div>
          <div id="chartPie" style="width: 100%; height: 500px;"
          ></div>
  
          <table id="mytableM1">
            <tr v-if="checkMonth === 0">
            <th v-for="item in headerTable" :key="item.id">{{ item.text }}</th>
          </tr>
          
          <tr v-else-if="checkMonth === 1">
            <th v-for="item in headerTable_2" :key="item.id">{{ item.text }}</th>
          </tr>
          <tr v-else>
            <th v-for="item in headerTable_3" :key="item.id">{{ item.text }}</th>
          </tr>
            <tr v-for="item in dataInbound" :key="item.id">
              <td>{{ item.type }}</td>
              <td v-if="item._01 !== undefined">{{ item._01 }}</td>
              <td v-else>0</td>
              <td v-if="item._02 !== undefined">{{ item._02 }}</td>
              <td v-else>0</td>
              <td v-if="item._03 !== undefined">{{ item._03 }}</td>
              <td v-else>0</td>
              <td v-if="item._04 !== undefined">{{ item._04 }}</td>
              <td v-else>0</td>
              <td v-if="item._05 !== undefined">{{ item._05 }}</td>
              <td v-else>0</td>
              <td v-if="item._06 !== undefined">{{ item._06 }}</td>
              <td v-else>0</td>
              <td v-if="item._07 !== undefined">{{ item._07 }}</td>
              <td v-else>0</td>
              <td v-if="item._08 !== undefined">{{ item._08 }}</td>
              <td v-else>0</td>
              <td v-if="item._09 !== undefined">{{ item._09 }}</td>
              <td v-else>0</td>
              <td v-if="item._10 !== undefined">{{ item._10 }}</td>
              <td v-else>0</td>
              <td v-if="item._11 !== undefined">{{ item._11 }}</td>
              <td v-else>0</td>
              <td v-if="item._12 !== undefined">{{ item._12 }}</td>
              <td v-else>0</td>
              <td v-if="item._13 !== undefined">{{ item._13 }}</td>
              <td v-else>0</td>
              <td v-if="item._14 !== undefined">{{ item._14 }}</td>
              <td v-else>0</td>
              <td v-if="item._15 !== undefined">{{ item._15 }}</td>
              <td v-else>0</td>
              <td v-if="item._16 !== undefined">{{ item._16 }}</td>
              <td v-else>0</td>
              <td v-if="item._17 !== undefined">{{ item._17 }}</td>
              <td v-else>0</td>
              <td v-if="item._18 !== undefined">{{ item._18 }}</td>
              <td v-else>0</td>
              <td v-if="item._19 !== undefined">{{ item._19 }}</td>
              <td v-else>0</td>
              <td v-if="item._20 !== undefined">{{ item._20 }}</td>
              <td v-else>0</td>
              <td v-if="item._21 !== undefined">{{ item._21 }}</td>
              <td v-else>0</td>
              <td v-if="item._22 !== undefined">{{ item._22 }}</td>
              <td v-else>0</td>
              <td v-if="item._23 !== undefined">{{ item._23 }}</td>
              <td v-else>0</td>
              <td v-if="item._24 !== undefined">{{ item._24 }}</td>
              <td v-else>0</td>
              <td v-if="item._25 !== undefined">{{ item._25 }}</td>
              <td v-else>0</td>
              <td v-if="item._26 !== undefined">{{ item._26 }}</td>
              <td v-else>0</td>
              <td v-if="item._27 !== undefined">{{ item._27 }}</td>
              <td v-else>0</td>
              <td v-if="item._28 !== undefined">{{ item._28 }}</td>
              <td v-else>0</td>
              <td v-if="item._29 !== undefined">{{ item._29 }}</td>
              <td>0</td>
              <td v-if="item._30 !== undefined">{{ item._30 }}</td>
              <td v-else-if="checkMonth === 0 || checkMonth === 1">0</td>
              <td v-if="item._31 !== undefined">{{ item._31 }}</td>
               <td v-else-if="checkMonth === 0 ">0</td>
              <td>{{ item.all }}</td>
            </tr>
          </table>
  
          <table id="mytableM2">
            <tr v-if="checkMonth === 0">
            <th v-for="item in headerTable" :key="item.id">{{ item.text }}</th>
          </tr>
          <tr v-else-if="checkMonth === 1">
            <th v-for="item in headerTable_2" :key="item.id">{{ item.text }}</th>
          </tr>
          <tr v-else>
            <th v-for="item in headerTable_3" :key="item.id">{{ item.text }}</th>
          </tr>
            <tr v-for="item in dataOutbound" :key="item.id">
              <td>{{ item.type }}</td>
              <td v-if="item._01 !== undefined">{{ item._01 }}</td>
              <td v-else>0</td>
              <td v-if="item._02 !== undefined">{{ item._02 }}</td>
              <td v-else>0</td>
              <td v-if="item._03 !== undefined">{{ item._03 }}</td>
              <td v-else>0</td>
              <td v-if="item._04 !== undefined">{{ item._04 }}</td>
              <td v-else>0</td>
              <td v-if="item._05 !== undefined">{{ item._05 }}</td>
              <td v-else>0</td>
              <td v-if="item._06 !== undefined">{{ item._06 }}</td>
              <td v-else>0</td>
              <td v-if="item._07 !== undefined">{{ item._07 }}</td>
              <td v-else>0</td>
              <td v-if="item._08 !== undefined">{{ item._08 }}</td>
              <td v-else>0</td>
              <td v-if="item._09 !== undefined">{{ item._09 }}</td>
              <td v-else>0</td>
              <td v-if="item._10 !== undefined">{{ item._10 }}</td>
              <td v-else>0</td>
              <td v-if="item._11 !== undefined">{{ item._11 }}</td>
              <td v-else>0</td>
              <td v-if="item._12 !== undefined">{{ item._12 }}</td>
              <td v-else>0</td>
              <td v-if="item._13 !== undefined">{{ item._13 }}</td>
              <td v-else>0</td>
              <td v-if="item._14 !== undefined">{{ item._14 }}</td>
              <td v-else>0</td>
              <td v-if="item._15 !== undefined">{{ item._15 }}</td>
              <td v-else>0</td>
              <td v-if="item._16 !== undefined">{{ item._16 }}</td>
              <td v-else>0</td>
              <td v-if="item._17 !== undefined">{{ item._17 }}</td>
              <td v-else>0</td>
              <td v-if="item._18 !== undefined">{{ item._18 }}</td>
              <td v-else>0</td>
              <td v-if="item._19 !== undefined">{{ item._19 }}</td>
              <td v-else>0</td>
              <td v-if="item._20 !== undefined">{{ item._20 }}</td>
              <td v-else>0</td>
              <td v-if="item._21 !== undefined">{{ item._21 }}</td>
              <td v-else>0</td>
              <td v-if="item._22 !== undefined">{{ item._22 }}</td>
              <td v-else>0</td>
              <td v-if="item._23 !== undefined">{{ item._23 }}</td>
              <td v-else>0</td>
              <td v-if="item._24 !== undefined">{{ item._24 }}</td>
              <td v-else>0</td>
              <td v-if="item._25 !== undefined">{{ item._25 }}</td>
              <td v-else>0</td>
              <td v-if="item._26 !== undefined">{{ item._26 }}</td>
              <td v-else>0</td>
              <td v-if="item._27 !== undefined">{{ item._27 }}</td>
              <td v-else>0</td>
              <td v-if="item._28 !== undefined">{{ item._28 }}</td>
              <td v-else>0</td>
              <td v-if="item._29 !== undefined">{{ item._29 }}</td>
              <td>0</td>
              <td v-if="item._30 !== undefined">{{ item._30 }}</td>
              <td v-else-if="checkMonth === 0 || checkMonth === 1">0</td>
              <td v-if="item._31 !== undefined">{{ item._31 }}</td>
               <td v-else-if="checkMonth === 0 ">0</td>
              <td>{{ item.all }}</td>
            </tr>
          </table>
               
          <table id="mytableM3">              
                      <tr>
                        <th colspan="2" >time</th>
                         <th  v-for="item in headerTabletime" :key="item.text">{{item.text}}</th>
                      </tr>                 
                      <tr >
                        <th rowspan="2">Inbound</th> 
                        <th >Volume</th>   
                        <td v-for="item in dataDirection.volume_inbound" :key="item">{{item}}</td>  
                       
                      </tr>  
                      <tr>
                        <th>Volume/day</th>  
                        <td  v-for="item in dataDirection.volume_mean_inbound" :key="item">{{item}}</td> 
                                                                
                      </tr>  
                      <tr >
                        <th rowspan="2">Outbound</th> 
                        <th >Volume</th>   
                        <td v-for="item in dataDirection.volume_outbound" :key="item">{{ item }}</td>
                                  
                      </tr>   
                      <tr >   
                        <th>Volume/day</th> 
                        <td v-for="item in dataDirection.volume_mean_volume_outbound" :key="item">{{ item }}</td>              
                      </tr>             
                     
          </table>
  
          <table  id="mytableM4">
                          <tr>
                            <th rowspan="2">TYPE/TIME</th>
                            <th v-for="item in headerTable3" :key="item.id" colspan="2">{{ item.text }}</th>
                          </tr>
                          <tr>
                            <th v-for="child in head" :key="child.id">{{ child.text }}</th>
                          </tr>
                          <tr v-for="item in dataRush" :key="item.id">
                            <th>{{ item.type }}</th>
                            <td>{{ item.in_0 }}</td>
                            <td>{{ item.out_0 }}</td>
                            <td>{{ item.in_1}}</td>
                            <td>{{ item.out_1 }}</td>
                            <td>{{ item.in_2 }}</td>
                            <td>{{ item.out_2 }}</td>
                            <td>{{ item.in_3 }}</td>
                            <td>{{ item.out_3 }}</td>
                            <td>{{ item.in_4}}</td>
                            <td>{{ item.out_4 }}</td>
                            <td>{{ item.in_5 }}</td>
                            <td>{{ item.out_5 }}</td>
                            <td>{{ item.in_all }}</td>
                            <td>{{ item.out_all }}</td>
                            
                            
                           
                          </tr>
          </table>
  

  <!-- violation -->

          <div id="chartLine_in_v" style="width: 100%; height: 500px;"></div>
          <div id="chartPie_in_v" style="width: 100%; height: 500px;"></div>
          <div id="chartLine_out_v" style="width: 100%; height: 500px;"></div>
          <div id="chartPie_out_v" style="width: 100%; height: 500px;"></div>
  
          <table id="mytableM1_v">
            <tr v-if="checkMonth === 0">
            <th v-for="item in headerTable" :key="item.id">{{ item.text }}</th>
          </tr>
          
          <tr v-else-if="checkMonth === 1">
            <th v-for="item in headerTable_2" :key="item.id">{{ item.text }}</th>
          </tr>
          <tr v-else>
            <th v-for="item in headerTable_3" :key="item.id">{{ item.text }}</th>
          </tr>
            <tr v-for="item in dataInbound_violation" :key="item.id">
              <td>{{ item.type }}</td>
              <td v-if="item._01 !== undefined">{{ item._01 }}</td>
              <td v-else>0</td>
              <td v-if="item._02 !== undefined">{{ item._02 }}</td>
              <td v-else>0</td>
              <td v-if="item._03 !== undefined">{{ item._03 }}</td>
              <td v-else>0</td>
              <td v-if="item._04 !== undefined">{{ item._04 }}</td>
              <td v-else>0</td>
              <td v-if="item._05 !== undefined">{{ item._05 }}</td>
              <td v-else>0</td>
              <td v-if="item._06 !== undefined">{{ item._06 }}</td>
              <td v-else>0</td>
              <td v-if="item._07 !== undefined">{{ item._07 }}</td>
              <td v-else>0</td>
              <td v-if="item._08 !== undefined">{{ item._08 }}</td>
              <td v-else>0</td>
              <td v-if="item._09 !== undefined">{{ item._09 }}</td>
              <td v-else>0</td>
              <td v-if="item._10 !== undefined">{{ item._10 }}</td>
              <td v-else>0</td>
              <td v-if="item._11 !== undefined">{{ item._11 }}</td>
              <td v-else>0</td>
              <td v-if="item._12 !== undefined">{{ item._12 }}</td>
              <td v-else>0</td>
              <td v-if="item._13 !== undefined">{{ item._13 }}</td>
              <td v-else>0</td>
              <td v-if="item._14 !== undefined">{{ item._14 }}</td>
              <td v-else>0</td>
              <td v-if="item._15 !== undefined">{{ item._15 }}</td>
              <td v-else>0</td>
              <td v-if="item._16 !== undefined">{{ item._16 }}</td>
              <td v-else>0</td>
              <td v-if="item._17 !== undefined">{{ item._17 }}</td>
              <td v-else>0</td>
              <td v-if="item._18 !== undefined">{{ item._18 }}</td>
              <td v-else>0</td>
              <td v-if="item._19 !== undefined">{{ item._19 }}</td>
              <td v-else>0</td>
              <td v-if="item._20 !== undefined">{{ item._20 }}</td>
              <td v-else>0</td>
              <td v-if="item._21 !== undefined">{{ item._21 }}</td>
              <td v-else>0</td>
              <td v-if="item._22 !== undefined">{{ item._22 }}</td>
              <td v-else>0</td>
              <td v-if="item._23 !== undefined">{{ item._23 }}</td>
              <td v-else>0</td>
              <td v-if="item._24 !== undefined">{{ item._24 }}</td>
              <td v-else>0</td>
              <td v-if="item._25 !== undefined">{{ item._25 }}</td>
              <td v-else>0</td>
              <td v-if="item._26 !== undefined">{{ item._26 }}</td>
              <td v-else>0</td>
              <td v-if="item._27 !== undefined">{{ item._27 }}</td>
              <td v-else>0</td>
              <td v-if="item._28 !== undefined">{{ item._28 }}</td>
              <td v-else>0</td>
              <td v-if="item._29 !== undefined">{{ item._29 }}</td>
              <td>0</td>
              <td v-if="item._30 !== undefined">{{ item._30 }}</td>
              <td v-else-if="checkMonth === 0 || checkMonth === 1">0</td>
              <td v-if="item._31 !== undefined">{{ item._31 }}</td>
               <td v-else-if="checkMonth === 0 ">0</td>
              <td>{{ item.all }}</td>
            </tr>
          </table>
  
          <table id="mytableM2_v">
            <tr v-if="checkMonth === 0">
            <th v-for="item in headerTable" :key="item.id">{{ item.text }}</th>
          </tr>
          <tr v-else-if="checkMonth === 1">
            <th v-for="item in headerTable_2" :key="item.id">{{ item.text }}</th>
          </tr>
          <tr v-else>
            <th v-for="item in headerTable_3" :key="item.id">{{ item.text }}</th>
          </tr>
            <tr v-for="item in dataOutbound_violation" :key="item.id">
              <td>{{ item.type }}</td>
              <td v-if="item._01 !== undefined">{{ item._01 }}</td>
              <td v-else>0</td>
              <td v-if="item._02 !== undefined">{{ item._02 }}</td>
              <td v-else>0</td>
              <td v-if="item._03 !== undefined">{{ item._03 }}</td>
              <td v-else>0</td>
              <td v-if="item._04 !== undefined">{{ item._04 }}</td>
              <td v-else>0</td>
              <td v-if="item._05 !== undefined">{{ item._05 }}</td>
              <td v-else>0</td>
              <td v-if="item._06 !== undefined">{{ item._06 }}</td>
              <td v-else>0</td>
              <td v-if="item._07 !== undefined">{{ item._07 }}</td>
              <td v-else>0</td>
              <td v-if="item._08 !== undefined">{{ item._08 }}</td>
              <td v-else>0</td>
              <td v-if="item._09 !== undefined">{{ item._09 }}</td>
              <td v-else>0</td>
              <td v-if="item._10 !== undefined">{{ item._10 }}</td>
              <td v-else>0</td>
              <td v-if="item._11 !== undefined">{{ item._11 }}</td>
              <td v-else>0</td>
              <td v-if="item._12 !== undefined">{{ item._12 }}</td>
              <td v-else>0</td>
              <td v-if="item._13 !== undefined">{{ item._13 }}</td>
              <td v-else>0</td>
              <td v-if="item._14 !== undefined">{{ item._14 }}</td>
              <td v-else>0</td>
              <td v-if="item._15 !== undefined">{{ item._15 }}</td>
              <td v-else>0</td>
              <td v-if="item._16 !== undefined">{{ item._16 }}</td>
              <td v-else>0</td>
              <td v-if="item._17 !== undefined">{{ item._17 }}</td>
              <td v-else>0</td>
              <td v-if="item._18 !== undefined">{{ item._18 }}</td>
              <td v-else>0</td>
              <td v-if="item._19 !== undefined">{{ item._19 }}</td>
              <td v-else>0</td>
              <td v-if="item._20 !== undefined">{{ item._20 }}</td>
              <td v-else>0</td>
              <td v-if="item._21 !== undefined">{{ item._21 }}</td>
              <td v-else>0</td>
              <td v-if="item._22 !== undefined">{{ item._22 }}</td>
              <td v-else>0</td>
              <td v-if="item._23 !== undefined">{{ item._23 }}</td>
              <td v-else>0</td>
              <td v-if="item._24 !== undefined">{{ item._24 }}</td>
              <td v-else>0</td>
              <td v-if="item._25 !== undefined">{{ item._25 }}</td>
              <td v-else>0</td>
              <td v-if="item._26 !== undefined">{{ item._26 }}</td>
              <td v-else>0</td>
              <td v-if="item._27 !== undefined">{{ item._27 }}</td>
              <td v-else>0</td>
              <td v-if="item._28 !== undefined">{{ item._28 }}</td>
              <td v-else>0</td>
              <td v-if="item._29 !== undefined">{{ item._29 }}</td>
              <td>0</td>
              <td v-if="item._30 !== undefined">{{ item._30 }}</td>
              <td v-else-if="checkMonth === 0 || checkMonth === 1">0</td>
              <td v-if="item._31 !== undefined">{{ item._31 }}</td>
               <td v-else-if="checkMonth === 0 ">0</td>
              <td>{{ item.all }}</td>
            </tr>
          </table>



        </section>
      </vue-html2pdf>
    
    </div>
    
  </template>
  <script>
     let doc = new jsPDF({ orientation: "l", unit: "pt" ,compress:true});
  import { jsPDF } from "jspdf";
  import fontTH from "../fontTH.js";
  import VueHtml2pdf from "vue-html2pdf";
  import VueApexCharts from "vue-apexcharts";
  import "jspdf-autotable";
  import TableToExcel from "@linways/table-to-excel";
  import THSarabunNewBold from "../THSarabunNewBold.js";
  import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";

am4core.useTheme(am4themes_animated);
  export default {
      props: ["downloadpdf","dataExport","date","checkMonth"],
    components: {
      VueHtml2pdf,
      apexchart: VueApexCharts,
    },
       watch: { 
            downloadpdf: function(newVal, oldVal) { // watch it
            console.log('Prop changed: ', newVal, ' | was: ', oldVal)     
            this.exportPDF();
              
      setTimeout(() => {
              this.width = '100%'
              this.height = '100%'
          }, 2000) 
  
             
          },
  
          },
    data() {
      return {
        dataRush:[],
        dataDirection:{},
        textCheckpoint :"",
       textDate:"",
       dataInbound:[],
       dataOutbound:[],
       dataInbound_violation:[],
       dataOutbound_violation:[],
       headerTable_2:[
        {
          text: "TYPE",
          id:0,
        },
        {
            text: "1",
            id:1,
        },
        {
            text: "2",
            id:2,
        },
        {
            text: "3",
            id:3,
        },
        {
            text: "4",
            id:4,
        },
        {
            text: "5",
            id:5,
        },
        {
            text: "6",
            id:6,
        },
        {
            text: "7",
            id:7,
        },
        {
            text: "8",
            id:8,
        },
        {
            text: "9",
            id:9,
        },
         {
            text: "10",
            id:10,
        },
        {
            text: "11",
            id:11,
        },
        {
            text: "12",
            id:12,
        },
        {
            text: "13",
            id:13,
        },
        {
            text: "14",
            id:14,
        },
        {
            text: "15",
            id:15,
        },
        {
            text: "16",
            id:16,
        },
        {
            text: "17",
            id:17,
        },
        {
            text: "18",
            id:18,
        },
        {
            text: "19",
            id:19,
        },
        {
            text: "20",
            id:20,
        },
        {
            text: "21",
            id:21,
        },
        {
            text: "22",
            id:22,
        },
        {
            text: "23",
            id:23,
        },
        {
            text: "24",
            id:24,
        },
        {
            text: "25",
            id:25,
        },
        {
            text: "26",
            id:26,
        },
        {
            text: "27",
            id:27,
        },
        {
            text: "28",
            id:28,
        },
        {
            text: "29",
            id:29,
        },
        {
            text: "30",
            id:30,
        },
        // {
        //     text: "31",
       // id:31,
        // },
        {
            text: "ALL",
        },
        
      ],
      headerTable_3:[
        {
          text: "TYPE",
          id:0,
        },
        {
            text: "1",
            id:1,
        },
        {
            text: "2",
            id:2,
        },
        {
            text: "3",
            id:3,
        },
        {
            text: "4",
            id:4,
        },
        {
            text: "5",
            id:5,
        },
        {
            text: "6",
            id:6,
        },
        {
            text: "7",
            id:7,
        },
        {
            text: "8",
            id:8,
        },
        {
            text: "9",
            id:9,
        },
         {
            text: "10",
            id:10,
        },
        {
            text: "11",
            id:11,
        },
        {
            text: "12",
            id:12,
        },
        {
            text: "13",
            id:13,
        },
        {
            text: "14",
            id:14,
        },
        {
            text: "15",
            id:15,
        },
        {
            text: "16",
            id:16,
        },
        {
            text: "17",
            id:17,
        },
        {
            text: "18",
            id:18,
        },
        {
            text: "19",
            id:19,
        },
        {
            text: "20",
            id:20,
        },
        {
            text: "21",
            id:21,
        },
        {
            text: "22",
            id:22,
        },
        {
            text: "23",
            id:23,
        },
        {
            text: "24",
            id:24,
        },
        {
            text: "25",
            id:25,
        },
        {
            text: "26",
            id:26,
        },
        {
            text: "27",
            id:27,
        },
        {
            text: "28",
            id:28,
        },
        {
            text: "29",
            id:29,
        },
        // {
        //     text: "30",
        //     id:30,
        // },
        // {
        //     text: "31",
       // id:31,
        // },
        {
            text: "ALL",
        },
        
      ],
      head: [
          { text: "IN" ,id:1 },
          { text: "OUT",id:2 },
          { text: "IN",id:3 },
          { text: "OUT",id:4 },
          { text: "IN" ,id:5},
          { text: "OUT" ,id:6},
          { text: "IN",id:7 },
          { text: "OUT",id:8 },
          { text: "IN",id:9 },
          { text: "OUT",id:10 },
          { text: "IN" ,id:11},
          { text: "OUT" ,id:12},
          { text: "IN" ,id:13},
          { text: "OUT",id:14 },
          { text: "IN" ,id:15},
          { text: "OUT",id:16 },
          { text: "IN" ,id:17},
          { text: "OUT",id:18 },
          { text: "IN" ,id:19},
          { text: "OUT",id:20 },
          { text: "IN",id:21 },
          { text: "OUT",id:22},
          { text: "IN" ,id:23},
          { text: "OUT",id:24 },
          { text: "IN" ,id:25},
          { text: "OUT",id:26 },
        ],
         headerTable3: [
          {
              id:1,
            text: "00-07",
            child:{
              in:"In",
              out:"Out"
            }
          },
          {
              id:2,
            text: "07-09",
            child:{
              in:"In",
              out:"Out"
            }
          },
          {
              id:3,
            text: "09-12",
            child:{
              in:"In",
              out:"Out"
            }
          },
          {
              id:4,
            text: "12-16",
            child:{
              in:"In",
              out:"Out"
            }
          },
          {
              id:5,
            text: "16-19",
            child:{
              in:"In",
              out:"Out"
            }
          },
          {
              id:6,
            text: "19-24",
            child:{
              in:"In",
              out:"Out"
            }
          },
          {
              id:7,
            text: "ALL",
            child:{
              in:"In",
              out:"Out"
            }
          }
        ],
               dataTable3:[
          {
              header:"รถยนต์ส่วนบุคคล",
              in: "time",
              out: "time",
          },
          {
              header:"รถจักรยานยนต์",
              in: "time",
              out: "time",
          },
          {
              header:"รถโดยสาร",
              in: "time",
              out: "time",
          },
          {
              header:"รถบรรทุก",
              in: "time",
              out: "time",
          },
          {
              header:"รถบรรทุกขนาดเล็ก",
              in: "time",
              out: "time",
          },
          {
              header:"รถตู้",
              in: "time",
              out: "time",
          },
          {
              header:"รถสามล้อเครื่อง",
              in: "time",
              out: "time",
          }
          ,
          {
              header:"รถSUV",
              in: "time",
              out: "time",
          }
          ,
          {
              header:"อื่นๆ",
              in: "time",
              out: "time",
          }
          ,
          {
              header:"จำนวนรวมทั้งหมด",
              in: "",
              out: "",
          }
          ,
          {
              header:"PCU",
              in: "",
              out: "",
          }
          ],
        imgPie:"",
        imgURI:"",
        optionspie: {
          
           labels: ['Apple', 'Mango', 'Orange', 'Watermelon'],
            total: {
            show: true,
            },
        },    
        seriespie: [44, 55, 41, 17, 15],
        
      options:{
              markers: {
    size: 4, 
  },
          dataLabels: {
            enabled: true,
          },
          colors: ["#FF9800", "#03A9F4"],
          chart: {
            type: "bar",
            stacked: true,
            toolbar: {
              show: false,
            },
            zoom: {
              enabled: true,
            },
          },
          responsive: [
            {
              breakpoint: 480,
              options: {
                legend: {
                  position: "bottom",
                  offsetX: -10,
                  offsetY: 0,
                },
              },
            },
          ],
          plotOptions: {
            bar: {
              horizontal: false,
              borderRadius: 10,
            },
          },
          xaxis: {
            type: "datetime",
            categories: [
              "01/01/2011 GMT",
              "01/02/2011 GMT",
              "01/03/2011 GMT",
              "01/04/2011 GMT",
              "01/05/2011 GMT",
              "01/06/2011 GMT",
              "01/07/2011 GMT",
              "01/08/2011 GMT",
              "01/09/2011 GMT",
              "01/10/2011 GMT",
              "01/11/2011 GMT",
              "01/12/2011 GMT",
            ],
          },
          legend: {
            position: "right",
            offsetY: 40,
          },
          fill: {
            opacity: 1,
          },
        },
        series: [
          {
            name: "PRODUCT A",
            data: [44, 55, 41, 67, 22, 43, 12, 65, 12, 23, 21, 11],
          },
          {
            name: "PRODUCT B",
            data: [13, 23, 20, 8, 13, 27, 34, 6, 23, 3, 45, 3],
          },
          // {
          //   name: 'PRODUCT C',
          //   data: [11, 17, 15, 15, 21, 14]
          // }, {
          //   name: 'PRODUCT D',
          //   data: [21, 7, 25, 13, 22, 8]
          // }
        ],
         headerTable:[
         {
          text: "TYPE",
          id:0,
        },
        {
            text: "1",
            id:1,
        },
        {
            text: "2",
            id:2,
        },
        {
            text: "3",
            id:3,
        },
        {
            text: "4",
            id:4,
        },
        {
            text: "5",
            id:5,
        },
        {
            text: "6",
            id:6,
        },
        {
            text: "7",
            id:7,
        },
        {
            text: "8",
            id:8,
        },
        {
            text: "9",
            id:9,
        },
         {
            text: "10",
            id:10,
        },
        {
            text: "11",
            id:11,
        },
        {
            text: "12",
            id:12,
        },
        {
            text: "13",
            id:13,
        },
        {
            text: "14",
            id:14,
        },
        {
            text: "15",
            id:15,
        },
        {
            text: "16",
            id:16,
        },
        {
            text: "17",
            id:17,
        },
        {
            text: "18",
            id:18,
        },
        {
            text: "19",
            id:19,
        },
        {
            text: "20",
            id:20,
        },
        {
            text: "21",
            id:21,
        },
        {
            text: "22",
            id:22,
        },
        {
            text: "23",
            id:23,
        },
        {
            text: "24",
            id:24,
        },
        {
            text: "25",
            id:25,
        },
        {
            text: "26",
            id:26,
        },
        {
            text: "27",
            id:27,
        },
        {
            text: "28",
            id:28,
        },
        {
            text: "29",
            id:29,
        },
        {
            text: "30",
            id:30,
        },
        {
            text: "31",
            id:31,
        },
        {
            text: "ALL",
        },
          
        ],

        headerTabletime:[
          
          {
              text: "00-01",
             
          },
          {
              text: "01-02",
          },
          {
              text: "02-03",
          },
          {
              text: "03-04",
          },
          {
              text: "04-05",
          },
          {
              text: "05-06",
          },
          {
              text: "06-07",
          },
          {
              text: "07-08",
          },
          {
              text: "08-09",
          },
           {
              text: "09-10",
          },
          {
              text: "10-11",
          },
          {
              text: "11-12",
          },
          {
              text: "12-13",
          },
          {
              text: "13-14",
          },
          {
              text: "14-15",
          },
          {
              text: "15-16",
          },
          {
              text: "16-17",
          },
          {
              text: "17-18",
          },
          {
              text: "18-19",
          },
          {
              text: "19-20",
          },
          {
              text: "20-21",
          },
          {
              text: "21-22",
          },
          {
              text: "22-23",
          },
          {
              text: "23-24",
          },
          {
              text: "ALL",
          },
          
        ],
       percent_violation_in:"",
       percent_violation_out:"",

      };
    },
    methods: {
      generateReport() {     
        this.$refs.html2Pdf.generatePdf();
      },
      genChartPiea(){
        var options = {
             chart: {
        type: 'pie',
        width:'300',
        animations: {
          enabled: false,
          },
      },
           
      series: [44, 55, 13, 33],
      labels: ['Apple', 'Mango', 'Orange', 'Watermelon'],
       
      }
  
           var chart = new ApexCharts(document.querySelector("#chartPie"), options);
          chart.render().then(() => {
          chart.dataURI().then(({ imgURI, blob }) => { //Here shows error
            this.imgPie = imgURI;
             
          })
             
          })
      },
      async genChartPie(data) {

return new Promise(async(resolve, reject) => {

  var chart = am4core.create("chartPie", am4charts.PieChart);
  data[0].color = am4core.color("#ED1C24")
  data[1].color = am4core.color("#235789")
  data[2].color =am4core.color("#F1D302")
  data[3].color = am4core.color("#020100")
  data[4].color = am4core.color("#eb8334")
  data[5].color = am4core.color("#34eb4c")
  data[6].color = am4core.color("#34e8eb")
  data[7].color = am4core.color("#9634eb")
  data[8].color = am4core.color("#eb34cc")
  chart.data = data
  //console.log(this.dataExport.dataPieChart);
  var pieSeries = chart.series.push(new am4charts.PieSeries());
pieSeries.dataFields.value = "volume";
pieSeries.dataFields.category = "car_type";
pieSeries.slices.template.propertyFields.fill = "color";

chart.legend = new am4charts.Legend();
pieSeries.hiddenInLegend = true;
var options = chart.exporting.getFormatOptions("png");
options.keepTainted = false;
chart.exporting.setFormatOptions("png", options);

//chart.exporting.export("png");
this.imgPie = await chart.exporting.getImage("png");

      resolve({
          status: "success",
        });
    
  // });
// });
})
},
      async genChartPieApex(cat,data) {
        return new Promise(async(resolve, reject) => {
          let img=''
      var options = {
        chart: {
          type: "pie",
          width: "300",
          animations: {
            enabled: false,
          },

        },
legend: {
    show: false,
          labels: {
            
            colors: "#ffff",
            useSeriesColors: false,
          },
        },
        series: data,
        labels: cat,
       colors: ['#1aa478', '#f79e69', '#8582f2', '#866846', '#96e637','#f9429e','#f1cbff','#3e1379','#9a1b5b'],
      };

      var chart = new ApexCharts(document.querySelector("#chartPie"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
         img = imgURI;
          //console.log("PIE",this.imgPie);
          resolve({
                  status: "success",
                  data: img
                });
        });
      });

     
   });
    },
          async genChartPieApex_in_v(cat,data) {
        return new Promise(async(resolve, reject) => {
          let img=''
      var options = {
        chart: {
          type: "pie",
          width: "300",
          animations: {
            enabled: false,
          },

        },
legend: {
    show: false,
          labels: {
            
            colors: "#ffff",
            useSeriesColors: false,
          },
        },
        series: data,
        labels: cat,
        colors: ['#1aa478', '#f79e69', '#8582f2', '#866846', '#96e637','#f9429e','#f1cbff','#3e1379','#9a1b5b'],
      };

      var chart = new ApexCharts(document.querySelector("#chartPie_in_v"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
         img = imgURI;
          //console.log("PIE",this.imgPie);
          resolve({
                  status: "success",
                  data: img
                });
        });
      });

     
   });
    },
          async genChartPieApex_out_v(cat,data) {
        return new Promise(async(resolve, reject) => {
          let img=''
      var options = {
        chart: {
          type: "pie",
          width: "300",
          animations: {
            enabled: false,
          },

        },
legend: {
    show: false,
          labels: {
            
            colors: "#ffff",
            useSeriesColors: false,
          },
        },
        series: data,
        labels: cat,
       colors: ['#1aa478', '#f79e69', '#8582f2', '#866846', '#96e637','#f9429e','#f1cbff','#3e1379','#9a1b5b'],
      };

      var chart = new ApexCharts(document.querySelector("#chartPie_out_v"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
         img = imgURI;
          //console.log("PIE",this.imgPie);
          resolve({
                  status: "success",
                  data: img
                });
        });
      });

     
   });
    },
      genPDFAdmin(index_pic){
        doc.addPage("a4", "l");

         doc.addFileToVFS("THSarabunNew.ttf",fontTH.th);
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
         doc.addFileToVFS('THSarabunNew-bold.ttf', THSarabunNewBold.font);
        doc.addFont('THSarabunNew-bold.ttf', 'THSarabunNewBold', 'bold');
        doc.setFont("THSarabunNew", "Bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
        doc.text("Report Volume & Cassification", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 76);
        doc.text("ถนน : "+this.roadName, 440, 53);
        doc.text("เดือน : "+this.date, 440, 98);
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (ขาเข้า) (คัน)", 40, 135);
        const logo = require("@/assets/img/BMALogo3.jpg");
        
        var imgLogo = new Image();
        imgLogo.src = logo;
        // console.log("logo", this.imgURL);
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
      const CheckPoint1 = require("@/assets/img/checkpointPicture/"+index_pic+".png");
         var imgCheckPoint = new Image();
        imgCheckPoint.src = CheckPoint1;
        doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
       
          doc.setFontSize(15);
          doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (ขาออก) (คัน)", 40, 310);
         
  
           doc.autoTable({ html: '#mytableM1', startY: 140,styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 9,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
  
           doc.autoTable({ html: '#mytableM2', startY: 315,styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 9,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
  
          doc.setFontSize(15);
          doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (คัน)", 40, 480);
          doc.autoTable({ html: '#mytableM3', startY: 485,styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 9,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
  
       
      },
      genPDFAdmin2(imgLine,imgPie,index_pic){
 
        doc.addPage("a4", "l");
        doc.addFileToVFS("THSarabunNew.ttf",fontTH.th);
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
        doc.setFont("THSarabunNew", "Bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
        doc.text("Report Volume & Cassification", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 76);
        doc.text("ถนน : "+this.roadName, 440, 53);
        doc.text("เดือน : "+this.date, 440, 98);
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรเฉลี่ยแยกตามประเภทรถในและนอกเวลาเร่งด่วน(คัน/วัน)", 40, 145);
        const logo2 = require("@/assets/img/BMALogo3.jpg");
        var imgLogo = new Image();
        imgLogo.src = logo2;
        // console.log("logo", this.imgURL);
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
            const CheckPoint1 = require("@/assets/img/checkpointPicture/"+index_pic+".png");
         var imgCheckPoint = new Image();
        imgCheckPoint.src = CheckPoint1;
        doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
        doc.autoTable({ html: '#mytableM4', startY: 150,tableWidth:500,styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 9,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
          doc.setFontSize(17);
            doc.text("Graph of Traffic Volume", 350, 340);
        doc.setFontSize(15);
        doc.text("(Inbound/Outbound)", 370, 350);
           doc.addImage(imgLine, "JPEG", 60, 360, 700, 200, undefined,'FAST');
           doc.setFontSize(17);
           doc.text("Volume&Classification Pie Graph", 620, 160);
           doc.addImage(imgPie, "JPEG", 600, 180, 200, 100, undefined,'FAST');
        
      },
      genPDFAdmin_in_v(imgLine,imgPie,index_pic){
        doc.addPage("a4", "l");

         doc.addFileToVFS("THSarabunNew.ttf",fontTH.th);
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
         doc.addFileToVFS('THSarabunNew-bold.ttf', THSarabunNewBold.font);
        doc.addFont('THSarabunNew-bold.ttf', 'THSarabunNewBold', 'bold');
        doc.setFont("THSarabunNew", "Bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
        doc.text("รายงานยานพาหนะฝ่าฝืนสัญญาณ\nไฟจราจรทางข้ามชนิดปุ่มกด", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 73);
        doc.text("ถนน : "+this.roadName, 440, 94);
        doc.text("เดือน : "+this.date, 440, 115);
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรในแต่ละวัน (ขาเข้า) (คัน)", 40, 135);
        const logo = require("@/assets/img/BMALogo3.jpg");
        
        var imgLogo = new Image();
        imgLogo.src = logo;
        // console.log("logo", this.imgURL);
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
            const CheckPoint1 = require("@/assets/img/checkpointPicture/"+index_pic+".png");
         var imgCheckPoint = new Image();
        imgCheckPoint.src = CheckPoint1;
        doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
       
          doc.setFontSize(15);
          doc.text("ปริมาณยานพาหนะฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกดในแต่ละวัน (ขาเข้า) (คัน)", 40, 295);
         
  
           doc.autoTable({ html: '#mytableM1', startY: 140,styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 8,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
  
           doc.autoTable({ html: '#mytableM1_v', startY: 300,styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 8,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
       doc.setFontSize(12);
        doc.text("จำนวนของการฝ่าสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด คิดเป็น "+this.percent_violation_in+"% ของปริมาณจราจรทั้งหมด", 40, 450);
       
  
         doc.setFontSize(15);
         doc.text("Traffic Volume Graph", 200, 470);
        doc.addImage(imgLine, "JPEG", 60, 475, 370, 100, undefined,'FAST');
        doc.text("Volume&Classification of Violation Pie Graph", 550, 465);
        doc.addImage(imgPie, "JPEG", 550, 475, 200, 100, undefined,'FAST');
        
          
       
      },
      genPDFAdmin_out_v(imgLine,imgPie,index_pic){
        doc.addPage("a4", "l");

         doc.addFileToVFS("THSarabunNew.ttf",fontTH.th);
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
         doc.addFileToVFS('THSarabunNew-bold.ttf', THSarabunNewBold.font);
        doc.addFont('THSarabunNew-bold.ttf', 'THSarabunNewBold', 'bold');
        doc.setFont("THSarabunNew", "Bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
        doc.text("รายงานยานพาหนะฝ่าฝืนสัญญาณ\nไฟจราจรทางข้ามชนิดปุ่มกด", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 73);
        doc.text("ถนน : "+this.roadName, 440, 94);
        doc.text("เดือน : "+this.date, 440, 115);
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรในแต่ละวัน (ขาออก) (คัน)", 40, 135);
        const logo = require("@/assets/img/BMALogo3.jpg");
        
        var imgLogo = new Image();
        imgLogo.src = logo;
        // console.log("logo", this.imgURL);
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
          const CheckPoint1 = require("@/assets/img/checkpointPicture/"+index_pic+".png");
         var imgCheckPoint = new Image();
        imgCheckPoint.src = CheckPoint1;
        doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
       
          doc.setFontSize(15);
          doc.text("ปริมาณยานพาหนะฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกดในแต่ละวัน (ขาออก) (คัน)", 40, 295);
         
  
           doc.autoTable({ html: '#mytableM2', startY: 140,styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 8,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
  
           doc.autoTable({ html: '#mytableM2_v', startY: 300,styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 8,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
        doc.setFontSize(12);
        doc.text("จำนวนของการฝ่าสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด คิดเป็น "+this.percent_violation_out+"% ของปริมาณจราจรทั้งหมด", 40, 450);
       
          
       doc.setFontSize(15);
        doc.text("Traffic Volume Graph", 200, 470);
        doc.addImage(imgLine, "JPEG", 60, 475, 370, 100, undefined,'FAST');
        doc.text("Volume&Classification of Violation Pie Graph", 550, 465);
        doc.addImage(imgPie, "JPEG", 550, 475, 200, 100, undefined,'FAST');
        
      },

      async genChartLineApex(cat,data) {
        return new Promise(async(resolve, reject) =>  {
          let img = ''
      var options = {
        chart: {
          height: 200,
          type: "line",
          animations: {
            enabled: false,
          },
          stacked: false,
          toolbar: {
            show: false,
          },
          zoom: {
            enabled: true,
          },
        },
        markers: {
          size: 4,
        },
        plotOptions: {
          bar: {
            horizontal: false,
            borderRadius: 10,
          },
        },
        dataLabels: {
          enabled: false,
          style: {
            colors: ["#000"],
          },
          offsetX: 0,
          offsetY: -10,
          background: {
            enabled: false,
          },
        },
        colors: ["#ff7f09", "#21b3ff"],
        // stroke: {
        //   show: true,
        //   width: 2,
        //   colors: ['transparent']
        // },
        series: data,
        xaxis: {
          categories: cat,
        },
        yaxis: {
          title: {
            text: "",
          },
        },
        fill: {
          opacity: 1,
        },
        tooltip: {
          y: {
            formatter: function(val) {
              return val ;
            },
          },
        },
      };
      var chart = new ApexCharts(document.querySelector("#chartLine"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
          img = imgURI;
          //console.log("PIE",this.imgPie);
          resolve({
                  status: "success",
                  data: img
                });

        });
      });
     
   });
    },
          async genChartLineApex_in_v(cat,data) {
            console.log(cat,data)
        return new Promise(async(resolve, reject) =>  {
          let img = ''
      var options = {
        chart: {
          height: 200,
          type: "line",
          animations: {
            enabled: false,
          },
          stacked: false,
          toolbar: {
            show: false,
          },
          zoom: {
            enabled: true,
          },
        },
        markers: {
          size: 4,
        },
        plotOptions: {
          bar: {
            horizontal: false,
            borderRadius: 10,
          },
        },
        dataLabels: {
          enabled: false,
          style: {
            colors: ["#000"],
          },
          offsetX: 0,
          offsetY: -10,
          background: {
            enabled: false,
          },
        },
        colors: ["#ff7f09", "#21b3ff"],
        // stroke: {
        //   show: true,
        //   width: 2,
        //   colors: ['transparent']
        // },
        series: data,
        xaxis: {
          categories: cat,
        },
        yaxis: {
          title: {
            text: "",
          },
        },
        fill: {
          opacity: 1,
        },
        tooltip: {
          y: {
            formatter: function(val) {
              return val ;
            },
          },
        },
      };
      var chart = new ApexCharts(document.querySelector("#chartLine_in_v"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
          img = imgURI;
          //console.log("PIE",this.imgPie);
          resolve({
                  status: "success",
                  data: img
                });

        });
      });
     
   });
    },
          async genChartLineApex_out_v(cat,data) {
        return new Promise(async(resolve, reject) =>  {
          let img = ''
      var options = {
        chart: {
          height: 200,
          type: "line",
          animations: {
            enabled: false,
          },
          stacked: false,
          toolbar: {
            show: false,
          },
          zoom: {
            enabled: true,
          },
        },
        markers: {
          size: 4,
        },
        plotOptions: {
          bar: {
            horizontal: false,
            borderRadius: 10,
          },
        },
        dataLabels: {
          enabled: false,
          style: {
            colors: ["#000"],
          },
          offsetX: 0,
          offsetY: -10,
          background: {
            enabled: false,
          },
        },
        colors: ["#ff7f09", "#21b3ff"],
        // stroke: {
        //   show: true,
        //   width: 2,
        //   colors: ['transparent']
        // },
        series: data,
        xaxis: {
          categories: cat,
        },
        yaxis: {
          title: {
            text: "",
          },
        },
        fill: {
          opacity: 1,
        },
        tooltip: {
          y: {
            formatter: function(val) {
              return val ;
            },
          },
        },
      };
      var chart = new ApexCharts(document.querySelector("#chartLine_out_v"), options);
      chart.render().then(() => {
        chart.dataURI().then(({ imgURI, blob }) => {
          //Here shows error
          img = imgURI;
          //console.log("PIE",this.imgPie);
          resolve({
                  status: "success",
                  data: img
                });

        });
      });
     
   });
    },
      async exportPDF(){
        console.log("exportMonth");
        let res = await this.loopGenPdf()
        if(res.status == 'success'){
        doc.save(`รายงานผลข้อมูลจราจร(รายเดือน).pdf`);
        this.$emit('closePDF')
        }
      },
      async loopGenPdf(){
        return new Promise(async(resolve, reject) =>  {
          for(let i = 0; i < this.dataExport.length;i++){
            let index_pic = this.dataExport[i].checkpoint_id
          this.generateReport();
        //this.genChartLine();
       // this.headerTable = this.dataExport[i].headerTable
       this.textCheckpoint = this.dataExport[i].checkpoint_name
       this.textDate= this.date
        this.dataInbound = this.dataExport[i].dataInbound
        this.dataOutbound = this.dataExport[i].dataOutbound
        this.dataDirection= this.dataExport[i].dataDirection
        this.dataRush= this.dataExport[i].dataRush
               this.percent_violation_in = this.dataExport[i].percent_violation_in
       this.percent_violation_out = this.dataExport[i].percent_violation_out
       this.roadName = this.dataExport[i].road_name
       // let pie = this.dataExport[i].dataPieChart.length > 0 ?await this.genChartPie(this.dataExport[i].dataPieChart) : { status: "success"}
        let pie = await this.genChartPieApex(this.dataExport[i].categories,this.dataExport[i].dataChart) 
        let line =  await this.genChartLineApex(this.dataExport[i].apex_cat,this.dataExport[i].apex_line) 
        //console.log(bar);
         //------------------------violation

          this.dataInbound_violation = this.dataExport[i].dataInbound_violation
          
        this.dataOutbound_violation = this.dataExport[i].dataOutbound_violation
        let pie_in_v = await this.genChartPieApex_in_v(this.dataExport[i].categories_violation,this.dataExport[i].PieChart_in_violation) 
        let line_in_v =  await this.genChartLineApex_in_v(this.dataExport[i].apex_cat_violation,this.dataExport[i].apex_line_in_violation) 
        let pie_out_v = await this.genChartPieApex_out_v(this.dataExport[i].categories_violation,this.dataExport[i].PieChart_out_violation) 
        let line_out_v =  await this.genChartLineApex_out_v(this.dataExport[i].apex_cat_violation,this.dataExport[i].apex_line_out_violation) 
        console.log("this.dataOutbound" ,this.dataOutbound_violation );
  
        if(pie.status === 'success' && line.status === 'success' && pie_in_v.status === 'success' && line_in_v.status === 'success' && pie_out_v.status === 'success' && line_out_v.status === 'success'){
           // console.log("success");
            if(i ==0){
              doc.addFileToVFS("THSarabunNew.ttf",fontTH.th);
        doc.addFont("THSarabunNew.ttf", "THSarabunNew", "Bold");
         doc.addFileToVFS('THSarabunNew-bold.ttf', THSarabunNewBold.font);
        doc.addFont('THSarabunNew-bold.ttf', 'THSarabunNewBold', 'bold');
        doc.setFont("THSarabunNew", "Bold");
        doc.setFontSize(18);
        doc.text("กองระบบเทคโนโลยีจราจร", 200, 30);
        doc.text("สำนักการจราจรและขนส่ง", 200, 50);
        doc.text("กรุงเทพมหานคร", 200, 70);
        doc.text("Report Volume & Cassification", 440, 30);
        doc.text("จุดติดตั้ง : "+this.textCheckpoint, 440, 76);
        doc.text("ถนน : "+this.roadName, 440, 53);
        doc.text("เดือน : "+this.date, 440, 98);
        doc.setFontSize(15);
        doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (ขาเข้า) (คัน)", 40, 135);
        const logo = require("@/assets/img/BMALogo3.jpg");
        
        var imgLogo = new Image();
        imgLogo.src = logo;
        // console.log("logo", this.imgURL);
        doc.addImage(imgLogo, "JPEG", 40, 20, 70, 70, undefined,'FAST');
        const CheckPoint1 = require("@/assets/img/checkpointPicture/"+index_pic+".png");
         var imgCheckPoint = new Image();
        imgCheckPoint.src = CheckPoint1;
        doc.addImage(imgCheckPoint, "PNG", 700, 20, 100, 100, undefined,'FAST');
       
          doc.setFontSize(15);
          doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (ขาออก) (คัน)", 40, 310);
          
  
           doc.autoTable({ html: '#mytableM1', startY: 140,styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 9,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
  
           doc.autoTable({ html: '#mytableM2', startY: 315,styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 9,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
  
          doc.setFontSize(15);
          doc.text("ปริมาณจราจรในแต่ละช่วงเวลา (คัน)", 40, 480);
          doc.autoTable({ html: '#mytableM3', startY: 485,styles: {
          font: "THSarabunNew",
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 9,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0], textColor: [0, 0, 0], lineWidth: 1.5 },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });
        
          this.genPDFAdmin2(line.data,pie.data,index_pic)
          this.genPDFAdmin_in_v(line_in_v.data,pie_in_v.data,index_pic)
          this.genPDFAdmin_out_v(line_out_v.data,pie_out_v.data,index_pic)
            }
           
          else{
              this.genPDFAdmin(index_pic)
              this.genPDFAdmin2(line.data,pie.data,index_pic)
             this.genPDFAdmin_in_v(line_in_v.data,pie_in_v.data,index_pic)
             this.genPDFAdmin_out_v(line_out_v.data,pie_out_v.data,index_pic)
            }
           
          }
        

        }
          resolve({
                  status: "success",
                });
            
          });
                
      }
    },
  };
  </script>
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Sarabun&display=swap');
  
  .font {
    font-family: 'Sarabun', sans-serif;
  }
  table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
  }
  </style>
  