# coding:utf-8
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time, sys, os

sys.path.append('./package')
sys.path.append('./bbs/test_case/models')
sys.path.append('./bbs/test_case/report')


# from package import email_send

# ==================定义发送邮件==========================
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("python+selenium 自动化测试报告", 'utf-8')
    msg['from'] = 'emptymiss@126.com'
    msg['to'] = '305030951@qq.com'

    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("emptymiss@126.com", "MDTFMYZKLYOCDGFR")
    smtp.sendmail("emptymiss@126.com", "305030951@qq.com", msg.as_string())
    smtp.quit()
    print('email has send out')


# ==========获取最新的测试报告，用于发送测试报告邮件=========
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


if __name__ == "__main__":
    # 生成测试报告
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # filename = "./bbs/report/result" + str(time.time()) + ".html"
    filename = "./bbs/report/" + now + 'result.html'

    # with open(filename, "w", encoding="utf-8") as fp:
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
    #                                            title="login测试报告",
    #                                            description="登录测试")

    with open(filename, 'w', encoding="utf-8") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title='博文视点测试报告',
                                               description='win10+Chrome+用例执行情况')
        test_dir = './bbs/test_case'
        discover = unittest.defaultTestLoader.discover(test_dir, pattern='login*.py')
        # runner = unittest.TextTestRunner()
        runner.run(discover)
        fp.close()  # 关闭生成的报告

    # 获取最新的测试报告

    # file_path = os.path.dirname(__file__) + '/bbs/report/'
    # new_file = new_report(file_path)
    # file_name = file_path + new_file
        file_path = new_report('./bbs/report/')

    # 发送邮件
        send_mail(file_path)
