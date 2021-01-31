<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <AdviceInfo />
  </v-card>
</template>

<script>
import Navdraw from "@/components/Navdraw.vue";
import AdviceInfo from "@/components/C_Advice-Info.vue";

export default {
  components: {
    Navdraw,
    AdviceInfo
  },
};
</script>

<style>
</style>