'''
cookie
接口测试时，如果开发没有提供文档时，如果界面已经有一些功能，可以通过抓包的方式去抓接口
'''

import requests
# head = {
#     "Cookie": '__asc=be069a341759c98d8d9a132f1db; __auc=be069a341759c98d8d9a132f1db; MEIQIA_TRACK_ID=1juNb3PBC22M8zeuBr9sV5MTOoH; MEIQIA_VISIT_ID=1juNb3CQERJT3h4WgKLssnnC4AN; _ga=GA1.2.403868535.1604650114; _gid=GA1.2.1924858226.1604650114; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1604650063,1604650943; BAGSESSIONID=b3f39f18-c5dd-4261-b6d0-5bf9ce894f65; JSESSIONID=A743C394172C8C89F417175806215772; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1604651155'
# }
# r = requests.get("https://www.bagevent.com/account/dashboard",headers = head)
# print(r.text)
#没登陆时，title显示为<title></title>
#登录后，title显示为<title>百格活动-账户总览</title>


'''
requests中自动管理cookies的机制
'''
s = requests.session() #创建了一个session,通过session发送请求
# print("登录之前的cookies",s.cookies)
canshu = {#从Fiddler里面拷贝，然后修改成这样的格式，删掉一部分
        "access_type":1,
        "loginType":1,
        "emailLoginWay":0,
        "account":"147298870@qq.com",
        "password":"xingkong",
        "remindmeBox":"on",
        "remindme":1
}
# 登录
r = s.post("https://www.bagevent.com/user/login",data= canshu)
# print("登录之后的cookies",s.cookies)
# print(r.text)
# 调用dashboard的接口
r = s.get("https://www.bagevent.com/account/dashboard")
# print(r.text)
print("<title>百格活动 - 账户总览</title>" in r.text)



#练习：查看某个调查的详细信息
#

#获取活动列表
r = s.get("https://www.bagevent.com/account/myevents?published=1")
