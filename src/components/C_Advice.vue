<template>
  <div class="container">
    <div class="row">
      <div class="col-1">
        <v-row justify="center">
          <v-dialog v-model="dialog" persistent max-width="600px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="primary mt-2"
                dark
                v-bind="attrs"
                v-on="on"
                v-if="isAdmin"
                >เพิ่ม</v-btn
              >
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
        <input
          type="text"
          id="myInput_Adv"
          @keyup="myFunction"
          placeholder="ค้นหาคำแนะนำ...."
          title="Type in a name"
        />
        <table class="table table-striped text-center" id="myTable_Adv">
          <tr>
            <th scope="col">วันที่</th>
            <th scope="col">หัวข้อ</th>
            <th scope="col">สถานะ</th>
            <th scope="col">รายละเอียด</th>
            <th scope="col">#</th>
          </tr>
          <tr v-for="(item, index) in advice" :key="index">
            <td>{{ item.data.date }}</td>
            <td>{{ item.data.title }}</td>
            <td v-if="item.data.status == 1">
              <span class="badge bg-success mt-2">ทำตามคำแนะนำแล้ว </span>
            </td>
            <td v-else>
              <span class="badge bg-danger">ยังไม่ทำตามคำแนะนำ</span>
            </td>
            <td>
              <button
                class="btn btn-info bg-info mt-2"
                @click="Watch(item.data.text)"
              >
                ดู
              </button>
              
            </td>
            <td>
              <button
                class="btn btn-info bg-info"
                @click="update(item.id)"
                v-if="item.data.status == 0 && !isAdmin"
              >
                <img
                  src="@/assets/icon/check.png"
                  height="15px"
                  alt=""
                  srcset=""
                />
              </button>
              <button
                class="btn btn-danger bg-danger mt-2 ms-5"
                @click="Delete(item.id)"
                v-if="item.data.status == 0 && isAdmin"
              >
                ลบ
              </button>
            </td>
          </tr>
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
    dialog2: false,
    advice: [],
    isAdmin: Boolean(parseInt(localStorage.getItem("isAdmin"))),
  }),

  async mounted() {
    // var db = firebase.firestore();
    // var docRef = db.collection("Advice");
    // docRef.get().then((doc) => {
    //   doc.forEach((element) => {
    //     this.advice.push(element.data());
    //   });
    // });

    var db = firebase.firestore();
    if (!localStorage.getItem("isAdmin")) {
      var docRef = await db
        .collection("Advice")
        .where("user", "==", localStorage.getItem("uid"))
        .orderBy("date", "desc");
    } else {
      var docRef = await db
        .collection("Advice")
        .where("user", "==", localStorage.getItem("uid"))
        .orderBy("date", "desc");
    }
    // var docRef = db.collection("Diary");
    docRef
      .get()
      .then((doc) => {
        doc.docs.forEach((element) => {
          this.advice.push({ id: element.id, data: element.data() });
          // console.log(element.id);
        });
        // doc.forEach((element) => {
        //   // console.log(element.data());
        //   this.diary.push(element.data());
        // });
      })
      .then(() => {
        // console.log(this.advice);
        this.advice.sort();
      });
  },
  methods: {
    Watch(id) {
      Swal.fire(id);
    },
    Delete(id) {
      var db = firebase.firestore();
      Swal.fire({
        title: "คุณต้องการลบคำแนะนำใช่หรือไม่",
        showCancelButton: true,
        icon: "question",
        confirmButtonText: `ยืนยัน`,
        cancelButtonText: "ยกเลิก",
      }).then((result) => {
        if (result.isConfirmed) {
          db.collection("Advice")
            .doc(id)
            .delete()
            .then(() => {
              console.log("Document successfully deleted!");
              Swal.fire({
                position: "center",
                icon: "success",
                title: "ลบสำเร็จ!",
                showConfirmButton: false,
                timer: 1500,
              }).then(() => {
                window.location.reload();
              });
            })
            .catch((error) => {
              console.error("Error removing document: ", error);
            });
        } else if (result.isDenied) {
          Swal.fire("Changes are not saved", "", "info");
        }
      });
    },
    myFunction() {
      var input, filter, table, tr, td, i, txtValue;
      input = document.getElementById("myInput_Adv");
      filter = input.value.toUpperCase();
      table = document.getElementById("myTable_Adv");
      tr = table.getElementsByTagName("tr");
      for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
          txtValue = td.textContent || td.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
          } else {
            tr[i].style.display = "none";
          }
        }
      }
    },
    async update(id) {
      var db = firebase.firestore();
      console.log(id);
      Swal.fire({
        title: "ยืนยัน",
        text: "คุณได้ปฏิบัติตามคำแนะนำใช่หรือไม่?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "ใช่",
        cancelButtonText: "ไม่",
      }).then((result) => {
        if (result.isConfirmed) {
          const update = db.collection("Advice").doc(id);
          update.update({
            status: 1,
          });
          Swal.fire({
            position: "center",
            icon: "success",
            title: "ยืนยันสำเร็จ!",
            showConfirmButton: false,
            timer: 1500,
          }).then(() => {
            location.reload();
          });
          // Swal.fire("ยืนยันสำเร็จ!", "ทำการอัปเดตเรียบร้อย", "success");
        }
      });
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
      if (minutes < 10) {
        minutes = "0" + minutes;
      }
      month += 1;
      var db = firebase.firestore();
      db.collection("Advice")
        .add({
          title: document.getElementById("nameAdvice").value,
          status: 0,
          user: localStorage.getItem("uid"),
          text: document.getElementById("textarea").value,
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
#myInput_Adv {
  background-position: 10px 10px;
  background-repeat: no-repeat;
  width: 100%;
  font-size: 16px;
  padding: 12px 20px 12px 40px;
  border: 1px solid #ddd;
  margin-bottom: 12px;
}
</style>