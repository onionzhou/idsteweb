from  selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import os
from utils.config import DRIVER_PATH,REPORT_PATH
import time
#browser drive
CHROMEDRIVER_PATH =DRIVER_PATH + '\chromedriver.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'
FIREFOXDRIVER_PATH = DRIVER_PATH +'\geckodriver.exe'

TYPES ={'chrome':webdriver.Chrome,
        'firefox':webdriver.Firefox,
        'phantomjs':webdriver.PhantomJS,
        }
EXE_PATH ={'chrome':CHROMEDRIVER_PATH,
           'phantomjs':PHANTOMJSDRIVER_PATH,
           'firefox':FIREFOXDRIVER_PATH,
           }

class UnsupprtBrowerTypeError(Exception):
    pass

class Browser(object):
    def __init__(self,browser_type='chrome'):
        self._type =browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnsupprtBrowerTypeError('only support [ %s' % ', '.join(TYPES.keys()), ']')
        self.driver = None

    def get(self,url,maximize_window =True,time_to_implicitly_wait =5):
        self.driver = self.browser(executable_path=EXE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        #这里可以增加显示等待功能，以后补充
        self.driver.implicitly_wait(time_to_implicitly_wait)
        return self

    def wait(self,time):
        return WebDriverWait(self.driver,time)

    def save_screen_shot(self, name ='screen_xx'):
        day =time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH +'\screenshot_%s' %day
        #file_name = '%s_%s' %(screen_name,screen_time)
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)
        tm = time.strftime('%H-%M-%S', time.localtime(time.time()))  # '%H:%M:%s' 有问题
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()

if __name__ == '__main__':
    b = Browser(browser_type='chrome').get('http://192.168.1.113')
    b.save_screen_shot()
    time.sleep(3)
    b.quit()