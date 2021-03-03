<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <div class="container">
      <div class="row">
        <div class="col mx-auto">
          <v-card
            elevation="6"
            outlined
            color="indigo darken-2"
            class="text-white"
          >
            <v-card-title>คนไข้ในระบบ</v-card-title>
            <div class="col text-end" style="font-size: 70px">
              {{ numrow }} คน
            </div>
            <!-- <div class="col text-end">คน</div> -->
          </v-card>
        </div>
      </div>
      <div class="row">
        <div class="col mx-auto">
          <Chart />
        </div>
      </div>
    </div>
  </v-card>
</template>

<script>
import firebase from "firebase";
import Navdraw from "@/components/Navdraw.vue";
import Chart from "@/components/Chartcomponent.vue";

export default {
  data() {
    return {
      numrow: 0,
      userlist_dohomework: [],
    };
  },
  components: {
    Navdraw,
    Chart,
  },
  async mounted() {
    await firebase.auth().onAuthStateChanged((user) => {
      if (!user) {
        // this.$router.replace("/login");
      } else {
      }
    });
    // get numrow patient
    var db = firebase.firestore();
    var docRef = db.collection("InfoPatient");
    docRef
      .get()
      .then((doc) => {
        this.numrow = doc.size;
        // console.log(doc.size);
      })
      .catch(function (error) {
        console.log("Error getting document:", error);
      });

    
     
  },
};
</script>

<style>
</style>