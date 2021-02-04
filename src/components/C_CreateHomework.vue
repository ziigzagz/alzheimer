<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col mx-auto">
          <label for="exampleFormControlInput1" class="form-label"
            >ชื่อการบ้าน</label
          >
          <input
            type="text"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder=""
          />
        </div>
        <div class="col mx-auto">
          <label for="exampleFormControlInput1" class="form-label"
            >เลือกรูป</label
          >
          <div class="row">
            <div class="col">
              <input type="file" id="files" />
            </div>
            <div class="col">
              <button class="btn btn-info" @click="upload">อัปโหลด</button>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col text-center">
          <button
            type="button"
            :id="'btncolorplt' + j"
            class="btn btn-default mx-auto"
            @click="setStateColor(j)"
            v-for="j in 16"
            v-bind:key="j"
          ></button>
          <div class="row mt-5">
            <div class="col text-center">
              <button class="btn btn-warning mr-3" @click="reset">reset</button>
              <button class="btn btn-success" @click="create">สร้าง</button>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <!-- คำตอบ -->
        <div class="col-6 mx-auto">
          <div v-for="i in 10" v-bind:key="i">
            <button
              type="button"
              :id="'btn' + i + j"
              class="btn btn-default"
              @click="changeColor(i, j)"
              v-for="j in 10"
              v-bind:key="j"
            ></button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import firebase from "firebase";
import Swal from "sweetalert2";
const axios = require("axios");
function componentToHex(c) {
  var hex = c.toString(16);
  return hex.length == 1 ? "0" + hex : hex;
}

function rgbToHex(r, g, b) {
  return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}
export default {
  data() {
    return {
      colorlist: [
        "#FFEC1F", //เหลืองเข้ม
        "#F6FF78", //เหลืองอ่อน
        "#21E83F", //เขียวเข้ม
        "#148F27", //เขียวอ่อน
        "#1F26FF", //น้ำเงิน
        "#A12DCF", // ม่วง
        "#F00800", //แดง
        "#FF892E", //ส้ม
        "#F266DD", //ชมพู
        "#EF9090", //เนื้อ
        "#6EDDFF", //ฟ้า
        "#B0FFF4", //ฟ้าอ่อน
        "#ffffff", //ขาว
        "#C2C2C2", //เทาอ่อน
        "#878787", //เทาเข้ม
        "#000000", //ดำ
      ],
    };
  },
  mounted() {
    // first view page set color
    var i, j, txtid;
    for (i = 0; i < 16; ++i) {
      txtid = "btncolorplt" + (i + 1);
      document.getElementById(txtid).style.backgroundColor = this.colorlist[i];
      // console.log(this.colorlist[i], txtid);
    }
  },
  methods: {
    // componentToHex(c) {
    //   var hex = c.toString(16);
    //   return hex.length == 1 ? "0" + hex : hex;
    // },
    // rgbToHex(r, g, b) {
    //   return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
    // },
    upload() {
      var r;
      var g;
      var b;
      var i = 0,
        j = 0;
      var storageRef = firebase.storage().ref("img");

      var file = document.getElementById("files").files[0];
      console.log(file);

      var thisRef = storageRef.child(file.name);

      thisRef.put(file).then((resupload) => {
        const storage = firebase.storage();
        storage
          .ref("img")
          .child(file.name)
          .getDownloadURL()
          .then((resdownload) => {
            console.log(resdownload);
            const path = "http://127.0.0.1:5000/get";
            axios
              .post(path, [resdownload])
              .then((res) => {
                res.data.forEach((row) => {
                  j = 1;
                  i++;
                  //row
                  row.forEach((col) => {
                    r = col[2];
                    g = col[1];
                    b = col[0];
                    // console.log(rgbToHex(r, g, b));
                    console.log(i, j);
                    var txt = "btn"+i+j;
                    document.getElementById(
                      txt
                    ).style.backgroundColor = rgbToHex(r, g, b);
                    j++;
                    
                    
                  });
                });
                // console.log(res.data);
                console.log(rgbToHex(r, g, b));
              })
              .catch((error) => {
                // eslint-disable-next-line
                console.log(error);
              });
          });
      });
    },
    create() {
      var db = firebase.firestore();
      db.collection("HomeworkTemplate")
        .add({
          Homework_name: document.getElementById("exampleFormControlInput1")
            .value,
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
            window.location.href = "/HomeworkList";
          });
        })
        .catch(function (error) {
          console.error("Error adding document: ", error);
        });
    },
    changeColor(i, j) {
      console.log(i, j);
      var txtid = "btn" + i + j;
      document.getElementById(txtid).style.backgroundColor = this.colorlist[
        localStorage.getItem("color") - 1
      ];
    },
    setStateColor(i) {
      localStorage.setItem("color", i);
    },
    reset() {
      var i, j, txtid;
      for (i = 0; i < 10; ++i) {
        for (j = 0; j < 10; ++j) {
          txtid = "btn" + (i + 1) + (j + 1);
          document.getElementById(txtid).style.backgroundColor = "#ffffff";
        }
      }
    },
  },
};
</script>

<style>
@import url("https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css");

.btn.btn-default {
  width: 55px;
  height: 55px;
  margin: 0 0;
  border-color: black;
}

.btnc {
  color: black;
  font-size: 1.5em;
  width: 70px;
  height: 45px;
  margin: 0 0;
}
</style>