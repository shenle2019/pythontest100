# coding:utf-8
from selenium import webdriver
import sys
import os

#截屏
def insert_img(driver,file_name):
	base_dir = os.path.dirname(os.path.dirname(__file__))
	#base_dir = str(base_dir)
	base_dir = base_dir.replace("\\","/")
	base_dir = base_dir.split('/test_case')[0]
	file_path = base_dir + "/report/image/" + file_name
	driver.get_screenshot_as_file(file_path)
	
# #获取最新的测试报告，用于发送测试报告邮件
# def new_report(file_path):
# 	files = os.listdir(file_path)
# 	f_times = []
# 	for f in files:
# 		if os.path.splitext(file_path + f)[1] == '.html':
# 			f_time = os.path.getmtime(file_path + f)
# 			f_times.append((f_time, f))
#
# 	return sorted(f_times)[-1][1]

	
if __name__ == '__main__':
	sys.path.append("D:\pythontest\mztestpro\mztestpro-master\bbs\test_case\models")
	print(sys.path)
	import driver
	driver = driver.browser()
	driver.get("http://www.baidu.com")
	insert_img(driver,"baidu.png")
	driver.quit()