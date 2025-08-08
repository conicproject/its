<template>
  <div id="headerbar" class="d-flex">
    <v-btn text @click.stop="closeDrawer()"><v-icon>menu</v-icon></v-btn>
    <!-- <v-btn text @click="logout()" class="user"><img src="../assets/img/icon/user.png" alt=""></v-btn> -->
    <div class="box-right" style="display: flex; align-items: center;">
      <div class="time">Update ข้อมูลล่าสุด {{ timeUpdate }} น.</div>
      <v-btn text @click="logout()"><v-icon>logout</v-icon></v-btn>
    </div>
  </div>
</template>
<script>

import checkDevice from "./check-device.vue";
import Swal from "sweetalert2/dist/sweetalert2.js";
const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});
export default {
  components: {
    checkDevice
  },
  data() {
    return {
      timeUpdate: "",
      drawer: true,
      showNotification: false,
      checkingNotification: null,
    }
  },
  created() {
    let count_notification = localStorage.getItem('count_notification');
    if (count_notification > 0) {
      this.showNotification = true
    }
  },
  methods: {
    closeDrawer() {
      this.drawer = !this.drawer;
      // console.log(this.drawer);
      this.$emit('close', this.drawer)
    },
    logout() {
      Swal.fire({
        title: 'ต้องการออกจากระบบ ?',
        showDenyButton: false,
        showCancelButton: true,
        confirmButtonText: 'ตกลง',
        cancelButtonText: `ยกเลิก`,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
          this.$store.dispatch("logout");
          this.$router.push('/')
        }
      })

    },
    gotoBlacklist() {
      // let param = {
      //   'date' : this.formatDate(),
      //   'page' : 1
      // }

      let param = {
        'startdate': this.format2Date("s"),
        'enddate': this.format2Date("e"),
        'page': 1
      }

      this.$router.push({ path: '/search-blacklist-table', query: param })
      localStorage.setItem('activepath', '/vehicle/search-blacklist')
      localStorage.setItem('activepathHeader', '/vehicle/add')
    },
    format2Date(type) {
      var d = new Date(),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate() - 5,
        year = d.getFullYear();

      if (month.length < 2)
        month = '0' + month;
      if (day.length < 2)
        day = '0' + day;

      var d_end = new Date(),
        month_end = '' + (d_end.getMonth() + 1),
        day_end = '' + d_end.getDate(),
        year_end = d_end.getFullYear();

      if (month_end.length < 2)
        month_end = '0' + month_end;
      if (day_end.length < 2)
        daday_endy = '0' + day_end;

      let start = [year, month, day].join('-')
      let end = [year_end, month_end, day_end].join('-')

      if (type === "s") {
        return start;
      } else {
        return end;
      }

      return start + "/" + end;
    },
    formatDate() {
      var d = new Date(),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate() - 5,
        year = d.getFullYear();

      if (month.length < 2)
        month = '0' + month;
      if (day.length < 2)
        day = '0' + day;

      var d_end = new Date(),
        month_end = '' + (d_end.getMonth() + 1),
        day_end = '' + d_end.getDate(),
        year_end = d_end.getFullYear();

      if (month_end.length < 2)
        month_end = '0' + month_end;
      if (day_end.length < 2)
        daday_endy = '0' + day_end;

      let start = [year, month, day].join('-')
      let end = [year_end, month_end, day_end].join('-')

      return start + "/" + end;
    },
    getDate() {
      this.timeUpdate = new Date(
        Date.now() - new Date().getTimezoneOffset() * 60000
      )
        .toISOString()
        .substr(11, 5);
    },
  }, mounted() {
    this.getDate()
  },
  beforeDestroy() {
    clearInterval(this.checkingNotification)
  }
}
</script>
<style scoped>
.user {
  margin-top: 20px
}
#headerbar{
  background-color: #02754B;
  padding: 0.2em 0;
  height: 3rem;
}
#headerbar .box-right{
  margin-left: auto;
}
#headerbar .time{
  color: #FFFFFF;
  opacity: 50%;
  font-style: italic;
}
</style>