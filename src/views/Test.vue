<template>
  <v-row justify="space-around" >
   
    <v-color-picker
    swatches-max-height = "300px"
      class="ma-2"
      disabled
      :swatches="swatches"
      show-swatches
      hide-canvas
      hide-inputs
      hide-sliders
      flat
      width = 500
      hide-mode-switch
    ></v-color-picker>
   
  </v-row>
</template>

<script>
  export default {
    data: () => ({
      swatches: [
        ['#FF0000', '#AA0000', '#550000'],
        ['#FFFF00', '#AAAA00', '#555500'],
        ['#00FF00', '#00AA00', '#005500'],
        ['#00FFFF', '#00AAAA', '#005555'],
        ['#0000FF', '#0000AA', '#000055'],
      ],
    }),
  }
</script>

<style>

</style>