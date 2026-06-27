<template>
  <div class="dashboard">
    <!-- 顶部标题 -->
    <div class="header-bar">
      <h2>📊 电商数据分析看板</h2>
      <span class="update-time">数据更新：2024-06-27 16:30</span>
    </div>

    <!-- 核心指标卡片 -->
    <el-row :gutter="20" class="summary-cards">
      <el-col :xs="12" :sm="6" v-for="(card, idx) in summaryCards" :key="idx">
        <div class="stat-card" :style="{borderLeft: '4px solid ' + card.color}">
          <div class="stat-label">{{ card.label }}</div>
          <div class="stat-value" :style="{color: card.color}">{{ card.value }}</div>
          <div class="stat-trend" :class="card.trendUp ? 'trend-up' : 'trend-down'">
            {{ card.trendUp ? '↑' : '↓' }} {{ card.change }}
          </div>
        </div>
      </el-col>
    </el-row>

    <!-- 图表区域 -->
    <el-row :gutter="20">
      <el-col :span="16">
        <div class="chart-card">
          <div class="chart-title">📈 月度销售趋势</div>
          <div ref="chart1" style="width:100%;height:340px;"></div>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="chart-card">
          <div class="chart-title">🥧 品类销售占比</div>
          <div ref="chart2" style="width:100%;height:340px;"></div>
        </div>
      </el-col>
    </el-row>

    <el-row :gutter="20" style="margin-top:20px;">
      <el-col :span="14">
        <div class="chart-card">
          <div class="chart-title">🏆 热销商品 TOP10</div>
          <div ref="chart3" style="width:100%;height:320px;"></div>
        </div>
      </el-col>
      <el-col :span="10">
        <div class="chart-card">
          <div class="chart-title">👥 用户增长趋势</div>
          <div ref="chart4" style="width:100%;height:320px;"></div>
        </div>
      </el-col>
    </el-row>

    <!-- 数据表格 -->
    <div class="table-section">
      <h3>📋 近期订单明细</h3>
      <el-table :data="orderTable" stripe border style="width:100%;">
        <el-table-column prop="orderId" label="订单号" width="150"/>
        <el-table-column prop="product" label="商品名称"/>
        <el-table-column prop="category" label="品类" width="100"/>
        <el-table-column prop="amount" label="金额(元)" width="100" align="right">
          <template #default="{row}"><b style="color:#f56c6c;">{{ row.amount }}</b></template>
        </el-table-column>
        <el-table-column prop="status" label="状态" width="90">
          <template #default="{row}">
            <el-tag :type="row.statusType" size="small">{{ row.status }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="time" label="下单时间" width="160"/>
      </el-table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import * as echarts from 'echarts'

const chart1 = ref(null)
const chart2 = ref(null)
const chart3 = ref(null)
const chart4 = ref(null)
let instances = []

// 指标卡数据
const summaryCards = ref([
  { label: '总销售额', value: '¥1,285,600', change: '+12.5%', trendUp: true, color: '#f56c6c' },
  { label: '总订单数', value: '15,826', change: '+8.3%', trendUp: true, color: '#409eff' },
  { label: '客单价', value: '¥81.24', change: '-2.1%', trendUp: false, color: '#e6a23c' },
  { label: '活跃用户', value: '8,542', change: '+18.7%', trendUp: true, color: '#67c23a' }
])

// 订单表格数据
const orderTable = ref([
  { orderId: 'ORD240627001', product: 'Apple iPhone 15 Pro Max', category: '数码电子', amount: 9999, status: '已完成', statusType: 'success', time: '2024-06-27 14:32:18' },
  { orderId: 'ORD240627002', product: 'Nike Air Jordan 1 Retro High', category: '运动户外', amount: 1299, status: '配送中', statusType: 'warning', time: '2024-06-27 13:15:44' },
  { orderId: 'ORD240627003', product: 'SK-II 神仙水 230ml', category: '美妆护肤', amount: 1540, status: '待支付', statusType: 'danger', time: '2024-06-27 12:08:33' },
  { orderId: 'ORD240627004', product: '戴森 V15 吸尘器', category: '家用电器', amount: 4990, status: '已完成', statusType: 'success', time: '2024-06-27 11:45:21' },
  { orderId: 'ORD240627005', product: '《深入理解Java虚拟机》', category: '图书文具', amount: 89, status: '已完成', statusType: 'success', time: '2024-06-27 10:22:09' }
])

onMounted(() => {
  renderAllCharts()
})

function initChart(refEl) {
  if (refEl?.value) {
    const inst = echarts.init(refEl.value)
    instances.push(inst)
    return inst
  }
}

function renderAllCharts() {
  // 图表1：销售额趋势（折线图）
  const c1 = initChart(chart1)
  if (c1) c1.setOption({
    tooltip: { trigger: 'axis' },
    legend: { data: ['销售额', '订单量'], top: 0 },
    grid: { left: 60, right: 20, bottom: 40 },
    xAxis: {
      type: 'category',
      data: ['1月','2月','3月','4月','5月','6月'],
      axisLabel: { fontSize: 12 }
    },
    yAxis: [
      { type: 'value', name: '销售额(万)', axisLabel: { formatter: '{value}w' }, splitLine: { lineStyle: { color:'#f0f0f0'} } },
      { type: 'value', name: '订单量', axisLabel: { formatter: '{value}' } }
    ],
    series: [
      {
        name: '销售额', type: 'line', smooth: true,
        data: [156, 189, 178, 215, 245, 278],
        lineStyle: { width: 3, color: '#f56c6c' },
        areaStyle: { color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{ offset: 0, color: 'rgba(245,108,108,0.3)' }, { offset: 1, color: 'rgba(245,108,108,0)' }]) },
        itemStyle: { color: '#f56c6c' }
      },
      {
        name: '订单量', type: 'bar', yAxisIndex: 1,
        data: [1820, 2100, 1980, 2350, 2680, 2980],
        itemStyle: { color: '#409eff', borderRadius: [4,4,0,0] }
      }
    ]
  })

  // 图表2：品类占比（饼图）
  const c2 = initChart(chart2)
  if (c2) c2.setOption({
    tooltip: { trigger: 'item', formatter: '{b}: ¥{c} ({d}%)' },
    legend: { orient: 'vertical', right: 10, top: 'center', textStyle: { fontSize: 12 } },
    series: [{
      type: 'pie', radius: ['40%', '70%'],
      center: ['38%', '50%'],
      avoidLabelOverlap: false,
      itemStyle: { borderRadius: 8, borderColor: '#fff', borderWidth: 2 },
      label: { show: false },
      emphasis: { label: { show: true, fontSize: 14, fontWeight: 'bold' } },
      data: [
        { value: 385600, name: '数码电子', itemStyle: { color: '#5470c6' }},
        { value: 298400, name: '服装鞋帽', itemStyle: { color: '#91cc75' }},
        { value: 215800, name: '美妆护肤', itemStyle: { color: '#fac858' }},
        { value: 186200, name: '家用电器', itemStyle: { color: '#ee6666' }},
        { value: 128500, name: '食品饮料', itemStyle: { color: '#73c0de' }},
        { value: 71100,  name: '其他',     itemStyle: { color: '#ba55d3' }}
      ]
    }]
  })

  // 图表3：热销商品TOP10（横向柱状图）
  const c3 = initChart(chart3)
  if (c3) c3.setOption({
    grid: { left: 120, right: 30, top: 10, bottom: 20 },
    xAxis: { type: 'value', axisLabel: { fontSize: 11 }, splitLine: { lineStyle: { color:'#f5f5f5'}} },
    yAxis: {
      type: 'category',
      data: ['小米14 Ultra', 'AirPods Pro 2', '戴森吸尘器V12', 'SK-II神仙水', 'Nike Dunk Low', 'MacBook Air M3', 'iPad Pro 12.9"', '华为Mate60 Pro', '索尼WH-1000XM5', '任天堂Switch OLED'],
      inverse: true,
      axisLabel: { fontSize: 12 }
    },
    series: [{
      type: 'bar',
      data: [2856, 2341, 1987, 1756, 1634, 1523, 1412, 1328, 1198, 1056],
      barMaxWidth: 22,
      itemStyle: {
        borderRadius: [0, 6, 6, 0],
        color: function(params) {
          const colors = ['#f56c6c','#e6a23c','#f39c12','#67c23a','#409eff','#5470c6','#91cc75','#ee6666','#73c0de','#ba55d3']
          return colors[params.dataIndex % colors.length]
        }
      },
      label: { show: true, position: 'right', fontSize: 11, color: '#666' }
    }]
  })

  // 图表4：用户增长趋势
  const c4 = initChart(chart4)
  if (c4) c4.setOption({
    tooltip: { trigger: 'axis' },
    grid: { left: 50, right: 15, bottom: 35, top: 20 },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: ['周一','周二','周三','周四','周五','周六','周日'],
      axisLabel: { fontSize: 11 }
    },
    yAxis: { type: 'value', splitLine: { lineStyle: {color:'#f0f0f0'}}, axisLabel: { fontSize: 11 }},
    series: [
      {
        type: 'line',
        smooth: true,
        symbolSize: 8,
        data: [1200, 1350, 1180, 1420, 1680, 2100, 1950],
        areaStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: 'rgba(102,126,234,0.4)' },
            { offset: 1, color: 'rgba(102,126,234,0)' }
          ])
        },
        lineStyle: { width: 3, color: '#667eea' },
        itemStyle: { color: '#667eea' }
      }
    ]
  })
}

onUnmounted(() => {
  instances.forEach(i => i.dispose())
  instances = []
})
</script>

<style scoped>
.dashboard { padding: 20px; max-width: 1300px; margin: 0 auto; background: #f5f7fa; min-height: 100vh; }

.header-bar {
  display:flex; justify-content:space-between; align-items:center;
  padding-bottom:16px; margin-bottom:4px;
}
.header-bar h2 { margin:0; font-size:24px; color:#303133; }
.update-time { font-size:13px; color:#909399; }

.summary-cards { margin-bottom: 20px; }
.stat-card {
  background:white; border-radius:10px;
  padding:20px; text-align:center;
  box-shadow:0 2px 8px rgba(0,0,0,0.04);
}
.stat-label { font-size:13px; color:#909399; margin-bottom:8px; }
.stat-value { font-size:26px; font-weight:bold; margin-bottom:4px; }
.stat-trend { font-size:12px; }
.trend-up { color:#67c23a; }
.trend-down { color:#f56c6c; }

.chart-card {
  background:white; border-radius:10px;
  padding:20px; box-shadow:0 2px 8px rgba(0,0,0,0.04);
}
.chart-title { font-size:16px; font-weight:bold; margin-bottom:12px; color:#303133; }

.table-section {
  background:white; border-radius:10px;
  padding:20px; margin-top:20px;
  box-shadow:0 2px 8px rgba(0,0,0,0.04);
}
.table-section h3 { margin:0 0 16px; font-size:16px; color:#303133; }
</style>
