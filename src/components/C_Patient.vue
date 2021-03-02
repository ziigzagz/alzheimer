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
              <td>{{ item.ชื่อ }}</td>
              <td>{{ item.อายุ }}</td>
              <td>{{ item.คนดูแล }}</td>
              <td>{{ item.เบอร์ }}</td>
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
              dataset["UID"] = element.id;
              dataset["ID"] = Info.data().ID;
              dataset["ชื่อ"] = Info.data().ชื่อ;
              dataset["อายุ"] = Info.data().อายุ;
              dataset["คนดูแล"] = Info.data().คนดูแล;
              dataset["เบอร์"] = Info.data().เบอร์;
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
            // console.log(element[29])
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
                    
                    Status:0,
                    ID: element[1],
                    คำนำหน้าชื่อ: element[2],
                    ชื่อ: element[3],
                    วันเกิด: element[4],
                    อายุ:this.calAge(date),
                    น้ำหนัก: element[5],
                    ส่วนสูง: element[6],
                    คนดูแล: element[7],
                    Email: element[8],
                    บ้านเลขที่: element[9],
                    หมู่: element[10],
                    ตรอกซอย: element[11],
                    ถนน: element[12],
                    อำเภอ: element[13],
                    จังหวัด: element[14],
                    รหัสไปรษณีย์: element[15],
                    เบอร์: element[16],
                    การศึกษา: element[17],
                    สาขาวิชา: element[18],
                    อาชีพ: element[19],
                    ประวัติการเจ็บป่วยในอดีต: element[20],
                    ประวัติการผ่าตัด: element[21],
                    โรคประจำตัว: element[22],
                    ยาที่รับประทานประจำ: element[23],
                    แพ้ยาอาหาร: element[24],
                    สูบบุหรี่: element[25],
                    การดื่มแอลกอฮอล: element[26],
                    ออกกำลังกาย: element[27],
                    การนอนหลับ: element[28],
                    เวลาเข้านอน: element[29].toString(),
                    เวลาตื่นนอน: element[30].toString(),
                    การรับประทานอาหาร: element[31],
                    งานอดิเรก: element[32],
                    มีปัญหาการมองเห็น: element[33],
                    มีปัญหาด้านการได้ยิน: element[34],
                    มีปัญหาด้านการเคลื่อนไหว: element[35],
                    มีปัญหาด้านความจำ: element[36],
                    มีปัญหาด้านสมาธิ: element[37],
                    มีปัญหาด้านการจัดการ: element[38],
                    หลงทางจำทางไม่ได้: element[39],
                    มีปัญหาด้านการอ่านเขียน: element[40],
                    หงุดหงิดโมโหง่าย: element[41],
                    การสร้างสัมพันธภาพ: element[42],
                    การรอคอยความอดทน: element[43],
                    การนึกคำพูดสื่อสาร: element[44],
                    ความเข้าใจในการสื่อสาร: element[45],
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