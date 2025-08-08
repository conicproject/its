<template>
  <v-app>
      <v-overlay :value="onProgress">
      <v-progress-circular indeterminate size="100" width="7"></v-progress-circular>
    </v-overlay>
    
    <v-layout v-if="$vuetify.breakpoint.width > 1100">
      <v-flex>
        <v-card class="elevation-0">
          <v-card-title>
            <img src="@/assets/img/logo_bkk_1_11zon.png" /> <v-spacer></v-spacer>
            <div class="text-right headtext">
              กองระบบเทคโนโลยีจราจร<br />
              สำนักการจราจรและขนส่ง กรุงเทพมหานคร
            </div>
          </v-card-title>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout v-else-if="$vuetify.breakpoint.width < 1100 && $vuetify.breakpoint.width > 925">
      <v-flex>
        <v-card class="elevation-0">
          <v-card-title>
            <img src="@/assets/img/logo_bkk_1_11zon.png" /> <v-spacer></v-spacer>
            <div class="text-right headtext-md">
              กองระบบเทคโนโลยีจราจร<br />
              สำนักการจราจรและขนส่ง กรุงเทพมหานคร
            </div>
          </v-card-title>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout v-else>
      <v-flex>
        <v-card class="elevation-0">
          <v-card-title>
            <img class="logo" src="@/assets/img/logo_bkk_1_11zon.png" />
          </v-card-title>
          <v-card-text
            ><div class="text-right headtext-mobile">
              กองระบบเทคโนโลยีจราจร<br />
              สำนักการจราจรและขนส่ง กรุงเทพมหานคร
            </div></v-card-text
          >
        </v-card>
      </v-flex>
    </v-layout>
    <!-- <v-parallax   height="100%" src="@/assets/background-login.jpeg"> -->
    <!-- <div id="bg"> -->
    <v-layout id="bg-login" row wrap align-center justify-center v-if="$vuetify.breakpoint.width > 1100">
      <v-flex xs12 lg7 class="ma-5" justify-center>
        <v-card class="mx-auto" >
          <v-card-title class="justify-center logintext"
            ><span class="headlogin"
              >ระบบกล้องโทรทัศน์วงจรปิด(CCTV) เพื่อตรวจจับการฝ่าฝืนสัญญารไฟจราจร<br />
             และเครื่องหมายจราจรบริเวณทางแยก ในพื้นที่กรุงเทพมหานคร
              </span>
          </v-card-title>
        </v-card>
        <br /><br />
         <v-layout row wrap align-center justify-center><v-btn large @click="$router.push('/dashboard')"><v-icon>mdi-arrow-left</v-icon><span class="textbutton">กลับไปหน้าหลัก</span></v-btn></v-layout>
        <!-- <v-card class="mx-auto pa-8" max-width="500">
          <v-card-text>
            <v-text-field v-model="username" filled rounded placeholder="Username"></v-text-field>
            <v-text-field 
            @click:append="showPassword = !showPassword"
            :type="showPassword ? 'text' : 'password'"  
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" 
            v-model="password" 
            filled 
            rounded 
            placeholder="Password"></v-text-field>
          </v-card-text>
          <v-card-actions class="justify-center pt-0">
            <v-btn id="btn-signin" large @click="login()"><span class="btn-text pa-7">Sign In</span></v-btn>
          </v-card-actions>
        </v-card> -->
      </v-flex>
    </v-layout>

    <v-layout id="bg-login-mobile" justify-center v-else-if="$vuetify.breakpoint.width < 1100 && $vuetify.breakpoint.width > 700">
      <v-flex class="ma-16">
        <v-layout>
          <v-flex justify-center>
            <v-card class="formtext">
              <v-card-title class="justify-center logintext-mobile"
                ><span class="headlogin"
                  >ระบบกล้องโทรทัศน์วงจรปิด(CCTV) เพื่อตรวจจับการฝ่าฝืนสัญญารไฟจราจร<br />
             และเครื่องหมายจราจรบริเวณทางแยก ในพื้นที่กรุงเทพมหานคร
                  </span
                >
              </v-card-title>
            </v-card>
          </v-flex>
        </v-layout>
        <br /><br />
         <v-layout row wrap align-center justify-center><v-btn large @click="$router.push('/dashboard')"><v-icon>mdi-arrow-left</v-icon><span class="textbutton">กลับไปหน้าหลัก</span></v-btn></v-layout>
        <!-- <v-layout>
          <v-flex>
            <v-card class="formlogin">
              <v-card-text>
                <v-text-field v-model="username" filled rounded placeholder="Username"></v-text-field>
                <v-text-field @click:append="showPassword = !showPassword" :type="showPassword ? 'text' : 'password'"  
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"  v-model="password" filled rounded placeholder="Password"></v-text-field>
              </v-card-text>
              <v-card-actions class="justify-center pt-0">
                <v-btn id="btn-signin" large @click="login()"><span class="btn-text pa-7">Sign In</span></v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout> -->
      </v-flex>
    </v-layout>

    <v-layout id="bg-login-mobile" justify-center v-else>
      <v-flex class="ma-16">
        <v-card >
          <v-card-title class="justify-center logintext-mobile"
            ><span class="headlogin-mobile"
              >ระบบกล้องโทรทัศน์วงจรปิด(CCTV) เพื่อตรวจจับการฝ่าฝืนสัญญารไฟจราจร<br />
             และเครื่องหมายจราจรบริเวณทางแยก ในพื้นที่กรุงเทพมหานคร
              </span
            >
          </v-card-title>
        </v-card>
        <br /><br />
         <v-layout row wrap align-center justify-center><v-btn large @click="$router.push('/dashboard')"><v-icon>mdi-arrow-left</v-icon><span class="textbutton">กลับไปหน้าหลัก</span></v-btn></v-layout>
        <!-- <v-card max-width="500">
          <v-card-text>
            <v-text-field v-model="username" filled rounded placeholder="Username"></v-text-field>
            <v-text-field @click:append="showPassword = !showPassword" :type="showPassword ? 'text' : 'password'"  
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"  v-model="password" filled rounded placeholder="Password"></v-text-field>
          </v-card-text>
          <v-card-actions class="justify-center pt-0">
            <v-btn id="btn-signin" large @click="login()"><span class="btn-text pa-7">Sign In</span></v-btn>
          </v-card-actions>
        </v-card> -->
      </v-flex>
    </v-layout>
    <!-- </v-parallax> -->
    <!-- </div> -->
  </v-app>
</template>
<script>
const baseUrl = require('../../baseUrl.json')
import Swal from "sweetalert2/dist/sweetalert2.js";
const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
});
export default {
  data() {
    return {
      onProgress: false,
      showPassword: false,
      username: "",
      password: "",
    };
  },
  methods: {

  },
  mounted() {
   
  }
};
</script>
<style>
@import "../assets/css/background.css";
/* @import '../sass/variables.scss'; */
.formlogin {
  margin-left: 25%;
  margin-right: 25%;
}
.formtext {
  margin-left: 15%;
  margin-right: 15%;
}
.btn-text {
  font-weight: bold;
}
#btn-signin {
  background-color: #02754B;
  color: white;
  border-radius: 15px;
}
#btn-signin > span {
  text-transform: capitalize;
}
.headlogin-mobile {
  font-weight: 700;
  font-size: 14px;
}
.headlogin {
  font-weight: 700;
}
.textbutton {
  font-weight: 700;
  color: #2463c1;
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
.logintext-mobile {
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
</style>
