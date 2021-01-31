<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <ExamList />
  </v-card>
</template>

<script>
import Navdraw from "@/components/Navdraw.vue";
import ExamList from "@/components/C_ExamList.vue";

export default {
  components: {
    Navdraw,
    ExamList
  },
};
</script>

<style>
</style>