<template>
  <v-app id="bg">
    <!-- Sidebar & Header -->
    <sidebar :sideNav="drawer" />
    <headerbar @close="toggleDrawer" class="nav-header" />

    <!-- Main Menu Content -->
    <v-container class="traffic-wrapper">
      <h1 class="title mb-6">Traffic Collection</h1>
      <hr /><br />
      <div class="traffic-grid">
        <div v-for="(item, index) in menuItems" :key="index" class="traffic-item hoverable text-center"
          @click="handleMenuClick(item)" :class="{ loading: loading }">
          <v-img class="box-menu" :src="getIconPath(item.icon)" :alt="item.title" contain />
          <span class="menu-title">{{ item.title }}</span>
        </div>
      </div>
    </v-container>
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
  name: "collection-combined",
  components: { sidebar, headerbar },
  data() {
    return {
      drawer: true,
      loading: false,
      menuItems: [
        { title: "ระบบค้นหาป้ายยานพาหนะ", icon: "enforce_1.png", route: "/collection/function/search" },
        { title: "ระบบบันทึกข้อมูลจราจร", icon: "enforce_2.png", route: "/collection/function/record" },
        { title: "รายงานสถิติการจราจร", icon: "enforce_3.png", route: "/collection/function/report" },
        // เพิ่มเมนูเพิ่มเติมได้ที่นี่
      ],
    };
  },
  methods: {
    toggleDrawer(param) {
      this.drawer = param;
    },
    handleMenuClick(menuItem) {
      if (this.loading) return;
      this.loading = true;

      Toast.fire({
        icon: 'info',
        title: `กำลังเข้าสู่ ${menuItem.title}`
      });

      setTimeout(() => {
        this.$router.push(menuItem.route).finally(() => {
          this.loading = false;
        });
      }, 500);
    },
    getIconPath(iconName) {
      try {
        return require(`@/assets/img/traffic-icons/${iconName}`);
      } catch (error) {
        console.error('Icon not found:', iconName);
        // ใช้ fallback สีเทา หรือ null แทน
        return null; // หรือใส่ path รูปอื่น เช่น require('@/assets/default-icon.png')
      }
    }
  },
  mounted() {
    console.log("Combined Collection Component Mounted");
  },
};
</script>

<style scoped>
#bg {
  background-color: #f5f5f5;
}

.nav-header {
  z-index: 1000;
}

.traffic-wrapper {
  max-width: 1280px;
  padding: 4rem 2rem;
  margin: 0 auto;
}

.title {
  font-weight: 600;
  font-size: 2rem !important;
  color: #333;
}

.traffic-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 2rem;
  cursor: pointer;
}

@media (max-width: 900px) {
  .traffic-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 600px) {
  .traffic-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .traffic-wrapper {
    padding: 2rem 1rem;
  }
}

.traffic-item {
  background: #fff;
  border-radius: 12px;
  padding: 1.5rem 1rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.07);
  transition: transform 0.2s ease, box-shadow 0.25s ease;
  border: 1px solid #e0e0e0;
}

.traffic-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.12);
  border-color: #1976d2;
}

.traffic-item:active {
  transform: translateY(-2px);
}

.box-menu {
  height: 100px;
  width: 100px;
  margin: 0 auto 1rem;
  border-radius: 8px;
}

.menu-title {
  display: block;
  width: 100%;
  max-width: 150px;
  margin: 0 auto;
  text-align: center;
  white-space: normal;
  word-wrap: break-word;
  font-size: 0.95rem;
  line-height: 1.25rem;
  color: #333;
  font-weight: 500;
}

.traffic-item.loading {
  opacity: 0.6;
  pointer-events: none;
}

.hoverable:hover .menu-title {
  color: #1976d2;
}
</style>
