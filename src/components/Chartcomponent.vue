<template>
  <div class="example mx-auto">
    <apexcharts
      width="100%"
      height="350"
      type="bar"
      :options="chartOptions"
      :series="series"
    ></apexcharts>
  </div>
</template>

<script>
import firebase from "firebase";
import VueApexCharts from "vue-apexcharts";

export default {
  name: "Chart",
  components: {
    apexcharts: VueApexCharts,
  },
  data() {
    return {
      userlist_dohomework: [],
      datas: {},
      chartOptions: {
        chart: {
          id: "basic-bar",
          animations: {
            speed: 200,
          },
        },
        dataLabels: {
          enabled: false,
        },
        plotOptions: {
          bar: {
            distributed: true,
          },
        },
        xaxis: {
          categories: ["แย่ลง", "เท่าเดิม", "ดีขึ้น"],
        },
      },
      series: [
        {
          name: "ผลการทำการบ้าน",
          data: [0, 0, 0],
        },
      ],
    };
  },
  mounted() {
    this.chartOptions = {
      colors: ["#F44336", "#E91E63", "#9C27B0"],
    };

    var db = firebase.firestore();
    var docRef = db
      .collection("Homework")
      .where("status", "==", 1)
      .where("timer_release", "!=", "0");
    var tmp = 0;
    var num1 = 0; //แย่ลง
    var num2 = 0; // เท่าเดิม
    var num3 = 0; // ดีขึ้น
    docRef.get().then((doc) => {
      doc.forEach((element) => {
        var release = parseInt(element.data().timer_release)
        var first = parseInt(element.data().timer_first)
        console.log(release < first);
        if (release > first) {
          num1++;
        }
        if (release == first) {
          num2++;
        }
        if (release < first) {
          num3++;
        }
        this.series = [{ data: [num1, num2, num3]}]
        console.log(this.series[0]["data"]);
      });
    });
  },
  methods: {
    updateTheme(e) {},
  },
};
</script>
