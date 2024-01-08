import requests

url = 'http://www.cpta.com.cn/category/search'
param = {
    "keywords": "人力资源",
    "搜 索": "搜 索"
}
header = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
# 发起了post请求：通过data参数携带了请求参数
response = requests.post(url=url, data=param, headers=header)
page_text = response.text

with open('renshi.html', 'w') as fp:
    fp.write(page_text)