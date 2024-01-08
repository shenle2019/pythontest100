import requests

url = 'http://www.cpta.com.cn/'

# User-Agent:请求载体（浏览器，爬虫程序）的身份表示
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
# 伪装了浏览器的请求头
response = requests.get(url=url, headers=header)

page_text = response.text

with open('kaoshi.html', 'w') as fp:
    fp.write(page_text)