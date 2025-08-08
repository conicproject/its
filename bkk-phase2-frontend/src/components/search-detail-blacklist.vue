<template>
    <v-container v-if="$vuetify.breakpoint.width > 1904">
      <v-layout justify-center class="pb-3">
        <v-flex lg3>
          <v-card height="100%" class="elevation-0 pa-3 text-center" id="bg-card"><span class="text-style">{{dataFilter.date}}</span></v-card>
        </v-flex>
        <v-flex lg6 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row
              ><v-col cols="4">
                <span class="title-style">จุดติดตั้ง:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.point}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
        <v-flex lg3 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col cols="7">
                <span class="title-style">ทิศทางการจราจร:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.direction}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex lg6>
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col cols="4" class="pr-0"><span class="title-style">สียานพาหนะ:</span></v-col>
              <v-col cols="2" class="pr-0"><span class="text-style">{{dataFilter.color}}</span></v-col>
              <v-divider vertical class="ma-2"></v-divider>
              <v-col class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col cols="2" class="text-right"> <span class="text-style">{{dataFilter.total}}</span></v-col>
              <v-col cols="2" class="text-right">
                <span class="title-style">คัน</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
        <v-flex lg6 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col height="100%" cols="4" class="pr-0"><span class="title-style">ประเภทยานพาหนะ:</span></v-col>
              <v-col height="100%" cols="2" class="pr-0"><span class="text-style">{{dataFilter.carType}}</span></v-col>
              <v-divider vertical class="ma-2"></v-divider>
              <v-col height="100%" class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col height="100%" cols="2" class="text-right"> <span class="text-style">{{dataFilter.total}}</span></v-col>
              <v-col height="100%" cols="2" class="text-right">
                <span class="title-style">คัน</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex lg6>
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col height="100%" cols="2" class="pr-0"><span class="title-style">จังหวัด:</span></v-col>
              <v-col height="100%" cols="4" class="pr-0"><span class="text-style">{{dataFilter.province}}</span></v-col>
              <v-divider vertical class="ma-2"></v-divider>
              <v-col height="100%"  class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col height="100%" cols="2" class="text-right"><span class="text-style">{{dataFilter.total}}</span></v-col
              ><v-col height="100%" cols="2" class="text-right">
                <span class="title-style">คัน</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
        <v-flex lg6 class="pl-3">
          <v-card height="100%" class="elevation-0 pa-3" id="bg-card">
            <v-row>
              <v-col height="100%" cols="4" class="pr-0"><span class="title-style">ทะเบียนยานพาหนะ:</span></v-col>
              <v-col height="100%" cols="2" class="pr-0"><span class="text-style">{{dataFilter.plate_no}}</span></v-col>
              <v-divider vertical class="ma-2"></v-divider>
              <v-col height="100%" class="pr-0">
                <span cols="2" class="title-style">จำนวน:</span> </v-col
              ><v-col height="100%" cols="2" class="text-right"> <span class="text-style">{{dataFilter.total}}</span></v-col
              ><v-col height="100%" class="text-right">
                <span cols="2" class="title-style">คัน</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout child-flex >
        <!-- <v-container> -->
        <v-data-table 
        :headers="headers" 
        :items="dataTable" 
        id="table-vehicle" 
        :items-per-page="20"
        :hide-default-footer="true"
        fluid fill-height
        loading-text="Loading"
      :loading="loading"
        >
          <template v-slot:[`header.picture`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.province`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.license`]="{ header }">
            <span>{{ header.text}}</span>
          </template>
          <template v-slot:[`header.type`]="{ header }">
            <span>{{ header.text}}</span>
          </template>
          <template v-slot:[`header.color`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.date`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.time`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.location`]="{ header }">
            <span>{{ header.text}}</span>
          </template>
          <template v-slot:[`header.direction`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.note`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
          <template v-slot:item="props">
            <tr>
              <td class="text-center"><img width="50%" height="50%" :src="props.item.picture"></td>
              <td class="text-center"><span style="font-size:20px;">{{ props.item.province }}</span></td>
              <td class="text-center"><span style="font-size:20px;">{{ props.item.license }}</span></td>
              <td class="text-center"><span style="font-size:20px;">{{ props.item.type }}</span></td>
              <td class="text-center"><span style="font-size:20px;">{{ props.item.color }}</span></td>
              <td class="text-center"><span style="font-size:20px;">{{ props.item.date }}</span></td>
              <td class="text-center"><span style="font-size:20px;">{{ props.item.time }}</span></td>
              <td class="text-center"><span style="font-size:20px;">{{ props.item.location }}</span></td>
              <td class="text-center" ><span style="font-size:20px;">{{ props.item.direction }}</span></td>
              <td  class="text-center">
                <v-btn text small @click="link(props.item)">
                 <v-icon>mdi-information-outline</v-icon>
                </v-btn>
              </td>
            </tr>
          </template>
        </v-data-table>
        <!-- </v-container> -->
      </v-layout>
    </v-container>
    <v-container v-else-if="$vuetify.breakpoint.width < 1904 && $vuetify.breakpoint.width > 1025">
      <v-layout justify-center class="pb-3">
        <v-flex lg3>
          <v-card class="elevation-0 pa-3 text-center" id="bg-card"><span class="text-style">{{dataFilter.date}}</span></v-card>
        </v-flex>
        <v-flex lg6 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card">
            <v-row
              ><v-col cols="3">
                <span class="title-style">จุดติดตั้ง:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.point}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
        <v-flex lg3 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col cols="7">
                <span class="title-style">ทิศทางการจราจร:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.direction}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex lg6>
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col cols="3" class="pr-0"><span class="title-style">สียานพาหนะ:</span></v-col>
              <v-col cols="3" class="pr-0"><span class="text-style">{{dataFilter.color}}</span></v-col>
              <v-divider vertical class="ma-2"></v-divider>
              <v-col class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col cols="2" class="text-right"> <span class="text-style">{{dataFilter.total}}</span></v-col>
              <v-col cols="2" class="text-right">
                <span class="title-style">คัน</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
        <v-flex lg6 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col cols="4" class="pr-0"><span class="title-style">ประเภทยานพาหนะ:</span></v-col>
              <v-col cols="2" class="pr-0"><span class="text-style">{{dataFilter.carType}}</span></v-col>
              <v-divider vertical class="ma-2"></v-divider>
              <v-col class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col cols="2" class="text-right"> <span class="text-style">{{dataFilter.total}}</span></v-col>
              <v-col cols="2" class="text-right">
                <span class="title-style">คัน</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex lg6>
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col cols="2" class="pr-0"><span class="title-style">จังหวัด:</span></v-col>
              <v-col cols="4" class="pr-0"><span class="text-style">{{dataFilter.province}}</span></v-col>
              <v-divider vertical class="ma-2"></v-divider>
              <v-col cols="2" class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col cols="2" class="text-right"> <span class="text-style">{{dataFilter.total}}</span></v-col
              ><v-col class="text-right">
                <span class="title-style">คัน</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
        <v-flex lg6 class="pl-3">
          <v-card class="elevation-0 pa-3" id="bg-card" height="100%">
            <v-row>
              <v-col cols="4" class="pr-0"><span class="title-style">ทะเบียนยานพาหนะ:</span></v-col>
              <v-col cols="2" class="pr-0"><span class="text-style">{{dataFilter.plate_no}}</span></v-col>
              <v-divider vertical class="ma-2"></v-divider>
              <v-col class="pr-0">
                <span cols="2" class="title-style">จำนวน:</span> </v-col
              ><v-col cols="2" class="text-right"> <span class="text-style">{{dataFilter.total}}</span></v-col
              ><v-col class="text-right">
                <span cols="2" class="title-style">คัน</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout child-flex >
        <!-- <v-container> -->
        <v-data-table 
        :headers="headers" 
        :items="dataTable" 
        id="table-vehicle" 
        :items-per-page="20"
        :hide-default-footer="true"
        fluid fill-height
        loading-text="Loading"
      :loading="loading"
        >
          <template v-slot:[`header.picture`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.province`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.license`]="{ header }">
            <span>{{ header.text}}</span>
          </template>
          <template v-slot:[`header.type`]="{ header }">
            <span>{{ header.text}}</span>
          </template>
          <template v-slot:[`header.color`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.date`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.time`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.location`]="{ header }">
            <span>{{ header.text}}</span>
          </template>
          <template v-slot:[`header.direction`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.note`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
          <template v-slot:item="props">
            <tr>
              <td class="text-center"><img width="50%" height="50%" :src="props.item.picture"></td>
              <td class="text-center"><span >{{ props.item.province }}</span></td>
              <td class="text-center"><span >{{ props.item.license }}</span></td>
              <td class="text-center"><span >{{ props.item.type }}</span></td>
              <td class="text-center"><span >{{ props.item.color }}</span></td>
              <td class="text-center"><span >{{ props.item.date }}</span></td>
              <td class="text-center"><span >{{ props.item.time }}</span></td>
              <td class="text-center"><span >{{ props.item.location }}</span></td>
              <td class="text-center" ><span >{{ props.item.direction }}</span></td>
              <td  class="text-center">
                <v-btn text small @click="link(props.item)">
                 <v-icon>mdi-information-outline</v-icon>
                </v-btn>
              </td>
            </tr>
          </template>
        </v-data-table>
        <!-- </v-container> -->
      </v-layout>
    </v-container>
  
    <v-container v-else>
      <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3 text-center" id="bg-card"><span class="text-style">{{dataFilter.date}}</span></v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3" id="bg-card" >
            <v-row
              ><v-col cols="4">
                <span class="title-style">จุดติดตั้ง:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.point}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3" id="bg-card">
            <v-row>
              <v-col cols="7">
                <span class="title-style">ทิศทางการจราจร:</span> </v-col
              ><v-col>
                <span class="text-style">{{dataFilter.direction}}</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3" id="bg-card">
            <v-row>
              <v-col cols="4" class="pr-0"><span class="title-style">สียานพาหนะ:</span></v-col>
              <v-col cols="2" class="pr-0"><span class="text-style">{{dataFilter.color}}</span></v-col>
              <v-divider vertical class="ma-2"></v-divider>
              <v-col class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col cols="2" class="text-right"> <span class="text-style">{{dataFilter.total}}</span></v-col>
              <v-col cols="2" class="text-right">
                <span class="title-style">คัน</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3" id="bg-card">
            <v-row>
              <v-col cols="4" class="pr-0"><span class="title-style">ประเภทยานพาหนะ:</span></v-col>
              <v-col cols="2" class="pr-0"><span class="text-style">{{dataFilter.carType}}</span></v-col>
              <v-divider vertical class="ma-2"></v-divider>
              <v-col class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col cols="2" class="text-right"> <span class="text-style">{{dataFilter.total}}</span></v-col>
              <v-col cols="2" class="text-right">
                <span class="title-style">คัน</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3" id="bg-card">
            <v-row>
              <v-col cols="2" class="pr-0"><span class="title-style">จังหวัด:</span></v-col>
              <v-col cols="4" class="pr-0"><span class="text-style">{{dataFilter.province}}</span></v-col>
              <v-divider vertical class="ma-2"></v-divider>
              <v-col cols="2" class="pr-0">
                <span class="title-style">จำนวน:</span> </v-col
              ><v-col cols="2" class="text-right"> <span class="text-style">{{dataFilter.total}}</span></v-col
              ><v-col class="text-right">
                <span class="title-style">คัน</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout justify-center class="pb-3">
        <v-flex>
          <v-card class="elevation-0 pa-3" id="bg-card">
            <v-row>
              <v-col cols="4" class="pr-0"><span class="title-style">ทะเบียนยานพาหนะ:</span></v-col>
              <v-col cols="2" class="pr-0"><span class="text-style">{{dataFilter.plate_no}}</span></v-col>
              <v-divider vertical class="ma-2"></v-divider>
              <v-col class="pr-0">
                <span cols="2" class="title-style">จำนวน:</span> </v-col
              ><v-col cols="2" class="text-right"> <span class="text-style">{{dataFilter.total}}</span></v-col
              ><v-col class="text-right">
                <span cols="2" class="title-style">คัน</span>
              </v-col>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
       <v-layout child-flex>
        <v-data-table 
        :headers="headers" 
        :items="dataTable" 
        id="table-vehicle" 
        :items-per-page="20"
        :hide-default-footer="true"
        loading-text="Loading"
      :loading="loading"
        >
          <template v-slot:[`header.picture`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.province`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.license`]="{ header }">
            <span>{{ header.text}}</span>
          </template>
          <template v-slot:[`header.type`]="{ header }">
            <span>{{ header.text}}</span>
          </template>
          <template v-slot:[`header.color`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.date`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.time`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.location`]="{ header }">
            <span>{{ header.text}}</span>
          </template>
          <template v-slot:[`header.direction`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <template v-slot:[`header.note`]="{ header }">
            <span>{{ header.text }}</span>
          </template>
          <!-- --------------------------------------------------------------------------------------------------------------------------------- -->
          <template v-slot:item="props">
            <tr>
              <td class="text-center"><img width="50" :src="props.item.picture"></td>
              <td class="text-center">{{ props.item.province }}</td>
              <td class="text-center">{{ props.item.license }}</td>
              <td class="text-center">{{ props.item.type }}</td>
              <td class="text-center">{{ props.item.color }}</td>
              <td class="text-center">{{ props.item.date }}</td>
              <td class="text-center">{{ props.item.time }}</td>
              <td class="text-center">{{ props.item.location }}</td>
              <td class="text-center">{{ props.item.direction }}</td>
              <td  class="text-right">
                <v-btn text small @click="link(props.item)">
                <v-icon>mdi-information-outline</v-icon>
                </v-btn>
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-layout>
    </v-container>
  </template>
  <script>
  export default {
    props: ["header", "dataTable","checkPage","dataFilter","dataPath", "queryPayload","loading"],
    data() {
      return {
        headers: this.header,

        export: [
          {
            i: 1,
            name: "save as..",
          },
          {
            i: 2,
            name: "Export PDF",
          },
          {
            i: 3,
            name: "Export Excel",
          },
        ],
      };
    },
    computed: {
      headerTable() {
        return {
          color: "red",
        };
      },
    },
    methods: {
      link(item) {
        // const dataQuery = this.$route.query
        //       let param ={
        //          'date': dataQuery.date,
        //          'time': dataQuery.date,
        //          'point': dataQuery.checkpoint || "-",
        //          'direction' : dataQuery.direction === "inbound" ? "ขาเข้า" : dataQuery.direction === "outbound"? "ขาออก":"-",
        //          'province': dataQuery.province || "-",
        //          'carType': dataQuery.vehicle_type || "-",
        //          'color': dataQuery.vehicle_color || "-",
        //          'plate_no': dataQuery.plate_no || "-",
        //       }
        item['queryPayload'] = this.$route.query
  
        this.$router.push({path:'/add-vehicle-blacklist', query:item,params:this.dataPath});

        // let route = this.$router.resolve({path:'/add-vehicle-blacklist', query:item,params:this.dataPath});
  
        // window.open(route.href, '_blank');
        
      },
    },
  
    mounted() {
    },
  };
  </script>
  <style>
  #table-vehicle table thead tr th:nth-child(1) , #table-vehicle table thead tr th:nth-child(2) ,
    #table-vehicle table thead tr th:nth-child(3) , #table-vehicle table thead tr th:nth-child(4) ,
    #table-vehicle table thead tr th:nth-child(5) , #table-vehicle table thead tr th:nth-child(6) ,
    #table-vehicle table thead tr th:nth-child(7) , #table-vehicle table thead tr th:nth-child(8) ,
    #table-vehicle table thead tr th:nth-child(9) , #table-vehicle table thead tr th:nth-child(10) 
    {background-color: #02754B; color: white; font-size: 18px;}
  
    #table-vehicle table tbody tr:nth-child(odd) {background-color: #ddf1fc;}
  </style>
  