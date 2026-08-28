# AwareLiquid 融资发送 · 精选收件人名单 + 发送脚本说明

> 说明：从 `ai-investor-email-directory.md`（167 邮箱）+ `robotics-companies-contacts.md` 中，**精选**与 AwareLiquid（MT-LNN / O(1) 端侧 / 电池 BMS / 合规文档）最匹配的收件人。**不群发全部**——分层、分批、避免 spam 与域名信誉风险。
> 发件账号：anmuning@awareliquid.ai（腾讯企业邮箱，授权码已验证有效）
> 发件人：Everest An（安沐凝）· +86 13653649378

---

## 首批（最对口，建议先发 5-8 家）

### 1) 机器人 / 具身 / 电池产业方（中文版 · 战略投资+技术合作）
| 公司 | 收件人 | 邮箱 | 叙事点 |
|---|---|---|---|
| 智元 AgiBot | 投融资经理 赵欣雨 | `zhaoxinyun@agibot.com` | O1 端侧大脑 / BMS |
| 宇树 Unitree | 商务+融资 | `marketing@unitree.com` / `fa_wf@unitree.com` | 端侧 MCU 大脑 |
| 优必选 UBTech | 投资者关系 | `investor@ubtrobot.com` | 具身智能协同 |
| 众擎 EngineAI | 商务 | `sales@engineai.com.cn` | 端侧 + 成本 500× |
| 银河通用 Galbot | 王鹤（CTO，北大） | `hewang@pku.edu.cn` | 具身泛化 + O(1) |

### 2) 美元 AI VC（英文版 · AI-native 优先，最懂技术）
| 基金 | 官网 | 邮箱 | 切入点 |
|---|---|---|---|
| Conviction（Sarah Guo） | conviction.com | `sarah@conviction.com` | AI-native 架构 |
| Radical Ventures | radical.vc | `hello@radical.vc` | LLM + 液态基座 |
| AIX Ventures | aixventures.com | `hello@aixventures.com` | 端侧/LLM 架构 |
| Zetta Venture Partners | zettavp.com | `info@zettavp.com` | B2B AI |
| Amplify Partners | amplifypartners.com | `info@amplifypartners.com` | 基础设施/技术创始人 |
| Basis Set Ventures | basisset.com | `bsv@basisset.ventures` | 应用 AI |
| Gradient Ventures | gradient.com | `investorhiring@gradient.com` | AI 专投 |

### 3) 人民币 AI 基金（中文版）
| 基金 | 邮箱 | 切入点 |
|---|---|---|
| 蓝驰创投 | （官网表单） | 硬科技/具身 |
| 联想创投 | （官网） | 具身 + 产业协同 |
| 源码资本 | （官网） | 技术驱动 |
| 奇绩创坛 | （官网） | 早期 + AI |

---

## 第二批（BP 附件+跟进）

- **美元平台层**：a16z、Sequoia、Thrive、Lightspeed、Menlo、Khosla、Founders Fund、Kleiner Perkins、Accel、Greylock、Index、General Catalyst、Bessemer、Lux、Madrona、Benchmark、NEA、Insight（邮箱见 `ai-investor-email-directory.md`）
- **更多机器人公司**：傅利叶 `info@fftai.com`、加速进化 `sales@boosterobotics.com`、乐聚 `pr@lejurobot.com`、星动纪元 `MKT@robotera.com`、逐际动力（官网表单）

---

## 发送策略

1. **分批**：首批 5-8 家，第二批覆盖平台层，间隔 1-2 天，避免同日大量外发触发风控（今天 SMTP 已因短时多次连接被限速）。
2. **个性化**：每封收件人姓名/公司名替换；正文用「版本一（产业方）/版本二（RMB）/版本三（美元）」对应。
3. **附件**：BP PDF（`AwareLiquid 三体暗源天使轮融资BP(3).pdf`）；美元基金可用英文 deck `out/Awareness-Investor-Deck-EN.pptx`。
4. **跟进**：5-7 个工作日无回音 → 简短跟进一次；有 demo/benchmark 更新再触达。

---

## 待连接恢复后执行

- 授权码：已验证有效（首次 `LOGIN_OK`）
- 当前状态：腾讯账号因短时频繁连接触发**风控限速**，TLS 握手超时；需 **等部分（约 10-30 分钟）** 或 **换网络（手机热点/不同出口）** 后重试。
- 重试即可用：`py send_campaign.py`（我稍后写好，含全部正文 + 附件 + 分层名单）
