import time
import unittest
import pytest
from Zhujia_Factory.page_object.login_page import Loginpage
from Zhujia_Factory.base.browser import *
from Zhujia_Factory.config.myddt import ddt,file_data

@ddt
class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        print('程序开始')
        cls.driver = webdriver.Chrome(options=Browser().browser_ui())             # 带UI界面启动
        #cls.driver=webdriver.Chrome(options=Browser().browser_headless())      # 无头模式启动
        cls.loginpage = Loginpage(cls.driver)


    @classmethod
    def tearDownClass(cls):
        print("\n")
        print('程序结束')
        cls.driver.quit()

    #@unittest.skip('unittest不执行这条测试用例')
    @file_data('../data/login_page_data.yaml')
    def test1_login(self,username,password):
        self.loginpage.login(username,password)
        time.sleep(3)


if __name__ == '__main__':
    pytest.main(['-s','test_case.py'])





