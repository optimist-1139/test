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


# 阶梯式加压的模型
class StepLoadShape(LoadTestShape):
    '''
      逐步加载实例

      参数解析：
          step_time -- 逐步加载时间
          step_load -- 用户每一步增加的量
          spawn_rate -- 用户在每一步的停止/启动
          time_limit -- 时间限制

      '''

    step_time = 30 #两个阶梯之间的时间
    step_load = 10  #每个阶梯增加的用户数
    spawn_rate = 10 #用户上线的速率
    time_limit = 600 #测试的时长

    def tick(self):  #控制执行时的用户数以及速率
        run_time = self.get_run_time()  #性能测试启动多长时间了，也就是运行多长时间了
        if run_time > self.time_limit:  #如果
            return None

        current_step = math.floor(run_time / self.step_time) + 1
        return (current_step * self.step_load, self.spawn_rate)



# -f 要执行的文件
# --host 被测系统
# --web-host locust web 页面的访问地址
# --web-port locust web 页面的访问端口
# 下面这句在下方Terminal中去执行
# locust -f locust_test.py --host=http://127.0.0.1:8089 --web-host=http://127.0.0.1 --web-port=8088
# locust -f locust\locust_test.py