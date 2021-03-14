<template>
  <div class="container">
    <div class="row">
      <div class="col-1">
        <v-row justify="center">
          <v-dialog v-model="dialog" persistent max-width="600px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="primary"
                dark
                v-bind="attrs"
                v-on="on"
                v-if="!isAdmin"
                >เพิ่ม</v-btn
              >
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">เพิ่มบันทึกประจำวัน</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <var
                    ><v-row>
                      <v-col>
                        <v-text-field
                          label="ชื่อบันทึก*"
                          id="name1"
                          hint=""
                          persistent-hint
                          required
                        ></v-text-field>
                      </v-col> </v-row
                  ></var>
                  <var
                    ><v-row>
                      <v-col>
                        <v-text-field
                          label="วันที่/เดือน/ปี พ.ศ.*"
                          id="date"
                          hint="ตัวอย่าง : 25/3/2564"
                        persistent-hint
                          required
                        ></v-text-field>
                      </v-col> </v-row
                  ></var>
                </v-container>

                <v-textarea
                  outlined
                  name=""
                  id="textarea"
                  label="รายละเอียด"
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
              <th>รายละเอียด</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in diary" :key="index">
              <th scope="row">{{ item.date }}</th>
              <th>{{ item.diary_name }}</th>
              <th>
                <v-dialog v-model="dialog1" persistent max-width="290">
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn color="primary" dark v-bind="attrs" v-on="on">
                      ดู
                    </v-btn>
                  </template>
                  <v-card>
                    <v-card-title class="headline"> รายละเอียด </v-card-title>
                    <v-card-text>
                      {{ diary[0].text }}
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="green darken-1 "
                        text
                        @click="dialog1 = false"
                      >
                        ปิด
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </th>
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
      dialog1: false,
      diary: [],
      isAdmin: Boolean(parseInt(localStorage.getItem("isAdmin"))),
    };
  },

  mounted() {
    //  console.log(this.isAdmin,localStorage.getItem("isAdmin"));
    //  console.log(this.isAdmin);
    var db = firebase.firestore();
    if (!localStorage.getItem("isAdmin")) {
      var docRef = db
        .collection("Diary")
        .where("user", "==", localStorage.getItem("uid"));
    } else {
      var docRef = db
        .collection("Diary")
        .where("user", "==", localStorage.getItem("uid"));
    }
    // var docRef = db.collection("Diary");
    docRef.get().then((doc) => {
      doc.docs.forEach((element) => {
        this.diary.push(element.data());
        // console.log(element.data())
      });
      // doc.forEach((element) => {
      //   // console.log(element.data());
      //   this.diary.push(element.data());
      // });
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
      var db = firebase.firestore();
      if (minutes < 10) {
        minutes = "0" + minutes;
      }
      month += 1;
      var name = document.getElementById("name1").value;
      name = name.replace(" ", "");
      var D_date = document.getElementById("date").value;
      D_date = D_date.replace(" ", "");
      console.log(name,name.length,D_date,D_date.length)
      if (name.length == 0 || D_date.length == 0) {
      
        Swal.fire({
          icon: "error",
          title: "Oops...",
          text: "กรุณากรอกชื่อหรือวันที่ให้ครบถ้วน",
          timer: 1500,
        });
      } else {
        db.collection("Diary")
          .add({
            diary_name: document.getElementById("name1").value,
            status: 0,
            user: localStorage.getItem("uid"),
            text: document.getElementById("textarea").value,
            D_date:document.getElementById("date").value,
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
            console.log("Document written with ID: ", docRef.id);
            this.dialog = false;
            Swal.fire({
              position: "center",
              icon: "success",
              title: "บันทึกข้อมูลสำเร็จ",
              showConfirmButton: false,
              timer: 1500,
            }).then(() => {
              // location.reload();
            });
          })
          .catch(function (error) {
            console.error("Error adding document: ", error);
          });
      }
    },
  },
};
</script>

<style>
</style>