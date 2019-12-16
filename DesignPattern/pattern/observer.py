import time
from abc import ABCMeta, abstractmethod


#####################################
#  生活实例:热水器


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, subject, *args):
        pass


class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, *args):
        for observer in self._observers:
            observer.update(self, *args)


class WaterHeater(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 25

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, temperature):
        self._temperature = temperature
        print("当前温度：" + str(self._temperature) + "摄氏度")
        self.notify_observers()


class WashingMode(Observer):

    def update(self, subject, *args):
        if isinstance(subject, WaterHeater) \
                and 50 <= subject.get_temperature() < 70:
            print("水已烧好！温度正好，可以用来洗澡了。")


class DrinkingMode(Observer):

    def update(self, subject, *args):
        if isinstance(subject, WaterHeater) and subject.get_temperature() >= 100:
            print("水已烧开！可以用来饮用了。")


def testWaterHeate():
    heater = WaterHeater()
    heater.add_observer(WashingMode())
    heater.add_observer(DrinkingMode())
    heater.set_temperature(40)
    heater.set_temperature(60)
    heater.set_temperature(100)



################################
# 异常登陆

class Account(Subject):
    def __init__(self):
        super().__init__()
        self._latest_ip = {}
        self._latest_region = {}

    def login(self, name, ip, time):
        region = self._get_region(ip)
        if self._is_long_distance(name, region):
            self.notify_observers({"name": name, "ip": ip, "region": region, "time": time})
        self._latest_ip[name] = ip
        self._latest_region[name] = region

    def _get_region(self, ip):
        ip_regions = {
            "101.47.18.9": "浙江省杭州市",
            "67.218.147.69": "美国洛杉矶"
        }
        region = ip_regions.get(ip, "")
        return  region

    def _is_long_distance(self, name, region):
        latest_region = self._latest_region.get(name)
        return  latest_region and latest_region != region


class SmsSender(Observer):


    def update(self, subject, object):
        print("[短信发送] " + object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "登录地区：" + object["region"] + "  登录ip：" + object["ip"] + "  登录时间："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


class MailSender(Observer):
    def update(self, observable, object):
        print("[邮件发送] " + object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "登录地区：" + object["region"] + "  登录ip：" + object["ip"] + "  登录时间："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


def test_login():
    accout = Account()
    accout.add_observer(SmsSender())
    accout.add_observer(MailSender())
    accout.login("Mr_Menand", "101.47.18.9", time.time())
    accout.login("Mr_Menand", "67.218.147.69", time.time())








