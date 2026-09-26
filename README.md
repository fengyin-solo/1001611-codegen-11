# 地质勘探项目管理平台

面向矿产勘探项目、钻探工程、岩芯编录、物探化探采集、样品检测与成果报告编制的一体化地质勘探项目管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 勘探项目 | `project` | 勘探项目 | 项目编号、项目名称、矿种类型 |
| 钻探工程 | `drilling` | 钻孔 | 钻孔编号、所属项目、设计孔深 |
| 岩芯编录 | `core` | 岩芯 | 岩芯编号、所属钻孔、回次编号 |
| 物探作业 | `geophysics` | 物探测线 | 测线编号、所属项目、物探方法 |
| 化探采样 | `geochem` | 化探样品 | 样品编号、所属测区、采样介质 |
| 测绘控制 | `surveying` | 控制点 | 控制点编号、控制点类型、所属测区 |
| 槽探工程 | `trenching` | 探槽 | 探槽编号、所属项目、设计长度 |
| 样品管理 | `sample` | 检测样品 | 样品编号、样品类型、所属钻孔 |
| 试验检测 | `labtest` | 检测任务 | 任务编号、委托单位、样品编号 |
| 成果报告 | `report` | 勘查报告 | 报告编号、所属项目、报告类型 |
| 安全管理 | `safety_geo` | 安全检查记录 | 检查编号、检查日期、检查地点 |
| 勘探许可 | `permit_geo` | 勘探许可证 | 许可证编号、许可类型、申请人 |
| 野外营地 | `camp` | 野外营地 | 营地编号、营地名称、所属项目 |
| 物资运输 | `transport_geo` | 运输任务 | 任务编号、运输物资、出发地 |
| 勘探设备 | `equipment_geo` | 勘探设备 | 设备编号、设备名称、设备类型 |
| 人员管理 | `personnel_geo` | 勘探人员 | 员工编号、姓名、岗位职务 |
| 经费预算 | `budget_geo` | 预算科目 | 科目编号、科目名称、费用类别 |
| 报告评审 | `review_geo` | 评审记录 | 评审编号、评审对象、评审类型 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
