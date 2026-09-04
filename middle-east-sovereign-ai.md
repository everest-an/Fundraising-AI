# 中东主权 AI 机构 · 投融资 / 实验室合作清单

> 整理日期：2026-08-30
> 背景：阿联酋（阿布扎比/迪拜）、沙特正以主权基金 + 国家战略重金押注 AI，但**自主架构研发普遍依赖外部**（见下），对「技术主权 + 非 Transformer 架构」有强需求——是 AwareLiquid（MT-LNN）融资/进实验室的高价值方向。
> 邮箱标注：✅ 官方/公开；⚠️ 第三方披露；❌ 官网表单。

---

## 一、核心洞察（为什么中东是 MT-LNN 的机会）

1. **有钱但缺自主架构**：中东主权 AI 的模型底座普遍是「买/借」的：
   - 阿联酋 **Falcon-H1** 用 **Mamba-Transformer 混合架构**（TII，2026-01 发布，彻底抛弃纯 Transformer）——**已经在 MT-LNN 的 state-space 赛道探索**
   - 沙特 **HUMAIN M3** 基于 **中国 MiniMax M3 底座**（2026-09 发布，投喂 1 万亿+ 阿拉伯语 token 后训练）
   - 阿联酋 **K2** 基于 **阿里 Qwen2.5**；**Jais** 是 MBZUAI/G42/Cerebras 合作
2. **要技术主权**：主权基金明确要"拥有并控制自己的计算、人才、平台，不依赖他国"——**自主架构（MT-LNN）正是它们缺的那块**
3. **资金量级**：MGX $49B（已关账）、HUMAIN $40B+、PIF $40B AI 基金、微软 $15.2B 阿联酋投入——远超任何美元 VC

---

## 二、阿联酋（阿布扎比 / 迪拜）

| 机构 | 类型 | 模型/业务 | 为什么对口 MT-LNN | 邮箱 / 入口 |
|---|---|---|---|---|
| **TII（Technology Innovation Institute）** | 政府研究院（ATRC 旗下） | **Falcon 系列**（Falcon 180B、Falcon 3、Falcon-H1 Arabic）| **Falcon-H1 用 Mamba-Transformer 混合架构** = 已探索非纯 Transformer；MT-LNN 液态网络是这方向的进阶 | ❌ tii.ae 官网合作表单（待补邮箱）|
| **ATRC（Advanced Technology Research Council）** | TII 上级委员会 | 统筹 Falcon/研发 | 国家 AI 主权顶层 | ❌ atrc.gov.ae |
| **G42（Group 42）** | AI 巨头（$20B，微软投 $1.5B） | Falcon/Jais 商业化、云、算力 | 运营商角色，可技术+算力合作 | ❌ g42.ai 官网 |
| **MGX** | AI 主权基金（$49B Fund I） | 投 OpenAI/Anthropic/xAI/Databricks | **直接投 AI 初创**，70% 北美 | ✅ `compliance@mgx.ae`（投递入口）|
| **Mubadala** | 主权基金（$385B AUM） | MGX 母公司，投前沿科技 | 长线资本 | ❌ mubadala.com |
| **MBZUAI / IFM（Institute of Foundation Models）** | AI 大学 + 基础模型研究所 | **Jais、K2** 模型；阿布扎比/硅谷/巴黎三地 | 明确"欢迎创始人/startup 在先进 AI 基础设施上共建" | ✅ `research@mbzuai.ac.ae`、`president@mbzuai.ac.ae`；❌ ifm.ai/collaborate 表单 |
| **Hub71** | 阿布扎比孵化器 | 早期 AI 初创 | 种子轮 + 落地 | ❌ hub71.com |
| **迪拜未来基金会 / Dubai AI** | 政府孵化 + 加速 | 早期科技 | 早期 | ❌ dubai.ai |

---

## 三、沙特

| 机构 | 类型 | 模型/业务 | 为什么对口 MT-LNN | 邮箱 / 入口 |
|---|---|---|---|---|
| **HUMAIN（王储任董事长，PIF 旗下）** | 主权 AI 公司（$40B+） | **ALLaM、HUMAIN M3**；6GW 数据中心 | **HUMAIN Ventures（$10B+ VC，今年推出）投 AI 初创**；CEO Tareq Amin 明确"不做被动投资，投承诺用沙特算力/带团队的 AI 公司"；**M3 用 MiniMax 底座 = 愿买外部架构** | ✅ `pr@humain.ai`（PR）；❌ humain.com 官网 |
| **PIF（公共投资基金）** | 主权基金 | HUMAIN 母公司；$40B AI 基金 | 主权资本 | ❌ pif.gov.sa |
| **SDAIA（沙特数据与AI局）** | 政府 AI 权威 | **ALLaM** 模型（与 Aramco 合作）、国家 AI 战略 | 国家 AI 主权顶层；ALLaM 作者可联系 | ⚠️ `skarim@sdaia.gov.sa`（ALLaM 论文作者）、`malfadly@sdaia.gov.sa`（Director）|
| **KAUST（阿卜杜拉国王科技大学）** | 大学 + GenAI CoE | 买 H100 建模型；GenAI Center of Excellence | 学术合作 + 算力 | ❌ kaust.edu.sa |
| **Aramco / Aramco Ventures / Aramco Digital** | 能源巨头 + CVC | 工业 AI + AI 基础设施 | 能源数据 + 算力；Aramco Ventures 已录 | ✅ Aramco Ventures `hotline@aramcoventures.com`（见主目录）|

---

## 四、最值得主动接触（按优先级）

1. **HUMAIN Ventures**（沙特，$10B+，投 AI 初创，明确"非被动投资、投本地化 AI"）—— `pr@humain.ai` 起步，或官网 form。**MT-LNN 的端侧/低算力叙事 + 愿进沙特数据中心/带团队 = 正中 HUMAIN 的"非被动投资"标准**。
2. **MGX**（阿布扎比，$49B，投 AI 前沿）—— `compliance@mgx.ae`。投 OpenAI/Anthropic 级别，早期未必对口，但可作为"架构/主权"叙事触达。
3. **TII / ATRC**（阿布扎比，Falcon，已在 Mamba-Transformer 混合架构探索）—— **最对口的技术合作/进实验室对象**：MT-LNN 是 Falcon-H1 的 Mamba 方向的进阶，可直接谈"架构合作/联合实验室"。
4. **MBZUAI IFM**（Jais/K2，明确欢迎 founder 共建基础模型）—— `research@mbzuai.ac.ae`，进实验室/联合研发路径最明确。
5. **SDAIA / KAUST**（沙特，ALLaM，主权模型）—— 学术+主权合作。

---

## 五、投递建议（针对中东主权机构）

1. **叙事切换**：对中东机构，重点不是"我们多快多强"，而是 **"技术主权"**——"你们的 Falcon/M3/K2 底座依赖外部架构；我们的 MT-LNN 是自主的、非 Transformer 的架构，可成为你们的技术主权底座"。
2. **呼应他们的动作**：Falcon-H1 用 Mamba（说明 TII 认可 state-space 方向）、HUMAIN M3 用 MiniMax（说明沙特愿买外部底座）—— **MT-LNN 是这两个动作的"自主版答案"**。
3. **HUMAIN 的"非被动投资"**：明确承诺"愿用沙特算力/在沙特设团队"能大幅提升 HUMAIN 兴趣（CEO 原话）。
4. **语言**：英文为主（这些机构国际团队为主），可附阿拉伯语一句话。
5. **邮箱命中率**：MGX `compliance@mgx.ae`、MBZUAI `research@` 是真实入口；HUMAIN/TII 走官网表单 + LinkedIn。

---

> 待补：TII/ATRC 的具体邮箱（被限流，后续补）；HUMAIN Ventures 的正式 intake（基金今年才推，官方入口待公布）。
