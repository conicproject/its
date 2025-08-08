<template>
  <div>
    <v-container v-if="checkPage == 'installpoint'">
      <span>{{ typeText }}</span>
      <v-select
        v-model="selectChart"
        :items="items_select"
        item-text="name"
        item-value="key"
        hide-details
        required
        dense
        outlined
        @change="fn_changChart(selectChart)"
      ></v-select>
    </v-container>

    <v-container v-else-if="checkPage == 'traffic'">
      <div v-if="$vuetify.breakpoint.width > 1024">
        <v-layout>
          <v-flex xs12 sm12>
            <span>{{ typeText }}</span>
          </v-flex>
          <v-flex xs12 sm12>
            <v-select
              v-model="selectChart"
              :items="items_select"
              item-text="name"
              item-value="key"
              hide-details
              required
              dense
              outlined
              @change="fn_changChart(selectChart)"
            ></v-select>
          </v-flex>
        </v-layout>
      </div>
      <div v-else>
        <v-flex xs12 sm12>
          <span>{{ typeText }}</span>
        </v-flex>
        <v-flex xs12 sm12>
          <v-select
            v-model="selectChart"
            :items="items_select"
            item-text="name"
            item-value="key"
            hide-details
            required
            dense
            outlined
            @change="fn_changChart(selectChart)"
          ></v-select>
        </v-flex>
      </div>
    </v-container>

    <v-container v-else>
      <div v-if="$vuetify.breakpoint.width > 1024">
        <v-layout>
          <v-flex offset-lg3 xs12 sm12>
            <v-select
              v-model="selectData"
              :items="items_selectData"
              item-text="name"
              item-value="key"
              hide-details
              required
              dense
              outlined
              @change="fn_changChartData(selectData)"
            ></v-select>
          </v-flex>
          <v-flex xs12 sm12>
            <v-select
              v-model="selectChart"
              :items="items_select"
              item-text="name"
              item-value="key"
              hide-details
              required
              dense
              outlined
              @change="fn_changChart(selectChart)"
            ></v-select>
          </v-flex>
        </v-layout>
      </div>
      <div v-else>
        <v-flex offset-lg3 xs12 sm12>
          <v-select
            v-model="selectData"
            :items="items_selectData"
            item-text="name"
            item-value="key"
            hide-details
            required
            dense
            outlined
            @change="fn_changChartData(selectData)"
          ></v-select>
        </v-flex>
        <v-flex xs12 sm12>
          <v-select
            v-model="selectChart"
            :items="items_select"
            item-text="name"
            item-value="key"
            hide-details
            required
            dense
            outlined
            @change="fn_changChart(selectChart)"
          ></v-select>
        </v-flex>
      </div>
    </v-container>

    <apexchart
      v-if="seriesReady"
      :width="width"
      height="100%"
      :type="typeChart"
      :options="options"
      :series="validatedSeries"
    ></apexchart>
    <div v-else>Loading chart data...</div>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";

export default {
  props: {
    dataChart: Object,
    dataIn: Array,
    dataOut: Array,
    cat: Array,
    checkPage: String,
    typeText: String,
    options: {
      type: Object,
      default: () => ({}),
    },
    series: {
      type: Array,
      default: () => [],
    },
    typeChart: String,
    dataText: {
      type: String,
      default: "all",
    },
  },

  components: {
    apexchart: VueApexCharts,
  },

  data() {
    return {
      headerTextChart: "",
      color: ["#FF9800", "#03A9F4"],
      stack: true,
      width: "150",
      selectChart: "bar",
      selectData: "all",
      items_select: [
        { key: "line", name: "กราฟเส้น" },
        { key: "bar", name: "กราฟแท่ง" },
      ],
      items_selectData: [
        {
          key: "all",
          name: "ปริมาณจราจรขาเข้าเมืองและขาออกเมือง (คัน)",
        },
        {
          key: "violate",
          name:
            "จำนวนยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด ขาเข้าและขาออกเมือง(คัน)",
        },
      ],
    };
  },

  computed: {
    validatedSeries() {
      if (!Array.isArray(this.series)) return [];
      return this.series.map((item) => ({
        name: item?.name || "Unnamed",
        data: Array.isArray(item?.data) ? item.data : [],
      }));
    },

    seriesReady() {
      return (
        Array.isArray(this.series) &&
        this.series.length > 0 &&
        this.series.every((s) => Array.isArray(s.data))
      );
    },
  },

  watch: {
    dataText(newVal) {
      this.fn_changChartData(newVal);

      this.headerTextChart =
        newVal === "all"
          ? "ปริมาณจราจรขาเข้าเมืองและขาออกเมือง (คัน)"
          : "จำนวนยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด ขาเข้าและขาออกเมือง(คัน)";
    },

    typeChart(newVal) {
      this.selectChart = newVal;
    },

    series(newVal) {
      // console.log("series updated:", newVal);
    },
  },

  methods: {
    fn_changChart(key) {
      this.typeChart = key;
      this.stack = key === "bar";
      this.$emit("stack", this.stack);
    },

    fn_changChartData(key) {
      this.stack = true;
      if (key === "all") {
        this.color = ["#FF9800", "#03A9F4"];
        this.$emit("color", "all");
      } else {
        this.color = ["#F44336", "#3F51B5"];
        this.$emit("color", this.color);
      }
    },
  },

  mounted() {
    this.headerTextChart =
      this.dataText === "all"
        ? "ปริมาณจราจรขาเข้าเมืองและขาออกเมือง (คัน)"
        : "จำนวนยานพาหนะที่ฝ่าฝืนสัญญาณไฟจราจรทางข้ามชนิดปุ่มกด ขาเข้าและขาออกเมือง(คัน)";

    setTimeout(() => {
      this.width = "100%";
    }, 500);
  },
};
</script>

<style scoped>
/* ใส่ style ถ้าต้องการ */
</style>
