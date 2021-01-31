<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <Advice />
  </v-card>
</template>

<script>
import Navdraw from "@/components/Navdraw.vue";
import Advice from "@/components/C_Advice.vue";

export default {
  components: {
    Navdraw,
    Advice
  },
};
</script>

<style>
</style>