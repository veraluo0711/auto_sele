from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#as 后自定义缩写名



class Base():
    def __init__(self, driver:webdriver.Firefox):
        # 括号里driver冒号这一串是为了在这里可以调用driver.find等函数（可以自动匹配出），否则没有
        #self.driver = webdriver.Firefox()
        self.driver = driver
        self.driver.maximize_window() #窗口最大化
        #self.driver.get("http://47.104.190.48:8000/xadmin/")


    def find(self, locator=("id", "xxx")):
        '''locator = ("id", "kw")'''
        ele = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*locator))
        return ele

    def findx(self, locator):
        ele = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(locator))
        #判断元素是否被定位到了,这里的locator本身就是个元组类型，所以不用加*号
        return ele


    def finds(self, locator):
        eles = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_elements(*locator))
        return eles

    def send(self, locator, text):
        ele = self.find(locator)
        ele.send_keys(text)

    def click(self, locator):
        self.find(locator).click()

    def clear(self, locator):
        self.find(locator).clear()

    def get_text(self, locator):
        ele = self.find(locator)
        return ele.text

    def is_element_exist(self,locator):
        try:
            self.find(locator)
            print("找到元素了")
            return True
        except:
            print("找不到元素")
            return False

    def text_in_element(self, locator, _text):
        '''判断元素text属性'''
        try:
            r = WebDriverWait(self.driver, 30, 1).until(EC.text_to_be_present_in_element(locator, _text))
            return r
        except:
            return False


    def value_in_element(self, locator, _text):
        '''判断元素value属性，有些页面上显示的文本如百度一下按钮，并不是text，而是value值'''
        try:
            r = WebDriverWait(self.driver, 30, 1).until(EC.text_to_be_present_in_element_value(locator, _text))
            return r
        except:
            return False

    def get_text(self, locator):
        '''获取元素文本值'''
        try:
            t = self.find(locator).text
        except:
            t = ""
        return t

    def move_to_element(self, locator):
        '''鼠标悬停'''
        element = self.find(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def select_by_index(self, locator, index=0):
        '''select下拉框，index索引'''
        element = self.find(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        '''select下拉框，value'''
        element = self.find(locator)
        Select(element).select_by_value(value)

    def select_by_visible_text(self, locator, _text):
        '''select下拉框，文本定位'''
        element = self.find(locator)
        Select(element).select_by_visible_text(_text)

    def is_alert(self, timeout=3):
        '''
        判断是否有alert，没有返回false，有返回！alert对象！'''
        try:
            alert = WebDriverWait(self.driver, timeout, 1).until(EC.alert_is_present())
            #判断alert是否存在，alert不需要locator定位
            return alert
        except:
            return False

    def js_focus_element(self, locator):
        '''聚焦元素'''
        target = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView()")

    def js_scroll_up(self, locator):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''
        js = (0, "document.body.scrollHeight")
        self.driver.execute_script(js)



if __name__ == '__main__':

    driver = webdriver.Firefox()
    driver.get("http://47.104.190.48:8000/xadmin/")

    # 定位元素 统一管理
    loc1 = ("id", "id_username")
    loc2 = ("id", "id_password")
    loc3 = ("xpath", ".//*[text()='登录']")
    login_xpath = ("xpath", "//*[@id='top-nav']/div[2]/ul/li[2]/a/strong")
    loc4 = ("xpath", ".//*[@class='active']")

    b = Base(driver)  #实例化
    b.send(loc1, "veratest1")
    b.send(loc2, "123456")
    b.click(loc3)
    t = b.get_text(login_xpath)
    print(t)
    assert t == "欢迎， veratest1"


