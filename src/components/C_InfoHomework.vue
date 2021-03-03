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
            class="btn btn-default mx-auto"
            @click="setStateColor(j)"
            v-for="j in 17"
            v-bind:key="j"
          ></button>
          <div class="row mt-5">
            <div class="col text-center">
              <button class="btnc btn-warning mr-3" @click="reset">
                reset
              </button>
              <button class="btnc btn-success" @click="check">ส่ง</button>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <!-- โจทย์ -->
        <div class="col-6 m-0">
          <div class="row">
            <div v-for="i in 18" v-bind:key="i" class="text-center">
              <button
                type="button"
                :id="'btnprop' + i + '/' + j"
                class="btn btn-default"
                v-for="j in 18"
                @click="testColor(i, j)"
                v-bind:key="j"
              ></button>
            </div>
          </div>
        </div>
        <!-- คำตอบ -->
        <div class="col-6 m-0">
          <div class="row">
            <div v-for="i in 18" v-bind:key="i" class="text-center">
              <button
                type="button"
                :id="'btn' + i + '/' + j"
                class="btn btn-default"
                @click="changeColor(i, j)"
                v-for="j in 18"
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
export default {
  data() {
    return {
      eightteen: [
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
      eightteen_ans: [
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
        "#b0ffF4", //ฟ้าอ่อน
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
      // console.log(txtid);
      document.getElementById(txtid).style.backgroundColor = this.colorlist[i];
      // console.log(this.colorlist[i], txtid);
    }

    var docRef = db
      .collection("HomeworkTemplate")
      .doc(localStorage.getItem("id_hwTemplate").toString());
    docRef.get().then((doc) => {
      // console.log(doc.data().Homework_data);
      // console.log(element.data());
      this.homeworkName = doc.data();
      var tmp = doc.data().Homework_data.split("*");
      // tmp = tmp.pop()
      // console.log(tmp[0].split("/"));
      var txtid;
      i = 0;
      j = 0;
      for (i = 0; i < 18; i++) {
        // console.log(tmp[i].split("/"))
        for (j = 0; j < 18; j++) {
          // console.log(tmp[i].split("/")[j]);
          txtid = "btnprop" + (i + 1) + "/" + (j + 1);
          this.eightteen[i][j] = tmp[i].split("/")[j];
          document.getElementById(txtid).style.backgroundColor = tmp[i].split(
            "/"
          )[j];
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
        console.log(h, m, s);
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
      console.log(i, j);
    },
    async check() {
      var count_correct = 0;
      var count_error = 0;
      var i = 0;
      var j = 0;
      var error = [];
      // console.log(document.getElementById("btn1/2").style.backgroundColor);
      // console.log(document.getElementById("btnprop1/2").style.backgroundColor);
      this.eightteen.forEach((element_i, i) => {
        element_i.forEach((element_j, j) => {
          if (element_j == this.eightteen_ans[i][j]) {
            count_correct++;
          } else {
            count_error++;
            // console.log(i, j);
            error.push([i, j]);
          }
          // console.log(element_j,this.eightteen_ans[i][j])
        });
      });
      localStorage.setItem("Error", JSON.stringify(error));
      // console.log("pass",100-count_error/324*100)
      // localStorage.setItem("isHomeworkPass","pass")
      if (100 - (count_error / 324) * 100 > 80) {
        localStorage.setItem("isHomeworkPass", "pass");
      } else {
        localStorage.setItem("isHomeworkPass", "not pass");
      }
      var str = "";
      localStorage.setItem("count_correct", count_correct);
      localStorage.setItem("count_error", count_error);
      this.eightteen_ans.forEach((element_i) => {
        element_i.forEach((element_j) => {
          str += element_j.toString() + "/";
        });
        str += "*";
      });
      // check firsttime
      var isFirsttime;
      var db = firebase.firestore();
      var docRef = await db
        .collection("Homework")
        .doc(localStorage.getItem("id_hw"));
      docRef
        .get()
        .then((data) => {
          console.log(data.data());
          if (data.data().timer_first == "0") {
            isFirsttime = 1;
            console.log(isFirsttime);
          } else {
            isFirsttime = 0;
            console.log(isFirsttime);
          }
        })
        .then(() => {
          console.log(str, 1);
          if (isFirsttime == 1) {
            if (localStorage.getItem("isHomeworkPass") == "pass") {
              localStorage.setItem("ans", str);
              console.log(str, 1);
              // console.log(str.split("*"));
              var db = firebase.firestore();
              const up = db
                .collection("Homework")
                .doc(localStorage.getItem("id_hw"));
              up.update({
                ans: str.split("*"),
                timer_first: localStorage.getItem("timer_ms"),
                status: 1,
              }).then(() => {
                localStorage.setItem("ans", str);
                window.location.href = "/CheckHomework";
              });
            } else {
              localStorage.setItem("ans", str);
              window.location.href = "/CheckHomework";
            }
          } else {
            if (localStorage.getItem("isHomeworkPass") == "pass") {
              localStorage.setItem("ans", str);
              console.log(str, 2);
              console.log(str.split("*"));
              var db = firebase.firestore();
              const up = db
                .collection("Homework")
                .doc(localStorage.getItem("id_hw"));
              up.update({
                ans: str.split("*"),
                timer_release: localStorage.getItem("timer_ms"),
                status: 1,
              }).then(() => {
                localStorage.setItem("ans", str);
                window.location.href = "/CheckHomework";
              });
            } else {
              localStorage.setItem("ans", str);
              window.location.href = "/CheckHomework";
            }
          }
          
        });
      // Insert hw to firebase
    },
    changeColor(i, j) {
      // console.log(i, j);
      var txtid = "btn" + i + "/" + j;
      document.getElementById(txtid).style.backgroundColor = this.colorlist[
        localStorage.getItem("color") - 1
      ];
      this.eightteen_ans[i - 1][j - 1] = this.colorlist[
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