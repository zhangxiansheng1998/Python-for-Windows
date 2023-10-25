""""
BasePage类是POM中的基类，主要用于提供常用的函数为页面对象进行服务
"""
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Basepage:

    def __init__(self, driver):
        print('程序开始')
        self.driver = driver
        self.timeformate = time.strftime("%Y-%m-%d %H-%M-%S")

    def visit(self, url):
        """访问网页"""
        try:
            self.driver.get(url)
        except Exception as e:
            print("输入的URL地址{}不正确，请重新输入".format(url))
            print("捕获的异常信息为:",e)

    def locator(self, loc):
        """定位单个元素"""
        try:
            return self.driver.find_element(*loc)
        except Exception as e:
            print("元素定位失败，捕获的异常信息为:", e)

    def locators(self, loc):
        """定位一组元素"""
        try:
            return self.driver.find_elements(*loc)
        except Exception as e:
            print("元素定位失败，捕获的异常信息为:", e)

    def input(self, loc, txt):
        """输入"""
        try:
            return self.locator(loc).send_keys(txt)
        except Exception as e:
            print("元素定位失败，捕获的异常信息为:", e)

    def click(self, loc):
        """点击某个元素"""
        try:
            return self.locator(loc).click()
        except Exception as e:
            print("元素定位失败，捕获的异常信息为:", e)

    def wait(self, seconds):
        """强制等待"""
        time.sleep(seconds)

    def implicitly_wait(self, seconds):
        """隐式等待，只需设置一次，全局有效，每隔0.5s查询一次"""
        try:
            self.driver.implicitly_wait(seconds)
        except Exception as e:
            print("超出当前最大等待时间，已报错，捕获的异常信息为:", e)

    def explicitly_wait(self, loc, seconds):
        """显式等待   loc：元素   seconds：等待时间"""
        try:
            WebDriverWait(self.driver, seconds).until(lambda x: x.find_element(*loc))
        except Exception as e:
            print("超出当前最大等待时间，已报错，捕获的异常信息为:", e)

    def max(self):
        """放大窗口"""
        self.driver.maximize_window()

    def select_all(self, loc):
        """全选"""
        try:
            self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'a')
        except Exception as e:
            print("元素定位失败，捕获的异常信息为:", e)

    def copy(self, loc):
        """复制"""
        try:
            self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'c')
        except Exception as e:
            print("元素定位失败，捕获的异常信息为:", e)

    def paste(self, loc):
        """粘贴"""
        try:
            self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'v')
        except Exception as e:
            print("元素定位失败，捕获的异常信息为:", e)

    def backspace(self, loc):
        """删除"""
        try:
            self.select_all(loc)
            self.driver.find_element(*loc).send_keys(Keys.BACKSPACE)
        except Exception as e:
            print("元素定位失败，捕获的异常信息为:", e)

    def js_scroll_bottom(self):
        """浏览器滚动到底部"""
        try:
            js = "var q=document.documentElement.scrollTop=10000"
            self.driver.execute_script(js)
        except Exception as e:
            print("js脚本执行失败，捕获的异常信息为:", e)

    def js_scroll_top(self):
        """浏览器滚动到顶部"""
        try:
            js = "var q=document.documentElement.scrollTop=0"
            self.driver.execute_script(js)
        except Exception as e:
            print("js脚本执行失败，捕获的异常信息为:", e)

    def screen(self):
        """截图"""
        try:
            self.driver.get_screenshot_as_file(u"../picture/" + self.timeformate + ".png")
        except Exception as e:
            print("截图失败，捕获的异常信息为:", e)

    def get_text(self, loc):
        """获取元素对应的文本内容(元素本身有内容)"""
        try:
            return self.locator(loc).text
        except Exception as e:
            print("元素定位失败，捕获的异常信息为:", e)

    def get_value(self, loc):
        """获取元素value属性中文本内容(元素本身没有内容，但是value值有内容)"""
        try:
            return self.locator(loc).get_attribute("value")
        except Exception as e:
            print("元素定位失败，捕获的异常信息为:", e)

    def get_list_value(self, list, value):
        """点击下拉框中某个特定的值   list：列表元素   value：具体的值"""
        try:
            for li in list:
                if value in li.text:
                    li.click()
                    break
        except Exception as e:
            print("无法选中下拉框中的{}，捕获的异常信息为:".format(value), e)

    def screen_template(self, loc):
        """定位失败时，截图并关闭浏览器"""
        self.driver.get_screenshot_as_file(u"../picture/failure/" + self.timeformate + ".png")
        print('未定位到元素:{element}, 已截图'.format(element=loc))
        self.driver.quit()

    def locator_png(self, loc):
        """定位单个元素（如果报错，会自动截图）"""
        try:
            return self.driver.find_element(*loc)
        except:
            self.screen_template(loc)

    def locators_png(self, loc):
        """定位一组元素（如果报错，会自动截图）"""
        try:
            return self.driver.find_elements(*loc)
        except:
            self.screen_template(loc)

    def click_png(self, loc):
        """点击某个元素（如果报错，会自动截图）"""
        try:
            self.locator(loc).click()
        except:
            self.screen_template(loc)

    def input_png(self, loc, txt):
        """输入内容（如果报错，会自动截图）"""
        try:
            self.locator(loc).send_keys(txt)
        except:
            self.screen_template(loc)

    def get_text_png(self, loc):
        """获取元素对应的文本内容（如果报错，会自动截图）"""
        try:
            return self.locator(loc).text
        except:
            self.screen_template(loc)

    def quit(self):
        """退出浏览器"""
        self.wait(1)
        self.driver.quit()
        print('程序结束')

    def assert_text_euqal(self,expectation,reality):
        """断言元素本身对应的文本内容   expectation：预期值   reality：实际值（传入元素）"""
        try:
            assert expectation == self.get_text(reality)
        except Exception as e:
            print("期望值'{}'与实际值'{}'不相等，断言失败!".format(expectation,self.get_text(reality)), e)

    def assert_value_euqal(self,expectation,reality):
        """断言元素value属性中的文本内容   expectation：预期值   reality：实际值（传入元素）"""
        try:
            assert expectation == self.get_value(reality)
        except Exception as e:
            print("期望值'{}'与实际值'{}'不相等，断言失败!".format(expectation,self.get_value(reality)), e)

