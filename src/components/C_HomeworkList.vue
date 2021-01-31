<template>
  <div class="container">
    <div class="row">
      <div class="col-1">
        <button class="btn btn-info" @click="CreateHomework">เพิ่ม</button>
        <v-row justify="center"> </v-row>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <table class="table table-striped text-center">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">การบ้าน</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in homeworkTemplate" :key="index">
              <th>{{ index + 1 }}</th>
              <th>{{ item }}</th>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import firebase from "firebase";
import Swal from "sweetalert2";
export default {
  data() {
    return {
      homeworkTemplate: [],
      dialog: false,
    };
  },
  mounted() {
    var db = firebase.firestore();
    var docRef = db.collection("HomeworkTemplate");
    docRef.get().then((doc) => {
      doc.forEach((element) => {
        console.log(element.data());
        this.homeworkTemplate.push(element.data().Homework_name);
      });
    });
  },
  methods: {
    CreateHomework() {
      window.location.href = "/CreateHomework";
    },
  },
};
</script>

<style>
</style>