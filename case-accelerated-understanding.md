# 案例补充：Accelerated Understanding（物理AI · Neural Operator）

> 整理日期：2026-08-25
> 来源：**路透社（Reuters）2026-08-25 独家报道**（作者 Jeffrey Dastin）+ CNA、CNBC、The Independent、凤凰网、虎嗅等多家转载。技术细节部分来自公司官网 acceleratedunderstanding.com，属公司自述，未经独立验证。

---

## 公司概况

| 项 | 内容 |
|---|---|
| 公司 | **Accelerated Understanding Inc.**（Pasadena, California） |
| 创始人 | **Anima Anandkumar**（加州理工教授、前英伟达 AI 研究总监 5 年、前亚马逊科学家）+ **Benedikt Jenik**（AI 基础设施工程师，Anandkumar 丈夫）|
| 公开亮相 | 2026-08-25 |
| 技术 | **神经算子（Neural Operator）**，**不用 Transformer**；一次推理处理 **5 万亿数据点**；4D（3D空间+时间）物理场演化 |
| 应用 | 芯片设计、机器人、极端天气、地质分析（能源）—— 企业优先，非消费级 |
| 官网自述 | 已训练超一年、数百次预训练（最大 1 万亿参数）、scaling 至 35T；分辨率不变 |

---

## ① 谁投资了 —— ❗无可确认的外部机构投资人

- Anandkumar **拒绝讨论融资**（Reuters: "declined to discuss funding"）
- **没有任何轮次、估值、投资方被公开**（"No round size, valuation or investor has been named"）
- 仅有**计算提供商合作伙伴**提供硬件集群（训练/推理），**拒绝透露名字**
- 结论：公司当前为**创始团队自筹 + compute partner** 状态，尚未披露机构投资者

---

## ② 谁想投、没投上 —— Jeff Bezos / Project Prometheus（被拒）

2024 年底，投资人兼生物科技企业家 **Vik Bajaj**（后与 Bezos 共同创办 Prometheus）在洛杉矶晚餐会撮合，随后递出 **「Project Prometheus」offer letter**（Reuters 见到的文件副本）：

- **35% 股权**（Anandkumar 任公众代表/董事/科学愿景归其所有；Jenik 任董事会观察员）
- 合计 **$1M 年薪**，3 个月后涨至 **$2M**
- 承诺 **$2B+**（"committed rounds"）至 **B 轮**，**含 Bezos 本人**出资

➡️ **Anima/Jenik 拒绝**，选择独立创业。

**Bezos/Bajaj 后续（与 AU 无关，仅供参考）**：Prometheus 于 2026-06 完成 **$12B B 轮**、估值 **$410B**，投资方含 **Bezos、摩根大通、高盛、贝莱德、DST Global、ARCH Venture Partners**。

> ⚠️ 上列大机构是 **Prometheus** 的投资人，**不是** Accelerated Understanding 的投资人。勿混淆。

---

## ③ 英伟达 —— 未投资（澄清 ✓）

- Reuters 询问英伟达是否支持该公司，**英伟达未回复**。
- **黄仁勋（Jensen Huang）**仅于 2021 GTC 展示 Anandkumar 的神经算子研究、**鼓励其继续研究**，**未投资**。
- 媒体"背后站着黄仁勋"系夸张演绎。

---

## 对 AwareLiquid 的参考价值

1. **视角差异**：AU 走"拒绝大资本、硬核物理 AI"的技术信仰路线；AwareLiquid 走"O(1) 内存 + 端侧 + 已落地"的工程+商业路线。两者都押「非 Transformer 架构」——**架构创新是被顶级投资人（Bezos）看重的方向**。
2. **贝索斯/大资本对物理AI的胃口**：Bezos 愿为物理 AI 付 $12B+、$410B 估值——**物理/具身/端侧 AI 是 2026 资本热浪的中心**，AwareLiquid 的电池 BMS/端侧正卡在这个风口。
3. **诚实案例**：连 Anima 这种顶级血统都选择**不依赖大基金**起步——说明物理 AI 早期可以靠技术+compute partner 冷启动，降低对融资的依赖。

---

## 补充到投资人人脉清单（大机构备注）

| 机构/个人 | 角色 | 与 AU 关系 | 邮箱/备注 |
|---|---|---|---|
| **Jeff Bezos（贝索斯）** | 投资人/创始人 | 通过 Prometheus 开出 $2B+ 邀约**被拒**；后投 Prometheus | explore@bezosexpeditions.com |
| **Vik Bajaj** | 生物科技投资人/连续创业者 | 撮合者，被拒；后与 Bezos 创 Prometheus | （LinkedIn） |
| **Project Prometheus** | 物理AI公司 | 曾想并购/吸纳 AU 创始团队**被拒** | （官网 PROMETHEUS 未公开） |
| **摩根大通 / 高盛 / 贝莱德 / DST Global / ARCH Venture Partners** | 大机构 | 均为 **Prometheus** 投资人（非 AU） | — |
| **Nvidia（英伟达）** | 芯片/算力 | **未投资 AU**；黄仁勋仅为学术鼓励 | kv@khoslaventures.com 不适用，见 email 库 |

> 注：此案例**不新增可投递的 AU 投资人邮箱**（因 AU 未披露投资人）。此表主要为「物理AI/具身AI 赛道 - 大资金动向」的人脉参考。
