"""
E_mail.py 配置收发邮件
"""
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time
from Zhujia_Factory.config.conf import *

now = time.strftime("%Y-%m-%d_%H-%M-%S")  # 获取当前时间
reportname = now + ".html"


def send_mail(report):
    f = open(report, "rb")
    mail_body = f.read()
    f.close()

    username = "1120620374@qq.com"  # 发件箱用户名
    password = "legbyrctuueyhggb"  # 发件箱密码（授权码）
    sender = "1120620374@qq.com"  # 发件人邮箱
    receivers = ["m15180381485@163.com", '596137586@qq.com']  # 收件人邮箱

    msg = MIMEMultipart(_subtype='html', _charset='utf-8')
    email_att = MIMEApplication(
    open('E:/pycharm/Jsfk/report/{latest}'.format(latest=reportname), 'rb').read())
    email_att.add_header('Content-Disposition', 'attachment', filename=report)
    msg.attach(email_att)
    content = MIMEText('******邮件自动发送无需回复，如需查看用例执行情况，请下载附件******', 'plain', 'utf-8')
    msg.attach(content)  # 正文内容

    # 邮件对象
    msg["Subject"] = "UI自动化测试报告"
    msg['From'] = '1120620374@qq.com'  # 发件人
    msg['To'] = "m15180381485@163.com,596137586@qq.com"  # 收件人,使用逗号隔开输入即可
    msg["date"] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")  # 邮箱服务器
    smtp.login(username, password)  # 登录邮箱
    smtp.sendmail(sender, receivers, msg.as_string())  # 发送者和接收者
    smtp.quit()
    print("邮件已发出,请注意查收!")


def new_report(test_report):
    """查找测试目录，找到最新生成的测试报告文件======"""
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    return file_new
