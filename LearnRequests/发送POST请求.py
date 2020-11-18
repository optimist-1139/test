'''
发送POST请求
1.使用data传表单格式的参数
2.使用json传json格式的参数
3.post也可以带请求头，使用headers参数
'''
import requests
#金融项目案例
#发送POST请求，如果带参数，可以用data或json传参，具体使用那个要看系统怎么实现的，支持谁就用谁
# 用上一步注册成功的手机号：验证登录，登录使用post

url = "http://jy001:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone":"17629562345","pwd":"147298870"}
r = requests.post(url,data=canshu)#系统支持data传参，所以登录成功
print (r.text)
r = requests.post(url,json=canshu)#金融系统不支持json方式传参
print(r.text)

#通过发送请求到httpbin，来观察data和json的区别
# r = requests.post("http://www.httpbin.org/post",data=canshu)#"Content-Type": "application/x-www-form-urlencoded",data传参是以表单格式传参
# print(r.text)
# r = requests.post("http://www.httpbin.org/post",json=canshu)#"Content-Type": "application/json"，json传参是以json格式传参
# print(r.text)


# post带请求头headers参数
tou = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
url = "http://jy001:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone":"17629562345","pwd":"147298870"}
r = requests.post(url,data= canshu,headers = tou)#headers参数调用tou，模拟浏览器
print(r.text)

