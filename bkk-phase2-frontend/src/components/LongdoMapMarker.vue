<template>
    <div>
    </div>
  </template>
  
  <script>
  const EVENTS = {
    'overlayClick': 'click',
    'overlayMove': 'move',
    'overlayHover': 'hover',
    'overlayChange': 'change',
    'overlayDrag': 'drag',
    'overlayLeave': 'leave'
  }
  export default {
    name: 'LongdoMapMarker',
    props: {
      map: Promise,
      marker: Object
    },
    created: function () {
     // console.log("this.marker",this.marker)
      this.map.then(map => {
        let detail = this.marker.detail ? this.marker.detail : {}
        var marker = new longdo.Marker(this.marker.location, detail),
        inject = {
          marker,
          location: this.marker.location,
          detail: detail
        }
        map.Overlays.add(marker)
        for (let longdoEventName in EVENTS) {
          map.Event.bind(longdoEventName, (overlay) => {
            if (overlay != marker) {
              return
            }
            this.$emit(EVENTS[longdoEventName], inject)
          })
        }
      })
    }
  }
  </script>