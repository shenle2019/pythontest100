# coding:utf-8
from HTMLTestRunner import HTMLTestRunner
import unittest
import time,sys,os
sys.path.append('./package')
sys.path.append('./bbs/test_case/models')
from package import email_send
import function

test_dir = './bbs/test_case'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='login*.py')

if __name__ == "__main__":

    #生成测试报告
    filename = "./bbs/report/result" + str(time.time()) + ".html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp,title="测试报告",description="用例执行情况")
    #runner = unittest.TextTestRunner()
    runner.run(discover)
    fp.close()

    #获取最新的测试报告

    file_path = os.path.dirname(__file__) + '/bbs/report/'
    new_file = function.new_report(file_path)
    file_name = file_path + new_file


    #发送邮件
    from_addr = "hulinjun2006@126.com"
    password = "tanglirong520"
    from_addr = "hulinjun2006@126.com"
    to_addr = ['453105647@qq.com','hulj@szap.com']
    send_email = email_send.Sendemail(password, from_addr, to_addr)
    msg = send_email.send_html(file_name)
    send_email.main(msg)
