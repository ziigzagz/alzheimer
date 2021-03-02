<template>
  <div class="container">
    <div class="row">
      <div class="col-6">
        <button class="btn btn-info m-2" @click="upload">เพิ่ม</button>
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
              <th scope="col">แก้ไข/ดู</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in datas" :key="index">
              <th scope="row">{{ item.ID }}</th>
              <td>{{ item.name }}</td>
              <td>{{ item.Age }}</td>
              <td>{{ item.UID }}</td>
              <td>{{ item.Tel }}</td>
              <td>
                <button class="btn btn-info" @click="viewInfo(item.UID)">
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
// status 0 = Patient , 1 = Staff
import firebase from "firebase";

export default {
  data() {
    return {
      datas: [],
    };
  },
  async mounted() {
    var db = firebase.firestore();
    var dataset = {};
    var docRef = await db.collection("InfoPatient").where("Status", "!=", 1);
    docRef
      .get()
      .then((doc) => {
        doc.forEach((element) => {
          var row = db.collection("InfoPatient").doc(element.id);
          row
            .get()
            .then((Info) => {
              // console.log(Info.data().Name);
              dataset["ID"] = Info.data().ID;
              dataset["name"] = Info.data().Name;
              dataset["UID"] = element.id;
              dataset["Birthday"] = Info.data().Birthday;
              dataset["Age"] = Info.data().Age;
              dataset["Tel"] = Info.data().Tel;
              dataset["Email"] = Info.data().Email;
              dataset["ww"] = Info.data().TEL;
              dataset["hh"] = Info.data().TEL;
              dataset["คนดูแล"] = Info.data().คนดูแล;
              // console.log(dataset);
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
    viewInfo(uid) {
      localStorage.setItem("uid", uid);
      window.location.href = "/Patient";
    },
    calAge(x) {
      var dob = new Date(x);
      //calculate month difference from current date in time
      var month_diff = Date.now() - dob.getTime();
      //convert the calculated difference in date format
      var age_dt = new Date(month_diff);
      //extract year from date
      var year = age_dt.getUTCFullYear();
      //now calculate the age of the user
      var age = Math.abs(year - 1970);
      var finalage;
      // console.log(age);
      // console.log(typeof(age));
      return age;
    },
    async upload() {
      var i = 0;
      const array1 = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
      ];
      var uid = ""
      var passwordHash = require("password-hash");
      var hashedPassword = passwordHash.generate("123456");
      const input = document.getElementById("input");
      await readXlsxFile(input.files[0]).then((rows) => {
        rows.forEach((element) => {
          const isLargeNumber = (element1) =>
            element1 == element[4].toString().split(" ")[1];
          var month = array1.findIndex(isLargeNumber) + 1;
          // console.log(month,element[4].toString().split(" ")[2]);
          var date =
            month.toString() +
            "/" +
            element[4].toString().split(" ")[2] +
            "/" +
            parseInt(element[4].toString().split(" ")[3]).toString();
          if (i == 0) {
            i++;
          } else {
            var db = firebase.firestore();
            firebase
              .auth()
              .createUserWithEmailAndPassword(element[2], "123456")
              .then((userCredential) => {
                console.log(userCredential.user.uid)
                uid = userCredential.user.uid;
              })
              .catch((error) => {
                var errorCode = error.code;
                var errorMessage = error.message;
                console.log(errorCode,errorMessage)
              });
              db.collection("InfoPatient")
                  .add({
                    ID: element[1],
                    Email: element[2],
                    name: element[3],
                    Birthday: element[4],
                    Age: this.calAge(date),
                    Tel: element[5],
                    ww: element[6],
                    hh: element[7],
                    คนดูแล: element[8],
                    Status: 0,
                    uid: uid,
                    Timestamp: firebase.firestore.FieldValue.serverTimestamp(),
                  })
                  .then(function (docRef) {
                    console.log("Document written with ID: ", docRef.id);
                    uid = ""
                  })
                  .catch(function (error) {
                    console.error("Error adding document: ", error);
                  });
          }
        });
      });
    },
  },
};
import readXlsxFile from "read-excel-file";
</script>

<style>
</style>