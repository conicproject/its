<template>
  <div style="overflow:initial;">
    <v-navigation-drawer v-model="isSelectedChild" app class="elevation-3 pr-3" height="100%" width="300">
      <v-list-item>
        <v-list-item-content>
          <img width="50%" height="45%" src="@/assets/img/logo_side_11zon.png" />
        </v-list-item-content>
      </v-list-item>

      <v-divider class="pb-3"></v-divider>

      <ul v-for="item in dataMenuBar" :key="item.name">
        <!-- ข้อมูลยานพาหนะที่กำหนด-->
         <p>id: {{item.id}}</p>
        <div v-if="item.id === 4" class="searchBlacklist pointer"
          v-bind:class="{ activeHeader: item.path === activeIdSearchBlacklist }">
          <li class="item pointer" @click="searchBlacklist(item.path, item.id)"
            v-bind:class="{ active: item.path === activeIdSearchBlacklist }">
            <b>{{ item.name }}</b>
          </li>
          <div class="searchChild pointer" v-show="testSearchBlacklist">
            <v-virtual-scroll class="ml-3 mr-3" :items="item.child_obj" height="110" item-height="30">
              <template v-slot:default="{ item }">
                <ul :key="item.type" style="padding-left:0px">
                  <li class="item pointer scroll" @click="searchBlacklistChild(item.path, item.id, item.id)"
                    v-bind:class="{ activeChild: item.path === activeIdSearchBlacklistChild }">
                    <b>{{ item.name }}</b>
                  </li>
                </ul>
              </template>
            </v-virtual-scroll>
          </div>
        </div>
        <!-- ข้อมูลยานพาหนะ-->
        <div v-else-if="item.id === 5" class="search pointer"
          v-bind:class="{ activeHeader: item.path === activeIdSearch }">
          <li class="item pointer" @click="searchVachine(item.path, item.id)"
            v-bind:class="{ active: item.path === activeIdSearch }">
            <b>{{ item.name }}</b>
          </li>
          <div class="searchChild pointer" v-show="testSearch">
            <v-virtual-scroll class="ml-3 mr-3" :items="item.child_obj" height="110" item-height="30">
              <template v-slot:default="{ item }">
                <ul :key="item.type" style="padding-left:0px">
                  <li class="item pointer scroll" @click="searchVachineChild(item.path, item.id, item.id)"
                    v-bind:class="{ activeChild: item.path === activeIdSearchChild }">
                    <b>{{ item.name }}</b>
                  </li>
                </ul>

              </template>
            </v-virtual-scroll>
          </div>
        </div>
        <!-- รายงานสถานะอุปกรณ์ -->
        <div v-else-if="item.id === 8" class="status pointer"
          v-bind:class="{ activeHeader: item.path === activeIdStatus }">
          <li class="item pointer" @click="statusDevice(item.path, item.id)"
            v-bind:class="{ active: item.path === activeIdStatus }">
            <b>{{ item.name }}</b>
          </li>
          <div class="statusChild pointer" v-show="testStatus">
            <v-virtual-scroll class="ml-3 mr-3" :items="item.child_obj" height="200" item-height="30">
              <template v-slot:default="{ item }">
                <ul :key="item.id" style="padding-left:0px" v-if="item.is_active">
                  <li class="item pointer scroll" @click="statusDeviceChild(item.path, item.id)"
                    v-bind:class="{ activeChild: item.path === activeIdStatusChild }">
                    <b class="scroll">
                      {{ item.name }}
                    </b>
                  </li>
                </ul>
                <ul style="padding-left:0px" v-else>
                  <li class="item pointer scroll" @click="statusDeviceChild(item.path, item.id)"
                    v-bind:class="{ activeChild: item.path === activeIdStatusChild }">
                    <b class="scroll disable">
                      {{ item.name }}
                    </b>
                  </li>
                </ul>
              </template>
            </v-virtual-scroll>
          </div>
        </div>
        <!-- ดูสภาพการจราจร -->
        <div class="watch pointer" v-else-if="item.id === 7" v-bind:class="{ activeHeader: item.path === activeIdWatch }">
          <li class="item pointer" @click="watchTraffic(item.path, item.id)"
            v-bind:class="{ active: item.path === activeIdWatch }">
            <b>{{ item.name }}</b>
          </li>
          <ul v-for="child in item.child_obj" :key="child.name" v-show="testWatch" style="padding-left:5%">
            <li class="item watchChild pointer" @click="watchTrafficChild(item.id, child)"
              v-bind:class="{ activeChild: child.path === activeIdWatchChild }">
              <b>{{ child.name }}</b>
            </li>
            <div>
              <v-virtual-scroll class="ml-3 mr-3" :items="child.child_obj" height="150" item-height="35"
                v-show="child.path === activeIdWatchChild">
                <template v-slot:default="{ item }">
                  <ul :key="item.id" style="padding-left:10%" v-if="item.is_active">
                    <li @click="watchTrafficSubChild(item)"
                      v-bind:class="{ activeSubChild: item.path === activeIdWatchSubChild }">
                      <b class="scroll">
                        {{ item.name }}
                      </b>
                    </li>
                  </ul>
                  <ul style="padding-left:10%" v-else>
                    <li>
                      <b class="scroll disable">
                        {{ item.name }}
                      </b>
                    </li>
                  </ul>
                </template>
              </v-virtual-scroll>
            </div>
          </ul>
        </div>
        <!-- จุดติดตั้ง -->
        <div class="installing pointer" v-else-if="item.id === 2"
          v-bind:class="{ activeHeader: item.path === activeIdInstalling }">
          <li class="item pointer" @click="installing(item.path, item.id)"
            v-bind:class="{ active: item.path === activeIdInstalling }">
            <b>{{ item.name }}</b>
          </li>
          <div class="installingChild pointer" v-show="testInstall">
            <v-virtual-scroll :items="item.child_obj" height="200" item-height="35" class="ml-3 mr-3">
              <template v-slot:default="{ item }">
                <ul :key="item.type" style="padding-left:0px" v-if="item.is_active">
                  <li class="item pointer scroll" @click="installChild(item.path, item.id)"
                    v-bind:class="{ activeChild: item.path === activeIdInstallChild }">
                    <b>
                      {{ item.name }}
                    </b>
                  </li>
                </ul>
                <ul style="padding-left:0px" v-else>
                  <li class="item pointer scroll disable">
                    <b>
                      {{ item.name }}
                    </b>
                  </li>
                </ul>
              </template>
            </v-virtual-scroll>
          </div>
        </div>
        <!-- system Configuration -->
        <div v-else-if="item.id === 10" class="admin pointer"
          v-bind:class="{ activeHeader: item.path === activeIdAdmin }">
          <li class="item pointer" @click="admin(item.path, item.id)"
            v-bind:class="{ active: item.path === activeIdAdmin }">
            <b>{{ item.name }}</b>
          </li>
          <div class="adminChild pointer" v-show="testAdmin">
            <v-virtual-scroll class="ml-3 mr-3" :items="item.child_obj" height="200" item-height="30">
              <template v-slot:default="{ item }">
                <ul :key="item.type" style="padding-left:0px">
                  <li class="item pointer scroll" @click="adminChild(item.path, item.id, item.id)"
                    v-bind:class="{ activeChild: item.path === activeIdAdminChild }">
                    <b>{{ item.name }}</b>
                  </li>
                </ul>

              </template>
            </v-virtual-scroll>
          </div>
        </div>

        <div v-else>
          <li class="item pointer" @click="other(item.path, item.id)"
            v-bind:class="{ active: item.path === activeIdOther }">
            <b>{{ item.name }}</b>
          </li>
        </div>


      </ul>


      <!-- <g> -->
      <!-- <div class="iBannerFix"> -->
      <v-card class="elevation-0 d-flex">
        <weather></weather>
      </v-card>

      <v-card class="weather-date elevation-0" color="#F4F4F4">
        <v-layout><span class="weather-text">{{ getDate.weekday }}</span><v-spacer></v-spacer><span
            class="weather-text">{{ getDate.time }}</span> </v-layout>
        <v-layout><span class="weather-text">{{ getDate.date }}</span> </v-layout>
      </v-card>
      <!-- </div> -->

      <!-- </g> -->


    </v-navigation-drawer>
    <noti :openSnackbar="snackbar" :date="date" @close="snackbar = false"></noti>
    <deviceNotification :display="showDeviceAlert" :message="deviceMsg" @close="showDeviceAlert = false">
    </deviceNotification>
  </div>
</template>

<script>
const baseUrl = require('../../baseUrl.json')
import noti from "./noti-blacklist.vue";
import { mapGetters } from "vuex";
import weather from "./weather-widget.vue";
import deviceNotification from "./notification-device.vue";


export default {
  props: ["sideNav", "listmenu"],
  components: {
    weather,
    noti,
    deviceNotification
  },
  data() {
    return {
      showDeviceAlert: false,
      checkingNotification: null,
      deviceMsg: "",
      menuBar: [],
      date: "",
      snackbar: false,
      isSelectedChild: null,
      activeColor: "blue",
      nameBar: {
        searchChild: 0,
        watchChild: 0,
        watchSubChild: 0,
        statusChild: 0,
      },
      items: ["Foo", "Bar", "Fizz", "Buzz", "Foo", "Bar", "Fizz", "Buzz", "Foo", "Bar", "Fizz", "Buzz"],
      right: null,
      status: false,
      report: false,
      search: false,
      traffic: false,
      present_model: true,
      past_model: false,
      testSearch: false,
      testAdmin: false,
      testStatus: false,
      testInstall: false,
      testWatch: false,
      testSearchBlacklist: false,
      activeIdSearch: 0,
      activeIdSearchChild: 0,
      activeIdSearchBlacklist: 0,
      activeIdSearchBlacklistChild: 0,
      activeIdOther: 0,
      activeIdStatus: 0,
      activeIdStatusChild: 0,
      activeIdInstalling: 0,
      activeIdInstallChild: 0,
      activeIdWatch: 0,
      activeIdWatchChild: 0,
      activeIdWatchSubChild: 0,
      activeIdAdmin: 0,
      activeIdAdminChild: 0,
    };
  },
  computed: {
    ...mapGetters(["dataMenuBar"]),
    getDate: function () {
      const d = new Date();
      const monthNames = [
        "มกราคม",
        "กุมภาพันธ์",
        "มีนาคม",
        "เมษายน",
        "พฤษภาคม",
        "มิถุนายน",
        "กรกฎาคม",
        "สิงหาคม",
        "กันยายน",
        "ตุลาคม",
        "พฤศจิกายน",
        "ธันวาคม",
      ];
      const month = d.getMonth();
      const weekday = [
        "อาทิตย์",
        "จันทร์",
        "อังคาร",
        "พุธ",
        "พฤหัสบดี",
        "ศุกร์",
        "เสาร์",
      ][d.getDay()];
      const date = `${d.getDate()}   ${monthNames[month]} ${d.getFullYear() + 543}`;
      const time = new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().substr(11, 5);
      return { date, weekday, time };
    },
  },
  watch: {
    sideNav: function () { // watch it 

      if (this.$vuetify.breakpoint.width > 1025) {
        this.isSelectedChild = this.sideNav;
      } else {
        this.isSelectedChild = true;
      }

      //console.log("sideNav", this.sideNav,this.isSelectedChild);
    },
    listMenu: function (newVal) { // watch it 


      console.log("listMenu", newVal);
    }

  },
  created() {

    this.menuBar = sessionStorage.getItem('menu')

    let myPath = this.$route.path.split("/");
    sessionStorage.setItem('myPath', this.$route.path)
    //console.log(myPath);
    let pathCheckPoint = ""
    for (let i = 1; i < myPath.length - 1; i++) {
      pathCheckPoint += "/" + myPath[i];
      //console.log(myPath[i]);
      if (i === myPath.length - 2) {
        pathCheckPoint += "/"
      }
    }
    let checkpath = localStorage.getItem('activepath')
    let checkpathHeader = localStorage.getItem('activepathHeader')

    if (this.$route.path === "/vehicle/add" ||
      this.$route.path === "/vehicle/list-blacklist" ||
      this.$route.path === "/vehicle/search-blacklist"
      //this.$route.path === "/vehicle/search"  || 
      //this.$route.path === "/vehicle/list-truck" 
      //  this.$route.path === "/add-vehicle-blacklist" ||
      //  this.$route.path === "/search-vehicle-detail" ||
      //  this.$route.path === "/truck-all" || 
      //  this.$route.path === "/add-vehicle-detail" 
    ) {
      //  console.log("checkpath",this.$route.path);
      this.testSearchBlacklist = true;
      this.activeIdSearchBlacklistChild = this.$route.path;
      // this.activeIdSearchBlacklist = checkpathHeader;
      this.activeIdSearchBlacklist = "/vehicle/add"


    } else if (this.$route.path === "/vehicle/search" ||
      this.$route.path === "/vehicle/list-truck" ||
      //  this.$route.path === "/add-vehicle-blacklist" ||
      // this.$route.path === "/search-vehicle-detail" ||
      this.$route.path === "/vehicle/search-violation"

      //  this.$route.path === "/add-vehicle-detail" 
    ) {
      this.testSearch = true;
      this.activeIdSearchChild = this.$route.path;
      // this.activeIdSearch = checkpathHeader;
      this.activeIdSearch = "/vehicle/search"

      //console.log("testSearch",this.testSearch);
    }
    else if (this.$route.path === "/add-vehicle-blacklist" ||
      //this.$route.path === "/search-vehicle-detail" || 
      // this.$route.path === "/add-vehicle-detail" || 
      //this.$route.path === "/vehicle/search"  || 
      // this.$route.path === "/truck-all" ||
      //this.$route.path === "/truck-detail" || 
      this.$route.path === "/search-blacklist-table"
    ) {

      this.testSearchBlacklist = true;
      this.activeIdSearchBlacklistChild = checkpath;
      // this.activeIdSearchBlacklist = checkpathHeader;
      this.activeIdSearchBlacklist = "/vehicle/add"


    } else if (this.$route.path === "/search-vehicle-detail" ||
      this.$route.path === "/search-violation-table" ||
      this.$route.path === "/truck-all" ||
      this.$route.path === "/truck-detail" ||
      this.$route.path === "/search-violation-detail" ||
      this.$route.path === "/add-vehicle-detail"
    ) {
      this.testSearch = true;
      this.activeIdSearchChild = checkpath;
      // this.activeIdSearch = checkpathHeader;
      this.activeIdSearch = "/vehicle/search"


    }
    else if (this.$route.path === "/user-management" ||
      this.$route.path === "/group-management" ||
      this.$route.path === "/permission-management" ||
      this.$route.path === "/installation-management" ||
      this.$route.path === "/camera-management" ||
      this.$route.path === "/road-management" ||
      // this.$route.path === "/secondary-road-management" ||
      this.$route.path === "/road-lane-management" ||
      this.$route.path === "/update-list-management"
    ) {
      this.testAdmin = true;
      this.activeIdAdminChild = this.$route.path;
      this.activeIdAdmin = checkpathHeader;

    }
    else if (this.$route.path === "/device-status") {
      this.testStatus = true;
      this.activeIdStatus = "/device-status"
      this.activeIdStatusChild = this.$route.path;

    } else if (pathCheckPoint === "/device-status/") {
      this.testStatus = true;
      this.activeIdStatus = "/device-status";
      this.activeIdStatusChild = this.$route.path;


    } else if (this.$route.path === "/Device-Status-alarm" || this.$route.path === "/Device-Status-all-sensors") {
      this.testStatus = true;
      this.activeIdStatus = "/device-status";
      this.activeIdStatusChild = checkpath;

    }
    else if (pathCheckPoint === "/installing/") {
      this.testInstall = true;
      this.activeIdInstalling = null;
      this.activeIdInstallChild = this.$route.path;
      // this.activeIdInstalling = checkpathHeader
      this.activeIdInstalling = "/installing/34"


    } else if (this.$route.path === "/traffic/present") {
      this.testWatch = true;
      // this.activeIdWatch = checkpathHeader;
      this.activeIdWatchChild = this.$route.path;
      this.past_model = false;
      this.present_model = true;
      this.activeIdWatch = "/traffic/present"

    } else if (pathCheckPoint === "/traffic/present/") {
      this.testWatch = true;
      this.activeIdWatch = checkpathHeader;
      this.activeIdWatchChild = "/traffic/present";
      this.activeIdWatchSubChild = this.$route.path
      this.past_model = false;
      this.present_model = true;

    } else if (this.$route.path === "/traffic/belated") {
      this.testWatch = true;
      this.past_model = true;
      this.present_model = false;
      this.activeIdWatch = checkpathHeader;
      this.activeIdWatchChild = "/traffic/belated";
      this.activeIdWatchSubChild = this.$route.path


      //console.log(this.activeIdInstallChild);
    } else if (pathCheckPoint === "/traffic/belated/") {
      this.testWatch = true;
      this.past_model = true;
      this.present_model = false;
      this.activeIdWatch = checkpathHeader;
      this.activeIdWatchChild = "/traffic/belated";
      this.activeIdWatchSubChild = this.$route.path

    }
    else if (this.$route.path === "/traffic-report" || this.$route.path === "/traffic-detail") {
      this.activeIdOther = "/traffic-detail"

    }
    else if (this.$route.path === "/origin-destination-detail" || this.$route.path === "/origin-destination-card" || this.$route.path === "/origin-destination-detail-table") {
      this.activeIdOther = "/origin-destination"

    }
    else {
      this.activeIdOther = this.$route.path


    }

    this.checkNotification()
  },
  methods: {
    searchVachine(link) {
      this.testSearch = true;
      this.activeIdSearch = link;

      this.activeIdInstalling = "";
      this.activeIdStatus = "";
      this.activeIdOther = ""
      this.activeIdWatch = ""

      this.testStatus = false;
      this.testWatch = false;
      this.testInstall = false;

      this.testAdmin = false;
      this.activeIdAdmin = "";

      this.testSearchBlacklist = false;
      this.activeIdSearchBlacklist = "";
      this.activeIdSearchBlacklistChild = link;
      localStorage.setItem("activepathHeader", link);
      this.$router.push(link);

    },
    searchBlacklist(link) {
      this.testSearchBlacklist = true;
      this.activeIdSearchBlacklist = link;

      this.activeIdInstalling = "";
      this.activeIdStatus = "";
      this.activeIdOther = ""
      this.activeIdWatch = ""

      this.testStatus = false;
      this.testWatch = false;
      this.testInstall = false;
      this.testSearch = false
      this.testAdmin = false;
      this.activeIdAdmin = "";
      this.activeIdSearch = "";
      this.activeIdSearchBlacklistChild = link;
      console.log("dd", link);
      localStorage.setItem("activepathHeader", link);
      this.$router.push(link);

    },
    searchVachineChild(link, id, headid) {
      this.$router.push(link);
      console.log(link);
      this.activeIdSearchChild = link;
      localStorage.setItem("activepath", link);

    },
    searchBlacklistChild(link, id, headid) {
      this.$router.push(link);
      console.log("dd", link);
      this.activeIdSearchBlacklistChild = link;
      localStorage.setItem("activepath", link);

    },
    admin(link) {
      this.testAdmin = true;
      this.activeIdAdmin = link;

      this.activeIdInstalling = "";
      this.activeIdStatus = "";
      this.activeIdOther = ""
      this.activeIdWatch = ""
      this.activeIdSearch = ""

      this.testStatus = false;
      this.testSearch = false;
      this.testWatch = false;
      this.testInstall = false;
      this.$router.push(link);

      this.activeIdSearchChild = link;
      localStorage.setItem("activepathHeader", link);
    },
    adminChild(link) {
      this.$router.push(link);

      this.activeIdSearchChild = link;
      localStorage.setItem("activepath", link);
    },
    statusDevice(link) {
      localStorage.setItem("activepath", link);
      this.testStatus === true
      this.$router.push(link);
      this.activeIdInstalling = "";
      this.activeIdSearch = "";
      this.activeIdWatch = "";
      this.activeIdOther = "";
      this.activeIdAdmin = ""

      this.testSearch = false;
      this.testWatch = false;
      this.testInstall = false;
      this.testAdmin = false;



    },
    statusDeviceChild(link, id) {
      localStorage.setItem("activepath", link);
      this.$router.push(link);
      this.activeIdStatusChild = link;
      console.log("activeIdStatusChild", link);
      this.$emit("loadPageStatus");

    },
    installing(link) {

      // localStorage.setItem("activepath", link);

      this.testInstall = true
      this.activeIdInstalling = link;

      this.activeIdSearch = "";
      this.activeIdStatus = "";
      this.activeIdWatch = "";
      this.activeIdOther = "";
      this.activeIdAdmin = "";

      this.testSearch = false;
      this.testWatch = false;
      this.testStatus = false;
      this.testAdmin = false;
      localStorage.setItem("activepath", link);
      localStorage.setItem("activepathHeader", link);

      this.$router.push(link);

    },
    installChild(link) {


      localStorage.setItem("activepath", link);

      this.$router.push(link);
      this.activeIdInstallChild = link;
      console.log(link);
      this.$emit("loadPage");

      //}
    },
    other(link) {
      console.log(link);
      localStorage.setItem("activepath", link);
      window.location.href = link;
      // window.open(link, '_blank');
      this.activeIdOther = link;
      this.activeIdSearch = "";
      this.activeIdStatus = "";
      this.activeIdWatch = "";
      this.activeIdInstalling = "";
      this.testInstall = false;
      this.testStatus = false;
      this.testSearch = false;
      this.testWatch = false;
      this.testAdmin = false;
      this.activeIdAdmin = "";

      this.testSearchBlacklist = false;
      this.activeIdSearchBlacklist = "";

    },
    watchTraffic(link,) {
      localStorage.setItem("activepath", link);
      localStorage.setItem("activepathHeader", link);
      this.testInstall = false;
      this.testStatus = false;
      this.testSearch = false;

      this.activeIdWatch = link
      this.testWatch = true
      this.activeIdSearch = "";
      this.activeIdStatus = "";
      this.activeIdInstalling = "";
      this.activeIdOther = "";

      this.testAdmin = false;
      this.activeIdAdmin = "";
      this.$router.push(link);

    },
    watchTrafficChild(main_id, child) {
      child.selected = !child.selected;
      console.log("test", child, name, this.dataMenuBar);
      this.dataMenuBar = JSON.parse(JSON.stringify(this.dataMenuBar.map(item => {
        if (item.id === main_id) {
          item.child_obj = item.child_obj.map(subitem => {
            if (subitem.name === child.name) {
              subitem.selected = true;

            } else {
              subitem.selected = false;
            }
            return subitem;
          });
        }
        return item;
      })))

      if (child.path === "/traffic/present") {
        console.log("test1", this.$route.path);
        if (this.$route.path !== "/traffic/present") {
          this.$router.push(child.path);
        }

        this.activeIdWatchSubChild = child.path
        this.past_model = false;
        this.present_model = true;

      } else {
        console.log("test2");
        //this.$router.push(child.path);
        //this.$router.push(child.path);
        this.activeIdWatchChild = "/traffic/belated"
        this.activeIdWatchSubChild = child.path
        this.past_model = true;
        this.present_model = false;

      }
    },
    watchTrafficSubChild(item) {
      //console.log("-----------------traffic",item);
      this.activeIdWatchSubChild = item.path;
      this.$router.push(item.path);
      this.$emit("loadPageTraffic");
    },
    childtest(item) {
      this.$router.push(item.path);
      if (item.key === "p") {
        // this.past_model = true;
        // this.present_model = false;
        localStorage.setItem("show", "past");
      } else if (item.key === "n") {
        // this.present_model = true;
        // this.past_model = true;
        localStorage.setItem("show", "now");
      }
    },
    openConnectNoti() {
      let session_data = localStorage.getItem("session");
      let url = baseUrl.ipServer + '/notification-blacklist?session=' + session_data

      var source = new EventSource(url);
      source.onmessage = this.onMessage
    },
    onMessage(event) {
      let extracted, sse_data;
      sse_data = event.data
      //console.log('sse from django---')
      //console.log(sse_data)

      extracted = JSON.parse(sse_data)
      //  console.log('sse response')
      //  console.log(extracted)
      //console.log(extracted.status)
      this.snackbar = extracted.status ? true : false
      this.date = extracted.date
      //console.log(this.snackbar);
    },

    checkNotification() {
      this.checkingNotification = setInterval(() => {

        let session_data = localStorage.getItem("session");
        let count_notification = Number(localStorage.getItem('count_notification'));
        let count_notification_device = Number(localStorage.getItem('device_fix'));
        let url = baseUrl.ipServer + "/blacklist-check"

        this.snackbar = false
        this.showDeviceAlert = false
        this.axios.get(url, { headers: { session: session_data } })
          .then((response) => {
            let _count = Number(response.data.data)
            let _count_device = Number(response.data.data_device)
            // console.log('fired...', _count)
            localStorage.setItem("count_notification", response.data.data);
            if (count_notification < _count) {
              // localStorage.setItem("count_notification", response.data.data);
              this.snackbar = true
              this.date = this.formatDate()
            }
            if (count_notification_device < _count_device) {
              localStorage.setItem("device_fix", _count_device);
              this.showDeviceAlert = true
              this.deviceMsg = this.formatDate()
            }
          }).catch((error) => {
            console.log(error);
          });
      }, 45000)
    },
    formatDate() {
      var d = new Date(),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

      if (month.length < 2)
        month = '0' + month;
      if (day.length < 2)
        day = '0' + day;

      let start = [year, month, day].join('-')
      let end = [year, month, day].join('-')

      return start + "/" + end;
    },
  },
  beforeDestroy() {
    clearInterval(this.checkingNotification)
  }
};
</script>

<style scoped>
/* .iBannerFix{
      height:50px;
      position:fixed;
      left:0px;
      bottom:0px;
      background-color:#00000000;
      width:100%;color:white;
      z-index: 99;
  } */
.v-sheet.v-card {
  border-radius: 10px;
}

.weather-text {
  color: #34B979;
  font-weight: 600;
}

.weather-date {
  padding: 5%;
  margin-left: 5%;
  margin-right: 5%;
  margin-bottom: 5%;
}

b {
  width: 100%;
  overflow: auto;
  overflow: scroll;
}

.scroll-auto {
  -webkit-overflow-scrolling: auto;
  /* Stops scrolling immediately */
}

.scroll {
  width: 170px;
  /* overflow: auto; */
  white-space: nowrap;
}

/* width */
::-webkit-scrollbar {
  width: 5px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #f1f1f100;

}

/* Handle */
::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0);
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0);
}

.pointer {
  cursor: pointer;
}

.disable {
  color: rgb(128, 127, 127) !important;
}

.active {
  background-color: #02754B;
  color: rgb(255, 255, 255) !important;
  border-radius: 15px;
  cursor: pointer;
}

.activeChild {
  cursor: pointer;
  color: #2463C1 !important;

}

.activeSubChild {
  cursor: pointer;
  color: #2463C1 !important;
}

.search.activeHeader {
  background-color: rgba(42, 158, 242, 0.59);
  color: rgb(255, 255, 255) !important;
  border-radius: 15px;
}

.searchBlacklist.activeHeader {
  background-color: rgba(42, 158, 242, 0.59);
  color: rgb(255, 255, 255) !important;
  border-radius: 15px;
}

.admin.activeHeader {
  background-color: rgba(42, 158, 242, 0.59);
  color: rgb(255, 255, 255) !important;
  border-radius: 15px;
}

.installing.activeHeader {
  background-color: rgba(42, 158, 242, 0.59);
  color: rgb(255, 255, 255) !important;
  border-radius: 15px;
}

.status.activeHeader {
  background-color: rgba(42, 158, 242, 0.59);
  color: rgb(255, 255, 255) !important;
  border-radius: 15px;
}

.watch.activeHeader {
  background-color: rgba(42, 158, 242, 0.59);
  color: rgb(255, 255, 255) !important;
  border-radius: 15px;
}

.activeChild.watchChild {
  color: #2463C1 !important;
  cursor: pointer;
}

.test {
  background-color: #68b6ff;
  color: rgb(0, 0, 0) !important;
  border-radius: 30px;
}

.bg-de {
  background-color: #68b6ff;
  color: rgb(0, 0, 0) !important;
  border-radius: 30px;
}

.item {
  padding: 10px;
}

.child {
  display: none;
}

a {
  text-decoration: none;
}

ul {
  list-style-type: none;
}

/* li{
    display: none;
} */
.hscroll {
  overflow-x: scroll;
  overflow-y: hidden;
  white-space: nowrap;
}

.custom-restricted {
  height: 90px;
  width: 150px;
  border: 1px solid white;
  border-radius: 4px;
  scroll-behavior: smooth;
}

div.scroll {
  margin: 4px, 4px;
  padding: 4px;
  /* background-color: green;  */
  /* width: 500px; 
                height: 70px;  */
  /* overflow-x: hidden; */
  overflow-x: auto;
  text-align: justify;
}

#abbbar {
  position: absolute;
  left: 100px;
  top: 100px;
  z-index: -1;
}

.v-list-group .v-list-group__header .v-list-item__icon.v-list-group__header__append-icon {
  align-self: center;
  margin: 0;
  min-width: 48px;
  justify-content: flex-end;
  display: none;
}

/* .list-group{
    max-height: 300px;
    margin-bottom: 10px;
    overflow:scroll;
    -webkit-overflow-scrolling: touch;
} */</style>
