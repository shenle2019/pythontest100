import requests

url = 'https://www.eastmoney.com/'
response = requests.get(url = url)
response.encoding = 'utf-8'
page_text = response.text

with open('dongfang.html','w') as fp:
    fp.write(page_text)


