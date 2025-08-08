<template>
  <v-container>
    <span v-if="headerShow == 'all'">ประเภทยานพาหนะ</span>
    <span v-else-if="headerShow == 'violate'">
      ประเภทยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด
    </span>

    <apexchart v-if="setSeries.length && Object.keys(setOptions).length" type="donut" :width="width" :height="height"
      :series="setSeries" :options="setOptions"></apexchart>
  </v-container>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
import * as am5 from "@amcharts/amcharts5";
import * as am5xy from "@amcharts/amcharts5/xy";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import * as am5percent from "@amcharts/amcharts5/percent";

export default {
  props: [
    "height",
    "headerShow",
    "btnShow",
    "textChart",
    "btnChart",
    "dataChart",
    "point",
  ],
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      width: "150",
      // กำหนดค่า default dataChart เพื่อป้องกัน undefined
      dataChartInternal: {
        series: [],
        options: {},
      },
      series: [44, 55, 41, 17, 15, 44, 55, 41, 17],
      chartOptions: {
        labels: [
          "รถจักรยานยนต์",
          "รถบรรทุก",
          "รถยนต์ส่วนบุคคล",
          "รถโดยสาร",
          "รถบรรทุกขนาดเล็ก",
          "รถตู้",
          "รถ SUV",
          "รถสามล้อเครื่ง",
          "อื่นๆ",
        ],
      },
    };
  },
  computed: {
    setOptions() {
      // ใช้ props dataChart ถ้ามี ไม่งั้นใช้ default internal
      return (this.dataChart && this.dataChart.options) || this.dataChartInternal.options;
    },
    setSeries() {
      if (this.dataChart && Array.isArray(this.dataChart.series)) {
        return this.dataChart.series;
      }
      return [];
    },
  },
  watch: {
    dataChart: {
      immediate: true,
      handler(newVal) {
        // อัพเดต dataChartInternal เมื่อ props dataChart เปลี่ยน เพื่อให้ computed ทำงานถูกต้อง
        if (newVal) {
          this.dataChartInternal = newVal;
        }
      },
    },
  },
  methods: {
    setoptions() {
      let label = [];
      this.series = [];
      if (!this.dataChart || !this.dataChart.volume) return;
      for (let i = 0; i < this.dataChart.volume.length; i++) {
        label.push(this.dataChart.volume[i].car_type);
        this.series.push(this.dataChart.volume[i].volume);
      }
      this.options = {
        chart: {
          type: "donut",
        },
        labels: label,
        total: {
          show: true,
        },
        dataLabels: {
          formatter: function (val, opts) {
            return opts.w.config.series[opts.seriesIndex];
          },
        },
      };
    },

    viewall() {
      console.log(this.point);
      if (this.point !== undefined) {
        if (this.textChart === "All Sensors") {
          this.$router.push({
            path: "/Device-Status-all-sensors",
            query: { checkpoint: this.point },
          });
        } else {
          this.$router.push({
            path: "/Device-Status-alarm",
            query: { checkpoint: this.point },
          });
        }
      } else {
        if (this.textChart === "All Sensors") {
          this.$router.push("/Device-Status-all-sensors");
        } else {
          this.$router.push("/Device-Status-alarm");
        }
      }
    },

    setNestChart() {
      var root = am5.Root.new("chartdiv");

      root.setThemes([am5themes_Animated.new(root)]);

      var chart = root.container.children.push(
        am5percent.PieChart.new(root, {
          radius: am5.percent(80),
          innerRadius: am5.percent(0.1),
        })
      );
      // Create series
      var series = chart.series.push(
        am5percent.PieSeries.new(root, {
          name: "Series",
          valueField: "sales",
          categoryField: "country",
        })
      );
      series.get("colors").set("colors", [am5.color(0x0ff000), am5.color(0xf0000f)]);
      series.data.setAll([
        {
          country: "France",
          sales: 100000,
        },
        {
          country: "Spain",
          sales: 160000,
        },
      ]);

      // Configuring slices
      series.slices.template.setAll({
        stroke: am5.color(0xffffff),
        strokeWidth: 2,
      });

      // Disabling labels and ticks
      series.labels.template.set("visible", false);
      series.ticks.template.set("visible", false);

      var series2 = chart.series.push(
        am5percent.PieSeries.new(root, {
          name: "Series",
          valueField: "sales",
          categoryField: "country",
          alignLabels: false,
        })
      );

      series2.get("colors").set("colors", [
        am5.color(0x00f0dc),
        am5.color(0x087f8c),
        am5.color(0x5aaa95),
        am5.color(0x86a873),
        am5.color(0xbb9f06),
      ]);

      series2.data.setAll([
        {
          country: "รถจักรยานยนต์",
          sales: 60000,
        },
        {
          country: "รถบรรทุก",
          sales: 60000,
        },
        {
          country: "รถยนต์ส่วนบุคคล",
          sales: 120000,
        },
        {
          country: "รถโดยสาร",
          sales: 90000,
        },
        {
          country: "รถบรรทุกขนาดเล็ก",
          sales: 60000,
        },
        {
          country: "รถตู้",
          sales: 60000,
        },
        {
          country: "รถ SUV",
          sales: 120000,
        },
        {
          country: "รถสามล้อเครื่อง",
          sales: 90000,
        },
      ]);

      // Configuring slices
      series2.slices.template.setAll({
        stroke: am5.color(0xffffff),
        strokeWidth: 2,
      });
      series2.labels.template.setAll({
        fontSize: 12,
        text: "{category}",
        textType: "adjusted",
        radius: 10,
      });
    },
  },
  mounted() {
    setTimeout(() => {
      this.width = "100%";
    }, 500);
    // this.setNestChart();
    // this.setoptions();
  },
};
</script>

<style>
#chartdiv {
  padding-top: 5%;
  width: 100%;
  height: 16em;
}
</style>
