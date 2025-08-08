<template>
    <v-app id="bg">
        <sidebar :sideNav="drawer"></sidebar>
        <headerbar @close="headerbar" class="nav-header"></headerbar>
        Data Collection
    </v-app>
</template>

<script>

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
    data: function () {
        return {
            drawer: true,
        };
    },
    methods: {
        headerbar(drawer) {
            this.drawer = drawer;
        },
    },
    mounted() {

    },
};
</script>
