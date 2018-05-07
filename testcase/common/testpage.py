from testcase.common import browser


class TestPage(browser.Browser):
    def __init__(self,page =None,browser_type='chrome'):
        if page:
            self.driver = page.driver
        else:
            super(TestPage, self).__init__(browser_type=browser_type)

    def getDriver(self):
        return  self.driver

    def find_element(self,*args):
        return  self.driver.find_element(*args)


