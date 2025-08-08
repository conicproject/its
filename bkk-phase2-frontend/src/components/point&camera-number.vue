<template>
    <v-card class="elevation-0" id="border">
                <v-row>
                  <v-col >
                    <div class="pl-5"><span>{{keyword.headL}}</span></div>
                    
                      <div class="text-right"><span class="dtpoint">{{keyword.number1}}</span> <span>{{keyword.unitL}}</span></div>
                    
                  </v-col>
                      <v-divider vertical  class="ma-4"></v-divider>
                  <v-col>
                    <div><span>{{keyword.headR}}</span></div>
                      
                      <div class="text-right pr-5"><span class="dtpoint">{{keyword.number2}}</span> <span>{{keyword.unitR}}</span></div>
                  </v-col>
                </v-row>
              </v-card>
</template>
<script>
export default {
    props:['keyword'],
}
</script>
<style>
.dtpoint{
  color: #2463C1;
  font-weight: 700;
  font-size: 40px;
}
</style>