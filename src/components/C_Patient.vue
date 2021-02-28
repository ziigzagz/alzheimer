<template>
  <div class="container">
    <div class="row">
      <div class="col-6">
        <button class="btn btn-info m-2" @click="test">เพิ่ม</button>
        <input type="file" id="input" />
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
          <tr v-for="(item, index) in datas" :key="index">
              <th scope="row"><a href="/Patient"> {{ item.ID }}</a>
               </th>
              <td>{{ item.Name }}</td>
              <td>{{  }}</td>
              <td>{{  }}111</td>
              <td>{{  }}</td>
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
              console.log(Info.data().Name);
              dataset["ID"] = Info.data().ID;
              dataset["Name"] = Info.data().Name;
              dataset["Birthday"] = Info.data().Birthday;
              dataset["Email"] = Info.data().Email;
              dataset["ww"] = Info.data().TEL;
              dataset["hh"] = Info.data().TEL;
              dataset["คนดูแล"] = Info.data().คนดูแล;
              console.log(dataset);
              this.datas.push(dataset);
              dataset = {};
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
              ID: element[1],
              Email: element[2],
              Name:element[3],
              Birthday: element[4],
              ww:element[5],
              hh: element[6],
              คนดูแล:element[7],
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