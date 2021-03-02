<template>
  
</template>

<script>
import firebase from "firebase";
export default {
 mounted(){
     admin
  .auth()
  .deleteUser(uid)
  .then(() => {
    console.log('Successfully deleted user');
  })
  .catch((error) => {
    console.log('Error deleting user:', error);
  });
 }
}
</script>

<style>

</style>