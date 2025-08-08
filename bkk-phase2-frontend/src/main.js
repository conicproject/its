import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
import 'canvas';
import axios from 'axios'
import VueAxios from "vue-axios";
import DisableAutocomplete from 'vue-disable-autocomplete';

Vue.use(DisableAutocomplete);
const VueScrollTo = require('vue-scrollto')
Vue.use(VueScrollTo)

Vue.use(VueSweetalert2);
Vue.use(VueAxios, axios);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
