<template>
  <div>
    <div class="container-fluid">
      <div class="row">
        <!-- โจทย์ -->
        <div class="col-6 offset-2 mt-5">
          <div v-for="i in 18" v-bind:key="i">
            <button
              type="button"
              :id="'btnprop' + i + '/' + j"
              class="btn btn-default mx-auto"
              v-for="j in 18"
              v-bind:key="j"
            ></button>
          </div>
        </div>
        <!-- คำตอบ -->
        <div class="col-3 text-center">
          <h3>ผลการตรวจ</h3>
          <!-- <h4>ความถูกต้องของช่อง : 100%</h4> -->
          <h4>
            ความถูกต้อง : {{ Math.floor(100 - (count_error / 324) * 100) }}%
          </h4>
          <h4>เวลาที่ใช้ : {{ timer_m }}:{{ timer_s }} {{ unit }}</h4>
          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count_error:localStorage.getItem("count_error"),
      timer_m:0,
      timer_s:0,
      unit:"นาที",
      eightteen_ans: [
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
        [
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
          "#FFFFFF",
        ],
      ],
    };
  },
  mounted() {
    // first view page set color
  document.getElementById("btnprop1/2").innerHTML =  'X<img src="@/assets/icon/check.png" height="15px" alt="" srcset="" />';
    var tmp = localStorage.getItem("timer").split(":");
    var h,m,s;
    this.timer_h = parseInt(tmp[0])
    this.timer_m = parseInt(tmp[1])
    this.timer_s = parseInt(tmp[2])
    if(this.timer_s < 10){
      this.timer_s = "0" + this.timer_s
    }
    if(this.timer_m < 10){
      this.timer_m = "0" + this.timer_m
    }

    // console.log(h,m,s)
    // console.log(tmp)
    var ans = localStorage.getItem("ans").split("*");
    var i = 0;
    var j = 0;
    var txtid;
    for (i = 0; i < 18; i++) {
      // console.log(tmp[i].split("/"))
      for (j = 0; j < 18; j++) {
        // console.log(ans[i].split("/")[j]);
        this.eightteen_ans[i][j] = ans[i].split("/")[j];
        txtid = "btnprop" + (i + 1) + "/" + (j + 1);
        document.getElementById(txtid).style.backgroundColor = ans[i].split(
          "/"
        )[j];
      }
      // console.log("---");
    }
  },
  methods: {},
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