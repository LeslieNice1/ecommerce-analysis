# 📊 电商数据分析系统

> 一个基于 Python Flask + Vue 3 + ECharts 的电商数据分析平台，提供丰富的可视化图表和实时数据监控。

## ✨ 功能特性

- 📈 **销售趋势分析**：多维度展示销售额、订单量趋势
- 🥧 **品类占比分析**：饼图展示各品类销售占比
- 🏆 **热销商品排行**：TOP10 商品销量排行（横向柱状图）
- 👥 **用户增长趋势**：用户注册/活跃趋势分析
- 📋 **订单明细查询**：支持按状态、时间筛选
- 📊 **核心指标卡片**：总销售额、总订单、客单价、活跃用户

## 🛠 技术栈

### 后端
- Python 3.8+
- Flask
- Flask-CORS
- Pandas（数据处理）
- SQLAlchemy（ORM）

### 前端
- Vue 3 (Composition API)
- Vite
- Element Plus
- ECharts 5.x
- Axios
- Vue Router

## 🚀 快速启动

### 前端（无需后端即可预览！）

本项目已内置**演示数据**，无需配置后端和数据库即可查看完整界面效果！

```bash
# 1. 克隆项目
git clone https://github.com/LeslieNice1/ecommerce-analysis.git
cd ecommerce-analysis/frontend

# 2. 安装依赖
npm install

# 3. 启动开发服务器
npm run dev
```

访问：http://localhost:5175/ 即可查看完整数据看板！

### 后端（可选，实时数据需要）

```bash
# 1. 安装 Python 依赖
cd backend
pip install -r requirements.txt

# 2. 启动后端服务
python app.py
```

后端运行在：http://localhost:5000/

## 📸 界面预览

### 数据看板首页
![数据看板](./screenshots/dashboard.png)

### 销售额趋势图
![趋势图](./screenshots/sales-trend.png)

### 品类占比饼图
![饼图](./screenshots/category-pie.png)

## 📂 项目结构

```
ecommerce-analysis/
├── backend/                # Flask 后端
│   ├── app.py            # 主应用入口
│   ├── models/          # 数据模型
│   ├── routes/          # API 路由
│   └── requirements.txt # Python 依赖
└── frontend/              # Vue 3 前端
    ├── src/views/        # 页面组件
    ├── src/components/   # 子组件
    ├── src/utils/        # 工具函数
    └── package.json      # npm 配置
```

## 🎯 核心功能讲解（面试必备）

### 1. ECharts 图表渲染

使用 `echarts-for-react` 或原生 ECharts 渲染图表：

```javascript
import * as echarts from 'echarts'

const chartRef = ref(null)

onMounted(() => {
  const chart = echarts.init(chartRef.value)
  chart.setOption({
    // ECharts 配置项
  })
})
```

### 2. RESTful API 设计

```
GET    /api/sales/summary       获取销售汇总
GET    /api/sales/trend         获取销售趋势
GET    /api/category/distribution获取品类分布
GET    /api/products/top10      获取热销商品TOP10
```

### 3. 数据聚合与处理

使用 Pandas 进行数据聚合：

```python
import pandas as pd

# 按日期聚合销售额
sales_by_date = df.groupby('date')['amount'].sum().reset_index()

# 按品类聚合订单量
orders_by_category = df.groupby('category')['order_id'].count().reset_index()
```

## 📧 联系我

- GitHub：[@LeslieNice1](https://github.com/LeslieNice1)
