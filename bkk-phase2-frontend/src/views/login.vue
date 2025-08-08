<template>
  <v-app>
    <v-overlay :value="onProgress">
      <v-progress-circular indeterminate size="100" width="7"></v-progress-circular>
    </v-overlay>
    
    <v-layout id="bg-login" row wrap align-center justify-center v-if="$vuetify.breakpoint.width > 1100">
      <v-flex xs12 lg7 class="ma-5" justify-center>
        <v-card class="mx-auto">
          <v-card-title class="justify-center logintextV2">
            <span class="headlogin">
              <span class="en">Intelligent traffic management system</span><br>
              <span class="th"> ระบบบริหารจัดการจราจรอัจฉริยะ</span>
            </span>
          </v-card-title>
        </v-card>
        <!-- <br /><br /> -->
        <v-card class="mx-auto pa-8" max-width="500">
          <form ref="form" @submit.prevent="handleLogin()">
            <h1 class="txt_login">LOGIN</h1>
            <v-card-text>
              <v-text-field v-model="username" filled rounded placeholder="USERNAME" name="username" class="user white-input" prepend-inner-icon="mdi-account-outline"></v-text-field>
              <v-text-field @click:append="showPassword = !showPassword" :type="showPassword ? 'text' : 'password'"
                :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" v-model="password" filled rounded
                placeholder="PASSWORD" name="password" class="white-input" prepend-inner-icon="mdi-lock-outline"></v-text-field>
            </v-card-text>
            <v-card-actions class="justify-center pt-0">
              <v-btn id="btn-signin" large type="submit"><span class="btn-text pa-7">LOGIN</span></v-btn>
            </v-card-actions>
          </form>
        </v-card>
      </v-flex>
    </v-layout>

    <v-layout id="bg-login" row wrap align-center justify-center
      v-else-if="$vuetify.breakpoint.width < 1100 && $vuetify.breakpoint.width > 627">
      <v-flex xs12 lg7 class="ma-5" justify-center>
        <v-card class="mx-auto">
          <v-card-title class="justify-center logintextV2">
            <span class="headlogin">
              <span class="en">Intelligent traffic management system</span><br>
              <span class="th">ระบบบริหารจัดการจราจรอัจฉริยะ</span>
            </span>
          </v-card-title>
        </v-card>
        <v-card class="mx-auto pa-8" max-width="500">
          <form ref="form" @submit.prevent="handleLogin()">
            <h1 class="txt_login">LOGIN</h1>
            <v-card-text>
              <v-text-field v-model="username" filled rounded placeholder="USERNAME" name="username" class="user white-input" prepend-inner-icon="mdi-account-outline"></v-text-field>
              <v-text-field @click:append="showPassword = !showPassword" :type="showPassword ? 'text' : 'password'"
                :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" v-model="password" filled rounded
                placeholder="PASSWORD" name="password" class="white-input" prepend-inner-icon="mdi-lock-outline"></v-text-field>
            </v-card-text>
            <v-card-actions class="justify-center pt-0">
              <v-btn id="btn-signin" large type="submit"><span class="btn-text pa-7">LOGIN</span></v-btn>
            </v-card-actions>
          </form>
        </v-card>
      </v-flex>
    </v-layout>

    <v-layout id="bg-login" row wrap align-center justify-center v-else>
      <v-flex xs12 lg7 class="ma-3" justify-center>
        <v-card class="mx-auto">
          <v-card-title class="justify-center logintextV2">
            <span class="headlogin">
              <span class="en">Intelligent traffic <br>management system</span><br>
              <span class="th">ระบบบริหารจัดการจราจรอัจฉริยะ</span>
            </span>
          </v-card-title>
        </v-card>
        <v-card class="mx-auto pa-6" max-width="400">
          <form ref="form" @submit.prevent="handleLogin()">
            <h1 class="txt_login">LOGIN</h1>
            <v-card-text>
              <v-text-field v-model="username" filled rounded placeholder="USERNAME" name="username" class="user white-input" prepend-inner-icon="mdi-account-outline"></v-text-field>
              <v-text-field @click:append="showPassword = !showPassword" :type="showPassword ? 'text' : 'password'"
                :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" v-model="password" filled rounded
                placeholder="PASSWORD" name="password" class="white-input" prepend-inner-icon="mdi-lock-outline"></v-text-field>
            </v-card-text>
            <v-card-actions class="justify-center pt-0">
              <v-btn id="btn-signin" large type="submit"><span class="btn-text pa-7">LOGIN</span></v-btn>
            </v-card-actions>
          </form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-app>
</template>

<script>
const baseUrl = require("../../baseUrl.json");
import VideoPlayer from "../components/VideoPlayer.vue";
import Swal from "sweetalert2/dist/sweetalert2.js";
const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});

export default {
  components: {
    VideoPlayer,
  },
  data() {
    return {
      onProgress: false,
      showPassword: false,
      username: "",
      password: "",
      playerOptions: {
        autoplay: true,
        controls: true,
        controlBar: {
          timeDivider: false,
          durationDisplay: false,
        },
      },
    };
  },
  computed: {
    player() {
      // ป้องกัน error กรณี this.$refs.videoPlayer ยังไม่มี
      return this.$refs.videoPlayer ? this.$refs.videoPlayer.player : null;
    },
    styleVideo() {
      return this.$vuetify.breakpoint.width > 950
        ? "width: 100%; height: 100%"
        : "width : 100%; height : 400px";
    },
  },
  methods: {
    handleLogin() {
      if (this.username === "" || this.password === "") {
        Toast.fire({
          icon: "error",
          title: "กรุณากรอกข้อมูลให้ครบถ้วน",
        });
        return;
      }

      const payload = {
        name: this.username,
        password: this.password,
      };
      console.log('baseUrl.ipServer  :>> ', baseUrl.ipServer );
      const url = baseUrl.ipServer + "/login";
      this.onProgress = true;
      this.axios
        .post(url, payload, { headers: { session: "" } })
        .then((response) => {
          console.log(response);
          localStorage.setItem("session", response.data.data.session);
          localStorage.setItem(
            "count_notification",
            response.data.count_notification
          );
          this.$store.dispatch("setMenubar").then((res) => {
            if (res.status === "success") this.$router.push("/dashboard");
            // if (res.status === "success") this.$router.push("/dashboard-itms");
          });
          this.onProgress = false;
        })
        .catch((error) => {
          console.log(error);
          this.onProgress = false;
          Toast.fire({
            icon: "error",
            title: "ไม่สามารถเข้าสู่ระบบได้ กรุณากรอกข้อมูลให้ถูกต้อง",
          });
        });
    },
    onPlayerPlay(player) { },
    onPlayerReady(player) {
      if (this.player) {
        this.player.play();
      }
    },
    playVideo(source) {
      console.log("ssd", source);
      source = "http://110.171.165.57:83/openUrl/e1CeuYM/live.m3u8";
      if (this.player) {
        this.player.src(source);
        this.player.play();
      }
    },
  },
  beforeDestroy() {
    // ป้องกัน error กรณี player ยังไม่มี
    if (this.player) {
      this.player.dispose();
    }
  },
};
</script>
<style>
@import "../assets/css/background.css";

/* @import '../sass/variables.scss'; */
.formlogin {
  margin-left: 25%;
  margin-right: 25%;
}

.formlogin-mobile {
  margin-left: 5%;
  margin-right: 5%;
}

.formtext-mobile {
  margin-left: 5%;
  margin-right: 5%;
}

.btn-text {
  font-weight: bold;
}

#btn-signin {
  /* background-color: #02754B; */
  background-color: #FFFFFF;
  width: 100%;
  color: #02754B;
  border-radius: 0.2rem;
}

#btn-signin>span {
  text-transform: capitalize;
}

.headlogin-mobile {
  font-weight: 700;
  font-size: 18px;
}

.headlogin-mobile-s {
  font-weight: 700;
  font-size: 18px;
}

.headlogin {
  /* font-weight: 700; */
  color: #FFFFFF;
  border: 0.2rem solid #ffffffff;
  padding: 1rem;
  border-radius: inherit;
  padding: 16px;
}

.logintext {
  font-weight: 700;
  font-size: 30px;
  line-height: 51px;
  align-items: center;
  text-align: center;
  color: #2463c1;
  font-weight: bold;
}

.logintextV2 {
  font-weight: 700;
  /* font-size: 30px; */
  line-height: 51px;
  align-items: center;
  text-align: center;
  color: #2463c1;
  font-weight: bold;
}

.logintext-mobile {
  font-weight: 700;
  font-size: 20px;
  line-height: 51px;
  align-items: center;
  text-align: center;
  color: #2463c1;
  font-weight: bold;
}

.logintext-mobile-s {
  font-weight: 700;
  font-size: 20px;
  line-height: 51px;
  align-items: center;
  text-align: center;
  color: #2463c1;
  font-weight: bold;
}

.headtext {
  font-weight: 400;
  font-size: 34.6111px;
  line-height: 128%;
  color: #1b8954;
  text-shadow: 1.23611px 1.23611px 2.47222px rgba(0, 0, 0, 0.25);
}

.headtext-md {
  font-weight: 400;
  font-size: 24px;
  line-height: 128%;
  color: #1b8954;
  text-shadow: 1.23611px 1.23611px 2.47222px rgba(0, 0, 0, 0.25);
}

.headtext-mobile {
  font-weight: 400;
  font-size: 18px;
  line-height: 128%;
  color: #1b8954;
  text-shadow: 1.23611px 1.23611px 2.47222px rgba(0, 0, 0, 0.25);
}

.logo {
  width: 50%;
}

.logo-mobile {
  width: 100%;
}

.hero-banner,
.hero-banner .v-toolbar__content,
.hero-banner .v-toolbar__image .v-image {
  height: 100% !important;
}

.excerp-login {
  font-size: 0.9rem !important;
}

.excerp-login-s {
  font-size: 0.5rem !important;
}

/* Desktop, Tablet, and Mobile styles - all use same ID */
#bg-login .theme--light.v-card{
  background-color: transparent;
  box-shadow: unset!important;
  padding: 0 32px!important;
}
#bg-login .v-input__slot{
  border-radius: 0.2rem;
  border: 1px solid #FFFFFF;
}
#bg-login .txt_login{
  text-align: center;
  color: #FFFFFF;
  font-size: 3rem;
  letter-spacing: 0.2rem;
  margin: 0;
}
#bg-login .white-input input,
#bg-login .white-input input::placeholder,
#bg-login .mdi-account-outline::before,
#bg-login .mdi-lock-outline::before {
  color: white;
  text-align: center;
}
#bg-login .user.white-input input{
  padding-right: 24px;
}
#bg-login input:-webkit-autofill,
#bg-login input:-webkit-autofill:hover,
#bg-login input:-webkit-autofill:focus,
#bg-login input:-webkit-autofill:active {
  -webkit-text-fill-color: white !important;
  transition: background-color 5000s ease-in-out 0s;
}
#bg-login .v-card__text{
  padding-top: 0!important;
}

/* Responsive font sizes */
@media (max-width: 1100px) and (min-width: 628px) {
  #bg-login .txt_login{
    font-size: 2.5rem;
  }
}

@media (max-width: 627px) {
  #bg-login .txt_login{
    font-size: 2rem;
  }
  #bg-login .theme--light.v-card{
    padding: 0 24px!important;
  }
}
</style>