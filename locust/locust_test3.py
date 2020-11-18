'''
任务集合；分层的方式，按模块或者子系统来管理
'''
from locust import TaskSet, HttpUser, between
from locust.user import task



class SystemManage(TaskSet):
    @task
    def task1(self):
        self.client.get("/carRental/sys/toUserManager.action")


    @task
    def task2(self):
        self.client.get("/carRental/sys/toRoleManager.action")

    @task
    def task3(self):
        self.client.get("/carRental/sys/toLogInfoManager.action")

# 基础管理模块
class BasicManage(TaskSet):
    @task(7) #权重也可以在这里加，表示比task2这个模块访问频率更高7倍。如果不写，默认是1
    def task1(self):
        self.client.get("/carRental/bus/toCustomerManager.action")

    @task(3)
    def task2(self):
        self.client.get("/carRental/bus/toCarManager.action")


class CarRentalTest(HttpUser):
    wait_time = between(1,3)# 任务之间的间隔时间
    tasks = [BasicManage,SystemManage]  # 任务集合，tasks是User中定义的属性，不能写错
    # tasks = {BasicManage:4,SystemManage:1}
    # 任务集合，以字典形式表达时，后面数字表示权重，比如访问基础管理模块的人会比访问系统配置的人多3倍；
    # 或者访问基础管理模块的频率比访问系统配置的频率高3倍


    def on_start(self): # 测试前置，登录，在开始运行时每个用户调用一次
        user = {"loginname":"admin","pwd":"123456"}
        self.client.post("/carRental/login/login.action",data=user)

    def on_stop(self): # 测试后置，退出登录，在结束运行时每个用户调用一次
        self.client.post("/carRental/logout/logout.action")  # 这个是乱写的接口，因为租车系统没有完成退出接口，测试会失败
        # locust -f locust\locust_test3.py --host=http://127.0.0.1:8089 --web-host=http://127.0.0.1 --web-port=8088