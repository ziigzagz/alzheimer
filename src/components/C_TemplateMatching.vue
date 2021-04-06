<template>
  <div>
    <div class="container-fluid">
      <div class="row">
        <div class="col-4">
          <label for="exampleFormControlInput1" class="form-label"
            >ชื่อการบ้าน</label
          >
          <input
            type="text"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder=""
            v-model="homeworkName.Homework_name"
            readonly
          />
        </div>
      </div>
      <div class="row">
        <div class="col text-center">
          <button
            type="button"
            :id="'btncolorplt' + j"
            class="btnc btn-default mx-auto"
            @click="setStateColor(j)"
            v-for="j in 17"
            v-bind:key="j"
          ></button>
          <div class="row mt-5">
            <div class="col text-center">
              <button class="btn btn-warning mr-3" @click="reset">reset</button>
              <button class="btn btn-success" @click="check">ส่ง</button>
            </div>
          </div>
        </div>
      </div>
      <div class="row rowexam">
        <!-- โจทย์ -->
        <div class="col-6 m-0" id="ten">
          <div class="row">
            <div v-for="i in 10" v-bind:key="i" class="text-center">
              <button
                type="button"
                :id="'btnprop10' + i + '/' + j"
                class="btn btn-default"
                v-for="j in 10"
                @click="testColor(i, j)"
                v-bind:key="j"
              ></button>
            </div>
          </div>
        </div>

        <!-- คำตอบ -->
        <div class="col-6 m-0" id="ten_ans">
          <div class="row">
            <div v-for="i in 10" v-bind:key="i" class="text-center">
              <button
                type="button"
                :id="'btn10' + i + '/' + j"
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
  </div>
</template>

<script>
import firebase from "firebase";
import Swal from "sweetalert2";
const axios = require("axios");
export default {
  data() {
    return {
      Hw_size: parseInt(localStorage.getItem("Hw_size")),
      ten: [
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
      ],
      ten_ans: [
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
      ],
      colorlist: [
        "#79661e", //น้ำตาล
        "#ffec1F", //เหลืองเข้ม
        "#f6ff78", //เหลืองอ่อน
        "#21e83f", //เขียวอ่อน
        "#148f27", //เขียวเข้ม
        "#1f26ff", //น้ำเงิน
        "#a12dcf", //ม่วง
        "#f00800", //แดง
        "#ff892e", //ส้ม
        "#f007ff", //ชมพู
        "#ef9090", //เนื้อ
        "#6eddff", //ฟ้า
        "#b0fff4", //ฟ้าอ่อน
        "#ffffff", //ขาว
        "#c2c2c2", //เทาอ่อน
        "#878787", //เทาเข้ม
        "#000000", //ดำ
      ],
      homeworktemplatelist: [],
      homeworkName: "",
    };
  },
  mounted() {
    var db = firebase.firestore();
    var timer = 0;
    // first view page set color
    this.timer();
    var i, j, txtid;
    var lst = [];
    for (i = 0; i < 17; i++) {
      txtid = "btncolorplt" + (i + 1);
      document.getElementById(txtid).style.backgroundColor = this.colorlist[i];
    }

    var docRef = db
      .collection("HomeworkTemplate")
      .doc(localStorage.getItem("id_hwTemplate").toString());
    docRef.get().then((doc) => {
      this.homeworkName = doc.data();
      var tmp = doc.data().Homework_data.split("*");
      var txtid;
      i = 0;
      j = 0;
      var x = doc.data().Homework_size;
      localStorage.setItem("Hw_size", x);
      console.log(x);
      for (i = 0; i < 10; i++) {
        for (j = 0; j < 10; j++) {
          txtid = "btnprop10" + (i + 1) + "/" + (j + 1);
          this.ten[i][j] = tmp[i].split("/")[j];
          document.getElementById(txtid).style.backgroundColor = tmp[i].split(
            "/"
          )[j];
        }
      }
    });
    var isFirsttime;
    // var db = firebase.firestore();
    var docRef = db.collection("Homework").doc(localStorage.getItem("id_hw"));
    docRef.get().then((data) => {
      if (data.data().timer_first == "0") {
        isFirsttime = 1;
        console.log(isFirsttime);
      } else {
        isFirsttime = 0;
        console.log(isFirsttime);
      }
      if (isFirsttime == 0) {
        for (var i = 0; i < this.Hw_size; ++i) {
          for (var j = 0; j < this.Hw_size; ++j) {
            var tmp = data.data().ans[i].split("/");
            txtid =
              "btn" + localStorage.getItem("Hw_size") + (i + 1) + "/" + (j + 1);
            if (this.Hw_size == 8) {
              this.eight_ans[i][j] = tmp[j];
            } else if (this.Hw_size == 10) {
              this.ten_ans[i][j] = tmp[j];
            } else if (this.Hw_size == 14) {
              this.fourteen_ans[i][j] = tmp[j];
            } else if (this.Hw_size == 18) {
              this.eightteen_ans[i][j] = tmp[j];
            } else if (this.Hw_size == 20) {
              this.twenty_ans[i][j] = tmp[j];
            }

            document.getElementById(txtid).style.backgroundColor = tmp[j];
          }
        }
      }
    });
    // const cityRef = db.collection("HomeworkTemplate").doc("Fn0shgkIBuukMLUhxgBa");
    // const doc = cityRef.get().then((val)=>{
    // console.log(val.data())
    // });

    // console.log(this.homeworktemplatelist[0]);
    // });
    //  document.getElementById("btnprop1/3").style.backgroundColor = "#F00800";
    // document.getElementById("btnprop24").style.backgroundColor = "#F00800";
    // document.getElementById("btnprop35").style.backgroundColor = "#F00800";
    // document.getElementById("btnprop26").style.backgroundColor = "#F00800";
    console.log(window.innerWidth);
  },
  methods: {
    timer() {
      var s = 1,
        m = 0,
        h = 0,
        ms = 0;
      var timer;
      var interval = setInterval(function () {
        timer = h.toString() + ":" + m.toString() + ":" + s.toString();
        localStorage.setItem("timer", timer);
        localStorage.setItem("timer_ms", ms++);
        // console.log(h, m, s);
        s++;
        if (s % 60 == 0 || s > 59) {
          s = 0;
          m++;
        }
        if (m % 60 == 0 && m > 59) {
          s = 0;
          m = 0;
          h++;
        }
      }, 1000);
    },
    testColor(i, j) {
      var txtid = "btnprop10" + i + "/" + j;
      document.getElementById(txtid).style.backgroundColor = this.colorlist[
        localStorage.getItem("color") - 1
      ];
      this.ten[i - 1][j - 1] = this.colorlist[
        localStorage.getItem("color") - 1
      ];
      console.log(i, j);
    },
    async check() {
      const path = "http://127.0.0.1:5000/tm";
      axios
        .post(path, [this.ten,this.ten_ans])
        .then((res) => {});
    },
    changeColor(i, j) {
      // console.log(i, j);
      var Hw_size = localStorage.getItem("Hw_size");
      var txtid = "btn10" + i + "/" + j;
      document.getElementById(txtid).style.backgroundColor = this.colorlist[
        localStorage.getItem("color") - 1
      ];
      this.ten_ans[i - 1][j - 1] = this.colorlist[
        localStorage.getItem("color") - 1
      ];
    },
    setStateColor(i) {
      localStorage.setItem("color", i);
      // console.log(i)
    },
    reset() {
      var i, j, txtid;
      for (i = 0; i < 18; ++i) {
        for (j = 0; j < 18; ++j) {
          txtid = "btn" + (i + 1) + "/" + (j + 1);
          this.eightteen_ans[i][j] = "#ffffff";
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
  width: 45px;
  height: 45px;
  /* /* max-height: 100%; */
  max-width: 100%;
  margin: 0 0 0 0;
  border-color: black;
}

.btna {
  width: 20px;
  height: 20px;
  /* /* max-height: 100%; */
  max-width: 100%;
  margin: 0 0;
  border-color: black;
}

.btnc {
  color: black;
  font-size: 1.5em;
  width: 70px;
  height: 45px;
  margin: 0 0;
  border-color: black;
}
</style>