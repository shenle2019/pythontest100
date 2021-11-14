# coding:utf-8
import unittest, sys, random

sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import Login
from time import sleep
from selenium.webdriver.common.by import By


class LoginTest(myunit.MyTest):
    '''社区登录'''

    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        Login(self.driver).user_login(username, password)

    def test_login1(self):
        '''用户名和密码都为空'''
        print("---------用户名密码开始验证----------" )
        self.user_login_verify()
        print("---------用户名密码验证完成----------" )
        po = Login(self.driver)
        # alert = po.alert_info()
        # print(alert)
        # username_mes = alert.text
        username_mes = po.find_element(By.ID, "Email-error").text
        print(username_mes)
        self.assertEqual(username_mes, '请输入邮箱')
        # alert.accept()
        sleep(1)
        function.insert_img(self.driver, 'username_pass_kong.jpg')

    # def test_login2(self):
    #     #     '''用户名正确，密码为空'''
    #     print("---------用户名密码开始验证2----------" )
    #     self.user_login_verify(username='305030951@qq.com')
    #     print("---------用户名密码验证完成2----------" )
    #     po = Login(self.driver)
    #     # alert = po.alert_info()
    #     # print(alert)
    #     # username_mes = alert.text
    #     password_mes = po.find_element(By.ID, "Password-error").text
    #     print(password_mes)
    #     self.assertEqual(password_mes, '请输入密码')
    #     # alert.accept()
    #     sleep(1)
    #     function.insert_img(self.driver, 'password_pass_kong.jpg')
    #
    #
    # # def test_login2(self):
    # #     '''用户名正确，密码为空'''
    # #     self.user_login_verify(username='18565660212')
    # #     po = Login(self.driver)
    # #     alert = po.alert_info()
    # #     username_mes = alert.text
    # #     print(username_mes)
    # #     self.assertEqual(username_mes, '账号或密码不能为空！')
    # #     alert.accept()
    # #     sleep(1)
    # #     function.insert_img(self.driver, 'password_kong.jpg')
    #
    #
    # def test_login3(self):
    #     #     '''用户名或者密码错误'''
    #     print("---------用户名密码开始验证3----------" )
    #     self.user_login_verify(username='305030952@qq.com',password='Change_Me123')
    #     print("---------用户名密码验证完成3---------" )
    #     po = Login(self.driver)
    #     # alert = po.alert_info()
    #     # print(alert)
    #     # username_mes = alert.text
    #
    #     # / html / body / div / div[3] / div / div / div / div / div / div[1] / form / div[5] / ul / li
    #
    #     error_message = po.find_element(By.XPATH, "/html/body/div/div[3]/div/div/div/div/div/div[1]/form/div[5]/ul/li").text
    #     print(error_message)
    #     self.assertEqual(error_message, '账号或密码错误')
    #     # alert.accept()
    #     sleep(1)
    #     function.insert_img(self.driver, 'username_or_password_error.jpg')
    #
    # def test_login4(self):
    #     #     '''用户名或者密码正确'''
    #     print("---------用户名密码开始验证4----------" )
    #     self.user_login_verify(username='305030951@qq.com',password='Change_Me123')
    #     print("---------用户名密码验证完成4---------" )
    #     po = Login(self.driver)
    #     success_message = po.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div[1]/div/a[1]").text
    #     print(success_message)
    #     success_message2 = '您好，shenle！'
    #     self.assertEqual(success_message, success_message2)
    #     sleep(1)
    #     function.insert_img(self.driver, 'username_or_password_correct.jpg')

if __name__ == '__main__':
    unittest.main()
