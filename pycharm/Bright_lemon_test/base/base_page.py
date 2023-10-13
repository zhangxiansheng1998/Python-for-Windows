""""
BasePage类是POM中的基类，主要用于提供常用的函数为页面对象进行服务
"""
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class Basepage:

    def __init__(self, driver):
        self.driver = driver
        self.timeformate = time.strftime("%Y-%m-%d %H-%M-%S")

    # 访问url
    def visit(self, url):
        self.driver.get(url)

    # 定位元素
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 定位一组元素
    def locators(self, loc):
        return self.driver.find_elements(*loc)

    # 输入
    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击某个元素
    def click(self, loc):
        self.locator(loc).click()

    # 强制等待
    def wait(self, seconds):
        time.sleep(seconds)

    # 隐式等待
    def implicitly_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    # 显式等待
    def explicitly_wait(self, loc, seconds):
        WebDriverWait(self.driver, seconds).until(lambda x: x.find_element(*loc))

    # 放大窗口
    def max(self):
        self.driver.maximize_window()

    # 全选
    def select_all(self, loc):
        self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'a')

    # 复制
    def copy(self, loc):
        self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'c')

    # 粘贴
    def paste(self, loc):
        self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'v')

    # 删除
    def backspace(self, loc):
        self.select_all(loc)
        self.driver.find_element(*loc).send_keys(Keys.BACKSPACE)

    # 滚动到底部
    def js_scroll_bottom(self):
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)

    # 滚动到顶部
    def js_scroll_top(self):
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)

    # 截图
    def screen(self):
        self.driver.get_screenshot_as_file(u"../picture/" + self.timeformate + ".png")

    # 获取元素对应的文本内容
    def get_text(self, loc):
        return self.locator(loc).text

    # 点击下拉框中包含特定的值
    def get_list_value(self, list, value):
        for li in list:
            if value in li.text:
                li.click()
                break

    # 元素定位失败后，截图的通用模板
    def screen_template(self,loc):
        self.driver.get_screenshot_as_file(u"../picture/failure/" + self.timeformate + ".png")
        print('未定位到元素:{element}, 已截图'.format(element=loc))
        self.driver.quit()

    # 定位单个元素（含截图）
    def locator_png(self, loc):
        try:
            return self.driver.find_element(*loc)
        except:
            self.screen_template(loc)

    # 定位一组元素（含截图）
    def locators_png(self, loc):
        try:
            return self.driver.find_elements(*loc)
        except:
            self.screen_template(loc)

    # 点击某个元素（含截图）
    def click_png(self, loc):
        try:
            self.locator(loc).click()
        except:
            self.screen_template(loc)

    # 输入（含截图）
    def input_png(self, loc, txt):
        try:
            self.locator(loc).send_keys(txt)
        except:
            self.screen_template(loc)

    # 获取元素对应的文本内容（含截图）
    def get_text_png(self, loc):
        try:
            return self.locator(loc).text
        except:
            self.screen_template(loc)



