<template>
  <v-app>
    <v-layout>
      <v-container>
        <v-card class="elevation-0">
          <v-card-text>
            <v-layout row wrap>
              <v-flex xs12 lg12>
                <!-- <section class="page_404">
                  <div class="container">
                    <div class="row">
                      <div class="col-sm-12 ">
                        <div class="col-sm-10 col-sm-offset-1  text-center">
                          <div class="four_zero_four_bg">
                            <h1 class="text-center ">ERROR 404</h1>
                          </div>

                          <div class="contant_box_404">
                            <h3 class="h2">
                              Look like you're lost
                            </h3>

                            <p>the page you are looking for not avaible!</p>

                            <a href="/" class="link_404">Go to Home</a>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </section> -->
                 <div class="container">
                    <div class="row"  >
                         <div class="col-sm-12 ">
                       <div class="col-sm-10 col-sm-offset-1  text-center" style="font-size:100px; text-align: center; padding-top:20%">
                        <p >ERROR 404!</p>
                        </div> 
                        <div class="col-sm-10 col-sm-offset-1  text-center" style="font-size:25px; text-align: center;">
                        <p >someting wrong ..</p> <a href="/" >Go to Home Page</a>
                        </div>
                    </div>
                 </div>
                 </div>
              </v-flex>
            </v-layout>
          </v-card-text>
        </v-card>
      </v-container>
    </v-layout>
  </v-app>
</template>
<script>
export default {};
</script>
<style scoped>
.page_404{ padding:40px 0; background:#fff; font-family: 'Arvo', serif;
}

.page_404  img{ width:100%;}

.four_zero_four_bg{
 
 background-image: url(https://cdn.dribbble.com/users/285475/screenshots/2083086/dribbble_1.gif);
    height: 400px;
    background-position: center;
 }
 
 
 .four_zero_four_bg h1{
 font-size:80px;
 }
 
  .four_zero_four_bg h3{
			 font-size:80px;
			 }
			 
			 .link_404{			 
	color: #fff!important;
    padding: 10px 20px;
    background: #39ac31;
    margin: 20px 0;
    display: inline-block;}
	.contant_box_404{ margin-top:-50px;}
</style>
