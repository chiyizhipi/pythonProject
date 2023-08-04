# -*- coding: utf-8 -*-
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from urllib.request import urlopen
import threading
import datetime
import sys

# smtplib模块主要负责发送邮件：是一个发送邮件的动作，连接邮箱服务器，登录邮箱，发送邮件（有发件人，收信人，邮件内容）。
# email模块主要负责构造邮件：指的是邮箱页面显示的一些构造，如发件人，收件人，主题，正文，附件等。
my_ip = urlopen('http://ifconfig.me/ip', timeout=5).read()
my_ip = my_ip.decode(encoding='utf-8')
sender_qq = 'liningyuan1998@163.com'  # 发送邮箱
receiver = ['593431101@qq.com', 'zzkkoo8@qq.com', 'yupeng.zheng@chaitin.com', 'wenjie.lv@chaitin.com']  # 接收邮箱
pwd = "XYJAOSAGGPPTZISZ"  # 授权码


def send_email(my_ip, time=None):
    host_server = 'smtp.163.com'  # qq邮箱smtp服务器
    mail_title = '公网地址发生改变'  # 邮件标题
    mail_content = "公网IP：{}\n发送时间：{}".format(my_ip, time)  # 邮件正文内容
    # 初始化一个邮件主体
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq
    # msg["To"] = Header("测试邮箱",'utf-8')
    msg['To'] = ";".join(receiver)
    # 邮件正文内容
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))
    smtp = SMTP_SSL(host_server)  # ssl登录

    # login(user,password):
    # user:登录邮箱的用户名。
    # password：登录邮箱的密码，像笔者用的是网易邮箱，网易邮箱一般是网页版，需要用到客户端密码，需要在网页版的网易邮箱中设置授权码，该授权码即为客户端密码。
    smtp.login(sender_qq, pwd)

    # sendmail(from_addr,to_addrs,msg,...):
    # from_addr:邮件发送者地址
    # to_addrs:邮件接收者地址。字符串列表['接收地址1','接收地址2','接收地址3',...]或'接收地址'
    # msg：发送消息：邮件内容。一般是msg.as_string():as_string()是将msg(MIMEText对象或者MIMEMultipart对象)变为str。
    smtp.sendmail(sender_qq, receiver, msg.as_string())

    # quit():用于结束SMTP会话。
    smtp.quit()


def ip_render():
    global my_ip
    global timer
    try:
        date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_ip = urlopen('http://ifconfig.me/ip').read()
        new_ip = new_ip.decode(encoding='utf-8')
        if new_ip != my_ip:
            my_ip = new_ip
            send_email(my_ip, time=date_time)
            print('IP changed:{} -time:{}'.format(my_ip, date_time))
            file = open("/Users/eugene/Music/history.txt", 'a+', encoding='UTF-8')
            # file.write('\nIP changed:{} -time:{}'.format(my_ip, date_time))
            file.write('\n{} Waring IP address changed {}'.format(date_time,my_ip))
            file.close()
        else:
            sys.stdout.write("\rIP doesn't change -time:{}".format(date_time))
            sys.stdout.flush()
            file = open("/Users/eugene/Music/history.txt", 'a+', encoding='UTF-8')
            #file.write('\nIP not change:{} -time:{}'.format(my_ip, date_time))
            file.write('\n{} IP not change {}'.format(date_time, my_ip))
            file.close()
    except Exception as e:
        print("Exception:{}".format(e))
    timer = threading.Timer(30, ip_render)  # 30s 获取IP一次（注意：断网时候会获取不到IP地址，已改为2小时）
    timer.start()

if __name__ == "__main__":
    print('IP:{}'.format(my_ip))
    timer = threading.Timer(5, ip_render)  # 5s后开始循环线程
    timer.start()


