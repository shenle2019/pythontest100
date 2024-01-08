# 方式1：
import requests

url = 'https://img0.baidu.com/it/u=540025525,3089532369&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500'
response = requests.get(url=url)
img_data = response.content
# content获取二进制形式的响应数据
with open('1.jpg', 'wb') as fp:
    fp.write(img_data)