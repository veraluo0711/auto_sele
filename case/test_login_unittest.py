import os
import unittest

import ddt
from pages.login_page import Login,login_url
from selenium import webdriver

from common.readexcel import ExcelUtil

curpath = os.path.dirname(os.path.realpath(__file__))

#os去获取文件logindata.xlsx的路径,
filepath = os.path.join(curpath,"logindata.xlsx")
#xls的路径写死："D:\\test1\\Test\\common\\logindata.xlsx"

print("logindata的路径%s" % filepath)

data = ExcelUtil(filepath, "Sheet1")
test_datas = data.dict_data()
print(test_datas)

'''
test_datas = [
    {"user": "testvera1", "psw": "123456", "expect": True},
    {"user": "testvera1333", "psw": "123456", "expect": False},
    {"user": "222", "psw": "123456", "expect": False},
    {"user": "testvera1", "psw": "123456", "expect": True},
]
'''

#AttributeError: 'TestLoader' object has no attribute 'makeTest' 鼠标没放到if下运行

@ddt.ddt
class TestLogin(unittest.TestCase):
    """测试注册/登录功能"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(login_url)
        self.a = Login(self.driver)

    def tearDown(self):
        self.driver.quit()

    @ddt.data(*test_datas)

    def test_login(self, data):
        """测试数据-成功 testvera1，123456"""
        print("测试数据：%s" % data)

        self.a.login(data["user"], data["psw"])
        result = self.a.is_login_success("登录成功")
        print("登录的实际结果： %s" % result)
        self.assertTrue(result == data["expect"])

    # def test_login_fail(self):
    #    """测试数据-登录失败 testxx111,123456"""
    #    self.a.login("testxx111", "123456")
    #    result = self.a.is_login_success("登录成功")
    #    print("登录的实际结果： %s" % result)
    #    self.assertFalse(result)




if __name__ == '__main__':
    unittest.main()
