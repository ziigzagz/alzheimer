<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <Edit />
  </v-card>
</template>

<script>
import Navdraw from "@/components/Navdraw.vue";
import Edit from "@/components/C_Edit.vue";

export default {
  components: {
    Navdraw,
    Edit
  },
};
</script>

<style>
</style>