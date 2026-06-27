<template>
  <div id="app">
    <el-container>
      <el-header class="header">
        <h2>📊 电商数据分析系统</h2>
        <span class="header-sub">实时监控 · 智能分析 · 数据驱动决策</span>
      </el-header>
      <el-main style="padding:0; background:#f5f7fa;">
        <router-view/>
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
</script>

<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
.header {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 16px 30px !important;
}
.header h2 { margin: 0; font-size: 22px; }
.header-sub { font-size: 13px; opacity: 0.8; margin-top: 4px; }
</style>
