<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <Homework/>
  </v-card>
</template>

<script>
import Navdraw from "@/components/Navdraw.vue";
import Homework from "@/components/C_Homework.vue";

export default {
  components: {
    Navdraw,
    Homework
  },
};
</script>

<style>
</style>