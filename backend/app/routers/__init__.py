"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import project as router_project
from app.routers import drilling as router_drilling
from app.routers import core as router_core
from app.routers import geophysics as router_geophysics
from app.routers import geochem as router_geochem
from app.routers import surveying as router_surveying
from app.routers import trenching as router_trenching
from app.routers import sample as router_sample
from app.routers import labtest as router_labtest
from app.routers import report as router_report
from app.routers import safety_geo as router_safety_geo
from app.routers import permit_geo as router_permit_geo
from app.routers import camp as router_camp
from app.routers import transport_geo as router_transport_geo
from app.routers import equipment_geo as router_equipment_geo
from app.routers import personnel_geo as router_personnel_geo
from app.routers import budget_geo as router_budget_geo
from app.routers import review_geo as router_review_geo

ROUTERS = [router_project, router_drilling, router_core, router_geophysics, router_geochem, router_surveying, router_trenching, router_sample, router_labtest, router_report, router_safety_geo, router_permit_geo, router_camp, router_transport_geo, router_equipment_geo, router_personnel_geo, router_budget_geo, router_review_geo]
