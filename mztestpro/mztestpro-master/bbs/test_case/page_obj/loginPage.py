# coding:utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from .base import Page
from time import sleep, time


class Login(Page):
    '''
    用户登录页面
    '''
    # url = '/baobeipc/html/login.html'
    url = ''
    # bbs_login_user_loc = (By.XPATH,".//*[@id='mzCust']/div/div[1]/img[1]")
    # bbs_login_button_loc = (By.ID,"mzLogin")
    # /html/body/div/div[2]/div/div/div/div/div/a[2]
    bbs_login_button_loc = (By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/a[2]')
    # bbs_login_button_loc = (By.XPATH, '//*[@id="loginLink"]')

    # 鼠标悬停
    # def hover(self, by, value):
    #     element = self.findbyElement(by, value)
    #     ActionChains(self.driver).move_to_element(element).perform()
    #
    # # ## 通过不同的方式查找界面元素
    # def findbyElement(self, by, value):
    #     if (by == "id"):
    #         element = self.driver.find_element_by_id(value)
    #         return element
    #     elif (by == "name"):
    #         element = self.driver.find_element_by_name(value)
    #         return element
    #     elif (by == "XPATH"):
    #         element = self.driver.find_element_by_xpath(value)
    #         return element
    #     elif (by == "classname"):
    #         element = self.driver.find_element_by_class_name(value)
    #         return element
    #     elif (by == "css"):
    #         element = self.driver.find_element_by_css_selector(value)
    #         return element
    #     elif (by == "link_text"):
    #         element = self.driver.find_element_by_link_text(value)
    #         return element
    #     else:
    #         print("无对应方法，请检查")
    #         return None

    def bbs_login(self):
        self.find_element(*self.bbs_login_button_loc).click()
        #self.find_element(*self.bbs_login_user_loc).click()
        # 获取登录头像，获取后移动到弹窗，然后点击登录
        # above = self.find_element(*self.bbs_my_link_loc)
        # ActionChains(self.driver).move_to_element(above).perform()
        # element = self.find_element(*self.bbs_login_button_loc)
        # print("---------找到登录按钮----------" + element.get_attribute(id))
        # self.find_element(*self.bbs_my_link_loc).click()

        # //*[@id="loginLink"]
        # self.hover(by='XPATH', value='//*[@id="loginLink"]')
        # loginbutton = self.driver.findElement(by='XPATH', value='//*[@id="loginLink"]')
        # print("---------loginbutton----------" + loginbutton)
        #
        # if loginbutton != None:
        #     self.assertEqual(1, 1)
        # else:
        #     self.assertEqual(1, 0)
        #     time.sleep(3)

    # login_username_loc = (By.CSS_SELECTOR,"ipt-account inp-focus")
    # login_password_loc = (By.CSS_SELECTOR,"inp-focus")
    # login_button_loc = (By.CLASS_NAME,"tipInfo")

    login_username_loc = (By.XPATH, '//*[@id="Email"]')
    login_password_loc = (By.XPATH, '//*[@id="Password"]')
    # /html/body/div/div[3]/div/div/div/div/div/div[1]/form/div[5]/button
    login_button_loc = (By.XPATH, "/html/body/div/div[3]/div/div/div/div/div/div[1]/form/div[5]/button")

    #登陆用户名

    def login_username(self,username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录密码

    def login_password(self,password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)


    #登录按钮

    def login_botton(self):
        self.find_element(*self.login_button_loc).click()


    #定义统一的登录入口

    def user_login(self,username="username",password="1111"):
        """获取的用户名登录"""
        self.open()
        print("---------base open验证完毕----------" )
        self.bbs_login()
        print("---------bbs login验证完毕----------" )
        self.login_username(username)
        print("---------用户名 验证完毕----------" )
        self.login_password(password)
        print("---------密码 验证完毕----------" )
        self.login_botton()
        print("---------点击登录按钮 验证完毕----------" )
        sleep(3)

    # #登录断言
    # username_erro_loc = (By.XPATH,"//span[@for='account']")
    # password_erro_loc = (By.XPATH,"//span[@for='password']")
    user_login_sucess_loc = (By.XPATH, "/html/body/div/div[2]/div/div/div/div[1]/div/a[1]")
    #
    # #用户名错误
    # def username_erro(self):
    #     return self.find_element(*self.username_erro_loc).text
    #
    # #密码错误
    # def password_erro(self):
    #     return self.find_element(*self.password_erro_loc).text
    #
    #登录成功
    # def user_login_success(self):
    #     return self.find_element(*self.user_login_sucess_loc).text















