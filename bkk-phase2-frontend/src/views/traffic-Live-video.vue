<template>
    <v-app>
        <v-container>
            <div style="width: 100%;height: 17rem;">
                <video-player ref="videoPlayer" style="width: 100%;height: 100%;" class="video-js vjs-default-skin"
                    :options="playerOptions" @play="onPlayerPlay($event)" @ready="onPlayerReady($event)" />
            </div>
        </v-container>
    </v-app>
</template>
<script>
const baseUrl = require("../../baseUrl.json");
import VideoPlayer from '@/components/VideoPlayer.vue';
export default {
    components: {
        VideoPlayer
    },
    data() {
        return {
            myPath: [],
            playerOptions: {
                autoplay: true,
                controls: true,
                controlBar: {
                    timeDivider: false,
                    durationDisplay: false
                }
            },
            isPublic: false,
        };
    },
    created() {
        if (baseUrl.pathImg === "110.171.165.57") {
            this.isPublic = true
        }
    },
    computed: {
        player() {
            return this.$refs.videoPlayer.player
        },
    },
    methods: {
        onPlayerPlay(player) {
        },
        onPlayerReady(player) {
            this.player.play()
        },
        playVideo: function (source) {
            const video = {
                withCredentials: false,
                type: 'application/x-mpegurl',
                src: source
            }
            this.player.reset() // in IE11 (mode IE10) direct usage of src() when <src> is already set, generated errors,
            this.player.src(video)
        },
        getData() {
            this.myPath = this.$route.path.split("/");
            let numberCamera = ''
            if (this.myPath[4]) {
                // console.log('sss')
                numberCamera = '&code_id=' + this.myPath[4]
            }
            let session_data = localStorage.getItem("session");
            var myHeaders = new Headers();
            myHeaders.append("session", session_data);
            var requestOptions = {
                method: 'GET',
                headers: myHeaders,
                redirect: 'follow'
            };
            let url =
                baseUrl.ipServer +
                "/traffic-view/live-sample?checkpoint=" +
                this.myPath[3] + numberCamera;;
            // this.playVideo("https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8")
            this.axios
                .get(url, { headers: { session: session_data } })
                .then((response) => {
                    console.log(response);
                    if (response.data.status_code === 200) {
                        let url = response.data.data.url
                        if (this.isPublic) {
                            url = url.replace(baseUrl.ipLiveviewInternal, baseUrl.ipLiveviewInternet)
                        }
                        
                        this.playVideo(url)
                    }
                });
        }

    },
    mounted() {
        this.getData();
    },
    beforeDestroy() {
        if (this.player != null) {
            this.player.dispose(); // dispose() Will delete Dom Elements
        }
    }
}
</script>