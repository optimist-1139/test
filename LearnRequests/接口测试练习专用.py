import pytest
import requests
from lxml import etree
# class register:
#     proxy = {
#         "http":"http://127.0.0.1:8888",
#         "https":"https://127.0.0.1:8888",
#     }
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
# # print(r.text)
#     def info(self,mobilephone,pwd,regname):
#         self.mobilephone = mobilephone
#         self.pwd = pwd
#         self.regname = regname

        # r = requests.post(url,data = canshu,proxies = proxy)

# canshu = {"mobilephone":"17623462153","pwd":"147298870","regname":"星空1"}

@pytest.fixture(params=[{'casedata': {'mobilephone': '18586820529', 'pwd': '123456', 'regname': 'cxm'},
                         'expect': {"status": 0, "code": "20110", "data": None, "msg": "手机号码已被注册"}},
                        {'casedata': {'mobilephone': '133', 'pwd': '123456', 'regname': 'cxm'},
                         'expect': {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}},
                        {'casedata': {'mobilephone': '1333333333333333333333', 'pwd': '123456', 'regname': 'cxm'},
                         'expect': {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}},
                        {'casedata': {'mobilephone': '13315016469', 'pwd': '12345', 'regname': 'cxm'},
                         'expect': {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
                        {'casedata': {'mobilephone': '13315016469', 'pwd': '1234511111111111111', 'regname': 'cxm'},
                         'expect': {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
                        {'casedata': {'mobilephone': '', 'pwd': '12345', 'regname': 'cxm'},
                         'expect': {"status": 0, "code": "20103", "data": None, "msg": "手机号不能为空"}},
                        {'casedata': {'mobilephone': '13315016469', 'pwd': '', 'regname': 'cxm'},
                         'expect': {"status": 0, "code": "20103", "data": None, "msg": "密码不能为空"}},
                        {'casedata': {'mobilephone': '13315016469', 'pwd': '123456', 'regname': ''},
                         'expect': {"status": 0, "code": "20110", "data": None, "msg": "手机号码已被注册"}},
                        {'casedata': {'mobilephone': '15127025432', 'pwd': '123456', 'regname': 'cxm'},
                         'expect': {"status": 1, "code": "10001", "data": None, "msg": "注册成功"}}])
def register(request):
    return request.param

def login():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url,data = register)
    assert r.json()['status_code'] == register.expect['code']
    assert r.json()['msg'] == register.expect['msg']





