# 电商数据分析系统

基于 Python Flask + Vue 3 + ECharts 的电商数据分析平台，支持销售数据可视化、品类分析、趋势分析等功能。

## 技术栈

### 后端
- Python 3.10+
- Flask 3.0
- pandas 2.1（数据分析）
- flask-cors（跨域支持）

### 前端
- Vue 3 + Vite
- ECharts 5.5（数据可视化）
- Axios
- Vue Router

## 功能模块

| 模块 | 功能 |
|------|------|
| 数据概览 | 总销售额、总订单数、客单价 |
| 趋势分析 | 销售额趋势折线图 |
| 品类分析 | 品类销售占比饼图 |
| 数据上传 | CSV 文件上传与解析（演示） |

## 快速启动

### 后端

```bash
cd backend
pip install -r requirements.txt
python app.py
# 后端运行在 http://localhost:5000
```

### 前端

```bash
cd frontend
npm install
npm run dev
# 前端运行在 http://localhost:5174
```

## 接口说明

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/sales` | GET | 获取销售数据 |
| `/api/sales/summary` | GET | 获取销售汇总 |
| `/api/upload` | POST | 上传数据文件 |

## 作者

曹成 - 2026 届本科应届生 - 湖南涉外经济学院 - 数据科学与大数据技术专业
