# -*- coding: utf-8 -*-
"""
MTLNN 投递邮件发送脚本（腾讯企业邮箱）
用法：
  1. 填好下方【配置区】
  2. 设置授权码环境变量：  $env:SMTP_PASSWORD="你的授权码"   （PowerShell）
     或运行后按提示输入（不显示）
  3. 运行：  py send_outreach.py
说明：
  - 腾讯企业邮箱 SMTP：smtp.exmail.qq.com:465 (SSL)
  - 授权码 ≠ 登录密码，需登录 mail.exmail.qq.com 在「设置-客户端设置」开启 IMAP/SMTP 并生成
"""
import os
import sys
import getpass
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from email.utils import formataddr

# ================= 配置区（请填写） =================
SMTP_HOST = "smtp.exmail.qq.com"
SMTP_PORT = 465          # SSL
SENDER_EMAIL = "anmuning@awareliquid.ai"
SENDER_NAME = "【你的姓名】"

# ---- MTLNN 技术细节（填真实数据，不要编造） ----
YOUR_NAME = "【姓名】"
YOUR_TITLE = "【公司/学校 + 职位】"
YOUR_CONTACT = "【电话 / 微信】"
YOUR_LINK = "【官网 / demo 链接】"

MTLNN_MECHANISM = "【一句话讲清泛化机制，例：通过多任务联合训练与跨域迁移，把机器人在任务A学到的能力迁移到从未见过的任务B】"
MTLNN_EVIDENCE = "【1-2条可验证证据：benchmark提升幅度 / 对比实验 / demo视频链接】"
FUNDRAISING_ASK = "【如有融资需求写明轮次/金额/用途；没有则写：暂无融资计划，仅技术合作】"

# 可选附件（BP / 一页纸），留空字符串则不带附件
ATTACHMENT_PATH = ""   # 例：r"C:\Users\ASUS\Documents\BP.pdf"
# ================= 配置区结束 =================

SIGNATURE = f"{YOUR_NAME}\n{YOUR_TITLE}\n{YOUR_CONTACT}\n{YOUR_LINK}"

EMAILS = [
    {
        "to": "zhaoxinyun@agibot.com",
        "subject": "具身智能泛化学习——MTLNN破解机器人「只会重复、不会泛化」的卡点",
        "body": (
            "赵经理，您好：\n\n"
            "在您的LinkedIn看到您在关注具身智能、机器人与AI领域的创业投资与技术合作，冒昧来信。\n\n"
            "人形机器人至今无法走入千家万户，根子不在本体，而在「大脑」——当前机器人靠海量数据做重复训练，"
            "学会的是特定场景的固定动作，环境或任务稍有变化就失效，缺乏真正的泛化学习能力。\n\n"
            f"我们团队研发的MTLNN（多任务学习神经网络）模型，正是冲着这个卡点去的：{MTLNN_MECHANISM}。\n\n"
            f"{MTLNN_EVIDENCE}\n\n"
            "我们希望与智元探讨两个方向：\n"
            "1. 技术合作——MTLNN接入贵司机器人，验证真实场景下的泛化能力提升；\n"
            f"2. 战略投资——{FUNDRAISING_ASK}。\n\n"
            "附件见BP/一页纸。期待与您或团队同事做一次简短交流。谢谢！\n\n"
            f"{SIGNATURE}"
        ),
    },
    {
        "to": "marketing@unitree.com",
        "subject": "机器人泛化学习技术合作——MTLNN模型",
        "body": (
            "宇树团队，您好：\n\n"
            "贵司的H1/G1等产品在硬件与运动控制上已是行业标杆。但行业共同面临一个瓶颈："
            "机器人「能跑能跳」却「不能举一反三」——现在的能力来自海量重复训练，"
            "缺乏跨任务、跨场景的泛化，这是机器人迟迟无法大规模进入家庭与泛化服务场景的根因。\n\n"
            f"我们团队研发的MTLNN模型，正是解决这个泛化问题：{MTLNN_MECHANISM}。\n\n"
            f"{MTLNN_EVIDENCE}\n\n"
            "我们想与宇树探讨技术合作：把MTLNN接入贵司机器人，验证在家庭多任务操作/跨场景迁移上的泛化能力提升。"
            "同时，若贵司对底层「大脑」模型有战略布局考虑，我们也欢迎交流投资可能。\n\n"
            "附件见BP/一页纸，盼复。谢谢！\n\n"
            f"{SIGNATURE}"
        ),
    },
]


def build_message(to, subject, body):
    msg = MIMEMultipart()
    msg["From"] = formataddr((str(Header(SENDER_NAME, "utf-8")), SENDER_EMAIL))
    msg["To"] = to
    msg["Subject"] = Header(subject, "utf-8")
    msg.attach(MIMEText(body, "plain", "utf-8"))
    if ATTACHMENT_PATH and os.path.exists(ATTACHMENT_PATH):
        with open(ATTACHMENT_PATH, "rb") as f:
            part = MIMEApplication(f.read(), Name=os.path.basename(ATTACHMENT_PATH))
        part["Content-Disposition"] = f'attachment; filename="{os.path.basename(ATTACHMENT_PATH)}"'
        msg.attach(part)
        print(f"  [附件] {os.path.basename(ATTACHMENT_PATH)}")
    return msg


def main():
    # 读取授权码：优先环境变量，否则交互输入（不回显）
    password = os.environ.get("SMTP_PASSWORD", "")
    if not password:
        password = getpass.getpass("请输入 SMTP 授权码（输入不回显）: ").strip()
    if not password:
        print("未提供授权码，退出。")
        sys.exit(1)

    # 安全检查：确认占位符已替换
    unedited = [k for k in ("【", "】") if k in (SENDER_NAME + YOUR_NAME + MTLNN_MECHANISM + MTLNN_EVIDENCE)]
    if unedited:
        print("⚠ 警告：配置区仍有未填写的占位符【】，邮件可能含空模板。")
        confirm = input("确认仍要发送？(输入 y 继续，其它取消): ").strip().lower()
        if confirm != "y":
            print("已取消。")
            sys.exit(0)

    log_lines = []
    server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=30)
    server.login(SENDER_EMAIL, password)
    print(f"已登录 {SMTP_HOST}，发件人 {SENDER_EMAIL}\n")

    for e in EMAILS:
        msg = build_message(e["to"], e["subject"], e["body"])
        try:
            server.sendmail(SENDER_EMAIL, [e["to"]], msg.as_string())
            status = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}  ✅ 已发送 → {e['to']}  |  {e['subject']}"
            print(status)
            log_lines.append(status)
        except Exception as err:
            status = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}  ❌ 发送失败 → {e['to']}  |  {err}"
            print(status)
            log_lines.append(status)

    server.quit()

    log_path = "send_log.txt"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write("\n".join(log_lines) + "\n")
    print(f"\n发送日志已写入 {log_path}")


if __name__ == "__main__":
    main()
