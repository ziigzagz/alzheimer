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
          data: [1, 1, 2],
        },
      ],
    };
  },
  mounted() {
    this.chartOptions = {
      colors: ["#F44336", "#E91E63", "#9C27B0"],
    };
    var chart = new ApexCharts();
    chart.updateSeries([
      {
        data: [32, 44, 31],
      },
    ]);
    var db = firebase.firestore();
    var docRef = db.collection("Homework");
    var tmp = 0;
    docRef
      .get()
      .then((doc) => {
        doc.forEach((element) => {
          // console.log(element.data());
          this.userlist_dohomework.forEach((element_tmp) => {
            // var tmp = 0;
            if (element_tmp == element.data().user) {
              tmp = 1;
            }
          });
          if (tmp == 1) {
            // console.log(555);
          } else {
            this.userlist_dohomework.push(element.data().user);
            // console.log(999);
          }
        });
      })
      .then(() => {
        console.log(this.userlist_dohomework);
        this.userlist_dohomework.forEach((element, i) => {
          var docRef = db.collection("Homework").where("user", "==", element);
          docRef.get().then((doc) => {
            doc.forEach((element) => {
              console.log(element.data(), i);
              if (
                element.data().timer_first != "0" &&
                element.data().timer_release != "0"
              ) {
                var t =
                  element.data().timer_first - element.data().timer_release;
                console.log(t);
                // this.series.forEach(tmp => {
                //   console.log(tmp.data)
                // });
                // this.series[0].data[0] += 1;
                // console.log(this.series[0].data[0]);
                if (t > 0) {
                  this.series[0].data[0] += 1;
                } else {
                  if (t == 0) {
                    this.series.data[1] += 1;
                  } else {
                    this.series.data[2] += 1;
                  }
                }
                console.log(this.series[0].data);
                // this.userlist_dohomework.forEach((data, i) => {
                //   console.log(data)
                // });
              }
              // console.log(element.data(), i);
            });
          });
        });
      });
  },
  methods: {
    updateTheme(e) {},
  },
};
</script>
