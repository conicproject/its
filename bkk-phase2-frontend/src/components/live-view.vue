<template>
    <v-row justify="center">
        <v-dialog  v-model="shower" scrollable persistent max-width="900px">
            <v-card>
                <v-card-title>
                Item
                </v-card-title>
                <v-card-text>
                     <v-container>
              </v-container>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <!-- <v-btn color="red" text @click="$emit('close')">Close</v-btn>
                    <v-btn color="primary" text @click="editItem()">Submit</v-btn> -->
                    
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>
<script>
export default {
    props: ['show'],
    data() {
    return {}},
    computed:{
        shower :{
            get() {
                if(this.show === true){
                }
                return this.show
            },
            set (value) {
                if (!value) {
                }
            }
        },
    },
    }
</script>
<style>

</style>