<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <CheckHomework/>
  </v-card>
</template>

<script>
import Navdraw from "@/components/Navdraw.vue";
import CheckHomework from "@/components/C_CheckHomework.vue";

export default {
  components: {
    Navdraw,
    CheckHomework
  },
};
</script>

<style>
</style>