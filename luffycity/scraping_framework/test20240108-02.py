import requests

game_title = input('enter a game key:')
# 字典需要存放请求携带的所有的请求参数
params = {
    'q': game_title
}  # 请求参数的数量和字典的键值对的数量保持一致

# 指定url
url = 'https://game.51.com/search/action/game/'

# 发起请求:向指定的url携带了指定的请求参数进行的请求发送
response = requests.get(url=url, params=params)

# 获取响应数据
page_text = response.text

# 持久化存储
with open('games.html', 'w') as fp:
    fp.write(page_text)