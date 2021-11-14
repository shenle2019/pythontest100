# coding:utf-8
# from selenium.webdriver import Remote
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#启动浏览器
def browser():
    option = webdriver.ChromeOptions()  # 加载浏览器配置
    option.add_argument('disable-infobars')  # 浏览器不显示受自动测试软件控制
    option.add_argument('-kiosk')

    driver = webdriver.Chrome(chrome_options=option)
    # host = "127.0.0.1:4444"
    # dc = {'browserName':'chrome'}
    # driver = Remote(command_executor ='http://' + host + '/wd/hub' ,desired_capabilities=dc)

    # 本地启动一个主hub和一个node节点（主机端口4444，node节点5555）的方法,本机ip172.16.10.66
    # java -jar selenium-server-standalone-2.48.2.jar -role hub
    # java -jar selenium-server-standalone-2.48.2.jar -role node port 5555
    # 启动一个远程node ，如172.16.10.34:6666
    # java -jar selenium-server-standalone-2.48.2.jar -role node port 6666 -hub http://172.16.10.66:4444/grid/register
    return driver


if __name__ == "__main__":
    print(__file__)
    dr = browser()
    dr.get("http://www.baidu.com")
    dr.quit()
