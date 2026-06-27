from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

# 示例数据
SAMPLE_DATA = [
    {"date": "2024-01", "sales": 12000, "orders": 340, "category": "电子产品"},
    {"date": "2024-02", "sales": 9800, "orders": 280, "category": "电子产品"},
    {"date": "2024-03", "sales": 15000, "orders": 420, "category": "电子产品"},
    {"date": "2024-01", "sales": 8500, "orders": 210, "category": "服装"},
    {"date": "2024-02", "sales": 7200, "orders": 180, "category": "服装"},
    {"date": "2024-03", "sales": 11000, "orders": 290, "category": "服装"},
]

@app.route('/api/sales')
def get_sales():
    df = pd.DataFrame(SAMPLE_DATA)
    result = df.to_dict('records')
    return jsonify({"code": 200, "data": result})

@app.route('/api/sales/summary')
def get_summary():
    df = pd.DataFrame(SAMPLE_DATA)
    summary = {
        "total_sales": int(df["sales"].sum()),
        "total_orders": int(df["orders"].sum()),
        "avg_order_value": round(df["sales"].sum() / df["orders"].sum(), 2),
        "by_category": df.groupby("category").agg({"sales": "sum", "orders": "sum"}).reset_index().to_dict('records')
    }
    return jsonify({"code": 200, "data": summary})

@app.route('/api/upload', methods=['POST'])
def upload_data():
    # 简化：实际应接收 CSV 文件并用 pandas 分析
    return jsonify({"code": 200, "message": "数据上传成功（演示功能）"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
