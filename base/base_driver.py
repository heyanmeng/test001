from appium import webdriver

def init_driver():
    # server启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.68.56.101:5555'
    # app信息，设置
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    # 解决中文不能输出
    desired_caps['unicodekeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 实例化webdriver对象并传入appium和设备信息
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver