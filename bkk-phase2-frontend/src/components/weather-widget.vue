
<script>
import axios from "axios";
export default {
  name: "App",
  data: () => ({
    api_url: "https://api.openweathermap.org/data/2.5/",
    api_key: "814ca0274a5978ef78c6b9b44ff87547",
    url_aqi: "https://api.waqi.info/feed/",
    key_aqi: "536469d490831f7a9a9fae04e952cb09222f4e61",
    query: "bangkok",
    weather: {},
    pm25:"",
    bookmarks: [],
    showBookmarks: false,
  }),
  methods: {
    fetchWeather() {
      axios
        .get(
          `${this.api_url}weather?q=${this.query}&units=metric&appid=${this.api_key}`
        )
        .then((response) => (this.weather = response.data))
        .catch((error) => console.log(error));

        //console.log("this.weather",this.weather );
    },
    fetchAQI() {
      this.axios
        .get(
          `${this.url_aqi}${this.query}/?token=${this.key_aqi}`
        )
        .then((response) => {
        //console.log("response",response.data.data.iaqi);
         this.pm25 = response.data.data.iaqi.pm25.v;
          })
        .catch((error) => console.log(error));
         
         //console.log(this.pm25);
    },
  },
  mounted() {
    this.fetchWeather();
    this.fetchAQI();

  },
  
};
</script>
<style lang="scss" scoped>
.container {
  border-radius: 10px;
  color: #ffffff;
  height: 230px;
}
.weather-side {
  position: relative;
  height: 100%;
  border-radius: 10px;
  //background-image: url("https://images.unsplash.com/photo-1559963110-71b394e7494d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=675&q=80");
  background: linear-gradient(133.64deg, #02754B 3.9%, #ABDDA3 96.1%);
;
  width: 100%;
  -webkit-box-shadow: 0 0 20px -10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 0 20px -10px rgba(0, 0, 0, 0.2);
  float: left;
 
}
.weather-gradient {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background-image: var(--gradient);
  border-radius: 10px;
  opacity: 0.8;
}
.date-container {
  position: absolute;
  top: 25px;
  left: 25px;
}
.date-dayname {
  margin: 0;
}
.date-day {
  display: block;
}
.location {
  display: inline-block;
  
}

.weather-icon {
  font-size: 65px;
}
.weather-img{
    margin-left: 18%;
    margin-top: 55%;
    position:absolute;
}
.weather-temptext{
    margin-top: 25%;
    margin-left: 15%;
    position:absolute;
   
}
.weather-temp {
  
  font-weight: 700;
  font-size: 4.0em;
}
.weather-desc {
  margin: 0;
}
.agi1{
    position: absolute;
    margin-bottom: 0px !important;
     top: 60%;
     left: 73%;
     font-size: 1.0em;
      font-weight: 400;
}
.agi2{
    position: absolute;
    margin-bottom: 0px !important;
     top: 65%;
     left: 73%;
      font-size: 2.0em;
      font-weight: 600;
}
.agi3{
    position: absolute;
    margin-bottom: 0px !important;
     top: 83%;
     left: 73%;
     font-size: 0.8em;
      font-weight: 400;
}
</style>
<template>
  <div class="container" v-if="typeof weather.main != 'undefined'">
    <div class="weather-side">
      <div class="weather-gradient"></div>
      <div class="date-container">
        <h2 class="location">
          {{ weather.name }}, {{ weather.sys.country }}
        </h2>
      </div>
      <div class="weather-temptext">
        <h2 class="weather-temp">{{ Math.round(weather.main.temp) }}°</h2>
         </div>
         <v-layout>
          <v-flex class="weather-img"><img v-if="weather.weather[0].icon === '01d'" src="@/assets/img/icon/clear_icon.png" width="50" height="50"/>
          <img v-else-if="weather.weather[0].icon === '01n'" src="@/assets/img/icon/night_icon.png" width="50" height="50"/>
         <img v-else-if="weather.weather[0].icon === '02d'" src="@/assets/img/icon/few_clouds_icon.png" width="50" height="50"/>
         <img v-else-if="weather.weather[0].icon === '02n'" src="@/assets/img/icon/few_clouds_night_icon.png" width="50" height="50"/>
         <img v-else-if="weather.weather[0].icon === '03d'" src="@/assets/img/icon/overcast_icon.png" width="50" height="50"/>
         <img v-else-if="weather.weather[0].icon === '04d' || weather.weather[0].icon === '04n'" src="@/assets/img/icon/clound.png" width="50" height="50"/>
         <img v-else-if="weather.weather[0].icon === '09d' || weather.weather[0].icon === '09n'" src="@/assets/img/icon/rain_icon.png" width="50" height="50"/>
         <img v-else-if="weather.weather[0].icon === '10d' || weather.weather[0].icon === '10n'" src="@/assets/img/icon/showers_icon.png" width="50" height="50"/>  
         <img v-else-if="weather.weather[0].icon === '11d' || weather.weather[0].icon === '11n'" src="@/assets/img/icon/storm_icon.png" width="50" height="50"/> 
         <img v-else-if="weather.weather[0].icon === '13d' || weather.weather[0].icon === '13n'" src="@/assets/img/icon/winter_icon.png" width="50" height="50"/> 
         <img v-else-if="weather.weather[0].icon === '50d' || weather.weather[0].icon === '50n'" src="@/assets/img/icon/mist.png" width="50" height="50"/>
          <h3 v-else class="weather-desc">{{ weather.weather[0].icon }}</h3>
        </v-flex>
        <v-flex>
            <!-- <ul>
                <li><img src="@/assets/img/icon/humidity.png" width="20" height="20"/><span class="value">{{ weather.main.humidity }} %</span></li>
                <li> <img src="@/assets/img/icon/wind.png" width="20" height="20"/><span class="value">{{ weather.wind.speed }} km/h</span></li>
           </ul> -->
           <div>
            <p class="agi1">PM2.5</p>
            <p class="agi2">{{pm25}}</p>
             <p class="agi3">ug/m³</p>
             </div>
           </v-flex>
          </v-layout>
          <!-- <h3 class="weather-desc">{{ weather.weather[0].icon }}</h3> -->
      
     
    </div>
  </div>
  
</template>