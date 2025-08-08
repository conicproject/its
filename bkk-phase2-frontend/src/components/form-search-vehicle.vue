<template>
    <v-container justify-center align-center >
          <v-row>
            <v-col>
              <v-menu
                v-model="menu"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field hint="ช่วงเวลาที่ค้นหาข้อมูลสูงสุด 15 วัน" persistent-hint placeholder="วัน เดือน ปี พ.ศ."  outlined class="input-adddata rounded-lg sl mb-2" v-model="dayformat" readonly v-bind="attrs" v-on="on"></v-text-field>
                  <!-- <v-text-field persistent-hint placeholder="วัน เดือน ปี" outlined class="input-adddata rounded-lg sl mb-2" v-model="dateformat" readonly v-bind="attrs" v-on="on"></v-text-field> -->
                </template>
                <v-date-picker no-title range locale="th" :min="min" :max="maxSelectDate" v-model="date" @input="setTimeRange()" >
                  <v-spacer></v-spacer>
                  <v-btn outlined color="error" @click="cancle">ล้าง</v-btn>
                  <v-btn color="primary" @click="menu=false">ตกลง</v-btn></v-date-picker>
                <!-- <v-date-picker locale="th"  :max="maxSelectDate" v-model="date" @input="menu = false"></v-date-picker> -->
              </v-menu>
              </v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="selectPoint" :items="listCheckPoint"  item-value="name" item-text="name"  outlined hide-details label="จุดติดตั้ง" class="sl"></v-select></v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="selectDirection" :items="direction" outlined hide-details label="ทิศทางการจราจร" class="sl"></v-select></v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="selectColor" :items="listColor" outlined hide-details label="สียานพาหนะ" class="sl"></v-select></v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="selectCarType" :items="listCarType" outlined hide-details label="ประเภทยานพาหนะ" class="sl"></v-select></v-col>
          </v-row>
          <v-row>
            <v-col><v-select v-model="selectProvince" :items="listProvince" outlined hide-details label="จังหวัด" class="sl"></v-select></v-col>
          </v-row>
          <v-row>
            <v-col><v-text-field 
              v-model="textLicense"
            outlined label="ป้ายทะเบียนยานพาหนะ" 
            class="input-adddata rounded-lg sl"
            hint="กรณีไม่ทราบเลขทะเบียนแน่ชัด ให้ละค่านั้นด้วย x เช่น 2กx 8xx " persistent-hint
            ></v-text-field></v-col>
          </v-row>
          <v-row class="justify-center mt-16">
            <v-btn color="primary" @click="confirm()">ตกลง</v-btn>
          </v-row>
        </v-container>
</template>
<script>
export default {
  props:["listColor","listCarType","listProvince","listCheckPoint"],
  data() {
    return {
      menu: false,
      // date: "",
      date: [],
      maxSelectDate: new Date().toISOString().substr(0, 10),
      min:'2022-08-01',
      direction:[
        "ขาเข้า","ขาออก"
      ],
      selectCarType:"",
      selectColor:"",
      selectPoint:"",
      selectProvince:"",
      selectDirection:"",
      textLicense:"",
    };
  },
  computed:{
    dayformat(){
     
     if(this.date.length === 0){
      
      console.log("null");
       return []

     }else{
       let data1 = this.date[0].split("-");
       let year1 = parseInt(data1[0])+543;
       if(this.date[1] !== undefined){
         let data2 = this.date[1].split("-");
         let year2 = parseInt(data2[0])+543;
         return data1[2]+"-"+data1[1]+"-"+year1.toString()+" ~ "+data2[2]+"-"+data2[1]+"-"+year2.toString()
       }
      
       return data1[2]+"-"+data1[1]+"-"+year1.toString();
     }
     
     
   },
    dateformat(){
      if(this.date === ""){
        return ""

      }
       //console.log(new Date(this.date).toLocaleDateString('th-TH', {year: 'numeric', month: 'numeric', day:'numeric'}).replace('/', '-'))
       let dateformat = new Date(this.date).toLocaleDateString('th-TH', {year: 'numeric', month: 'numeric', day:'numeric'})
        let data = this.date.split("-");
        let year = parseInt(data[0])+543;
        return data[2]+"-"+data[1]+"-"+year.toString();
      
    },
  },
    methods:{
      cancle(){
      this.date = []
       this.min= '2022-08-01'
       this.maxSelectDate = new Date().toISOString().substr(0, 10)
       //this.menu=false
    },
    setTimeRange(){
      
      var now = new Date();
      var endDate = new Date(this.date[0]);
       endDate.setDate(endDate.getDate() + 14);
       now.setDate(now.getDate());
       this.min = this.date[0]
       if(now.getTime() < endDate.getTime()){
        
          this.maxSelectDate = now.toISOString().substr(0, 10)
       }else{
         this.maxSelectDate = endDate.toISOString().substr(0, 10)
       }
      //   let end = endDate.toISOString().substr(0, 10)
      //   let data = end.split("-");
      //   let year = parseInt(data[0])+543;
      //   return data[2]+"-"+data[1]+"-"+year.toString();
      //  this.maxSelectDate =
      },
        confirm(){       
          this.$emit('confirm',this.selectCarType,this.selectColor,this.selectPoint,this.selectProvince,this.selectDirection,this.date,this.textLicense)
        }
    }
}
</script>
<style>
.headertext{
  font-weight: 600;
  font-size: 24px;
  color: #FFFFFF;
}
.input-adddata {background-color: white; height: 56px;}
.sl {background: rgba(255, 255, 255, 0.9);border-radius: 15px;}
.search-vahicle {width: 50%;}
</style>