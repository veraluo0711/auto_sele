import unittest
from selenium import webdriver
import time

class TestProjectLogin(unittest.TestCase):
    """测试注册/登录功能"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://47.104.190.48:8000/login/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        """注册成功"""
        self.driver.find_element_by_link_text("新用户先注册").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='id_username']").send_keys("veratest1")
        self.driver.find_element_by_xpath(".//*[@id='id_password']").send_keys("123456")
        self.driver.find_element_by_xpath(".//*[@name='email']").send_keys("abc123@163.com")
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
        time.sleep(2)
        t2 = self.driver.find_element_by_xpath(".//div/a").text
        print(t2)
        self.assertTrue(t2 == '我已注册，去登录！')




    def test_login_success(self):
        """登录成功"""
        self.driver.find_element_by_xpath(".//*[@id='id_username']").send_keys("veratest1")
        self.driver.find_element_by_xpath(".//*[@id='id_password']").send_keys("123456")
        self.driver.find_element_by_xpath(".//*[@value='确定']").click()

        t = self.driver.find_element_by_xpath('.//div/h1').text
        print("获取的实际结果：%s"%t)
        self.assertTrue(t == "登录成功！")



    def test_login_fail(self):
        """登录失败"""
        self.driver.find_element_by_xpath(".//*[@id='id_username']").send_keys("veratesttt")
        self.driver.find_element_by_xpath(".//*[@id='id_password']").send_keys("123456")
        self.driver.find_element_by_xpath(".//*[@value='确定']").click()
        t3 = self.driver.find_element_by_xpath('/html/body/div/form/p[3]').text
        print("获取实际结果：%s"%t3)
        self.assertTrue(t3 == "账号或密码错误！")

if __name__ == '__main__':
    unittest.main()




