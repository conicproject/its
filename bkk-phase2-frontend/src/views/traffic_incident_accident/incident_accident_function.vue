<template>
  <v-app id="bg">
    <sidebar :sideNav="drawer" />
    <headerbar @close="headerbar" class="nav-header" />
    <router-view />
  </v-app>
</template>

<script>
const baseUrl = require("../../../baseUrl.json");

import sidebar from "../../components/sidebar-new.vue";
import headerbar from "../../components/header-bar.vue";
import Swal from "sweetalert2/dist/sweetalert2.js";

const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});

export default {
  components: { 
    sidebar, 
    headerbar,
  },
  data() {
    return {
      drawer: true,
    };
  },
  methods: {
    headerbar(param) {
      this.drawer = param;
    }
  },
  mounted() { },
};
</script>