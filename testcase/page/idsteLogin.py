from selenium.webdriver.common.by import By

from testcase.common.testpage import TestPage


class IDsteWebLogin(TestPage):
    phone_input = (By.CLASS_NAME,'el-input__inner')
    login_button = (By.CLASS_NAME,'login-btn')

    def login(self,number):
        self.find_element(*self.phone_input).send_keys(str(number))
        self.find_element(*self.login_button).click()