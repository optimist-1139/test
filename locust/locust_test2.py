'''
性能测试
'''
import math

from locust import HttpUser, between, task, LoadTestShape

'''
1.为要模拟的用户定义一个类，从HttpUser继承。
'''
class CarRental(HttpUser):
    # between 是User类中定义的一个方法
    # wait_time是User类定义的一个属性，表示等待时间
    wait_time = between(3,8)   # 任务跟任务之间的等待时间在3~8秒之间取随机数

    @task
    def carManage(self):
        #
        self.client.get("/carRental/rent/loadAllRent.action?page=1&limit=10")

    @task
    def loadAllMenu(self):
        self.client.get("/carRental/menu/loadAllMenu.action?page=1&limit=10")


# 基于时间阶段的测试模型
class StagesShape(LoadTestShape):
    '''
    在不同的阶段 具有不同的用户数和 产生率的 图形形状


    参数解析:
        stages ：字典列表，每个字典都具有下列这些键值的阶段:
            duration -- 持续时间，  经过多少秒后，进入到下个阶段
            users -- 总用户数
            spawn_rate -- 产生率，即每秒启动/停止的用户数
            stop -- 可以在特定阶段停止测试的值
        stop_at_end -- 可以在所有阶段设置运行后停止

    '''

    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 10},
        {"duration": 100, "users": 50, "spawn_rate": 10},
        {"duration": 180, "users": 100, "spawn_rate": 10},
        {"duration": 220, "users": 30, "spawn_rate": 10},
        {"duration": 230, "users": 10, "spawn_rate": 10},
        {"duration": 240, "users": 1, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None


# -f 要执行的文件
# --host 被测系统
# --web-host locust web 页面的访问地址
# --web-port locust web 页面的访问端口
# 下面这句在下方Terminal中去执行
# locust -f locust_test.py --host=http://127.0.0.1:8089 --web-host=http://127.0.0.1 --web-port=8088
# locust -f locust\locust_test2.py