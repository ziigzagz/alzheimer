<template>
  <div>
    <div class="container">
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
            v-for="j in 16"
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
        <div class="col-6">
          <div v-for="i in 10" v-bind:key="i">
            <button
              type="button"
              :id="'btnprop' + i + j"
              class="btn btn-default"
              v-for="j in 10"
              v-bind:key="j"
            ></button>
          </div>
        </div>
        <!-- คำตอบ -->
        <div class="col-6">
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
      console.log(this.colorlist[i], txtid);
    }
    document.getElementById("btnprop13").style.backgroundColor = "#F00800";
    document.getElementById("btnprop24").style.backgroundColor = "#F00800";
    document.getElementById("btnprop35").style.backgroundColor = "#F00800";
    document.getElementById("btnprop26").style.backgroundColor = "#F00800";
    document.getElementById("btnprop17").style.backgroundColor = "#F00800";
    document.getElementById("btnprop28").style.backgroundColor = "#F00800";
    document.getElementById("btnprop39").style.backgroundColor = "#F00800";
    document.getElementById("btnprop48").style.backgroundColor = "#F00800";
    document.getElementById("btnprop57").style.backgroundColor = "#F00800";
    document.getElementById("btnprop66").style.backgroundColor = "#F00800";
    document.getElementById("btnprop75").style.backgroundColor = "#F00800";
    document.getElementById("btnprop22").style.backgroundColor = "#F00800";
    document.getElementById("btnprop13").style.backgroundColor = "#F00800";
    document.getElementById("btnprop31").style.backgroundColor = "#F00800";
    document.getElementById("btnprop42").style.backgroundColor = "#F00800";
    document.getElementById("btnprop53").style.backgroundColor = "#F00800";
    document.getElementById("btnprop64").style.backgroundColor = "#F00800";
    document.getElementById("btnprop23").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop27").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop32").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop33").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop34").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop36").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop37").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop38").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop43").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop44").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop45").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop46").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop47").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop54").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop55").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop56").style.backgroundColor = "#F266DD";
    document.getElementById("btnprop65").style.backgroundColor = "#F266DD";
  },
  methods: {
    check() {
      window.location.href = "/CheckHomework";
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

.btn {
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