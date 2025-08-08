<template>
  <div class="function-speed-container">
    <div class="content">
      <h2>ระบบเหตุการณ์</h2>
      <p>function_event - หน้าจอสำหรับจัดการระบบเหตุการณ์</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "FunctionSpeed",
  methods: {

  }
};
</script>

<style scoped>
.function-speed-container {
  padding: 20px;
}

.header-actions {
  margin-bottom: 20px;
}

.back-button {
  background: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.back-button:hover {
  background: #45a049;
}

.content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.content h2 {
  color: #333;
  margin-bottom: 10px;
}
</style>