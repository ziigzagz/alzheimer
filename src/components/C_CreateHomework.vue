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
            id="homeworkName"
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
        <div class="col-6 mx-auto">
          <select
            class="form-select"
            aria-label="Default select example"
            @change="myFunction()"
            id="select"
          >
            <option selected>กรุณาเลือกขนาด</option>
            <option value="1">8x8</option>
            <option value="2">10x10</option>
            <option value="3">14x14</option>
            <option value="4">18x18</option>
            <option value="5">20x20</option>
          </select>
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
              <button class="btn btn-warning mr-3" @click="reset">reset</button>
              <button class="btn btn-success" @click="create">สร้าง</button>
            </div>
          </div>
        </div>
      </div>
      <div class="row justify-content-center" id="eight">
        <!-- คำตอบ -->
        <div class="col-6 offset-4 align-self-center p-0">
          <div v-for="i in 8" v-bind:key="i">
            <div class="mx-auto">
              <button
                type="button"
                :id="'btn8' + i + '/' + j"
                class="btn btn-default"
                @click="changeColor8(i, j)"
                v-for="j in 8"
                v-bind:key="j"
              ></button>
            </div>
          </div>
        </div>
      </div>
      <div class="row" id="ten">
        <!-- คำตอบ -->
        <div class="col-6 mx-auto offset-4">
          <div v-for="i in 10" v-bind:key="i">
            <button
              type="button"
              :id="'btn10' + i + '/' + j"
              class="btn btn-default"
              @click="changeColor10(i, j)"
              v-for="j in 10"
              v-bind:key="j"
            ></button>
          </div>
        </div>
      </div>
      <div class="row" id="fourteen">
        <!-- คำตอบ -->
        <div class="col-9 mx-auto offset-2">
          <div v-for="i in 14" v-bind:key="i">
            <button
              type="button"
              :id="'btn14' + i + '/' + j"
              class="btn btn-default"
              @click="changeColor14(i, j)"
              v-for="j in 14"
              v-bind:key="j"
            ></button>
          </div>
        </div>
      </div>
      <div class="row" id="eightteen">
        <!-- คำตอบ -->
        <div class="col mx-auto text-center">
          <div v-for="i in 18" v-bind:key="i">
            <button
              type="button"
              :id="'btn18' + i + '/' + j"
              class="btn btn-default"
              @click="changeColor18(i, j)"
              v-for="j in 18"
              v-bind:key="j"
            ></button>
          </div>
        </div>
      </div>
      <div class="row" id="twenty">
        <!-- คำตอบ -->
        <div class="col mx-auto text-center">
          <div v-for="i in 20" v-bind:key="i">
            <button
              type="button"
              :id="'btn20' + i + '/' + j"
              class="btn btn-default"
              @click="changeColor20(i, j)"
              v-for="j in 20"
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
      eight: [
        [
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
        ],
      ],
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
      foueteen: [
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
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
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
      twenty:[
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
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],[
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ]
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
    };
  },
  mounted() {
    // ===================== setting ========================
    // none is disable
    // ======================================================
    var x = document.getElementById("eight");
    x.style.display = "none";
    x = document.getElementById("ten");
    x.style.display = "none";
    x = document.getElementById("fourteen");
    x.style.display = "none";
    x = document.getElementById("eightteen");
    x.style.display = "none";
    x = document.getElementById("twenty");
    x.style.display = "none";
    // first view page set color
    var i, j, txtid;
    for (i = 0; i < 17; i++) {
      txtid = "btncolorplt" + (i + 1);
      console.log(txtid);
      document.getElementById(txtid).style.backgroundColor = this.colorlist[i];
      // console.log(this.colorlist[i], txtid);
    }
  },
  methods: {
    // onchange select
    myFunction() {
      var x = document.getElementById("select").value;
      if (x == 1) {
        localStorage.setItem("Hw_size", 8);
        x = document.getElementById("eight");
        x.style.display = "block";
        x = document.getElementById("ten");
        x.style.display = "none";
        x = document.getElementById("fourteen");
        x.style.display = "none";
        x = document.getElementById("eightteen");
        x.style.display = "none";
        x = document.getElementById("twenty");
        x.style.display = "none";
      } else if (x == 2) {
        localStorage.setItem("Hw_size", 10);
        x = document.getElementById("eight");
        x.style.display = "none";
        x = document.getElementById("ten");
        x.style.display = "block";
        x = document.getElementById("fourteen");
        x.style.display = "none";
        x = document.getElementById("eightteen");
        x.style.display = "none";
        x = document.getElementById("twenty");
        x.style.display = "none";
      } else if (x == 3) {
        localStorage.setItem("Hw_size", 14);
        x = document.getElementById("eight");
        x.style.display = "none";
        x = document.getElementById("ten");
        x.style.display = "none";
        x = document.getElementById("fourteen");
        x.style.display = "block";
        x = document.getElementById("eightteen");
        x.style.display = "none";
        x = document.getElementById("twenty");
        x.style.display = "none";
      } else if (x == 4) {
        localStorage.setItem("Hw_size", 18);
        x = document.getElementById("eight");
        x.style.display = "none";
        x = document.getElementById("ten");
        x.style.display = "none";
        x = document.getElementById("fourteen");
        x.style.display = "none";
        x = document.getElementById("eightteen");
        x.style.display = "block";
        x = document.getElementById("twenty");
        x.style.display = "none";
      } else if (x == 5) {
        localStorage.setItem("Hw_size", 20);
        x = document.getElementById("eight");
        x.style.display = "none";
        x = document.getElementById("ten");
        x.style.display = "none";
        x = document.getElementById("fourteen");
        x.style.display = "none";
        x = document.getElementById("eightteen");
        x.style.display = "none";
        x = document.getElementById("twenty");
        x.style.display = "block";
      }
    },
    upload() {
      var r;
      var g;
      var b;
      var i = 0,
        j = 0;
      var storageRef = firebase.storage().ref("img");

      var file = document.getElementById("files").files[0];
      // console.log(file);

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
              .post(path, [resdownload, localStorage.getItem("Hw_size")])
              .then((res) => {
                console.log(res);
                res.data.forEach((row) => {
                  j = 1;
                  i++;
                  //row
                  row.forEach((col) => {
                    // console.log(col);
                    r = col[2];
                    g = col[1];
                    b = col[0];
                    // console.log(rgbToHex(r, g, b));
                    // console.log(i, j);
                    var hw_size = localStorage.getItem("Hw_size");
                    if (hw_size == "8") {
                      var txt = "btn8" + i + "/" + j;
                      this.eight[i - 1][j - 1] = rgbToHex(r, g, b);
                      document.getElementById(
                        txt
                      ).style.backgroundColor = rgbToHex(r, g, b);
                    } else {
                      if (hw_size == "10") {
                        var txt = "btn10" + i + "/" + j;
                        this.eightteen[i - 1][j - 1] = rgbToHex(r, g, b);
                        document.getElementById(
                          txt
                        ).style.backgroundColor = rgbToHex(r, g, b);
                      } else {
                        if (hw_size == "14") {
                          var txt = "btn14" + i + "/" + j;
                          this.eightteen[i - 1][j - 1] = rgbToHex(r, g, b);
                          document.getElementById(
                            txt
                          ).style.backgroundColor = rgbToHex(r, g, b);
                        } else {
                          if (hw_size == "18") {
                            var txt = "btn18" + i + "/" + j;
                            this.eightteen[i - 1][j - 1] = rgbToHex(r, g, b);
                            document.getElementById(
                              txt
                            ).style.backgroundColor = rgbToHex(r, g, b);
                          } else {
                            if (hw_size == "20") {
                              var txt = "btn20" + i + "/" + j;
                              this.eightteen[i - 1][j - 1] = rgbToHex(r, g, b);
                              document.getElementById(
                                txt
                              ).style.backgroundColor = rgbToHex(r, g, b);
                            } else {
                            }
                          }
                        }
                      }
                    }

                    j++;
                  });
                  console.log("END");
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
      console.log(this.eightteen);
    },
    create() {
      var db = firebase.firestore();
      var homeworkName = document.getElementById("homeworkName").value;
      if (homeworkName.length == 0) {
        console.log(homeworkName.length);
        Swal.fire({
          icon: "error",
          title: "Oops...",
          text: "กรุณาใส่ชื่อการบ้าน",
          timer: 1500,
        });
      } else {
        var newdata = {};
        var str = "";
        var i = 0;
        var j = 0;
        var hw_size = localStorage.getItem("Hw_size");
        if (hw_size == "8") {
          this.eight.forEach((element_i) => {
            element_i.forEach((element_j) => {
              str += element_j.toString() + "/";
            });
            str += "*";
          });
        } else {
          if (hw_size == "8") {
            this.eight.forEach((element_i) => {
              element_i.forEach((element_j) => {
                str += element_j.toString() + "/";
              });
              str += "*";
            });
          } else {
            if (hw_size == "10") {
              this.eight.forEach((element_i) => {
                element_i.forEach((element_j) => {
                  str += element_j.toString() + "/";
                });
                str += "*";
              });
            } else {
              if (hw_size == "14") {
                this.eight.forEach((element_i) => {
                  element_i.forEach((element_j) => {
                    str += element_j.toString() + "/";
                  });
                  str += "*";
                });
              } else {
                if (hw_size == "18") {
                  this.eight.forEach((element_i) => {
                    element_i.forEach((element_j) => {
                      str += element_j.toString() + "/";
                    });
                    str += "*";
                  });
                } else {
                  if (hw_size == "20") {
                    this.eight.forEach((element_i) => {
                      element_i.forEach((element_j) => {
                        str += element_j.toString() + "/";
                      });
                      str += "*";
                    });
                  }
                }
              }
            }
          }
        }
        console.log(str);
        db.collection("HomeworkTemplate")
          .add({
            Homework_name: homeworkName,
            Homework_data: str,
            Homework_size: localStorage.getItem("Hw_size"),
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
              // window.location.href = "/HomeworkList";
            });
          })
          .catch(function (error) {
            console.error("Error adding document: ", error);
          });
      }

      // console.log(homeworkName.length);
      // console.log(homeworkName);
    },
    changeColor8(i, j) {
      console.log(i, j);
      this.eight[i - 1][j - 1] = this.colorlist[
        localStorage.getItem("color") - 1
      ];
      var txtid = "btn8" + i + "/" + j;
      document.getElementById(txtid).style.backgroundColor = this.colorlist[
        localStorage.getItem("color") - 1
      ];
    },
    changeColor10(i, j) {
      console.log(i, j);
      var txtid = "btn10" + i + "/" + j;
      document.getElementById(txtid).style.backgroundColor = this.colorlist[
        localStorage.getItem("color") - 1
      ];
    },
    changeColor14(i, j) {
      console.log(i, j);

      var txtid = "btn14" + i + "/" + j;
      document.getElementById(txtid).style.backgroundColor = this.colorlist[
        localStorage.getItem("color") - 1
      ];
    },
    changeColor18(i, j) {
      console.log(i, j);
      this.eightteen[i - 1][j - 1] = this.colorlist[
        localStorage.getItem("color") - 1
      ];
      var txtid = "btn18" + i + "/" + j;
      document.getElementById(txtid).style.backgroundColor = this.colorlist[
        localStorage.getItem("color") - 1
      ];
      console.log(this.eightteen);
    },
    changeColor20(i, j) {
      console.log(i, j);
      var txtid = "btn20" + i + "/" + j;
      document.getElementById(txtid).style.backgroundColor = this.colorlist[
        localStorage.getItem("color") - 1
      ];
    },
    setStateColor(i) {
      localStorage.setItem("color", i);
      console.log(i);
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