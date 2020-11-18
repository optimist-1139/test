import requests

'''
练习：查看某个调查的详细信息
登录百格网后，获取百格网活动列表
'''

s = requests.session()
canshu = {
    "access_type":1,
    "loginType":1,
    "emailLoginWay":0,
    "account":"147298870@qq.com",
    "password":"xingkong",
    "remindmeBox":"on",
    "remindme":1
}
r = s.post("https://www.bagevent.com/user/login",data=canshu)
r = s.get("https://www.bagevent.com/account/myevents?published=1")
assert r.status_code == 200
assert r.reason == 'OK'
print("<title>百格活动 - 我创建的活动</title>" in r.text)