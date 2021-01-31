<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <InfoHomework/>
  </v-card>
</template>

<script>
import Navdraw from "@/components/Navdraw.vue";
import InfoHomework from "@/components/C_InfoHomework.vue";

export default {
  components: {
    Navdraw,
    InfoHomework
  },
};
</script>

<style>
</style>