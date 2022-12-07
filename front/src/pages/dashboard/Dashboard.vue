<template>
  <div class="charts">
    <!-- 为 ECharts 准备一个定义了宽高的 DOM -->
    <!--  -->
    <div
      id="menus"
      style="width: 400px; height: 400px; border: 1px solid green"
    ></div>
    <div
      id="menus"
      style="width: 400px; height: 400px; border: 1px solid green"
    ></div>
    <div
      id="menus"
      style="width: 400px; height: 400px; border: 1px solid green"
    ></div>
    <div
      id="menus"
      style="width: 400px; height: 400px; border: 1px solid green"
    ></div>
  </div>
</template>

<script>
export default {
  name: "Dashboard",

  components: {},

  mounted() {
    this.menusCharts();
  },
  methods: {
    menusCharts() {
      // 基于准备好的dom，初始化echarts实例
      var elm = document.querySelectorAll("#menus");
      console.log(elm);
      elm.forEach(e => {
        console.log(e);
        var myChart = this.$echarts.init(e);
        // 指定图表的配置项和数据

        const option = {
          title: {
            text: "分类菜单分布",
            left: "10px",
            top: "5px",
          },
          tooltip: {
            trigger: "item",
          },
          legend: {
            left: "center",
            top: "bottom",
          },
          series: [
            {
              type: "pie",
              radius: ["40%", "70%"],
              avoidLabelOverlap: false,
              itemStyle: {
                borderRadius: 10,
                borderColor: "#fff",
                borderWidth: 1,
              },
              label: {
                show: false,
                position: "center",
              },
              emphasis: {
                label: {
                  show: false,
                  fontSize: "20",
                  fontWeight: "normal",
                },
              },
              labelLine: {
                show: false,
              },
              data: [
                { value: 1048, name: "服务器" },
                { value: 735, name: "宝塔" },
                { value: 580, name: "日常" },
                { value: 484, name: "工作" },
                { value: 300, name: "其他" },
              ],
            },
          ],
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
      })
    },
  },
};
</script>

<style>
.charts {
  margin-top: 30px;
  border: 1px solid red;
}
.charts > * {
  display: inline-block;
  margin: 5px;
}
</style>