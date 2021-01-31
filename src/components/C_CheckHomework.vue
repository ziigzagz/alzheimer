<template>
  <div>
    <div class="container">
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
        <div class="col-6 text-center">
          <h3>ผลการตรวจ</h3>
          <h4>ความถูกต้องของช่อง : 100%</h4>
          <h4>ความถูกต้องของสี : 100%</h4>
          <h4>
            เวลาที่ใช้ : 5:12 นาที
          </h4>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  mounted() {
    // first view page set color
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
  methods: {},
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