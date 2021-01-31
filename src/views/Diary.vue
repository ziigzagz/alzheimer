<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <Diary />
  </v-card>
</template>

<script>
import Navdraw from "@/components/Navdraw.vue";
import Diary from "@/components/C_Diary.vue";

export default {
  components: {
    Navdraw,
    Diary
  },
};
</script>

<style>
</style>