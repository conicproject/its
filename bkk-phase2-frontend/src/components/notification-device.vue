<template>
    <v-snackbar v-model="display" right top :timeout="-1" color="orange accent-2">
        <v-container>
            <v-layout>
                <v-flex>
                    <v-icon class="noti" large>error</v-icon>
                </v-flex>
                <v-flex class="pt-1 pl-2">
                    <h2>{{ text }}</h2>
                </v-flex>
            </v-layout>
            <h3 @click="gotoDevicePage()" class="pointer text-right">หน้ารายงานสถานะ<v-icon>mdi-arrow-right-thick
                </v-icon>
            </h3>
        </v-container>
    </v-snackbar>
</template>
<script>
export default {
    props: ["display", "message"],
    data() {
        return {
            text: `อุปกรณ์บางส่วนในระบบมีปัญหา`,
            test: true,
        }
    },
    watch: {
        display: {
            handler(value, oldValue) {

            }
        }
    },
    computed: {
        shower: {
            get() {
                if (this.show === true) {
                }
                return this.show
            },
            set(value) {
                if (!value) {

                }
            }
        },
    },
    methods: {
        gotoDevicePage() {
            this.$router.push({ path: '/device-status' })
        },
    },
}
</script>
<style>
.noti {
    animation-name: example;
    animation-duration: 4s;
}

@keyframes example {
    0% {
        left: 0px;
        right: 0px;
    }

    3% {
        left: 0px;
        right: 5px;
    }

    9% {
        left: 5px;
        right: 0px;
    }

    12% {
        left: 0px;
        right: 5px;
    }

    15% {
        left: 5px;
        right: 0px;
    }

    18% {
        left: 0px;
        right: 5px;
    }

    21% {
        left: 5px;
        right: 0px;
    }

    24% {
        left: 0px;
        right: 5px;
    }

    27% {
        left: 5px;
        right: 0px;
    }

    30% {
        left: 0px;
        right: 5px;
    }

    33% {
        left: 5px;
        right: 0px;
    }

    36% {
        left: 0px;
        right: 5px;
    }

    39% {
        left: 5px;
        right: 0px;
    }

    42% {
        left: 0px;
        right: 5px;
    }

    45% {
        left: 5px;
        right: 0px;
    }

    48% {
        left: 0px;
        right: 5px;
    }

    51% {
        left: 5px;
        right: 0px;
    }

    54% {
        left: 0px;
        right: 5px;
    }

    100% {
        left: 0px;
        right: 0px;
    }
}

.pointer {
    cursor: pointer;
}

h3 {
    position: relative;
}

h3::before {
    content: '';
    position: absolute;
    width: 100%;
    height: 4px;
    border-radius: 4px;
    background-color: #ffffff;
    bottom: 0;
    left: 0;
    transform-origin: right;
    transform: scaleX(0);
    transition: transform .3s ease-in-out;
}

h3:hover::before {
    transform-origin: right;
    transform: scaleX(1);
}
</style>