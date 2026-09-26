"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class ProjectEntry(BaseModel):
    """勘探项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 项目名称
    field_2: str | None = None  # 矿种类型
    field_3: str | None = None  # 勘查阶段
    field_4: str | None = None  # 探矿权证号
    field_5: str | None = None  # 勘查面积
    field_6: str | None = None  # 项目周期
    field_7: str | None = None  # 项目状态

class DrillingEntry(BaseModel):
    """钻孔明细结构。"""

    field_0: str | None = None  # 钻孔编号
    field_1: str | None = None  # 所属项目
    field_2: str | None = None  # 设计孔深
    field_3: str | None = None  # 实际孔深
    field_4: str | None = None  # 开孔日期
    field_5: str | None = None  # 终孔日期
    field_6: str | None = None  # 施工机组
    field_7: str | None = None  # 钻孔状态

class CoreEntry(BaseModel):
    """岩芯明细结构。"""

    field_0: str | None = None  # 岩芯编号
    field_1: str | None = None  # 所属钻孔
    field_2: str | None = None  # 回次编号
    field_3: str | None = None  # 进尺段
    field_4: str | None = None  # 岩性描述
    field_5: str | None = None  # 矿化特征
    field_6: str | None = None  # 编录人
    field_7: str | None = None  # 编录日期

class GeophysicsEntry(BaseModel):
    """物探测线明细结构。"""

    field_0: str | None = None  # 测线编号
    field_1: str | None = None  # 所属项目
    field_2: str | None = None  # 物探方法
    field_3: str | None = None  # 测线长度
    field_4: str | None = None  # 点距
    field_5: str | None = None  # 仪器型号
    field_6: str | None = None  # 施工日期
    field_7: str | None = None  # 测线状态

class GeochemEntry(BaseModel):
    """化探样品明细结构。"""

    field_0: str | None = None  # 样品编号
    field_1: str | None = None  # 所属测区
    field_2: str | None = None  # 采样介质
    field_3: str | None = None  # 采样深度
    field_4: str | None = None  # 采集日期
    field_5: str | None = None  # 采样人员
    field_6: str | None = None  # 分析方法
    field_7: str | None = None  # 样品状态

class SurveyingEntry(BaseModel):
    """控制点明细结构。"""

    field_0: str | None = None  # 控制点编号
    field_1: str | None = None  # 控制点类型
    field_2: str | None = None  # 所属测区
    field_3: str | None = None  # 经度坐标
    field_4: str | None = None  # 纬度坐标
    field_5: str | None = None  # 高程值
    field_6: str | None = None  # 建点日期
    field_7: str | None = None  # 点位状态

class TrenchingEntry(BaseModel):
    """探槽明细结构。"""

    field_0: str | None = None  # 探槽编号
    field_1: str | None = None  # 所属项目
    field_2: str | None = None  # 设计长度
    field_3: str | None = None  # 实际长度
    field_4: str | None = None  # 开挖深度
    field_5: str | None = None  # 开工日期
    field_6: str | None = None  # 完工日期
    field_7: str | None = None  # 探槽状态

class SampleEntry(BaseModel):
    """检测样品明细结构。"""

    field_0: str | None = None  # 样品编号
    field_1: str | None = None  # 样品类型
    field_2: str | None = None  # 所属钻孔
    field_3: str | None = None  # 采样位置
    field_4: str | None = None  # 送检日期
    field_5: str | None = None  # 检测项目
    field_6: str | None = None  # 留存份数
    field_7: str | None = None  # 样品状态

class LabtestEntry(BaseModel):
    """检测任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 委托单位
    field_2: str | None = None  # 样品编号
    field_3: str | None = None  # 检测项目
    field_4: str | None = None  # 检测标准
    field_5: str | None = None  # 接收日期
    field_6: str | None = None  # 报告日期
    field_7: str | None = None  # 任务状态

class ReportEntry(BaseModel):
    """勘查报告明细结构。"""

    field_0: str | None = None  # 报告编号
    field_1: str | None = None  # 所属项目
    field_2: str | None = None  # 报告类型
    field_3: str | None = None  # 编写人
    field_4: str | None = None  # 编写日期
    field_5: str | None = None  # 报告摘要
    field_6: str | None = None  # 附图数量
    field_7: str | None = None  # 报告状态

class SafetyGeoEntry(BaseModel):
    """安全检查记录明细结构。"""

    field_0: str | None = None  # 检查编号
    field_1: str | None = None  # 检查日期
    field_2: str | None = None  # 检查地点
    field_3: str | None = None  # 检查人员
    field_4: str | None = None  # 隐患类别
    field_5: str | None = None  # 整改要求
    field_6: str | None = None  # 复查日期
    field_7: str | None = None  # 检查状态

class PermitGeoEntry(BaseModel):
    """勘探许可证明细结构。"""

    field_0: str | None = None  # 许可证编号
    field_1: str | None = None  # 许可类型
    field_2: str | None = None  # 申请人
    field_3: str | None = None  # 申请日期
    field_4: str | None = None  # 批准日期
    field_5: str | None = None  # 有效期限
    field_6: str | None = None  # 审批机关
    field_7: str | None = None  # 许可状态

class CampEntry(BaseModel):
    """野外营地明细结构。"""

    field_0: str | None = None  # 营地编号
    field_1: str | None = None  # 营地名称
    field_2: str | None = None  # 所属项目
    field_3: str | None = None  # 驻扎人员
    field_4: str | None = None  # 建营日期
    field_5: str | None = None  # 撤营日期
    field_6: str | None = None  # 补给周期
    field_7: str | None = None  # 营地状态

class TransportGeoEntry(BaseModel):
    """运输任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 运输物资
    field_2: str | None = None  # 出发地
    field_3: str | None = None  # 目的地
    field_4: str | None = None  # 承运车辆
    field_5: str | None = None  # 驾驶员
    field_6: str | None = None  # 预计到达
    field_7: str | None = None  # 任务状态

class EquipmentGeoEntry(BaseModel):
    """勘探设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备名称
    field_2: str | None = None  # 设备类型
    field_3: str | None = None  # 规格型号
    field_4: str | None = None  # 所属机组
    field_5: str | None = None  # 校准日期
    field_6: str | None = None  # 下次校准
    field_7: str | None = None  # 设备状态

class PersonnelGeoEntry(BaseModel):
    """勘探人员明细结构。"""

    field_0: str | None = None  # 员工编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 岗位职务
    field_3: str | None = None  # 所属项目
    field_4: str | None = None  # 进队日期
    field_5: str | None = None  # 出队日期
    field_6: str | None = None  # 执业资格
    field_7: str | None = None  # 在队状态

class BudgetGeoEntry(BaseModel):
    """预算科目明细结构。"""

    field_0: str | None = None  # 科目编号
    field_1: str | None = None  # 科目名称
    field_2: str | None = None  # 费用类别
    field_3: str | None = None  # 预算金额
    field_4: str | None = None  # 已用金额
    field_5: str | None = None  # 剩余余额
    field_6: str | None = None  # 预算周期
    field_7: str | None = None  # 科目状态

class ReviewGeoEntry(BaseModel):
    """评审记录明细结构。"""

    field_0: str | None = None  # 评审编号
    field_1: str | None = None  # 评审对象
    field_2: str | None = None  # 评审类型
    field_3: str | None = None  # 评审专家
    field_4: str | None = None  # 评审日期
    field_5: str | None = None  # 评审结论
    field_6: str | None = None  # 修改意见
    field_7: str | None = None  # 评审状态
