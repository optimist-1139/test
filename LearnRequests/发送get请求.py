'''
发送get请求
'''

import requests
# 接口地址："https://www.baidu.com"
#发送一个get请求，变量r是收到的响应
r = requests.get("https://www.baidu.com")
# 打印文本格式的响应内容
# print(r.text)
# 打印响应码
# print(r.status_code)
assert r.status_code == 200#断言响应码是200
# 响应信息：OK
# print(r.reason)
assert r.reason == 'OK'#断言响应信息是OK

# 练习：返回jy金融的用户列表
# http://jy001:8081/futureloan/mvc/api/模块/接口名
#发送请求
l = requests.get("http://jy001:8081/futureloan/mvc/api/member/list")
#打印结果
l.encoding = 'utf-8'
# print(l.json())
# print(l.text)
#检查结束
assert l.status_code == 200
assert l.reason == 'OK'
assert l.json()['status'] == 1
assert l.json()['code'] == '10001'



# get 请求带参数
# 注册
# 方法1：拼接到URL后面（金融项目注册接口）
# url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=17629562345&pwd=147298870&regname='星空'"
# n = requests.get(url)
# print(n.json())
# print(n.text)
# assert n.status_code == 200
# assert n.reason == 'OK'
# assert n.json()['status'] == 1
# assert n.json()['code'] == '10001'

# 方法2：使用params传参数
# 如果用POST传参，就用data和json传参，如果用get，那就用params传参,书写方式都是一样的
# url = "http://jy001:8081/futureloan/mvc/api/member/register"#注意与方法一的路径区别
# canshu = {"mobilephone":"13924052456","pwd":"123456","regname":"小星空"}#params规定的参数是字典格式和列表格式，所以这里选择传字典格式
# n = requests.get(url,params=canshu)
# print(n.text)
# 登录
url = "http://jy001:8081/futureloan/mvc/api/member/login?mobilephone=17629562345&pwd=147298870"
d = requests.get(url)
print(d.text)
print(d.json())


#get 请求带请求头，设置User-Agent伪装成浏览器发送的请求，避免服务器屏蔽自动化发的请求
# User-Agent 包含浏览器的版本号、操作系统的版本号等信息
# url = "http://www.httpbin.org/get"#这是一个测试网站，get是接口名字，后面可以跟参数，发送的请求，原封的返回来
# r = requests.get(url)
# print(r.text)# 返回值中有一个"User-Agent": "python-requests/2.24.0", 是版本号
# tou = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
# r = requests.get(url,headers = tou)
# print(r.text)


# 从https网页抓取数据，并打印

# 设置User-Agent,模拟浏览器
tou = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
# 输入目标网址
url = "https://wenku.baidu.com/view/027d607deff9aef8941e06c0.html"
# 发送请求
r = requests.get(url,headers = tou)#headers参数调用tou，模拟浏览器
# 打印当前网页的html信息
# print(r.text)
# 判断"蜂群算法源代码"是否在html文本信息中，结果为true
print("蜂群算法源代码"in r.text)

