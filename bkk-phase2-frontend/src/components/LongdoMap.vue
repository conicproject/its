<template>
    <div style="height:100%">
        <div :style="{'width': width, 'height': height}" :id="_uid"></div>
        <template>
            <slot :marker="marker" :map="getMap"></slot>
        </template>
    </div>
</template>

<script>
export default {
  name: 'LongoMap',
  props: {
    apiKey: {
      type: String,
      required: true
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '100%'
    },
    center: {
      type: Object,
      default: function () {
        return {
          lat: 18.7716998,
          lon: 98.816391
        }
      }
    },
    zoomLevel: {
      type: Number,
      default: 11
    },
    markers: {
      type: Array,
      default: function () {
        return []
      }
    },
    marker: Object,
  },
  data: function () {
    return {
      isAttachedScript: false,
      map: null
    }
  },
  created: function () {
  },
  mounted: function () {
    this.getMap.then(map => {
      this.init(map)
    })
  },
  methods: {
    init: function (map) {
      this.moveToCenter(map, this.center)
      this.doZoom(map, this.zoomLevel)
    },
    moveToCenter: function (map, location) {
      map.location(location)
    },
    doZoom: function (map, zoomLevel) {
      map.zoom(zoomLevel)
    }
  },
  watch: {
    center: function (newValue, oldValue) {
      this.moveToCenter(newValue)
    }
  },
  computed: {
    getMap: async function () {
      var self = this
      function attachMap () {
        return new Promise(resolve => {
          let script = document.querySelector('script[id=longo-map]')
          if (!script) {
            let scriptBlock = document.createElement('script')
            scriptBlock.setAttribute('id', 'longdo-map')
            scriptBlock.setAttribute('src', `http://api.longdo.com/map/?key=${self.apiKey}`)
            scriptBlock.onload = () => {
              var map = new longdo.Map({
                placeholder: document.getElementById(self._uid)
              })
              resolve(map)
            }
            document.head.appendChild(scriptBlock)
          }
        })
      }
      let map = await attachMap()
      return map
    }
  }
}
</script>