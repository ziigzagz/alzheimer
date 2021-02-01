<template>
  <div class="container">
    <div class="row">
      <div class="col-6">
        <button class="btn btn-info m-2" @click="test">เพิ่ม</button>
        <input type="file" id="input" />
        <button class="btn btn-info m-2" @click="upload">อัปโหลด</button>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <table class="table table-striped text-center">
          <thead>
            <tr>
              <th scope="col">HN</th>
              <th scope="col">ชื่อ-สกุล</th>
              <th scope="col">อายุ</th>
              <th scope="col">ชื่อผู้ดูแล</th>
              <th scope="col">เบอร์โทรติดต่อ</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="i in datas" v-bind:key="i">
              <th scope="row"><a href=""> {{ i.ID }}</a>
               </th>
              <td>{{ i.FNAME }} {{ i.LNAME }}</td>
              <td>{{ i.AGE }}</td>
              <td>{{ i.คนดูแล }}</td>
              <td>{{ i.TEL }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import firebase from "firebase";

export default {
  data() {
    return {
      datas: [],
    };
  },
  mounted() {
    var db = firebase.firestore();
    var dataset = {};
    var docRef = db.collection("InfoPatient");
    docRef
      .get()
      .then((doc) => {
        doc.forEach((element) => {
          var row = db.collection("InfoPatient").doc(element.id);
          row
            .get()
            .then((Info) => {
              // console.log(Info.data().ID);
              dataset["ID"] = Info.data().ID;
              dataset["FNAME"] = Info.data().FNAME;
              dataset["LNAME"] = Info.data().LNAME;
              dataset["AGE"] = Info.data().AGE;
              dataset["คนดูแล"] = Info.data().คนดูแล;
              dataset["TEL"] = Info.data().TEL;
              console.log(dataset);
              this.datas.push(dataset);
              dataset = [];
            })
            .catch(function (error) {
              console.log("Error getting document:", error);
            });
        });
      })
      .catch(function (error) {
        console.log("Error getting document:", error);
      });
  },
  methods: {
    async click() {},
    async test() {
      const input = document.getElementById("input");
      await readXlsxFile(input.files[0]).then((rows) => {
        rows.forEach((element) => {
          var db = firebase.firestore();
          db.collection("InfoPatient")
            .add({
              ID: element[0],
              FNAME: element[1],
              LNAME: element[2],
              AGE: element[3],
              คนดูแล: element[4],
              TEL: element[5],
            })
            .then(function (docRef) {
              console.log("Document written with ID: ", docRef.id);
              location.reload();
            })
            .catch(function (error) {
              console.error("Error adding document: ", error);
            });
        });
      });
    },
  },
};
import readXlsxFile from "read-excel-file";
</script>

<style>
</style>