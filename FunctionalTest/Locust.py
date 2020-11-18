'''
练习locust使用方法
'''
import math

from locust import HttpUser, between, LoadTestShape, constant

'''
为要模拟的用户定义一个类，从HttpUser继承
'''

class CarRental(HttpUser):
    wait_time = between(3,10)


    def on_start(self):
        user = {"loginname":"admin","pwd":"123456"}
        self.client.post("/carRental/login/login.action",data=user)

    def on_stop(self):
        self.client.post("/carRental/login/getCode.action")



class DoubleWave(LoadTestShape):
    '''
    自定义一个双波形图形，
    模拟在某两个时间点的最高值


    参数解析:
        min_users ： 最小用户数
        peak_one_users ： 用户在第一个峰值
        peak_two_users ： 用户在第二个峰值
        time_limit ： 测试执行总时间


    '''

    min_users = 20
    peak_one_users = 60
    peak_two_users = 40
    time_limit = 600

    def tick(self):
        run_time = round(self.get_run_time())

        if run_time < self.time_limit:
            user_count = (
                (self.peak_one_users - self.min_users)
                * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 5) ** 2)
                + (self.peak_two_users - self.min_users)
                * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 10) ** 2)
                + self.min_users
            )
            return (round(user_count), round(user_count))
        else:
            return None

# locust -f FunctionalTest\Locust.py