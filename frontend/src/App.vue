<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">地质勘探项目管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向矿产勘探项目、钻探工程、岩芯编录、物探化探采集、样品检测与成果报告编制的一体化地质勘探项目管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "勘探项目", path: "/project" }, { label: "钻探工程", path: "/drilling" }, { label: "岩芯编录", path: "/core" }, { label: "物探作业", path: "/geophysics" }, { label: "化探采样", path: "/geochem" }, { label: "测绘控制", path: "/surveying" }, { label: "槽探工程", path: "/trenching" }, { label: "样品管理", path: "/sample" }, { label: "试验检测", path: "/labtest" }, { label: "成果报告", path: "/report" }, { label: "安全管理", path: "/safety_geo" }, { label: "勘探许可", path: "/permit_geo" }, { label: "野外营地", path: "/camp" }, { label: "物资运输", path: "/transport_geo" }, { label: "勘探设备", path: "/equipment_geo" }, { label: "人员管理", path: "/personnel_geo" }, { label: "经费预算", path: "/budget_geo" }, { label: "报告评审", path: "/review_geo" }]
</script>
