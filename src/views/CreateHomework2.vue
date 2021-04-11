<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <CreateHomework/>
  </v-card>
</template>

<script>
import Navdraw from "@/components/Navdraw.vue";
import CreateHomework from "@/components/C_CreateHomework2.vue";

export default {
  components: {
    Navdraw,
    CreateHomework
  },
};
</script>

<style>
</style>