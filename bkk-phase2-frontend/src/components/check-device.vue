<template>
  <div class="float">
    
    <v-menu top offset-y>
      <template v-slot:activator="{ on, attrs }">
        <!-- <v-btn absolute dark fab top right color="orange" v-bind="attrs" v-on="on"> -->
          <v-btn fab v-bind="attrs" v-on="on">
          <v-badge inline  color="error" v-if="showNotification" :content="numberAlert">
            <v-icon >build</v-icon>
          </v-badge>
          <v-icon v-else>build</v-icon>
        </v-btn>
      </template>
      
      <v-list dense>
        <v-subheader>REPORTS ({{numberAlert}})</v-subheader>
        
        <v-list-item-group v-model="selectedItem" color="primary">
          <v-list-item v-for="(item, i) in items" :key="i">
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
              <v-list-item-subtitle v-text="item.name"></v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>

        <v-list-item-group v-model="selectedItem" color="primary">
          <v-list-item v-for="(item, i) in item_ptrg" :key="i">
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title >{{item.text}} ({{item.type}})</v-list-item-title>
              <v-list-item-subtitle>{{item.checkpoint}} ip: {{item.ip}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>

      </v-list>
     
    </v-menu>
  </div>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
export default {
  data: () => ({
    showNotification: true,
    numberAlert: "0",
    checkingDevice: null,
    selectedItem: 0,
    numberCameraFix: 6,
    numberPtrgFix: 4,
    items:[],
    itemsBk: [
        {
            "code": "1aaad96bdb544e95ae72154fda74cde2",
            "text": "Camera",
            "icon": "videocam",
            "checkpoint": "หน้าวัดดอนเมือง ",
            "name": "DonMueang_Amari_OUT_C1"
        },
        {
            "code": "80543a5242e446a4a8c2a23c8bd33aca",
            "text": "Camera",
            "icon": "videocam",
            "checkpoint": "หน้าวัดดอนเมือง ",
            "name": "DonMueang_Amari_OUT_C2"
        },
        {
            "code": "a881ab60e0a34244b21faa7c9069ce44",
            "text": "Camera",
            "icon": "videocam",
            "checkpoint": "หน้าวัดดอนเมือง ",
            "name": "DonMueang_Amari_OUT_C4"
        },
        {
            "code": "41fee573bed644d99d6ae0e6d9589239",
            "text": "Camera",
            "icon": "videocam",
            "checkpoint": "หน้าวัดดอนเมือง ",
            "name": "DonMueang_Amari_IN_C1"
        },
        {
            "code": "6c66eaeba3e34c1e844400965d3d022a",
            "text": "Camera",
            "icon": "videocam",
            "checkpoint": "หน้าวัดดอนเมือง ",
            "name": "DonMueang_Amari_OUT_C3"
        },
        {
            "code": "f8b14fea254a4846b24bb4281629ad12",
            "text": "Camera",
            "icon": "videocam",
            "checkpoint": "หน้าวัดดอนเมือง ",
            "name": "DonMueang_Amari_IN_C2"
        }
    ],
    item_ptrg:[],
    item_ptrgBk:[
      {
          "id": "2081",
          "type": "switch",
          "checkpoint": "ถ.อ่อนนุช สุขุมวิท77\n",
          "text": "Device",
          "icon": "storage",
          "ip": "10.251.33.16"
      },
      {
          "id": "2123",
          "type": "ups",
          "checkpoint": "ถ.อ่อนนุช สุขุมวิท77\n",
          "text": "Device",
          "icon": "storage",
          "ip": "10.133.90.51"
      },
      {
          "id": "2124",
          "type": "terminal",
          "checkpoint": "ถ.อ่อนนุช สุขุมวิท77\n",
          "text": "Device",
          "icon": "storage",
          "ip": "10.133.90.52"
      },
      {
          "id": "2066",
          "type": "server",
          "checkpoint": null,
          "text": "Device",
          "icon": "storage",
          "ip": "10.151.1.74\n"
      },
    ]
  }),
  created() {
    this.getData()
  },
  methods: {

    calculate() {
      this.numberAlert = (this.numberCameraFix + this.numberPtrgFix).toString()
    },
    getData(){
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + "/camera-status"

      this.axios.get(url,{headers:{session:session_data}})
        .then((response) => {
          let data = response.data
          this.numberCameraFix = data.count_camera
          this.numberPtrgFix = data.count_ptrg

          this.items = data.data_camera
          this.item_ptrg = data.ptrg_data

          this.numberAlert = (this.numberCameraFix + this.numberPtrgFix).toString()

      }).catch((error) => {
        console.log(error);
      });
    }
  },
  mounted() {

  },
 
}
</script>
<style scoped>
/* .float {
  z-index: 4;
  position: fixed;
  bottom: 40px;
  right: 5px;
} */
.float {



  float: left;
}
.v-btn--fab.v-size--default {
    height: 30px;
    width: 60px;
    font-size: 10px;
}
.v-btn--round {
    border-radius: unset;
}
.v-btn--is-elevated.v-btn--fab {
    box-shadow: unset;
}
.v-btn--is-elevated {
    box-shadow: unset ;
}
.theme--light.v-btn.v-btn--has-bg {
    background-color: unset;
}


</style>