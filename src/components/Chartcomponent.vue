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
import VueApexCharts from "vue-apexcharts";

export default {
  name: "Chart",
  components: {
    apexcharts: VueApexCharts,
  },
  data() {
    return {
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
          name: "คนไข้ (คน)",
          data: [30, 40, 45],
        },
      ],
    };
  },
  mounted() {
    this.chartOptions = {
      colors:['#F44336', '#E91E63', '#9C27B0']
    };
  },
  methods: {
    updateTheme(e) {},
  },
};
</script>
