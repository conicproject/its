import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import VueAxios from "vue-axios";
import router from '@/router'
const baseUrl = require('../../baseUrl.json')
import Swal from "sweetalert2/dist/sweetalert2.js";
const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});
Vue.use(Vuex);

Vue.use(VueAxios, axios);
export default new Vuex.Store({
  state: {
    menubar: [],
    data: {},
    carType: [],
  },
  mutations: {
    setMenubar(state, menubar) {
      state.menubar = menubar;
    },
    setDataSearch(state, data) {
      state.data = data
    },
    setLogOut(state, data) {
      state.menubar = {}
    }
  },
  actions: {

    async setMenubar({ commit }, menubar) {
      let session_data = localStorage.getItem("session");
      if (session_data) {
        try {
          var result = await axios.get(baseUrl.ipServer + "/menu-bar", { headers: { session: session_data } });
          console.log(result.data.status_code)
          if (result.data.status_code === 200) {
            let menuSuper = {
              "id": 11,
              "name": "CCTV เพื่อตรวจจับการฝ่าฝืนสัญญาณไฟจราจรบริเวณทางแยก",
              // "path": "/violation-crossroad",
              "path": "http://10.151.1.227:3000/",
              "child_obj": []
            }
            result.data.data.push(menuSuper);

            commit("setMenubar", result.data.data);
            return new Promise((resolve, reject) => {
              resolve({ status: "success", message: "success" });
            });
          } else {
            Toast.fire({
              icon: "error",
              title: "ไม่สามารถล็อกอินได้",
            });

            return new Promise((resolve, reject) => {
              reject({ status: "error", message: "error" });
            });
          }
        } catch (ex) {
          // Toast.fire({
          //   icon: "error",
          //   title: "ไม่สามารถล็อกอินได้",
          // });

          localStorage.clear();
          sessionStorage.clear();
          router.push("/");
          return new Promise((resolve, reject) => {
            reject({ status: "error", message: ex });
          });
        }
      }
    },
    logout({ commit }, data) {
      localStorage.clear();
      sessionStorage.clear();
      commit("setLogOut", data);
    },
    setDataSearch({ commit }, data) {
      commit("setDataSearch", data);
    },

  },
  getters: {
    dataMenuBar: (state) => {
      return state.menubar;
    },
    dataSearch: (state) => {
      return state.data
    },

  },
  modules: {},
});
