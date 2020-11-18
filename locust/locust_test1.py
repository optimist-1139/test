'''
性能测试
'''
import math

from locust import HttpUser, between, task, LoadTestShape, TaskSet, constant

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

class UserTasks(TaskSet):
    @task
    def get_root(self):
        self.client.get("/")


class WebsiteUser(HttpUser):
    wait_time = constant(0.5)
    tasks = [UserTasks]

# 双波形测试模型
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




# -f 要执行的文件
# --host 被测系统
# --web-host locust web 页面的访问地址
# --web-port locust web 页面的访问端口
# 下面这句在下方Terminal中去执行
# locust -f locust_test1.py --host=http://127.0.0.1:8089 --web-host=http://127.0.0.1 --web-port=8088
# locust -f locust\locust_test1.py