<template>
  <div class="elevation-0" id="border" v-if="$vuetify.breakpoint.width > 900">
    <v-row>
      <v-col class="pb-0 rectangle">
        <v-container class="pa-0">
          <v-list-item v-for="item in [...this.Vehtype_1, ...this.Vehtype_2]" :key="'A' + item.id">
            <v-list-item-title class="pa-0">
              <v-row class="pb-1">
                <v-col cols="3" class="text-center pt-5 pb-0"><img width="100%" heigh="100%"
                    :src="require(`@/assets/img/vehicle/${item.image}`)" /></v-col>

                <v-col class="mt-0 mb-1">
                  <v-row>
                    <v-col class="pb-1">
                      <span class="textVeh">{{ item.name }}</span>
                    </v-col>
                  </v-row>
                  <v-row class="mt-0">
                    <v-col class="text-right"><span class="textNum">{{ item.dataWithComma }}</span><span
                        class="textUnit">&nbsp;&nbsp;คัน</span></v-col>
                    <v-col v-if="dataText.keyCard == 'violate'" class="text-right">
                      <span class="textNum">{{ item.percent }}</span>

                      <span class="textUnit">&nbsp;&nbsp;%</span></v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-list-item-title>
          </v-list-item>
        </v-container>
      </v-col>
      <!-- <v-divider vertical class="mt-3 mb-3"></v-divider> -->

    </v-row>
  </div>
</template>
<script>
export default {
  props: ["vehicle", "dataText"],
  data: function () {
    return {
      Vehtype_1: [],
      Vehtype_2: [],
    };
  },
  watch: {
    vehicle(newVal) {
      if (!newVal || !newVal.volume || !newVal.percent) {
        this.Vehtype_1 = [];
        this.Vehtype_2 = [];
        return;
      }

      this.Vehtype_1 = newVal.volume
        .filter((_, index) => index < 5)
        .map((item, index) => ({
          id: index,
          image: item.car_type + ".png",
          name: item.car_type,
          data: item.volume,
          dataWithComma: this.toCommas(item.volume),
          percent: newVal.percent[index]?.percent ? newVal.percent[index].percent.toFixed(0) : "0"
        }));

      this.Vehtype_2 = newVal.volume
        .filter((_, index) => index >= 5)
        .map((item, index) => ({
          id: 5 + index,
          image: item.car_type + ".png",
          name: item.car_type,
          data: item.volume,
          dataWithComma: this.toCommas(item.volume),
          percent: newVal.percent[5 + index]?.percent ? newVal.percent[5 + index].percent.toFixed(0) : "0"
        }));
    }
  },

  methods: {
    setCarType() {

      if (this.vehicle.volume) {
        this.Vehtype_1 = this.vehicle.volume
          .filter((_, index) => index < 5)
          .map((item, index) => ({
            id: index,
            image: item.car_type + ".png",
            name: item.car_type,
            data: item.volume,
            percent: this.vehicle.percent[index]['percent'].toFixed(0)
          }));

        this.Vehtype_2 = this.vehicle.volume
          .filter((_, index) => index >= 5)
          .map((item, index) => ({
            id: 4 + index,
            image: item.car_type + ".png",
            name: item.car_type,
            data: item.volume,
            percent: this.vehicle.percent[4 + index]['percent'].toFixed(0)
          }));

      }

    },
    toCommas(value) {
      return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }
  },
  mounted() {
    // console.log(this.Vehtype_2);
    this.$emit('changeSrceen')
    this.setCarType()
  }
};
</script>
<style>
.textVeh {
  font-weight: 400;
  font-size: 16px;
}

.textNum {
  font-weight: 500;
  font-size: 20px;
  color: #2463c1;
}

.textUnit {
  font-weight: 500;
  font-size: 16px;
}
</style>
