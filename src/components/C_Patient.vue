<template>
  <div class="container">
    <div class="row justify-content-between">
      <div class="col-4 text-center">
        <button class="btn btn-info ms-2" @click="upload">เพิ่ม</button>
        <input type="file" id="input" accept=".xlsx" />
      </div>
      <div class="col-4 text-rigth">
        <button class="btn btn-danger me-0" @click="clear">ลบข้อมูล</button>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <input
          type="text"
          id="myInput"
          @keyup="myFunction"
          placeholder="ค้นหาหมายเลขผู้ป่วย...."
          title="Type in a name"
          accept=".jpg, .png, .jpeg, .gif, .bmp, .tif, .tiff|image/*"
        />
        <!-- <table class="table table-striped text-center" id="myTable1">
          <thead>
            <tr>
              <th scope="col">HN1</th>
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
                <button @click="somethingWithjQuery()">123</button>
              </td>
            </tr>
          </tbody>
        </table> -->
        <table id="myTable" class="table table-striped text-center">
          <tr>
            <th scope="col">HN</th>
            <th scope="col">ชื่อ-สกุล</th>
            <th scope="col">อายุ</th>
            <th scope="col">ชื่อผู้ดูแล</th>
            <th scope="col">เบอร์โทรติดต่อ</th>
            <th scope="col"></th>
          </tr>
          <tr v-for="(item, index) in datas" :key="index" class="mt-2">
            <td scope="row">{{ item.ID }}</td>
            <td>{{ item.ชื่อ }}</td>
            <td>{{ item.อายุ }}</td>
            <td>
              {{ item.คนดูแล }}
            </td>
            <td>{{ item.เบอร์ }}</td>
            <td>
              <button
                class="btn btn-info bg-info mt-2"
                @click="viewInfo(item.UID)"
              >
                ดูข้อมูล
              </button>
            </td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
// status 0 = Patient , 1 = Staff
import firebase from "firebase";
import Swal from "sweetalert2";
import $ from "jquery";
import { somethingWithjQuery } from "../main";
export default {
  data() {
    return {
      datas: [],
      numrow: 0,
      database_hospital: [],
      ID_hospital: [],
      ID_Error: [], //ซ้ำ
    };
  },

  async mounted() {
    var db = firebase.firestore();
    var dataset = {};
    var docRef = await db.collection("InfoPatient").orderBy("ID", "asc");
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
              this.ID_hospital.push(Info.data().ID);
            })
            .catch(function (error) {
              console.log("Error getting document:", error);
            });
        });
      })
      .catch(function (error) {
        console.log("Error getting document:", error);
      });
    var db = firebase.firestore();
    var docRef_InfoPatient_Database = db.collection("InfoPatient_Database");
    docRef_InfoPatient_Database.get().then((doc) => {
      doc.forEach((Info) => {
        console.log(Info.data());
        dataset["UID"] = Info.id;
        dataset["ID"] = Info.data().ID;
        dataset["ชื่อ"] = Info.data().ชื่อ;
        dataset["อายุ"] = Info.data().อายุ;
        dataset["คนดูแล"] = Info.data().คนดูแล;
        dataset["เบอร์"] = Info.data().เบอร์;
        this.database_hospital.push(dataset);
        this.ID_hospital.push(Info.data().ID);
        dataset = {};
      });
    });
  },
  methods: {
    myFunction() {
      var input, filter, table, tr, td, i, txtValue;
      input = document.getElementById("myInput");
      filter = input.value.toUpperCase();
      table = document.getElementById("myTable");
      tr = table.getElementsByTagName("tr");
      for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
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
    toggleOrder() {
      this.sortDesc = !this.sortDesc;
    },
    nextSort() {
      let index = this.headers.findIndex((h) => h.value === this.sortBy);
      index = (index + 1) % this.headers.length;
      this.sortBy = this.headers[index].value;
    },
    viewInfo(uid) {
      localStorage.setItem("uid", uid);
      localStorage.setItem("Tab_mode", 3);

      window.location.href = "/Patient";
    },
    calAge(x) {
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
      var dob = new Date(1998, 11, 4);
      //calculate month difference from current date in time
      var year = x.split(" ")[3];
      var month = x.split(" ")[1];
      var day = x.split(" ")[2];
      var count_month = 1;
      var i;
      for (i = 0; i < 12; ++i) {
        if (array1[i] == month) {
          break;
        }
        count_month++;
      }
      year = parseInt(year);
      day = parseInt(day);
      // console.log("x", x);
      // console.log("dob", dob);
      // console.log("year", year);
      // console.log("month", month);
      // console.log("count_month", count_month);
      // console.log("day", day);
      var dob = new Date(year, count_month, day);
      // var dob = new Date(1998, 11, 4);
      var month_diff = Date.now() - dob.getTime();
      //convert the calculated difference in date format
      var age_dt = new Date(month_diff);
      //extract year from date
      var year = age_dt.getUTCFullYear();
      //now calculate the age of the user
      var age = Math.abs(year - 1970);
      var finalage;
      // console.log(age, x);
      // console.log(typeof(age));
      return age;
    },
    clear() {
      Swal.fire({
        title: "ยืนยัน",
        text: "คุณต้องการยืนยันลบข้อมูลทั้งหมดใช่หรือไม่?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "ใช่",
        cancelButtonText: "ไม่",
      }).then((result) => {
        if (result.isConfirmed) {
          const ref = firebase.firestore().collection("InfoPatient");
          ref.onSnapshot((snapshot) => {
            snapshot.docs.forEach((doc) => {
              ref.doc(doc.id).delete();
            });
          });
          Swal.fire({
            position: "center",
            icon: "success",
            title: "ลบข้อมูลสำเร็จ!",
            showConfirmButton: false,
            timer: 1500,
          }).then(() => {
            location.reload();
          });
          // Swal.fire("ยืนยันสำเร็จ!", "ทำการอัปเดตเรียบร้อย", "success");
        }
      });
    },
    // Use it like this:

    async upload() {
      var db = firebase.firestore();
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
      var uid = "";
      var passwordHash = require("password-hash");
      var hashedPassword = passwordHash.generate("123456");
      const input = document.getElementById("input");
      await readXlsxFile(input.files[0]).then((rows) => {
        rows.forEach((element) => {
          if (i == 0) {
            i++;
          } else {
            const isLargeNumber = (element1) =>
              element1 == element[4].toString().split("/")[0];
            var month = array1.findIndex(isLargeNumber) + 1;
            console.log(element[4].toString().split("/"), month);
            var date =
              element[4].toString().split("/")[0] +
              "/" +
              element[4].toString().split("/")[1] +
              "/" +
              element[4].toString().split("/")[2];
            firebase
              .auth()
              .createUserWithEmailAndPassword(element[8], "123456")
              .then((userCredential) => {
                console.log(userCredential.user.uid);
                uid = userCredential.user.uid;
              })
              .catch((error) => {
                var errorCode = error.code;
                var errorMessage = error.message;
                console.log(errorCode, errorMessage);
              });
            
            if (this.ID_hospital.includes(element[1])) {
              this.ID_Error.push(element[1]);
              console.log("fail : ", element[1]);
            } else {
              console.log("success : ", element[1]);
              db.collection("InfoPatient")
                .add({
                  Status: 0,
                  ID: element[1],
                  คำนำหน้าชื่อ: element[2],
                  ชื่อ: element[3],
                  วันเกิด: element[4],
                  อายุ: this.calAge(date),
                  // อายุ: 20,
                  น้ำหนัก: element[5],
                  ส่วนสูง: element[6],
                  คนดูแล: element[7],
                  Email: element[8],
                  ผู้ให้ข้อมูล: element[9],
                  เบอร์ผู้ให้ข้อมูล: element[10],
                  บ้านเลขที่: element[11],
                  หมู่: element[12],
                  ตรอกซอย: element[13],
                  ถนน: element[14],
                  อำเภอ: element[15],
                  จังหวัด: element[16],
                  รหัสไปรษณีย์: element[17],
                  เบอร์: element[18],
                  การศึกษา: element[19],
                  สาขาวิชา: element[20],
                  อาชีพ: element[21],
                  ประวัติการเจ็บป่วยในอดีต: element[22],
                  ประวัติการผ่าตัด: element[23],
                  โรคประจำตัว: element[24],
                  ยาที่รับประทานประจำ: element[25],
                  แพ้ยาอาหาร: element[26],
                  สูบบุหรี่: element[27],
                  การดื่มแอลกอฮอล: element[28],
                  ออกกำลังกาย: element[29],
                  การนอนหลับ: element[30],
                  เวลาเข้านอน: element[31].toString(),
                  เวลาตื่นนอน: element[32].toString(),
                  การรับประทานอาหาร: element[33],
                  งานอดิเรก: element[34],
                  มีปัญหาการมองเห็น: element[35],
                  มีปัญหาด้านการได้ยิน: element[36],
                  มีปัญหาด้านการเคลื่อนไหว: element[37],
                  มีปัญหาด้านความจำ: element[38],
                  มีปัญหาด้านสมาธิ: element[39],
                  มีปัญหาด้านการจัดการ: element[40],
                  หลงทางจำทางไม่ได้: element[41],
                  มีปัญหาด้านการอ่านเขียน: element[42],
                  หงุดหงิดโมโหง่าย: element[43],
                  การสร้างสัมพันธภาพ: element[44],
                  การรอคอยความอดทน: element[45],
                  การนึกคำพูดสื่อสาร: element[46],
                  ความเข้าใจในการสื่อสาร: element[47],
                  Timestamp: firebase.firestore.FieldValue.serverTimestamp(),
                })
                .then(function (docRef) {
                  console.log("Document written with ID: ", docRef.id);
                  uid = "";
                })
                .catch(function (error) {
                  console.error("Error adding document: ", error);
                });
            }
            console.log(this.ID_hospital.includes(element[1]));
          }
        });
      });
      Swal.fire({
        position: "top-end",
        icon: "success",
        title: "เพิ่มข้อมูลสำเร็จ",
        showConfirmButton: false,
        timer: 1500,
      }).then(() => {
        // alert(this.ID_Error);
        var s = "";
        this.ID_Error.forEach((element) => {
          s += element + "\n";
        });
        console.log(this.ID_Error.length);
        Swal.fire({
          icon: "error",
          title: "ไม่สามารถเพิ่มผู้ป่วยที่มีหมายเลขต่อไปนี้ได้",
          text: s,
        });
        // location.reload();
      });
    },
  },
};
import readXlsxFile from "read-excel-file";
</script>

<style>
#myInput {
  background-position: 10px 10px;
  background-repeat: no-repeat;
  width: 100%;
  font-size: 16px;
  padding: 12px 20px 12px 40px;
  border: 1px solid #ddd;
  margin-bottom: 12px;
}
</style>