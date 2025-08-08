<template>
  <div class="speed-detection-container">
    <!-- ปุ่มเปิด/ปิดตัวกรอง -->
    <div class="page-header">
      <div class="header-left">
        <h2>ระบบตรวจจับการใช้ความเร็วเกินกำหนด</h2>
        <button class="settings-btn" @click="showFilter = !showFilter">
          <i :class="showFilter ? 'fas fa-eye-slash' : 'fas fa-cog'"></i>
        </button>
        <span class="ml-2" style="color: red; font-size: 13px;">
          #กดปุ่มนี้ เพื่อเปิด/ปิด ตัวกรอง
        </span>
      </div>
      <div class="header-right">
        <span class="record-count">พบ {{ filteredRecords.length }} รายการ</span>
        <button class="export-btn" @click="exportData">
          <i class="fas fa-download"></i> Export
        </button>
      </div>
    </div>

    <!-- ฟอร์มกรองข้อมูล -->
    <transition name="fade">
      <div v-if="showFilter" class="filter-form">
        <!-- Row 1 -->
        <div class="form-row">
          <input type="text" placeholder="ทะเบียนรถ" v-model="filter.plate" @input="resetPagination" />
          <input type="date" v-model="filter.date" @change="resetPagination" />
          <input type="text" placeholder="สถานที่" v-model="filter.location" @input="resetPagination" />
          <input type="text" placeholder="กล้องที่ตรวจจับ" v-model="filter.camera" @input="resetPagination" />
        </div>

        <!-- Row 2 -->
        <div class="form-row form-row-2">
          <input type="text" placeholder="ประเภทรถ" v-model="filter.vehicleType" @input="resetPagination" />
          <input type="number" placeholder="ความเร็วขั้นต่ำ" v-model.number="filter.minSpeed"
            @input="resetPagination" />
          <input type="number" placeholder="ความเร็วสูงสุด" v-model.number="filter.maxSpeed" @input="resetPagination" />
          <select v-model="filter.status" @change="resetPagination">
            <option value="">สถานะทั้งหมด</option>
            <option value="รอดำเนินการ">รอดำเนินการ</option>
            <option value="ยืนยัน">ยืนยัน</option>
            <option value="ปฏิเสธ">ปฏิเสธ</option>
          </select>
          <label class="checkbox-label">
            <input type="checkbox" v-model="filter.showVideo" />
            วิดีโอช่วงกระทำผิด
          </label>
        </div>

        <!-- Row 3 -->
        <!-- <div class="form-actions">
          <button class="clear-btn" @click="clearFilters">
            <i class="fas fa-times"></i> ล้างตัวกรอง
          </button>
        </div> -->
      </div>
    </transition>

    <!-- ตาราง -->
    <div class="table-container">
      <div v-if="loading" class="loading">กำลังโหลดข้อมูล...</div>
      <div v-else-if="paginatedRecords.length === 0" class="no-data">
        ไม่พบข้อมูลที่ตรงกับเงื่อนไขการค้นหา
      </div>
      <table v-else class="data-table">
        <thead>
          <tr>
            <th @click="sortBy('plateNumber')" class="sortable">
              ป้ายทะเบียน
              <i :class="getSortIcon('plateNumber')"></i>
            </th>
            <th>เลขป้ายทะเบียน</th>
            <th @click="sortBy('location')" class="sortable">
              สถานที่ตรวจวัด
              <i :class="getSortIcon('location')"></i>
            </th>
            <th @click="sortBy('vehicleType')" class="sortable">
              ประเภทรถ
              <i :class="getSortIcon('vehicleType')"></i>
            </th>
            <th @click="sortBy('actualSpeed')" class="sortable">
              ความเร็วที่ตรวจพบ
              <i :class="getSortIcon('actualSpeed')"></i>
            </th>
            <th @click="sortBy('dateTime')" class="sortable">
              วันที่ - เวลา
              <i :class="getSortIcon('dateTime')"></i>
            </th>
            <th @click="sortBy('speedLimit')" class="sortable">
              ความเร็วข้อกฎหมาย
              <i :class="getSortIcon('speedLimit')"></i>
            </th>
            <th @click="sortBy('camera')" class="sortable">
              กล้องที่ตรวจวัด
              <i :class="getSortIcon('camera')"></i>
            </th>
            <th @click="sortBy('status')" class="sortable">
              สถานะ
              <i :class="getSortIcon('status')"></i>
            </th>
            <th>จัดการ</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="record in paginatedRecords" :key="record.id">
            <td>
              <div class="license-plate">{{ record.plateNumber }}</div>
            </td>
            <td>{{ record.plateNumber }}</td>
            <td>{{ record.location }}</td>
            <td>{{ record.vehicleType }}</td>
            <td>
              <span class="speed-value" :class="{ 'over-speed': record.actualSpeed > record.speedLimit }">
                {{ record.actualSpeed }} km/h
              </span>
            </td>
            <td>{{ formatDateTime(record.dateTime) }}</td>
            <td>{{ record.speedLimit }} km/h</td>
            <td>{{ record.camera }}</td>
            <td>
              <span :class="['status-badge', getStatusClass(record.status)]">
                {{ record.status }}
              </span>
            </td>
            <td>
              <div class="action-buttons">
                <button class="btn-view" @click="viewRecord(record)">
                  <i class="fas fa-eye"></i> รายละเอียด
                </button>
                <button v-if="record.status === 'รอดำเนินการ'" class="btn-edit" @click="confirmRecord(record)">
                  <i class="fas fa-check"></i> ยืนยัน
                </button>
                <button v-if="record.status === 'รอดำเนินการ'" class="btn-delete" @click="rejectRecord(record)">
                  <i class="fas fa-times"></i> ปฏิเสธ
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Pagination -->
    <div class="pagination" v-if="filteredRecords.length > 0">
      <div class="pagination-info">
        แสดง {{ (currentPage - 1) * itemsPerPage + 1 }} - {{ Math.min(currentPage * itemsPerPage,
          filteredRecords.length) }}
        จาก {{ filteredRecords.length }} รายการ
      </div>
      <div class="pagination-controls">
        <button class="pagination-btn" :disabled="currentPage === 1" @click="prevPage">
          <i class="fas fa-chevron-left"></i> ก่อนหน้า
        </button>
        <span class="page-info">หน้า {{ currentPage }} จาก {{ totalPages }}</span>
        <button class="pagination-btn" :disabled="currentPage === totalPages" @click="nextPage">
          ถัดไป <i class="fas fa-chevron-right"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FunctionSpeed",
  data() {
    return {
      showFilter: true,
      currentPage: 1,
      itemsPerPage: 10,
      loading: false,
      sortKey: '',
      sortOrder: 'asc',
      filter: { plate: '', date: '', location: '', camera: '', vehicleType: '', minSpeed: null, maxSpeed: null, status: '', showVideo: true },
      allRecords: [
        { id: 1, plateNumber: "1กข-1234", location: "หยุดสีเขียว ควบคุมจราจร", vehicleType: "รถยนต์ส่วนตัว", actualSpeed: 125, dateTime: new Date("2024-06-27T14:12:00"), speedLimit: 100, camera: "CAM-002", status: "รอดำเนินการ", hasVideo: true },
        { id: 2, plateNumber: "5อธ-8765", location: "ถนนสุขุมวิท", vehicleType: "รถยนต์ส่วนตัว", actualSpeed: 135, dateTime: new Date("2024-06-27T11:25:00"), speedLimit: 120, camera: "CAM-004", status: "ยืนยัน", hasVideo: true },
        { id: 3, plateNumber: "3กง-9876", location: "ถนนเพชรบุรี", vehicleType: "รถบรรทุก", actualSpeed: 95, dateTime: new Date("2024-06-26T09:30:00"), speedLimit: 80, camera: "CAM-001", status: "รอดำเนินการ", hasVideo: false },
        { id: 4, plateNumber: "7กค-5432", location: "ถนนรัชดาภิเษก", vehicleType: "รถจักรยานยนต์", actualSpeed: 85, dateTime: new Date("2024-06-25T16:45:00"), speedLimit: 60, camera: "CAM-003", status: "ปฏิเสธ", hasVideo: true },
        { id: 5, plateNumber: "2ขก-1111", location: "ถนนพหลโยธิน", vehicleType: "รถยนต์ส่วนตัว", actualSpeed: 110, dateTime: new Date("2024-06-24T13:20:00"), speedLimit: 90, camera: "CAM-005", status: "ยืนยัน", hasVideo: true }
      ]
    };
  },
  computed: {
    filteredRecords() {
      let records = [...this.allRecords];
      const f = this.filter;

      if (f.plate.trim()) records = records.filter(r => r.plateNumber.toLowerCase().includes(f.plate.toLowerCase()));
      if (f.date) records = records.filter(r => new Date(r.dateTime).toDateString() === new Date(f.date).toDateString());
      if (f.location.trim()) records = records.filter(r => r.location.toLowerCase().includes(f.location.toLowerCase()));
      if (f.camera.trim()) records = records.filter(r => r.camera.toLowerCase().includes(f.camera.toLowerCase()));
      if (f.vehicleType.trim()) records = records.filter(r => r.vehicleType.toLowerCase().includes(f.vehicleType.toLowerCase()));
      if (f.minSpeed > 0) records = records.filter(r => r.actualSpeed >= f.minSpeed);
      if (f.maxSpeed > 0) records = records.filter(r => r.actualSpeed <= f.maxSpeed);
      if (f.status) records = records.filter(r => r.status === f.status);
      if (!f.showVideo) records = records.filter(r => !r.hasVideo);

      if (this.sortKey) {
        records.sort((a, b) => {
          let aVal = a[this.sortKey], bVal = b[this.sortKey];
          if (this.sortKey === 'dateTime') { aVal = new Date(aVal); bVal = new Date(bVal); }
          if (typeof aVal === 'string') { aVal = aVal.toLowerCase(); bVal = bVal.toLowerCase(); }

          if (aVal < bVal) return this.sortOrder === 'asc' ? -1 : 1;
          if (aVal > bVal) return this.sortOrder === 'asc' ? 1 : -1;
          return 0;
        });
      }
      return records;
    },
    totalPages() { return Math.ceil(this.filteredRecords.length / this.itemsPerPage); },
    paginatedRecords() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      return this.filteredRecords.slice(start, start + this.itemsPerPage);
    }
  },

  watch: { filteredRecords() { if (this.currentPage > this.totalPages && this.totalPages > 0) this.currentPage = 1; } },

  methods: {
    sortBy(key) {
      if (this.sortKey === key) this.sortOrder = this.sortOrder === 'asc' ? 'desc' : 'asc';
      else { this.sortKey = key; this.sortOrder = 'asc'; }
    },
    getSortIcon(key) {
      if (this.sortKey !== key) return 'fas fa-sort';
      return this.sortOrder === 'asc' ? 'fas fa-sort-up' : 'fas fa-sort-down';
    },
    getStatusClass(status) {
      const classes = { 'รอดำเนินการ': 'status-pending', 'ยืนยัน': 'status-confirmed', 'ปฏิเสธ': 'status-rejected' };
      return classes[status] || '';
    },
    formatDateTime(dateTime) {
      const date = new Date(dateTime);
      const day = date.getDate().toString().padStart(2, '0');
      const month = (date.getMonth() + 1).toString().padStart(2, '0');
      const year = date.getFullYear() + 543;
      const hours = date.getHours().toString().padStart(2, '0');
      const minutes = date.getMinutes().toString().padStart(2, '0');
      return `${day}/${month}/${year}; ${hours}:${minutes}น.`;
    },
    clearFilters() {
      this.filter = { plate: '', date: '', location: '', camera: '', vehicleType: '', minSpeed: null, maxSpeed: null, status: '', showVideo: true };
      this.currentPage = 1; this.sortKey = ''; this.sortOrder = 'asc';
    },
    resetPagination() { this.currentPage = 1; },
    viewRecord(record) { alert(`ดูรายละเอียดของ ${record.plateNumber}\nความเร็ว: ${record.actualSpeed} km/h\nสถานที่: ${record.location}`); },
    confirmRecord(record) {
      if (confirm(`คุณต้องการยืนยันรายการ ${record.plateNumber} หรือไม่?`)) {
        const index = this.allRecords.findIndex(r => r.id === record.id);
        if (index !== -1) this.allRecords[index].status = 'ยืนยัน';
      }
    },
    rejectRecord(record) {
      if (confirm(`คุณต้องการปฏิเสธรายการ ${record.plateNumber} หรือไม่?`)) {
        const index = this.allRecords.findIndex(r => r.id === record.id);
        if (index !== -1) this.allRecords[index].status = 'ปฏิเสธ';
      }
    },
    prevPage() { if (this.currentPage > 1) this.currentPage--; },
    nextPage() { if (this.currentPage < this.totalPages) this.currentPage++; },
    exportData() {
      const headers = ['ป้ายทะเบียน', 'สถานที่', 'ประเภทรถ', 'ความเร็วที่ตรวจพบ', 'วันที่-เวลา', 'ความเร็วกฎหมาย', 'กล้อง', 'สถานะ'];
      const csvRows = [headers.join(',')];
      this.filteredRecords.forEach(record => {
        const row = [record.plateNumber, record.location, record.vehicleType, `${record.actualSpeed} km/h`, this.formatDateTime(record.dateTime), `${record.speedLimit} km/h`, record.camera, record.status];
        csvRows.push(row.join(','));
      });

      const csvContent = '\uFEFF' + csvRows.join('\n');
      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
      const link = document.createElement('a');
      const url = URL.createObjectURL(blob);
      link.setAttribute('href', url);
      link.setAttribute('download', `speed_violations_${new Date().toISOString().split('T')[0]}.csv`);
      link.style.visibility = 'hidden';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  }
};
</script>

<style scoped>
.speed-detection-container {
  padding: 20px;
  background: #f5f5f5;
  min-height: calc(100vh - 3rem);
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  background: white;
  padding: 15px 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 15px;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 15px;
}

.record-count {
  color: #666;
  font-size: 14px;
  font-weight: 500;
}

.page-header h2 {
  margin: 0;
  color: #333;
  font-size: 18px;
}

.settings-btn {
  background: #eee;
  border: none;
  padding: 6px 10px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.2s;
}

.settings-btn:hover {
  background: #ddd;
}

.export-btn {
  background: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: background 0.2s;
}

.export-btn:hover {
  background: #45a049;
}

.filter-form {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.form-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 15px;
  align-items: center;
  margin-bottom: 15px;
}

.form-row-2 {
  grid-template-columns: repeat(5, 1fr);
}

.form-row:last-of-type {
  grid-template-columns: repeat(5, 1fr);
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  padding-top: 10px;
  border-top: 1px solid #eee;
}

.form-row input,
.form-row select {
  padding: 10px;
  font-size: 14px;
  border-radius: 4px;
  border: 1px solid #ccc;
  transition: border-color 0.2s;
}

.form-row input:focus,
.form-row select:focus {
  outline: none;
  border-color: #4CAF50;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  font-size: 14px;
}

.clear-btn {
  background: #f44336;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 5px;
  transition: background 0.2s;
}

.clear-btn:hover {
  background: #d32f2f;
}

.table-container {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.loading,
.no-data {
  text-align: center;
  padding: 40px;
  color: #666;
  font-size: 16px;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
}

.data-table th {
  background: #f8f9fa;
  padding: 12px 8px;
  text-align: center;
  font-weight: 500;
  color: #333;
  border-bottom: 2px solid #dee2e6;
  font-size: 14px;
  position: relative;
}

.sortable {
  cursor: pointer;
  user-select: none;
  transition: background 0.2s;
}

.sortable:hover {
  background: #e9ecef;
}

.sortable i {
  margin-left: 5px;
  opacity: 0.6;
}

.data-table td {
  padding: 12px 8px;
  text-align: center;
  border-bottom: 1px dashed #ddd;
  font-size: 13px;
}

.license-plate {
  background: #333;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-weight: bold;
  display: inline-block;
  min-width: 80px;
}

.speed-value {
  font-weight: 500;
}

.over-speed {
  color: #dc3545;
  font-weight: bold;
}

.status-badge {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
}

.status-pending {
  background: #fff3cd;
  color: #856404;
  border: 1px solid #ffeaa7;
}

.status-confirmed {
  background: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.status-rejected {
  background: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

.action-buttons {
  display: flex;
  gap: 5px;
  justify-content: center;
  flex-wrap: wrap;
}

.action-buttons button {
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 12px;
  display: flex;
  align-items: center;
  gap: 5px;
  transition: all 0.2s;
  white-space: nowrap;
}

.btn-view {
  background: #17a2b8;
  color: white;
}

.btn-view:hover {
  background: #138496;
}

.btn-edit {
  background: #28a745;
  color: white;
}

.btn-edit:hover {
  background: #218838;
}

.btn-delete {
  background: #dc3545;
  color: white;
}

.btn-delete:hover {
  background: #c82333;
}

.pagination {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: white;
  padding: 15px 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.pagination-info {
  color: #666;
  font-size: 14px;
}

.pagination-controls {
  display: flex;
  align-items: center;
  gap: 20px;
}

.pagination-btn {
  background: #fff;
  border: 1px solid #ddd;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 5px;
  transition: all 0.2s;
}

.pagination-btn:hover:not(:disabled) {
  background: #f8f9fa;
  border-color: #4CAF50;
}

.pagination-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-info {
  color: #666;
  font-size: 14px;
  font-weight: 500;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Responsive Design */
@media (max-width: 1200px) {
  .form-row {
    grid-template-columns: repeat(2, 1fr);
  }

  .form-row:last-of-type {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 768px) {
  .speed-detection-container {
    padding: 10px;
  }

  .page-header {
    flex-direction: column;
    gap: 15px;
    align-items: stretch;
  }

  .header-left,
  .header-right {
    justify-content: center;
  }

  .form-row,
  .form-row:last-of-type {
    grid-template-columns: 1fr;
  }

  .data-table {
    font-size: 12px;
  }

  .data-table th,
  .data-table td {
    padding: 8px 4px;
  }

  .action-buttons {
    flex-direction: column;
    gap: 3px;
  }

  .action-buttons button {
    font-size: 11px;
    padding: 5px 8px;
    gap: 3px;
  }

  .pagination {
    flex-direction: column;
    gap: 10px;
  }
}

@media (max-width: 480px) {
  .page-header h2 {
    font-size: 16px;
  }

  .table-container {
    overflow-x: auto;
  }

  .data-table {
    min-width: 800px;
  }
}
</style>