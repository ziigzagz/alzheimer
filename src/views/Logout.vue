<template></template>

<script>
import firebase from "firebase";
export default {
  beforeCreate() {
    localStorage.clear();
    firebase
      .auth()
      .signOut()
      .then(() => {
        this.$router.replace("/Login");
      });
  },
  mounted() {},
};
</script>

<style></style>