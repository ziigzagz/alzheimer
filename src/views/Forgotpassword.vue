<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <Forgotpassword />
  </v-card>
</template>

<script>
import Navdraw from "@/components/Navdraw.vue";
import Forgotpassword from "@/components/C_Forgotpassword.vue";

export default {
  components: {
    Navdraw,
    Forgotpassword
  },
};
</script>

<style>
</style>