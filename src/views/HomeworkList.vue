<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <HomeworkList/>
  </v-card>
</template>

<script>
import Navdraw from "@/components/Navdraw.vue";
import HomeworkList from "@/components/C_HomeworkList.vue";

export default {
  components: {
    Navdraw,
    HomeworkList
  },
};
</script>

<style>
</style>