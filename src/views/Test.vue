<template>
  <div>
    <label for="favcolor">Select your favorite color:11</label>
    <br />
    <br /><br />
    <div class="container">
      <div class="row">
        <input
      type="color"
      id="favcolor"
      name="favcolor"
      value="#ff0000"
    />
        <div class="col" id="testcolor">
          color
        </div>
      </div>
    </div>
    <button class="btn btn-info" @click="send">เลือก</button>
    <div class="container">
      <div class="row">
        <div class="col">
          <button
            type="button"
            :id="'btncolorplt' + j"
            class="btn btn-default mx-auto"
            @click="setStateColor(j)"
            v-for="j in 16"
            v-bind:key="j"
          ></button>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
const axios = require("axios");
export default {
  data: () => ({
    swatches: [
      ["#FF0000", "#AA0000", "#550000"],
      ["#FFFF00", "#AAAA00", "#555500"],
      ["#00FF00", "#00AA00", "#005500"],
      ["#00FFFF", "#00AAAA", "#005555"],
      ["#0000FF", "#0000AA", "#000055"],
    ],
    colorlist: [
      "#FFEC1F", //เหลืองเข้ม
      "#F6FF78", //เหลืองอ่อน
      "#21E83F", //เขียวเข้ม
      "#148F27", //เขียวอ่อน
      "#1F26FF", //น้ำเงิน
      "#A12DCF", //ม่วง
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
  }),
  mounted() {
    var t = [1,2,3]
    
    var i, j, txtid;
    for (i = 0; i < 16; ++i) {
      txtid = "btncolorplt" + (i + 1);
      document.getElementById(txtid).style.backgroundColor = this.colorlist[i];
      // console.log(this.colorlist[i], txtid);
    }
  },
  methods: {
    send() {
      const path = "http://127.0.0.1:5000/save";
      var x = document.getElementById("favcolor").value;
      console.log(x);
      axios.post(path, [x, localStorage.getItem("color")]).then((res) => {
        console.log(res);
      });
    },
    setStateColor(i) {
      document.getElementById("testcolor").style.backgroundColor = this.colorlist[i-1];
      // document.body.style.backgroundColor = "red";
      localStorage.setItem("color", this.colorlist[i-1]);
    },
  },
};
</script>

<style>
</style>