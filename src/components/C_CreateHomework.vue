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
            v-model="Hw_name"
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
            <option value="6">t</option>
          </select>
        </div>
      </div>
      <div class="row">
        <button class="btn btn-warning m-2" @click="reset" id="reset">
          รีเซ็ท
        </button>
        <button class="btn btn-success m-2" id="create" @click="create">
          สร้าง
        </button>
        <button class="btn btn-success m-2" id="update" @click="update">
          อัพเดต
        </button>
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
            <div class="col text-center"></div>
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
      Hw_name: "",
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
      fourteen: [
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
      twenty: [
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
          "#ffffff",
          "#ffffff",
        ],
      ],
      colorlist: [
        "#79661e", //น้ำตาล
        "#ffec1f", //เหลืองเข้ม
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
        "#b0fff4", //ฟ้าอ่อน B0FFF4
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
    var have_hw_size = localStorage.getItem("Hw_size");
    if (have_hw_size) {
      console.log(12312312313);
      var create = document.getElementById("create");
      create.style.display = "none";
      var Hw_size = parseInt(have_hw_size);
      var select = document.getElementById("select");
      select.style.display = "none";
      var update = document.getElementById("update");
      update.style.display = "block";
      this.Hw_name = localStorage.getItem("Hw_name");
      var oldhw = localStorage.getItem("EditHomework");
      oldhw = oldhw.split("*");
      console.log(oldhw);
      if (parseInt(have_hw_size) == 8) {
        var x = document.getElementById("eight");
        x.style.display = "block";
        x = document.getElementById("ten");
        x.style.display = "none";
        x = document.getElementById("fourteen");
        x.style.display = "none";
        x = document.getElementById("eightteen");
        x.style.display = "none";
        x = document.getElementById("twenty");
        x.style.display = "none";
        for (i = 0; i < Hw_size; i++) {
          console.log(oldhw[i].split("/"));
          for (j = 0; j < Hw_size; j++) {
            this.eight[i][j] = oldhw[i].split("/")[j];
            txtid = "btn" + Hw_size + (i + 1) + "/" + (j + 1);
            // console.log(oldhw[i].split("/")[j],j)
            // console.log(txtid)
            document.getElementById(txtid).style.backgroundColor = oldhw[
              i
            ].split("/")[j];
          }
        }
      }
      if (parseInt(have_hw_size) == 10) {
        var x = document.getElementById("eight");
        x.style.display = "none";
        x = document.getElementById("ten");
        x.style.display = "block";
        x = document.getElementById("fourteen");
        x.style.display = "none";
        x = document.getElementById("eightteen");
        x.style.display = "none";
        x = document.getElementById("twenty");
        x.style.display = "none";
        for (i = 0; i < Hw_size; i++) {
          console.log(oldhw[i].split("/"));
          for (j = 0; j < Hw_size; j++) {
            this.ten[i][j] = oldhw[i].split("/")[j];
            txtid = "btn" + Hw_size + (i + 1) + "/" + (j + 1);
            // console.log(oldhw[i].split("/")[j],j)
            // console.log(txtid)
            document.getElementById(txtid).style.backgroundColor = oldhw[
              i
            ].split("/")[j];
          }
        }
      }
      if (parseInt(have_hw_size) == 14) {
        var x = document.getElementById("eight");
        x.style.display = "none";
        x = document.getElementById("ten");
        x.style.display = "none";
        x = document.getElementById("fourteen");
        x.style.display = "block";
        x = document.getElementById("eightteen");
        x.style.display = "none";
        x = document.getElementById("twenty");
        x.style.display = "none";
        for (i = 0; i < Hw_size; i++) {
          console.log(oldhw[i].split("/"));
          for (j = 0; j < Hw_size; j++) {
            this.fourteen[i][j] = oldhw[i].split("/")[j];
            txtid = "btn" + Hw_size + (i + 1) + "/" + (j + 1);
            // console.log(oldhw[i].split("/")[j],j)
            // console.log(txtid)
            document.getElementById(txtid).style.backgroundColor = oldhw[
              i
            ].split("/")[j];
          }
        }
      }
      if (parseInt(have_hw_size) == 18) {
        var x = document.getElementById("eight");
        x.style.display = "none";
        x = document.getElementById("ten");
        x.style.display = "none";
        x = document.getElementById("fourteen");
        x.style.display = "none";
        x = document.getElementById("eightteen");
        x.style.display = "block";
        x = document.getElementById("twenty");
        x.style.display = "none";
        for (i = 0; i < Hw_size; i++) {
          console.log(oldhw[i].split("/"));
          for (j = 0; j < Hw_size; j++) {
            this.eightteen[i][j] = oldhw[i].split("/")[j];
            txtid = "btn" + Hw_size + (i + 1) + "/" + (j + 1);
            // console.log(oldhw[i].split("/")[j],j)
            // console.log(txtid)
            document.getElementById(txtid).style.backgroundColor = oldhw[
              i
            ].split("/")[j];
          }
        }
      }
      if (parseInt(have_hw_size) == 20) {
        var x = document.getElementById("eight");
        x.style.display = "none";
        x = document.getElementById("ten");
        x.style.display = "none";
        x = document.getElementById("fourteen");
        x.style.display = "none";
        x = document.getElementById("eightteen");
        x.style.display = "none";
        x = document.getElementById("twenty");
        x.style.display = "block";
        for (i = 0; i < Hw_size; i++) {
          console.log(oldhw[i].split("/"));
          for (j = 0; j < Hw_size; j++) {
            this.twenty[i][j] = oldhw[i].split("/")[j];
            txtid = "btn" + Hw_size + (i + 1) + "/" + (j + 1);
            // console.log(oldhw[i].split("/")[j],j)
            // console.log(txtid)
            document.getElementById(txtid).style.backgroundColor = oldhw[
              i
            ].split("/")[j];
          }
        }
      }
    } else {
      var update = document.getElementById("update");
      update.style.display = "none";
      console.log(789);
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
      } else if (x == 6) {
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
        x.style.display = "none";
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
                console.log(res.data);
                console.log("res");
                res.data.forEach((row) => {
                  j = 1;
                  i++;
                  //row
                  row.forEach((col) => {
                    r = col[2];
                    g = col[1];
                    b = col[0];
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
                        this.ten[i - 1][j - 1] = rgbToHex(r, g, b);
                        document.getElementById(
                          txt
                        ).style.backgroundColor = rgbToHex(r, g, b);
                      } else {
                        if (hw_size == "14") {
                          var txt = "btn14" + i + "/" + j;
                          this.fourteen[i - 1][j - 1] = rgbToHex(r, g, b);
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
                              this.twenty[i - 1][j - 1] = rgbToHex(r, g, b);
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
    update() {
      var id = localStorage.getItem("id_hwTemplate");
      var db = firebase.firestore();
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
        console.log("8");
      } else {
        if (hw_size == "10") {
          this.ten.forEach((element_i) => {
            element_i.forEach((element_j) => {
              str += element_j.toString() + "/";
            });
            str += "*";
          });
          console.log("10", str.split("*"));
        } else {
          if (hw_size == "14") {
            this.fourteen.forEach((element_i) => {
              element_i.forEach((element_j) => {
                str += element_j.toString() + "/";
              });
              str += "*";
            });
            console.log("14");
          } else {
            if (hw_size == "18") {
              this.eightteen.forEach((element_i) => {
                element_i.forEach((element_j) => {
                  str += element_j.toString() + "/";
                });
                str += "*";
              });
              console.log("18");
            } else {
              if (hw_size == "20") {
                this.twenty.forEach((element_i) => {
                  element_i.forEach((element_j) => {
                    str += element_j.toString() + "/";
                  });
                  str += "*";
                });
              }
              console.log("20");
            }
          }
        }
      }
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
        console.log(str);
        var id = localStorage.getItem("id_hwTemplate");
        var Hw_name = document.getElementById("homeworkName").value;
        const update = db.collection("HomeworkTemplate").doc(id);
        console.log(Hw_name);
        update
          .update({
            Homework_data: str,
            Homework_name: Hw_name,
          })
          .then((docRef) => {
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
      }
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
          if (hw_size == "10") {
            this.ten.forEach((element_i) => {
              element_i.forEach((element_j) => {
                str += element_j.toString() + "/";
              });
              str += "*";
            });
          } else {
            if (hw_size == "14") {
              this.fourteen.forEach((element_i) => {
                element_i.forEach((element_j) => {
                  str += element_j.toString() + "/";
                });
                str += "*";
              });
            } else {
              if (hw_size == "18") {
                this.eightteen.forEach((element_i) => {
                  element_i.forEach((element_j) => {
                    str += element_j.toString() + "/";
                  });
                  str += "*";
                });
              } else {
                if (hw_size == "20") {
                  this.twenty.forEach((element_i) => {
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
        console.log(str);
        db.collection("HomeworkTemplate")
          .add({
            Homework_name: homeworkName,
            Homework_data: str,
            Homework_size: localStorage.getItem("Hw_size"),
            statusdel: 0,
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
      this.ten[i - 1][j - 1] = this.colorlist[
        localStorage.getItem("color") - 1
      ];
      var txtid = "btn10" + i + "/" + j;
      document.getElementById(txtid).style.backgroundColor = this.colorlist[
        localStorage.getItem("color") - 1
      ];
    },
    changeColor14(i, j) {
      console.log(i, j);
      this.fourteen[i - 1][j - 1] = this.colorlist[
        localStorage.getItem("color") - 1
      ];
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
      this.twenty[i - 1][j - 1] = this.colorlist[
        localStorage.getItem("color") - 1
      ];
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
      var Hw_size = localStorage.getItem("Hw_size");
      console.log(Hw_size, typeof Hw_size);
      for (i = 0; i < Hw_size; ++i) {
        for (j = 0; j < Hw_size; ++j) {
          txtid = "btn" + Hw_size + (i + 1) + "/" + (j + 1);
          console.log(txtid);
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

