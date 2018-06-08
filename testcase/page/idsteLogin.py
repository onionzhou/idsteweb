from selenium.webdriver.common.by import By
from testcase.common import browser
from testcase.common.locators import LoginPageLocators
from selenium.webdriver.support.wait import WebDriverWait


class IDsteWebLogin(browser.Browser,):
    # phone_input = (By.CLASS_NAME,'el-input__inner')
    # login_button = (By.CLASS_NAME,'login-btn')
    def __init__(self,page=None,browser_type='chrome'):
        if page:
            self.driver = page.driver
        else:
            self.driver = super(IDsteWebLogin, self).__init__(browser_type=browser_type)
    def login(self,user,passwd):
        # WebDriverWait(self.driver,2).until(lambda test: test.find_element(*LoginPageLocators.login_button))
        self.wait(2).until(lambda test: test.find_element(*LoginPageLocators.login_button))
        t = self.driver.find_elements(*LoginPageLocators.input)
        t[0].clear()
        t[1].clear()
        t[0].send_keys(user)  # 账号
        t[1].send_keys(passwd)  # 密码
        self.driver.find_element(*LoginPageLocators.login_button).click()
    def err_message(self):
        self.wait(4).until(lambda test: test.find_element(*LoginPageLocators.login_error))
        return self.driver.find_element(*LoginPageLocators.login_error).text
    def err_message_disappear(self):
        self.wait(2).until_not(lambda test: test.find_element(*LoginPageLocators.login_error))

if __name__ =='__main__':
    pass
