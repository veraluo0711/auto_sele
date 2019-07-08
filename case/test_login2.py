import unittest
from selenium import webdriver
import time

class TestProjectForgetPsw(unittest.TestCase):
    """测试忘记/找回密码功能"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://47.104.190.48:8000/login/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_forget_psw(self):
        """忘记密码"""
        self.driver.find_element_by_xpath(".//*[text()='忘记密码?']").click()
        body = self.driver.find_element_by_tag_name("body").text
        print("body的全部文本：%s"%str(body))
        self.assertTrue("忘记密码，找回密码" in body)

    def test_psw_retrieve_fail(self):
        """密码找回失败"""
        self.driver.find_element_by_xpath(".//*[text()='忘记密码?']").click()
        self.driver.find_element_by_css_selector('#id_user').send_keys("veratest1")
        self.driver.find_element_by_css_selector('#id_mail').send_keys("1@1.com")
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
        body = self.driver.find_element_by_tag_name("body").text
        print("body的全部文本：%s"%str(body))
        self.assertTrue("请用注册邮箱找回！" in body)

if __name__ == '__main__':
    unittest.main()