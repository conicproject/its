<template>
  <div id="sidebar-new" style="overflow:initial;">
    <v-navigation-drawer v-model="isSelectedChild" app class="elevation-3 pr-3" height="100%" width="300">
      <div class="menu">
        <v-list-item>
          <v-list-item-content>
            <h1 class="logo">LOGO</h1>
          </v-list-item-content>
        </v-list-item>
        <ul v-for="item in dataMenuBar" :key="item.name">
          <div :class="{ activeHeader: item.path === activeIdOther }">
            <div class="menu pointer" v-if="item.child_obj && item.child_obj.length > 0"
              :class="{ activeHeader: item.path === activeIDMenu }">
              <li class="item pointer" @click="handleMenu(item.path, item.id)"
                :class="{ active: item.path === activeIDMenu }">
                <b>{{ item.name }}</b>
              </li>
              <!-- Dynamic child menu display -->
              <div class="menuChild pointer" v-show="activeIDMenu === item.path">
                <v-virtual-scroll :items="item.child_obj" height="100" item-height="35" class="ml-3 mr-3">
                  <template v-slot:default="{ item: child }">
                    <ul :key="child.type" style="padding-left:0px" v-if="child.is_active">
                      <li class="item pointer scroll" @click="menuChild(child.path, item.id, item.path)"
                        :class="{ activeChild: child.path === activeIdMenuChild }">
                        <b>{{ child.name }}</b>
                      </li>
                    </ul>
                    <ul style="padding-left:0px" v-else>
                      <li class="item pointer scroll disable">
                        <b>{{ child.name }}</b>
                      </li>
                    </ul>
                  </template>
                </v-virtual-scroll>
              </div>
            </div>
            <div v-else>
              <li class="item pointer" @click="other(item.path, item.id)"
                :class="{ active: item.path === activeIdOther }">
                <b>{{ item.name }}</b>
              </li>
            </div>
          </div>
        </ul>
      </div>
    </v-navigation-drawer>
    <noti :openSnackbar="snackbar" :date="date" @close="snackbar = false"></noti>
    <deviceNotification :display="showDeviceAlert" :message="deviceMsg" @close="showDeviceAlert = false" />
  </div>
</template>

<script>
const baseUrl = require('../../baseUrl.json');
import menuITMS from "./menu_itms.json";
import noti from "./noti-blacklist.vue";
import deviceNotification from "./notification-device.vue";

export default {
  props: ["sideNav", "listmenu"],
  components: {
    noti,
    deviceNotification
  },
  data() {
    return {
      dataMenuBar: menuITMS,
      isSelectedChild: null,
      activeIdOther: '',
      snackbar: false,
      date: "",
      showDeviceAlert: false,
      deviceMsg: '',
      checkingNotification: null,
      activeIDMenu: '',
      activeIdMenuChild: '',
      activeExpandId: null,
    };
  },
  watch: {
    sideNav(newVal) {
      if (this.$vuetify.breakpoint.width > 1025) {
        this.isSelectedChild = newVal;
      } else {
        this.isSelectedChild = true;
      }
    },
    listMenu(newVal) {
      console.log("listMenu", newVal);
    }
  },
  mounted() {
    this.initializeActiveMenu();
  },
  methods: {
    initializeActiveMenu() {
      // Get current path from URL
      const currentPath = this.$route.path;
      
      // Check saved paths for fallback
      const savedPath = localStorage.getItem('activepath');
      const savedHeaderPath = localStorage.getItem('activepathHeader');
      
      // Use current path if available, otherwise use saved path
      const pathToCheck = currentPath || savedPath;

      if (pathToCheck) {
        // Check if the path is a child menu
        const parentMenu = this.findParentMenuByChildPath(pathToCheck);
        
        if (parentMenu && (savedHeaderPath || currentPath)) {
          // It's a child menu
          this.activeIDMenu = savedHeaderPath || parentMenu.path;
          this.activeIdMenuChild = pathToCheck;
          this.activeIdOther = '';
        } else if (this.isParentMenuWithChildren(pathToCheck)) {
          // It's a parent menu with children
          this.activeIDMenu = pathToCheck;
          this.activeIdOther = '';
        } else {
          // It's a regular menu item
          this.activeIdOther = pathToCheck;
          this.activeIDMenu = '';
          this.activeIdMenuChild = '';
        }
        
        // Save current path to localStorage
        localStorage.setItem('activepath', pathToCheck);
      } else {
        // Default path
        this.activeIdOther = '/dashboard';
        localStorage.setItem('activepath', '/dashboard');
      }
    },

    findParentMenuByChildPath(childPath) {
      return this.dataMenuBar.find(menu => 
        menu.child_obj && menu.child_obj.some(child => child.path === childPath)
      );
    },

    isParentMenuWithChildren(path) {
      return this.dataMenuBar.some(menu => 
        menu.path === path && menu.child_obj && menu.child_obj.length > 0
      );
    },

    other(link, id) {
      this.activeIdOther = link;
      this.activeIDMenu = '';
      this.activeIdMenuChild = '';
      this.activeExpandId = null;
      
      // Save current path
      localStorage.setItem("activepath", link);
      // Remove header path for regular menu items
      localStorage.removeItem("activepathHeader");
      
      this.$router.push(link);
      console.log("Active menu main:", link);
    },

    handleMenu(link, id) {
      this.activeIdOther = '';
      this.activeIDMenu = link;
      
      // Find the menu item with children
      const menuItem = this.dataMenuBar.find(item => item.path === link);
      
      if (menuItem && menuItem.child_obj && menuItem.child_obj.length > 0) {
        // Find the first active child
        const firstActiveChild = menuItem.child_obj.find(child => child.is_active);
        
        if (firstActiveChild) {
          // Auto-select the first active child
          this.activeIdMenuChild = firstActiveChild.path;
          
          // Save paths to localStorage
          localStorage.setItem("activepath", firstActiveChild.path);
          localStorage.setItem("activepathHeader", link);
          
          // Navigate to the first child
          this.$router.push(firstActiveChild.path);
          console.log("Auto-selected first child:", firstActiveChild.path);
        } else {
          // No active children, just clear child selection
          this.activeIdMenuChild = '';
          localStorage.setItem("activepath", link);
          localStorage.removeItem("activepathHeader");
          this.$router.push(link);
        }
      } else {
        // No children, clear child selection
        this.activeIdMenuChild = '';
        localStorage.setItem("activepath", link);
        localStorage.removeItem("activepathHeader");
        this.$router.push(link);
      }
      
      console.log("menu menu:", link);
    },

    menuChild(link, id, parentPath) {
      this.activeIdMenuChild = link;
      this.activeIdOther = '';
      
      // Save child path
      localStorage.setItem("activepath", link);
      // Save parent path
      localStorage.setItem("activepathHeader", parentPath);
      
      this.$router.push(link);
      console.log("Active child menu:", link, id);
      console.log("Parent header:", parentPath);
    }
  }
};
</script>

<style scoped>
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
  border-radius: 5px;
  cursor: pointer;
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
  padding: 0;
}

.hscroll {
  overflow-x: scroll;
  overflow-y: hidden;
  white-space: nowrap;
}

#sidebar-new .v-list-item {
  cursor: pointer;
  flex: unset;
}

#sidebar-new .menu {
  display: flex;
  flex-direction: column;
  height: 100%;
}

#sidebar-new .dropdown {
  margin-top: auto;
  text-align: center;
}

#sidebar-new .elevation-3 {
  padding: 0 1rem !important;
}

#sidebar-new .btn_overview {
  background: #02754B;
  padding: 0.8rem;
  border-radius: 0.7rem;
  color: #FFFFFF;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

#sidebar-new .btn_overview::before {
  content: '';
  background-image: url('../assets/img/icon/Vector.png');
  width: 18px;
  height: 12px;
  margin-right: 1rem;
}

#sidebar-new .btn_dropdown {
  width: 100%;
  height: 50px !important;
  border-radius: 0.7rem;
  justify-content: space-between;
  background-color: #02754B;
}

#sidebar-new .logo {
  text-align: center;
  font-size: 4em;
  color: #02754B;
}

.activeHeader {
  background-color: #06a36a;
  color: rgb(255, 255, 255) !important;
  border-radius: 15px;
}

.activeChild {
  color: #54ff7f !important;
  font-weight: bold;
}
</style>