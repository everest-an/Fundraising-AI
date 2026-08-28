# AwareLiquid 融资邮件 · 终稿（三版本）

> 公司：深圳三体暗源科技（AwareLiquid / Awareness）
> 创始人：Everest An（安沐凝）· CTO：Eric
> 融资：**Seed/A 轮 $3.5M**（BP「The Ask」页）
> 官网 awareliquid.ai · 论文 huggingface.co/EverestAn/MT-LNN · 代码 github.com/everest-an/M1 · Demo huggingface.co/spaces/EverestAn/Awareness01
> 创始人：everest9812@gmail.com · WeChat/Telegram: EverestAn · 电话 +86 13653649378

---

## 核心卖点（所有版本通用，从中选 2-3 条）

- **O(1) 内存，打破 KV 缓存墙**：1M 上下文下携带状态 **0.381 MB**，同级 Transformer KV 缓存 **3,072 MB**（**8,063 倍差距**，实测非外推）。1000 tokens：4.1 KB vs 1020 KB。
- **成本低 2-3 个数量级**：100 用户并发 10 万字文档，Transformer 需 ~60 块 A100（$100K/月）；MT-LNN 仅 **1 块 RTX 4090（$200/月）**，成本降约 **500 倍**。API 推理成本比 Transformer 低 ~90%。
- **端侧 / MCU 可部署**：O1 边缘系列——电池健康度流式回归携带状态仅 **2.6 KB**、智能穿戴唤醒词 **5.12 KB**，无云端依赖、毫秒级延迟。物理上可塞进手机、可穿戴、车载、工业传感、**机器人**、电池 **BMS** 芯片。
- **不规则时序鲁棒（液态原生）**：NASA PCoE 电池数据，**80% 样本缺失下仅退化 +7.7%**（LSTM +31.1% / GRU +32.8%）。
- **合规文档实测**：金融文档多域标注 **91.7%（44/48）**，每题约 1.3 次模型调用、~2.8k tokens，全程本地私有化，179 项测试全绿。
- **诚实定位**（专业投资人最看重）：不在通用智能指数上竞争（MMLU 对 48M-1.1B 接近随机）；取胜点是**长上下文 + 端侧成本**，同尺寸 200K 下全序列召回领先（T=32 89.5% vs 67.6%，T=229 ≈2×）。

---

## 版本一：中文 · 机器人/具身智能/电池产业方（宇树、智元、优必选等）

**主题：** AwareLiquid 天使轮｜MT-LNN O(1) 边缘模型，为机器人/电池提供 MCU 级端侧大脑

---

尊敬的王总/江总/投融资团队：

冒昧来信。我是深圳三体暗源科技（AwareLiquid）创始人安沐凝。我们做的是——**把 LLM 的「大脑」压缩到能塞进机器人、电池、穿戴的端侧芯片里，且成本是现有方案的千分之一**。

**为什么我们和贵司是天作之合：**

**1. 端侧大脑，MCU 级可部署**
我们的 **O1 边缘模型**（MT-LNN 液态神经网络）做到了 Transformer 物理上做不到的事：**恒定 O(1) 推理内存**——1M 上下文携带状态仅 **0.381 MB**（同级 KV 缓存 3,072 MB，差 8,063 倍实测）。已在**电池健康度 2.6 KB、智能穿戴唤醒词 5.12 KB** 场景实测，纯 CPU、毫秒级、无云端依赖。这正是机器人具身智能和 BMS 电池管理苦求的「端侧大脑」。

**2. 不规则时序鲁棒，为真实世界而生**
真实传感器数据从不完美。在 NASA PCoE 电池数据集，**80% 时间步缺失下我们的模型仅退化 +7.7%**（LSTM +31.1% / GRU +32.8%）。液态 ODE 是原生属性，不是补丁——机器人、电池、工业传感器这类连续流式数据，天然适配。

**3. 硬核顶会级背书 + 已落地**
核心模型 MT-LNN 为 AAAI-27 投稿（#36767）；金融文档多域评测 **91.7%**，全程本地私有化；已在为企业客户做数据清洗、电池端侧模型部署。团队含香港理工博士组、Stable Diffusion 架构师顾问。

**4. 极致成本**
Transformer 处理 100 用户并发 10 万字文档需 ~60 块 A100（$100K/月）；我们 **1 块 RTX 4090**（$200/月），成本低约 500 倍。

我们本轮融资 **$3.5M**（Seed/A），用于原生 2B 推理引擎训练 + GTM。若贵司看好「端侧具身智能」，我们非常期待探讨**技术合作 + 战略投资**——把 MT-LNN 装进贵司下一代机器人/BMS。

附中文 BP。盼复，谢谢！

安沐凝（Everest An）
AwareLiquid 创始人 · 电话/微信 +86 13653649378
www.awareliquid.ai

---

## 版本二：中文 · 人民币基金（蓝驰、联想创投、源码、高榕、五源/顺为/奇绩等）

**主题：** AwareLiquid 天使轮 $3.5M｜MT-LNN 打破 KV 缓存墙，端侧 AI 的液冷范式

---

尊敬的【基金】投资团队：

冒昧来信。我是深圳三体暗源科技（AwareLiquid）创始人安沐凝。我们想请你投一个正在从根上改写 LLM 推理经济学的架构。

**一句话：** MT-LNN（AAAI-27 投稿）用受微管启发的液态神经网络，把 Transformer 的 O(N) KV 缓存变成**恒定 O(1) 状态**——1M 上下文 **0.381 MB vs 3,072 MB**，成本**低 2-3 个数量级**，且能塞进 MCU 级端侧芯片。

**为什么现在投：**
- **已被验证的硬指标**：纯 CPU 吞吐 6,164→6,645 tok/s；电池 80% 缺失仅退化 +7.7%；金融文档 91.7%，179 项测试全绿；~100 用户已在使用。
- **诚实的定位**：我们不在通用智能（MMLU）上硬碰 AGI 模型，而是在**长上下文 + 端侧成本**这个被低估但确定性极强的赛道做斩杀线。同尺寸 200K 参数，全序列召回领先（T=32 89.5% vs 67.6%）。
- **双收入流**：B2B 本地部署授权（法律/金融/国防）+ 云端 API（成本比 Transformer 低 ~90%）。
- **市场**：TAM $120B / SAM $45B / **SOM $2.5B+**（被云端隐私风险阻断、急需低成本私有化超长上下文的 B2B）。

**本轮 $3.5M**：50% 算力（H100/A100 跑 2B 基座 + 缩放曲线）、30% LNN 核心研究、20% GTM。12 个月里程碑：≥10 家机构 MoU/PoC，3-5 家转付费 design partner，发布生产级 2B 检查点 + 公开 benchmark。

附中文 BP + 一页纸。期待与您做一次简短交流。

安沐凝（Everest An）
AwareLiquid 创始人 · +86 13653649378 · www.awareliquid.ai

---

## 版本三：英文 · 美元基金 / 美国 AI VC（Conviction、Radical、a16z、Sequoia 等）

**Subject:** AwareLiquid — $3.5M Seed/A｜MT-LNN: O(1) memory kills the KV-cache wall; edge-deployable AI

---

Dear [Investor/Team],

I'm Everest An, founder of AwareLiquid (Shenzhen). We built **MT-LNN**, a microtubule-inspired liquid neural architecture that replaces the Transformer's O(N) KV cache with a **constant O(1) state** — and in doing so, rewrites the economics of long-context and edge inference.

**The core insight:** At 1M context, our carried state is **0.381 MB vs 3,072 MB** for an equivalent Transformer KV cache (an **8,063× gap, measured not extrapolated**). At 1K tokens: **4.1 KB vs 1,020 KB**. Cost is **2-3 orders of magnitude** lower: 100 concurrent users over a 100K-token doc need ~60 A100s ($100K/mo) on Transformer; **we use 1 RTX 4090 ($200/mo)** — about a **500×** reduction.

**Why this is investable now:**
- **Edge / MCU deployment, physically impossible for Transformer**: our O1 edge models run battery health at **2.6 KB** and wearables keyword-spotting at **5.12 KB**, pure CPU, millisecond latency, no cloud. Built for robots, BMS, wearables, automotive, industrial sensors.
- **Robust to irregular time series (native, not patched)**: on NASA PCoE battery data, with **80% of timesteps missing we degrade only +7.7%** (LSTM +31.1% / GRU +32.8%).
- **Real, validated traction**: financial-document multi-domain eval **91.7% (44/48)**, fully local/private, 179/179 tests green; **~100 users** in production; live enterprise data-cleaning + battery on-device deployments.
- **Honest positioning (what sophisticated investors want to hear)**: we do **not** compete on general-intelligence benchmarks (MMLU is near-random for sub-1B models). We win decisively on **long-context + edge cost** — at equal 200K params, full-sequence recall leads at every length (T=32: 89.5% vs 67.6%; T=229: ≈2×).
- **AAAI-27 submission** (#36767) + reproducible recipe across Qwen/Llama base models.
- **Dual revenue**: B2B on-prem licensing (legal/finance/defense) + high-throughput API at ~90% below Transformer pricing.

**Market:** TAM $120B / SAM $45B / **SOM $2.5B+** (B2B blocked by cloud-privacy risk, desperate for low-cost private long-context).

**The ask: $3.5M Seed/A** — 50% compute (2B base + scaling curves on H100/A100), 30% LNN core research, 20% GTM. 12-month milestones: ≥10 institutional MoUs/PoCs, 3-5 converting to paid design partners, first production 2B checkpoint + public benchmark.

Attached is our English deck. I'd welcome a short call.

Best,
Everest An
Founder, AwareLiquid · +86 13653649378 · www.awareliquid.ai · everest9812@gmail.com

---

## 投递清单（按 BP「联系方式」页）

- **创始人邮箱（BP 公开）**：everest9812@gmail.com
- **发件账号**：anmuning@awareliquid.ai（企业邮箱，已验证 SMTP `smtp.exmail.qq.com:465`）
- **官网/论文/代码/Demo**：awareliquid.ai · huggingface.co/EverestAn/MT-LNN · github.com/everest-an/M1 · huggingface.co/spaces/EverestAn/Awareness01
- **机器人/具身/电池产业方**（走中文版一，RMB 战略投资+技术合作叙事）：宇树、智元、优必选、众擎、银河通用、傅利叶、加速进化、乐聚、星动纪元、逐际动力 + 电池厂（宁德/比亚迪/BMS 厂商）
- **人民币基金**（中文版二）：蓝驰、联想创投、中科创星、源码、高榕、五源、顺为、奇绩创坛、真格、理想/小米等
- **美元基金**（英文版三）：AI-native（Conviction、Radical、AIX、Zetta、Amplify、Basis Set、Gradient、Glasswing、Theory、DCVC、Hyperplane、Air Street）+ 平台层（a16z、Sequoia、Thrive、Lightspeed、Menlo、Khosla、Founders Fund、Kleiner Perkins、Accel、Greylock、Index、GC、Bessemer、Lux、Madrona、Benchmark、NEA、Insight）
