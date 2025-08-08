<template>
    <v-snackbar
      v-model="openSnackbar"
      right
      top
      :timeout="-1"
      color="red accent-2"
      
    >
    <v-container  >
        <v-layout>
        <v-flex>
            <v-icon class="noti" large>notifications_active</v-icon>
        </v-flex>
      <v-flex class="pt-1 pl-2">
        <h1>{{ text }}</h1>
        </v-flex>    
    </v-layout>
    <h3 @click="gotoBlacklist()" class="pointer text-right" >go to blacklist<v-icon>mdi-arrow-right-thick</v-icon></h3> 
    </v-container>
      <!-- <template v-slot:action="{ attrs }">
        <v-btn
          dark
          text
          v-bind="attrs"
          @click="gotoBlacklist"
        >
          ตรวจสอบ
        </v-btn>
      </template> -->
    </v-snackbar>
</template>
<script>
export default {
    props:["openSnackbar","date"],
     data() {
      return {
      text: `ตรวจพบ ยานพาหนะที่กำหนด`,
      test:true,
      }},
      watch:{
        openSnackbar:{ 
            handler(value, oldValue) {
          console.log(`Favorite color changed from ${oldValue} to ${value}`);
        }
         }
      },
      computed:{
        shower :{
            get() {
                if(this.show === true){
                //  console.log("show",this.dataItem);
                
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
      methods: {
        gotoBlacklist() {
           console.log("gotoBlacklist")
           let param = {
            'date' : this.date,
            'page' : 1
           }
           console.log(param);
        this.$router.push({ path: '/search-blacklist-table' ,query:param})
        localStorage.setItem('activepath','/vehicle/search-blacklist') 
        localStorage.setItem('activepathHeader','/vehicle/add') 
        this.$emit('close')
        },
      },
}
</script>
<style>
.noti{
  animation-name: example;
  animation-duration: 4s;
}
@keyframes example {
  0%   {left:0px; right:0px;}
  3%  {left:0px; right:5px;}
  9%  {left:5px; right:0px;}
  12%  {left:0px; right:5px;}
  15% {left:5px; right:0px;}
  18%   {left:0px; right:5px;}
  21%  {left:5px; right:0px;}
  24%  {left:0px; right:5px;}
  27%  {left:5px; right:0px;}
  30% {left:0px; right:5px;}
  33% {left:5px; right:0px;}
  36% {left:0px; right:5px;}
  39%  {left:5px; right:0px;}
  42%  {left:0px; right:5px;}
  45%  {left:5px; right:0px;}
  48% {left:0px; right:5px;}
  51% {left:5px; right:0px;}
  54% {left:0px; right:5px;}
  100% {left:0px; right:0px;}
}
.pointer {cursor: pointer;}
h3 {
  position: relative;
}

h3::before {
    content: '';
    position: absolute;
    width: 100%;
    height: 4px;
    border-radius: 4px;
    background-color: #ffffff;
    bottom: 0;
    left: 0;
    transform-origin: right;
    transform: scaleX(0);
    transition: transform .3s ease-in-out;
  }

h3:hover::before {
  transform-origin: left;
  transform: scaleX(1);
}
</style>