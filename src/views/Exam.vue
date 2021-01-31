<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <Info />
  </v-card>
</template>

<script>
import Navdraw from "@/components/Navdraw.vue";
import Info from "@/components/C_InfoExam.vue";

export default {
  components: {
    Navdraw,
    Info
  },
};
</script>

<style>
</style>