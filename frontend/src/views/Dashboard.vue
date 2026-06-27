<template>
  <div class="dashboard">
    <h2>电商数据分析看板</h2>

    <div class="summary-cards">
      <div class="card">总销售额：¥{{ summary.total_sales }}</div>
      <div class="card">总订单数：{{ summary.total_orders }}</div>
      <div class="card">客单价：¥{{ summary.avg_order_value }}</div>
    </div>

    <div ref="chart1" style="width:100%;height:400px;"></div>
    <div ref="chart2" style="width:100%;height:400px;margin-top:40px;"></div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import axios from 'axios'
import * as echarts from 'echarts'

const summary = ref({ total_sales: 0, total_orders: 0, avg_order_value: 0, by_category: [] })
const salesData = ref([])
const chart1 = ref(null)
const chart2 = ref(null)
let chart1Instance = null
let chart2Instance = null

onMounted(() => {
  axios.get('http://localhost:5000/api/sales/summary').then(res => {
    summary.value = res.data.data
  })
  axios.get('http://localhost:5000/api/sales').then(res => {
    salesData.value = res.data.data
    renderCharts()
  })
})

function renderCharts() {
  // 图表1：销售额趋势
  chart1Instance = echarts.init(chart1.value)
  const dates = [...new Set(salesData.value.map(d => d.date))]
  const categories = [...new Set(salesData.value.map(d => d.category))]
  const series = categories.map(cat => ({
    name: cat,
    type: 'line',
    data: dates.map(date => {
      const item = salesData.value.find(d => d.date === date && d.category === cat)
      return item ? item.sales : 0
    })
  }))
  chart1Instance.setOption({
    title: { text: '销售额趋势' },
    tooltip: { trigger: 'axis' },
    legend: { data: categories },
    xAxis: { type: 'category', data: dates },
    yAxis: { type: 'value' },
    series
  })

  // 图表2：品类销售占比
  chart2Instance = echarts.init(chart2.value)
  chart2Instance.setOption({
    title: { text: '品类销售占比', left: 'center' },
    tooltip: { trigger: 'item' },
    series: [{
      type: 'pie',
      radius: '60%',
      data: summary.value.by_category.map(c => ({ name: c.category, value: c.sales }))
    }]
  })
}

onUnmounted(() => {
  chart1Instance?.dispose()
  chart2Instance?.dispose()
})
</script>

<style scoped>
.dashboard { padding:20px; max-width:1200px; margin:0 auto; }
.summary-cards { display:flex; gap:20px; margin:20px 0; }
.card { flex:1; padding:20px; background:#f5f7fa; border-radius:8px; text-align:center; font-size:18px; font-weight:bold; }
</style>
