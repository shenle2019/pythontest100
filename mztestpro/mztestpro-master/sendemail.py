# coding:utf-8
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib,sys,os
sys.path.append('./bbs')
from bbs import test
from email.header import Header

#得到最新的报告文件
def lis(file_path):
    files = os.listdir(file_path)
    f_time = []
    for f in files:
        kuo = os.path.splitext(f)[1]
        if kuo == ".html":
            fil = file_path + f
            f_times = os.path.getctime(fil)
            f_time.append((f_times,f))
            f_time = sorted(f_time,key=lambda f_time : f_time[0])
    return f_time[-1][1]

#格式化收件人的显示名字，貌似现在不起作用了
def _format_addr(s):
    '''格式化一个邮件地址。因为如果包含中文，需要通过Header对象进行编码'''
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#打开测试报告
def open_report(file_path):
    file = file_path + 'result1479201561.9369092.html'
    print(file)


# 输入Email地址和口令:
from_addr = "emptymiss@126.com"
password = "Change_Me123"
# 输入收件人地址:
to_addr = "305030951@qq.com"
# 输入SMTP服务器地址:
smtp_server = "smtp.126.com"
#发送纯文本
#msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
#发送html格式的
#msg = MIMEText('<html><body><h1>你好：</h1><p>我是来自<a href="http://www.baidu.com">打开百度</a></p></body></html>','html','utf-8')
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['Subject'] = Header(u'来自大西洋的问候', 'utf8').encode()
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg.attach(MIMEText('hello, send by Python...', 'plain', 'utf-8'))

#构造附件
file_path = 'bbs/report/'
new_file = lis(file_path)
new_file_path = file_path + new_file
print(new_file_path)
att1=MIMEText(open(new_file_path,'rb').read(),'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="1.html"'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(att1)

#发送邮件
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)#打印发送过程
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
print("邮件发送成功")
server.quit()

if __name__ == "__main__":
    file_path = "./bbs/report/"
    open_report(file_path)
