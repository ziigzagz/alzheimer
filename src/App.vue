<template>
  <v-app>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import firebase from "firebase";
export default {
  name: "App",
};
</script>
<style>
body {
  font-family: "Kanit", sans-serif;

  background-color: #65f5f5;
}
</style>
