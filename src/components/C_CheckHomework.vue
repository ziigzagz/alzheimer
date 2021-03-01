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