<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <TemplateMatching/>
  </v-card>
</template>

<script>
import Navdraw from "@/components/Navdraw.vue";
import TemplateMatching from "@/components/C_TemplateMatching.vue";

export default {
  components: {
    Navdraw,
    TemplateMatching
  },
};
</script>

<style>
</style>