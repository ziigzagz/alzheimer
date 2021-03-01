<template>
  <div class="container">
    <div class="row">
      <div class="col-1">
        <v-row justify="center">
          <v-dialog v-model="dialog" persistent max-width="600px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark v-bind="attrs" v-on="on">เพิ่ม</v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">เพิ่มการบ้าน</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col>
                      <select
                        class="form-select"
                        aria-label="Default select example"
                        id="select"
                      >
                        <option
                          v-for="i in homeworkTemplate"
                          :key="i"
                          :value="i.id"
                        >
                          {{ i.data }}
                        </option>
                      </select>
                    </v-col>
                  </v-row>
                </v-container>

                <small>*indicates required field</small>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close"> ปิด </v-btn>
                <v-btn color="blue darken-1" text @click="save"> บันทึก </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-row>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <table class="table table-striped text-center">
          <thead>
            <tr>
              <th scope="col">ครั้งที่</th>
              <th scope="col">หัวข้อ</th>
              <th scope="col">เวลา</th>
              <th scope="col">สถานะ</th>
              <th scope="col">#</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in homework" :key="index">
              <td scope="row">{{ index + 1 }}</td>
              <td>{{ item.Name }}</td>
              <td>{{ item.data.date }}</td>
              <td><span class="badge bg-danger">ยังไม่สำเร็จ</span></td>
              <td>
                {{ item.data.homeworkTemplate }}
                <button class="btn btn-info" @click="viewInfo(item.data.homeworkTemplate)">
                  ดูข้อมูล
                </button>
              </td>
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
      dialog: false,
      homeworkTemplate: [],
      homework: [],
      homework_id: "",
    };
  },

  mounted() {
    var db = firebase.firestore();
var docRef2 = db.collection("HomeworkTemplate");
    // get data homework Template
    var docRef = db.collection("HomeworkTemplate");
    docRef.get().then((doc) => {
      doc.forEach((element) => {
        console.log(element.data(), element.id);
        this.homeworkTemplate.push({
          id: element.id,
          data: element.data().Homework_name,
        });
      });
    });

    // get data homework patient
    var docRef = db
      .collection("Homework")
      .where("user", "==", localStorage.getItem("uid"));
    docRef.get().then((doc) => {
      //  console.log(doc.docs[0].id)
      doc.forEach((element) => {
        console.log(element.data().homeworkTemplate);
        docRef2 = db.collection("HomeworkTemplate").doc(element.data().homeworkTemplate);
        docRef2.get().then((doc2) => {
          this.homework.push({ id: element.id, data: element.data(),Name:doc2.data().Homework_name });
          });
        
        // this.homework_id;
      });
    });
  },
  methods: {
    viewInfo(id) {
      console.log(id);
      localStorage.setItem("ID_Homework", id);
      window.location.href = "/InfoHomework";
    },
    close() {
      this.dialog = false;
    },
    save() {
      var d = new Date();
      var date = d.getDate();
      var month = d.getMonth();
      var year = d.getFullYear();
      var hours = d.getHours();
      var minutes = d.getMinutes();
      var db = firebase.firestore();
      if (minutes < 10) {
        minutes = "0" + minutes;
      }
      month += 1;
      // console.log(document.getElementById("select").value, 99);
      db.collection("Homework")
        .add({
          user: localStorage.getItem("uid"),
          homeworkTemplate: document.getElementById("select").value,
          date:
            date +
            "/" +
            month +
            "/" +
            year +
            " " +
            hours +
            ":" +
            minutes +
            "น.",
        })
        .then((docRef) => {
          // console.log("Document written with ID: ", docRef.id);
          this.dialog = false;
          Swal.fire({
            position: "center",
            icon: "success",
            title: "บันทึกข้อมูลสำเร็จ",
            showConfirmButton: false,
            timer: 1500,
          }).then(() => {
            location.reload();
          });
        })
        .catch(function (error) {
          console.error("Error adding document: ", error);
        });
    },
  },
};
</script>

<style>
</style>