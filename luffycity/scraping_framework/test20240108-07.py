from urllib.request import urlretrieve
#图片地址
img_url = 'https://img0.baidu.com/it/u=4271728134,3217174685&fm=253&fmt=auto&app=138&f=JPEG?w=400&h=500'
#参数1：图片地址
#参数2：图片存储路径
#urlretrieve可以根据图片地址将图片数据请求到直接存储到参数2表示的图片存储路径中
urlretrieve(img_url,'2.jpg')