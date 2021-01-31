<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <Patient />
  </v-card>
</template>

<script>
import Navdraw from "@/components/Navdraw.vue";
import Patient from "@/components/C_Patient.vue";

export default {
  components: {
    Navdraw,
    Patient
  },
};
</script>

<style>
</style>