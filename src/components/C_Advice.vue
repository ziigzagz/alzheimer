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
              <span class="headline">เพิ่มคำแนะนำ</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col>
                    <v-text-field
                      label="คำแนะนำ *"
                      id="nameAdvice"
                      hint=""
                      persistent-hint
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>

              <v-textarea
                outlined
                name=""
                id="textarea"
                label="รายละเอียด *"
                value=""
              ></v-textarea>
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
              <th scope="col">วันที่</th>
              <th scope="col">หัวข้อ</th>
              <th scope="col">รายละเอียด</th>
              <th scope="col">สถานะ</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in advice" :key="index">
              <td>{{ item.date }}</td>
              <th>{{ item.title }}</th>
              <td>{{ item.text }}</td>

              <td v-if="item.status == 1">
                <span class="badge bg-success">สำเร็จ</span>
              </td>
              <td v-else><span class="badge bg-danger">ไม่สำเร็จ</span></td>
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
  data: () => ({
    dialog: false,
    advice: [],
  }),

  mounted() {
    var db = firebase.firestore();
    var docRef = db.collection("Advice");
    docRef.get().then((doc) => {
      doc.forEach((element) => {
        this.advice.push(element.data());
      });
    });
  },
  methods: {
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
       if (minutes < 10) {
        minutes = "0" + minutes;
      }
      month += 1;
      var db = firebase.firestore();
      db.collection("Advice")
        .add({
          title: document.getElementById("nameAdvice").value,
          status: 0,
          user: "",
          text: document.getElementById("textarea").value,
          date:
            date +
            "/" +
            month +
            1 +
            "/" +
            year +
            " " +
            hours +
            ":" +
            minutes +
            "น.",
        })
        .then((docRef) => {
          console.log("Document written with ID: ", docRef.id);
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