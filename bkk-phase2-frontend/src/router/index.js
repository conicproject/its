import Vue from "vue";
import VueRouter from "vue-router";
import login from "../views/login.vue";
import store from "../store";
Vue.use(VueRouter);

const ifAuthenticated = async (to, from, next) => {
  let session_ = localStorage.getItem("session");

  if (store.getters.dataMenuBar.length == 0) {

    store.dispatch("setMenubar").then(res => {
      // console.log(res);
    })
  }
  if (session_) {
    next();
    return;
  } else {
    next("/");
    return;
  }
};

const ifAuthenticatedLogin = (to, from, next) => {

  let session_ = localStorage.getItem("session");
  if (store.getters.dataMenuBar.length == 0) {
    store.dispatch("setMenubar").then(res => {
    })
  }
  if (session_) {
    next("/dashboard");
    return;
  } else {
    next();
    return;
  }
};

const metaTitle = "CPTS In Bangkok"

const routes = [
  {
    path: "/",
    name: "login",
    component: login,
    beforeEnter: ifAuthenticatedLogin,
    meta: { title: metaTitle }
  },
  {
    path: "/dashboard",
    name: "dashboard",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Dashboard.vue")
  },
  {
    path: "/traffic-detail",
    name: "traffic-detail",
    meta: { title: metaTitle },
    query: {},
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Traffic-Report.vue")
  },
  {
    path: "/traffic-report",
    name: "traffic-report",
    meta: { title: metaTitle },
    query: {},
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Traffic-Report-detail.vue")
  },
  {
    path: "/traffic/belated",
    name: "traffic-condition-belated",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Traffic-Condition-belated.vue")
  },
  {
    path: "/vehicle/add",
    name: "add-vehicle",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Add-Vehicle.vue")
  },
  {
    path: "/add-vehicle-detail",
    name: "add-vehicle-detail",
    meta: { title: metaTitle },
    query: {},
    params: {},
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Add-Vehicle-detail.vue")
  },
  {
    path: "/add-vehicle-blacklist",
    name: "add-vehicle-blacklist",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Add-Vehicle-blacklist.vue")
  },
  {
    path: "/vehicle/search",
    name: "search-vehicle",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Search-Vehicle.vue")
  },
  {
    path: "/search-vehicle-detail",
    name: "search-vehicle-detail",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Search-Vehicle-detail.vue")
  },
  {
    path: "/vehicle/search-blacklist",
    name: "search-vehicle-blacklist",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Search-Vehicle-blacklist.vue")
  },
  {
    path: "/vehicle/list-blacklist",
    name: "search-blacklist-detail",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Search-Blacklist-detail.vue")
  },
  {
    path: "/device-status/:id",
    name: "device-Status-report-point",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Device-Status-report-point.vue")
  },
  {
    path: "/installing/:id",
    name: "installing",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Installing-Point.vue")
  },
  {
    path: "/device-status",
    name: "device-Status-report",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Device-Status-report.vue")
  },
  {
    path: "/traffic/present",
    name: "traffic-Condition",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Traffic-Condition.vue")
  },
  {
    path: "/traffic/present/:id",
    name: "traffic-Condition-video",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Traffic-Condition-video.vue")
  },
  // {
  //   path: "/traffic/belated",
  //   name: "traffic-Condition",
  //   meta: { title: metaTitle },
  //   beforeEnter: ifAuthenticated,
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/Traffic-Condition.vue")
  // },
  {
    path: "/traffic/belated/:id",
    name: "traffic-Playblack-video",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Traffic-Playblack.vue")
  },
  {
    path: "/truck-all",
    name: "truck-all",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Truck-all.vue")
  },
  {
    path: "/truck-detail",
    name: "truck-detail",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Truck-detail.vue")
  },
  {
    path: "/vehicle/list-truck",
    name: "search-truck",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Search-truck.vue")
  },
  {
    path: "/Device-Status-all-sensors",
    name: "device-Status-all-sensors",
    meta: { title: metaTitle },
    query: {},
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Device-Status-all-sensors.vue")
  },
  {
    path: "/Device-Status-alarm",
    name: "device-Status-alarm",
    meta: { title: metaTitle },
    query: {},
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Device-Status-alarm.vue")
  },
  {
    path: "/error",
    name: "error",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/errorPage.vue")
  },
  {
    path: "/report-bkk",
    name: "report-bkk",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/exportAdmin.vue")
  },
  {
    path: "/search-blacklist-table",
    name: "search-blacklist-table",
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/search-blacklist-table.vue")
  },
  {
    path: "/blacklistpdf",
    name: "blacklistpdf",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/blacklistpdf.vue")
  },
  {
    path: "/traffic/live-view/:id/:subid",
    name: "traffic-Live-video",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/traffic-Live-video.vue")
  },
  {
    path: "/user-management",
    name: "user-management",
    meta: { title: metaTitle + " | System Configuration" },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../adminManagement/user-management.vue")
  },
  {
    path: "/group-management",
    name: "group-management",
    meta: { title: metaTitle + " | System Configuration" },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../adminManagement/group-management.vue")
  },
  {
    path: "/permission-management",
    name: "permission-management",
    meta: { title: metaTitle + " | System Configuration" },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../adminManagement/permission-management.vue")
  },
  {
    path: "/installation-management",
    name: "installation-management",
    meta: { title: metaTitle + " | System Configuration" },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../adminManagement/installation-management.vue")
  },
  {
    path: "/camera-management",
    name: "camera-management",
    meta: { title: metaTitle + " | System Configuration" },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../adminManagement/camera-management.vue")
  },
  {
    path: "/road-management",
    name: "road-management",
    meta: { title: metaTitle + " | System Configuration" },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../adminManagement/road-management.vue")
  },
  // {
  //   path: "/secondary-road-management",
  //   name: "secondary-road-management",
  //   meta: { title: metaTitle+" | System Configuration" },
  //   beforeEnter: ifAuthenticated,
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../adminManagement/secondary-road-management.vue")
  // },
  {
    path: "/road-lane-management",
    name: "road-lane-management",
    meta: { title: metaTitle + " | System Configuration" },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../adminManagement/road-lane-management.vue")
  },
  {
    path: "/update-list-management",
    name: "update-list-management",
    meta: { title: metaTitle + " | System Configuration" },
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../adminManagement/update-list-management.vue")
  },
  {
    path: "/origin-destination",
    name: "origin-destination",
    meta: { title: metaTitle },
    query: {},
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/origin-destination.vue")
  },
  {
    path: "/origin-destination-detail",
    name: "origin-destination-detail",
    meta: { title: metaTitle },
    query: {},
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/origin-destination-detail.vue")
  },
  {
    path: "/origin-destination-detail-table",
    name: "origin-destination-detail-table",
    meta: { title: metaTitle },
    query: {},
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/origin-destination-detail-table.vue")
  },
  {
    path: "/origin-destination-card",
    name: "origin-destination-card",
    meta: { title: metaTitle },
    query: {},
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/origin-destination-card.vue")
  },
  {
    path: "/vehicle/search-violation",
    name: "/vehicle/search-violation",
    meta: { title: metaTitle },
    query: {},
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/search-violation.vue")
  },
  {
    path: "/search-violation-table",
    name: "/search-violation-table",
    meta: { title: metaTitle },
    query: {},
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/search-violation-table.vue")
  },
  {
    path: "/search-violation-detail",
    name: "search-violation-detail",
    meta: { title: metaTitle },
    query: {},
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/search-violation-detail.vue")
  },
  {
    path: "/violation-crossroad",
    name: "violation-crossroad",
    meta: { title: metaTitle },
    query: {},
    beforeEnter: ifAuthenticated,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/violation-crossroad.vue")
  },
  {
    path: "/enforcement/dashboard",
    name: "enforcement-dashboard",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import("../views/traffic_enforcement/enforcement_dashboard.vue")
  },
  {
    path: '/enforcement/function',
    beforeEnter: ifAuthenticated,
    component: () => import("../views/traffic_enforcement/enforcement_function.vue"),
    children: [
      {
        path: '',
        name: 'enforcement-funcetion-menu',
        component: () => import("../views/traffic_enforcement/enforcement_menu.vue"),
      },
      {
        path: 'speed',
        name: 'enforcement-funcetion-speed',
        component: () => import("../views/traffic_enforcement/function/speed.vue"),
        meta: {
          title: 'ระบบตรวจจับการใช้ความเร็วเกินกำหนด'
        }
      },
      {
        path: "wrong_way",
        name: "enforcement-funcetion-wrong_way",
        meta: { title: metaTitle },
        beforeEnter: ifAuthenticated,
        component: () =>
          import("../views/traffic_enforcement/function/wrong_way.vue")
      },
      {
        path: "red_light",
        name: "enforcement-funcetion-red_light",
        meta: { title: metaTitle },
        beforeEnter: ifAuthenticated,
        component: () =>
          import("../views/traffic_enforcement/function/red_light.vue")
      },
      {
        path: "parking",
        name: "enforcement-funcetion-parking",
        meta: { title: metaTitle },
        beforeEnter: ifAuthenticated,
        component: () =>
          import("../views/traffic_enforcement/function/parking.vue")
      },
      {
        path: "lane",
        name: "enforcement-funcetion-lane",
        meta: { title: metaTitle },
        beforeEnter: ifAuthenticated,
        component: () =>
          import("../views/traffic_enforcement/function/lane.vue")
      },
      {
        path: "entrance",
        name: "enforcement-funcetion-entrance",
        meta: { title: metaTitle },
        beforeEnter: ifAuthenticated,
        component: () =>
          import("../views/traffic_enforcement/function/entrance.vue")
      },
      {
        path: "blacklist",
        name: "enforcement-funcetion-blacklist",
        meta: { title: metaTitle },
        beforeEnter: ifAuthenticated,
        component: () =>
          import("../views/traffic_enforcement/function/blacklist.vue")
      },
    ]
  },
  {
    path: "/collection/dashboard",
    name: "collection-dashboard",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import("../views/traffic_collection/collection_dashboard.vue")
  },
  {
    path: '/collection/function',
    beforeEnter: ifAuthenticated,
    component: () => import("../views/traffic_collection/collection_function.vue"),
    children: [
      {
        path: '',
        name: 'collection-funcetion-menu',
        component: () => import("../views/traffic_collection/collection_menu-bk.vue"),
      },
      {
        path: 'search',
        name: 'collection-funcetion-search',
        component: () => import("../views/traffic_collection/function/search.vue"),
        meta: {
          title: 'ระบบค้นหาป้ายยานพาหนะ'
        }
      },
    ]
  },
  {
    path: "/management/dashboard",
    name: "management-dashboard",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import("../views/traffic_management/management_dashboard.vue")
  },
  {
    path: '/management/function',
    beforeEnter: ifAuthenticated,
    component: () => import("../views/traffic_management/management_function.vue"),
    children: [
      {
        path: '',
        name: 'management-funcetion-menu',
        component: () => import("../views/traffic_management/management_menu.vue"),
      },
      {
        path: 'manage',
        name: 'management-funcetion-search',
        component: () => import("../views/traffic_management/function/manage.vue"),
        meta: {
          title: 'ระบบจัดการ'
        }
      },
    ]
  },
  {
    path: "/incident-accident/dashboard",
    name: "incident-accident-dashboard",
    meta: { title: metaTitle },
    beforeEnter: ifAuthenticated,
    component: () =>
      import("../views/traffic_incident_accident/incident_accident_dashboard.vue")
  },
  {
    path: '/incident-accident/function',
    beforeEnter: ifAuthenticated,
    component: () => import("../views/traffic_incident_accident/incident_accident_function.vue"),
    children: [
      {
        path: '',
        name: 'incident-accident-funcetion-menu',
        component: () => import("../views/traffic_incident_accident/incident_accident_menu.vue"),
      },
      {
        path: 'event',
        name: 'incident-accident-funcetion-event',
        component: () => import("../views/traffic_incident_accident/function/event.vue"),
        meta: {
          title: 'ระบบเหตุการณ์'
        }
      },
    ]
  },

];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

const DEFAULT_TITLE = metaTitle;

router.afterEach(to => {
  // Use next tick to handle router history correctly
  // see: https://github.com/vuejs/vue-router/issues/914#issuecomment-384477609
  Vue.nextTick(() => {
    document.title = to.meta.title || DEFAULT_TITLE;
  });

  // store.commit('setLoading', false)
});

export default router;
