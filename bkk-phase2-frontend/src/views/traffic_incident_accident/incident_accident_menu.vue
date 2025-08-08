<template>
  <v-container class="traffic-wrapper">
    <h1 class="title mb-6">Traffic Operating Management</h1>
    <hr /><br />
    <div class="traffic-grid">
      <div v-for="(item, index) in menuItems" :key="index" class="traffic-item hoverable text-center"
        @click="handleClick(item)">
        <v-img class="box-menu" :src="getIconPath(item.icon)" :alt="item.title" contain />
        <span class="menu-title">{{ item.title }}</span>
      </div>
    </div>
  </v-container>
</template>

<script>
export default {
  name: "incident-accident-menu",
  data() {
    return {
      menuItems: [
        { title: "ระบบเหตุการณ์", icon: "enforce_1.png", route: "/incident-accident/function/event"},
      ],
    }
  },
  methods: {
    handleClick(menuItem) {
      // เปลี่ยน route ไปยังหน้าที่ต้องการ
      this.$router.push(menuItem.route);
    },
    getIconPath(iconName) {
      try {
        return require(`@/assets/img/traffic-icons/${iconName}`);
      } catch (error) {
        console.error('Icon not found:', iconName);
        return '';
      }
    }
  }
};
</script>

<style scoped>
.traffic-wrapper {
  max-width: 1280px;
  padding: 4rem 2rem;
  margin: 0 auto;
}

.title {
  font-weight: 600;
  font-size: 2rem !important;
}

/* กำหนดให้ grid มี 5 คอลัมน์ตายตัว */
.traffic-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 2rem;
  cursor: pointer;
}

/* Responsive: ถ้าจอแคบกว่า 900px ให้ลดเหลือ 3 คอลัมน์ */
@media (max-width: 900px) {
  .traffic-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

/* Responsive: จอมือถือ ลดเหลือ 2 คอลัมน์ */
@media (max-width: 600px) {
  .traffic-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

.traffic-item {
  background: #fff;
  border-radius: 12px;
  padding: 1.5rem 1rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.07);
  transition: transform 0.2s, box-shadow 0.25s;
}

.traffic-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.12);
}

.box-menu {
  height: 100px;
  width: 100px;
  margin: 0 auto 1rem;
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
}
</style>