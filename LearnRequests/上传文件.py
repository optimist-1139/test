'''
上传文件：
一般都是post接口，用post.files参数上传文件
'''

import requests

url = "http://www.httpbin.org/post"

'''
files参数，字典的格式，'name':file-tuple
file-tuple可以是2-tuple('filename',fileobj)、3-tuple('filename',fileobj,'content_type')、4-tuple
'''
with open("D:/user.txt",encoding='utf-8') as f:#将本地文件上传到网站上，这个本地文件必须存在
    file = {"file1":("user.txt",f,"text/plain")}# MIME类型：text/plain（表示纯文本文件）; image/png 、image/gif 、 application/json
    # text/plain，二元组如果上传文本文件，可以去掉content_type,默认文件类型是文本文件。
    r = requests.post(url,files = file)
    print(r.text)
    print(r.json())
    #输出结果:"file1": "\u897f\u6e56\u7f8e\u666f\uff0c\u4e09\u6708\u5929\
    #\u897f\u6e56\这是unicode编码，网上有unicode转中文，中文转unicode的小工具，可以在线转


# 上传一张png格式的图片，大小为60k，越大越耗时间
# with open("C:/Users/Administrator/Desktop/接口测试/13.png",mode='rb') as e:#上传图片，音频文件时，需要修改为二进制，才能上传，也就是mode='rb'
    # png = {"file2":("13.png",e,"image/png")}
    # r = requests.post(url,files = png)
    # print(r.text)

# 一次上传多个文件
# 因为是key:value的字典形式，所以可以一次上传多个文件
# 写法一：
g = {"file3":[("filen1",open("D:/user.txt"),"text/plain"),("filen2",open("C:/Users/Administrator/Desktop/接口测试/13.png","rb",),"image/png")]}
z = requests.post(url,g)
print(z.text)
# 写法二
# with open("D:/user.txt",encoding='utf-8') as f1:
#     with open("C:/Users/Administrator/Desktop/接口测试/13.png",mode = 'rb')as f2:
#         file = {
#             "file1":("text.txt",f1),
#             "file2":("13.png",f2,"image/png")
#         }
#         r = requests.post(url,files = file)
#         print(r.text)

