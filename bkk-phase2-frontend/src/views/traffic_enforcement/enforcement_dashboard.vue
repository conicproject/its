<template>
    <v-app id="bg">
        <sidebar :sideNav="drawer"></sidebar>
        <headerbar @close="headerbar" class="nav-header"></headerbar>
        <div class="header">
            <div class="logo-section">
                <div class="shield-icon">
                    <i class="fas fa-shield-alt"></i>
                </div>
                <div class="title-section">
                    <h1>Traffic Enforcement Dashboard</h1>
                    <p>ระบบจราจรและควบคุมการกระทำผิดกฎหมาย</p>
                </div>
            </div>
            <div class="time-section">
                <div class="current-time" id="currentTime">{{ currentTime }}</div>
                <div class="current-date">วันจันทร์ที่ 23 มิถุนายน 2568</div>
            </div>
        </div>

        <div class="stats-container">
            <div class="stat-card speeding">
                <div class="stat-icon speeding">S</div>
                <div class="stat-label">Speeding Violation<br>การขับรถเร็วเกินกำหนด</div>
                <div class="stat-number speeding">33,900 <span class="stat-unit">ครั้ง</span></div>
            </div>

            <div class="stat-card truck">
                <div class="stat-icon truck">T</div>
                <div class="stat-label">Truck Time<br>Restriction Violation</div>
                <div class="stat-number truck">11,300 <span class="stat-unit">ครั้ง</span></div>
            </div>

            <div class="stat-card red-light">
                <div class="stat-icon red-light">R</div>
                <div class="stat-label">Red Light Violation<br>ฝ่าไฟแดง</div>
                <div class="stat-number red-light">16,950 <span class="stat-unit">ครั้ง</span></div>
            </div>

            <div class="stat-card parking">
                <div class="stat-icon parking">P</div>
                <div class="stat-label">Parking Violation<br>จอดรถผิดกฎหมาย</div>
                <div class="stat-number parking">22,600 <span class="stat-unit">ครั้ง</span></div>
            </div>

            <div class="stat-card sidewalk">
                <div class="stat-icon sidewalk">W</div>
                <div class="stat-label">Driving on Sidewalk<br>ขับรถบนทางเท้า</div>
                <div class="stat-number sidewalk">9,040 <span class="stat-unit">ครั้ง</span></div>
            </div>

            <div class="stat-card lane">
                <div class="stat-icon lane">L</div>
                <div class="stat-label">Lane Changing<br>Over Solid Line</div>
                <div class="stat-number lane">13,560 <span class="stat-unit">ครั้ง</span></div>
            </div>
        </div>

        <div class="main-content">
            <div class="left-section">
                <div class="map-section">
                    <div class="section-title">
                        <i class="fas fa-map-marked-alt"></i>
                        แผนที่แสดงจุดติดตั้งกล้องการจราจร
                    </div>
                    <div class="map-container">
                        <div class="map-marker marker-1" @mouseenter="hoverMarker" @mouseleave="leaveMarker">S</div>
                        <div class="map-marker marker-2" @mouseenter="hoverMarker" @mouseleave="leaveMarker">T</div>
                        <div class="map-marker marker-3" @mouseenter="hoverMarker" @mouseleave="leaveMarker">R</div>
                        <div class="map-marker marker-4" @mouseenter="hoverMarker" @mouseleave="leaveMarker">P</div>
                        <div class="map-marker marker-5" @mouseenter="hoverMarker" @mouseleave="leaveMarker">W</div>
                        <div class="map-marker marker-6" @mouseenter="hoverMarker" @mouseleave="leaveMarker">L</div>
                    </div>
                    <div class="legend">
                        <div class="legend-item">
                            <div class="legend-color" style="background: #E53935;"></div>
                            <span>การขับรถเร็วเกินกำหนด</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background: #FB8C00;"></div>
                            <span>รถบรรทุกไม่ปฏิบัติตามเวลา</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background: #E53935;"></div>
                            <span>ฝ่าไฟแดง</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background: #FF7043;"></div>
                            <span>จอดรถผิดกฎหมาย</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background: #EC407A;"></div>
                            <span>ขับรถบนทางเท้า</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background: #FFC107;"></div>
                            <span>เปลี่ยนเลนผิดกฎหมาย</span>
                        </div>
                    </div>
                </div>

                <div class="chart-section">
                    <div class="section-title">
                        <i class="fas fa-chart-line"></i>
                        กราฟแสดงจำนวนการกระทำผิดกฎหมายการจราจร
                    </div>
                    <div class="chart-container">
                        <canvas id="violationChart"></canvas>
                    </div>
                </div>
            </div>

            <div class="right-section">
                <div class="stats-list">
                    <div class="section-title">
                        <i class="fas fa-list-ul"></i>
                        อันดับพื้นที่ที่มีการกระทำผิดมากที่สุด
                    </div>
                    <div class="stats-columns">
                        <div class="stats-column">
                            <h4>อันดับที่ 1-5</h4>
                            <div class="stat-item">
                                <span class="stat-name">ถ.เพชรบุรี</span>
                                <span class="stat-value">245 ครั้ง</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-name">ถ.ดาวกำดร้าน</span>
                                <span class="stat-value">230 ครั้ง</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-name">ถ.วิภาวดีรังสิต</span>
                                <span class="stat-value">215 ครั้ง</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-name">ถ.ลาดพร้าว</span>
                                <span class="stat-value">200 ครั้ง</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-name">ถ.ป่อเสื่อม</span>
                                <span class="stat-value">185 ครั้ง</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-name">ถ.จิตกาลิน</span>
                                <span class="stat-value">170 ครั้ง</span>
                            </div>
                        </div>
                        <div class="stats-column">
                            <h4>อันดับที่ 6-10</h4>
                            <div class="stat-item">
                                <span class="stat-name">ถ.ซอยเขมหรูก</span>
                                <span class="stat-value">230 ครั้ง</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-name">ถ.เพชรร่วม</span>
                                <span class="stat-value">215 ครั้ง</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-name">ถ.วิเศษกาญจน์</span>
                                <span class="stat-value">200 ครั้ง</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-name">ถ.ลาดพร้าว</span>
                                <span class="stat-value">185 ครั้ง</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-name">ถ.ประชาวิชยาน</span>
                                <span class="stat-value">170 ครั้ง</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-name">ถ.ราชวิถี</span>
                                <span class="stat-value">160 ครั้ง</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="warning-section">
                    <div class="section-title">
                        <i class="fas fa-exclamation-triangle"></i>
                        การกำหนดเวลาเตือนภัย
                    </div>
                    <div class="warning-grid">
                        <div class="warning-day">วันจันทร์</div>
                        <div class="warning-day">วันอังคาร</div>
                        <div class="warning-day">วันพุธ</div>
                        <div class="warning-day active">วันพฤหัส</div>
                        <div class="warning-day">วันศุกร์</div>
                        <div class="warning-day">วันเสาร์</div>
                        <div class="warning-day">วันอาทิตย์</div>
                    </div>
                </div>
            </div>
        </div>
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
    data() {
        return {
            drawer: true,
            currentTime: "14:20:39",
            timeInterval: null,
            chart: null
        };
    },
    methods: {
        headerbar(param) {
            this.drawer = param;
        },
        updateTime() {
            const now = new Date();
            this.currentTime = now.toLocaleTimeString('th-TH', { hour12: false });
        },
        initChart() {
            // Make sure Chart.js is loaded
            if (typeof Chart === 'undefined') {
                console.error('Chart.js is not loaded');
                return;
            }
            
            const ctx = document.getElementById('violationChart');
            if (!ctx) {
                console.error('Canvas element not found');
                return;
            }
            
            this.chart = new Chart(ctx.getContext('2d'), {
                type: 'line',
                data: {
                    labels: ['ม.ค.', 'ก.พ.', 'มี.ค.', 'เม.ย.', 'พ.ค.', 'มิ.ย.', 'ก.ค.', 'ส.ค.', 'ก.ย.', 'ต.ค.', 'พ.ย.', 'ธ.ค.'],
                    datasets: [
                        {
                            label: 'การขับรถเร็วเกินกำหนด',
                            data: [15000, 18000, 16000, 14000, 17000, 19000, 16000, 15000, 17000, 18000, 16000, 15000],
                            borderColor: '#E53935',
                            backgroundColor: 'rgba(229, 57, 53, 0.1)',
                            tension: 0.4
                        },
                        {
                            label: 'ฝ่าไฟแดง',
                            data: [8000, 9000, 8500, 7000, 8800, 9200, 8000, 7500, 8500, 9000, 8200, 7800],
                            borderColor: '#FB8C00',
                            backgroundColor: 'rgba(251, 140, 0, 0.1)',
                            tension: 0.4
                        },
                        {
                            label: 'จอดรถผิดกฎหมาย',
                            data: [12000, 13000, 12500, 11000, 13500, 14000, 12000, 11500, 13000, 13500, 12800, 12200],
                            borderColor: '#FF7043',
                            backgroundColor: 'rgba(255, 112, 67, 0.1)',
                            tension: 0.4
                        },
                        {
                            label: 'ขับรถบนทางเท้า',
                            data: [4000, 4500, 4200, 3800, 4600, 4800, 4000, 3900, 4300, 4500, 4100, 3950],
                            borderColor: '#EC407A',
                            backgroundColor: 'rgba(236, 64, 122, 0.1)',
                            tension: 0.4
                        },
                        {
                            label: 'เปลี่ยนเลนผิดกฎหมาย',
                            data: [6000, 6500, 6200, 5800, 6600, 6800, 6000, 5900, 6300, 6500, 6100, 5950],
                            borderColor: '#FFC107',
                            backgroundColor: 'rgba(255, 193, 7, 0.1)',
                            tension: 0.4
                        },
                        {
                            label: 'รถบรรทุกไม่ปฏิบัติตามเวลา',
                            data: [5000, 5200, 4800, 4500, 5100, 5300, 4900, 4700, 5000, 5200, 4950, 4800],
                            borderColor: '#9C27B0',
                            backgroundColor: 'rgba(156, 39, 176, 0.1)',
                            tension: 0.4
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                usePointStyle: true,
                                padding: 20,
                                font: {
                                    size: 11
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                callback: function(value) {
                                    return value.toLocaleString();
                                }
                            }
                        }
                    },
                    interaction: {
                        intersect: false,
                        mode: 'index'
                    }
                }
            });
        },
        hoverMarker(event) {
            event.target.style.transform = 'scale(1.3)';
            event.target.style.zIndex = '10';
        },
        leaveMarker(event) {
            event.target.style.transform = 'scale(1)';
            event.target.style.zIndex = '1';
        }
    },
    mounted() {
        // Start time update interval
        this.updateTime();
        this.timeInterval = setInterval(this.updateTime, 1000);
        
        // Initialize chart after component is mounted
        this.$nextTick(() => {
            this.initChart();
        });
    },
    beforeDestroy() {
        // Clean up interval when component is destroyed
        if (this.timeInterval) {
            clearInterval(this.timeInterval);
        }
        
        // Clean up chart when component is destroyed
        if (this.chart) {
            this.chart.destroy();
        }
    }
};
</script>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    background-color: #f5f5f5;
    color: #333;
}

.header {
    background: white;
    padding: 15px 30px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 3px solid #2196F3;
}

.logo-section {
    display: flex;
    align-items: center;
    gap: 15px;
}

.shield-icon {
    width: 50px;
    height: 50px;
    background: linear-gradient(45deg, #2196F3, #1976D2);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 24px;
}

.title-section h1 {
    font-size: 28px;
    font-weight: bold;
    color: #1976D2;
    margin-bottom: 5px;
}

.title-section p {
    font-size: 14px;
    color: #666;
}

.time-section {
    text-align: right;
}

.current-time {
    font-size: 24px;
    font-weight: bold;
    color: #333;
}

.current-date {
    font-size: 14px;
    color: #666;
}

.stats-container {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 20px;
    padding: 30px;
}

.stat-card {
    background: white;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    position: relative;
    overflow: hidden;
}

.stat-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
}

.stat-card.speeding::before {
    background: #E53935;
}

.stat-card.truck::before {
    background: #FB8C00;
}

.stat-card.red-light::before {
    background: #E53935;
}

.stat-card.parking::before {
    background: #FF7043;
}

.stat-card.sidewalk::before {
    background: #EC407A;
}

.stat-card.lane::before {
    background: #FFC107;
}

.stat-icon {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 15px;
    color: white;
    font-size: 20px;
    font-weight: bold;
}

.stat-icon.speeding {
    background: #E53935;
}

.stat-icon.truck {
    background: #FB8C00;
}

.stat-icon.red-light {
    background: #E53935;
}

.stat-icon.parking {
    background: #FF7043;
}

.stat-icon.sidewalk {
    background: #EC407A;
}

.stat-icon.lane {
    background: #FFC107;
}

.stat-label {
    font-size: 12px;
    color: #666;
    margin-bottom: 8px;
    line-height: 1.4;
}

.stat-number {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 5px;
}

.stat-number.speeding {
    color: #E53935;
}

.stat-number.truck {
    color: #FB8C00;
}

.stat-number.red-light {
    color: #E53935;
}

.stat-number.parking {
    color: #FF7043;
}

.stat-number.sidewalk {
    color: #EC407A;
}

.stat-number.lane {
    color: #FFC107;
}

.stat-unit {
    font-size: 14px;
    color: #999;
}

.main-content {
    display: grid;
    grid-template-columns: 1fr 300px;
    gap: 30px;
    padding: 0 30px 30px;
}

.left-section {
    background: white;
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.map-section {
    margin-bottom: 30px;
}

.section-title {
    font-size: 16px;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.map-container {
    height: 300px;
    background: #f0f0f0;
    border-radius: 8px;
    position: relative;
    overflow: hidden;
    background-image:
        linear-gradient(45deg, #e0e0e0 25%, transparent 25%),
        linear-gradient(-45deg, #e0e0e0 25%, transparent 25%),
        linear-gradient(45deg, transparent 75%, #e0e0e0 75%),
        linear-gradient(-45deg, transparent 75%, #e0e0e0 75%);
    background-size: 20px 20px;
    background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
}

.map-marker {
    position: absolute;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    color: white;
    font-size: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    cursor: pointer;
    transition: transform 0.2s;
}

.map-marker:hover {
    transform: scale(1.2);
}

.marker-1 {
    background: #E53935;
    top: 60px;
    left: 80px;
}

.marker-2 {
    background: #FB8C00;
    top: 120px;
    left: 120px;
}

.marker-3 {
    background: #E53935;
    top: 80px;
    left: 200px;
}

.marker-4 {
    background: #FF7043;
    top: 150px;
    left: 180px;
}

.marker-5 {
    background: #EC407A;
    top: 180px;
    left: 250px;
}

.marker-6 {
    background: #FFC107;
    top: 100px;
    left: 300px;
}

.legend {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-top: 15px;
    padding: 15px;
    background: #f8f9fa;
    border-radius: 8px;
}

.legend-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12px;
}

.legend-color {
    width: 12px;
    height: 12px;
    border-radius: 50%;
}

.chart-section {
    margin-top: 30px;
}

.chart-container {
    height: 250px;
    position: relative;
}

.right-section {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.stats-list {
    background: white;
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.stats-columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 15px;
}

.stats-column h4 {
    font-size: 14px;
    color: #2196F3;
    margin-bottom: 15px;
    padding-bottom: 8px;
    border-bottom: 2px solid #2196F3;
}

.stat-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0;
    border-bottom: 1px solid #eee;
}

.stat-item:last-child {
    border-bottom: none;
}

.stat-name {
    font-size: 13px;
    color: #666;
}

.stat-value {
    font-weight: bold;
    color: #333;
}

.warning-section {
    background: white;
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    border-left: 4px solid #FF9800;
}

.warning-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 15px;
    margin-top: 15px;
}

.warning-day {
    text-align: center;
    padding: 15px 5px;
    border: 2px dashed #ddd;
    border-radius: 8px;
    font-size: 12px;
    color: #666;
}

.warning-day.active {
    border-color: #FF9800;
    background: #FFF3E0;
    color: #FF9800;
}

@media (max-width: 1200px) {
    .stats-container {
        grid-template-columns: repeat(3, 1fr);
    }

    .main-content {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 768px) {
    .stats-container {
        grid-template-columns: repeat(2, 1fr);
    }

    .header {
        flex-direction: column;
        gap: 15px;
        text-align: center;
    }
}
</style>