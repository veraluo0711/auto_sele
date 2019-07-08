import time
import unittest

from pages.login_page import Login, login_url #写在最外层的参数也可以直接导入
from selenium import webdriver

from pages.add_student_info_page import AddStudentInfo, home_url


class TestAddStudentInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(login_url)
        #先登录
        a = Login(cls.driver)  #起始位置
        a.login()
        cls.student = AddStudentInfo(cls.driver)
        cls.student.gengduo()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.get(home_url)
    #每条用例完了以后会执行
    #不加这个第二个用例是接着第一个用例跑，起始位置错了，所以要回到起始位置
    #要回到登录成功后的第一个页面，所以重新刷新输入地址即可


    def test_add_01(self):
        '''登录-添加学生信息-成功案例: 测试数据， 20000008，zzzsss'''
        s_id = str(time.time()) #int
        #改成用时间戳来生成学号，这样每次录入的都是不一样的学号，实例化名字是s_id，所以要把以下个例学号改成这个s_id
        #学号本身是int数字的，要改成str字符串输入
        self.student.add_student(s_id, "李四")
        #AddStudentInfo是add student page里的类，实例化是student，要传过来，
        # 这里是self，不是cls，所以改成self.student
        #result = self.student.is_add_student_success("noooos")
        #print("结果: %s"%result)
        t3 = self.student.is_add_success(s_id)
        print("实际结果：%s"%str(t3))
        self.assertTrue(t3)

    def test_add_02(self):
        '''登录-添加学生信息-无法提交 测试数据缺少id'''
        self.student.add_student_id_missing("张三")
        time.sleep(3)
        loc_x = ("css selector", ".default.btn.btn-primary.hide-xs")
        #定位，判断“保存”按钮仍然显示在页面上
        #实际结果
        result = self.student.is_element_exist(loc_x)
        print("实际结果: %s" % result)
        #期望结果
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()



