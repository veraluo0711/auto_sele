
from common.Base import Base  #导入基类，Base

from pages.login_page import Login  #导入登录

home_url = "http://47.104.190.48:8000/xadmin/"

class AddStudentInfo(Base):
    loc1 = ("link text", "进主页更多功能")  #更多
    loc2 = ("xpath", ".//*[@id='left-side']/ul[1]/li[7]/a")  #左侧学生钮
    loc3 = ("xpath", ".//*[@id='content-block']/div[1]/div[2]/div/a") #增加学生钮
    loc4 = ("name", "student_id") #录入页学生id
    loc5 = ("name", "name") #录入页学生名字
    #选男女这是很典型的一个选择框，它不是selelct但是，不同的性别class属性会变。
    #div下拉框（不是select）如何定位：
    #1. 选中框，可能点不中， 在代码里选
    loc6 = ("xpath", ".//*[@id='div_id_gender']/div/div/div[1]")  #录入页学生性别 选框
    #2. 选择选项，文本定位
    #loc7 = ("xpath",".//*[text()='女']" )
    #写完先去调试，发现定位到三个，找区别，细化定位，如找父一级
    #可惜最后还是不好细化，稍后用复数查找+下标 finds（）
    #试验发现上述方法也失败
    loc7 = ("xpath",".//*[@id='div_id_gender']/div/div/div[2]/div/div[2]" )  #录入页学生性别 女
    loc8 = ("id", "id_age") #录入页学生年龄
    loc9 = ("xpath",".//*[@id='student_form']/div[2]/button" ) #录入页 保存钮

    loc_r = ("xpath", ".//*[@id='changelist-form']/div[1]/table/tbody/tr[1]/td[2]")


    def gengduo(self):
        self.click(self.loc1)
        #把点击“更多”单独拿出来，为了后边写case时的tear down从新回到正确的起始页
        #同时，这个类里边的以下的方法里，都不用单独写self.click(self.loc1)这一步了


    def add_student(self, s_id, s_name):
        '''正常流程，成功'''
        self.click(self.loc2)
        self.click(self.loc3)

        self.send(self.loc4, s_id)
        self.send(self.loc5, s_name)

        self.click(self.loc6)
        self.click(self.loc7)

        self.send(self.loc8, "212")
        self.click(self.loc9)

    def add_student_id_missing(self, s_name):
        '''参数缺失 id'''
        self.click(self.loc2)
        self.click(self.loc3)

        # self.send(self.loc4, s_id)
        self.send(self.loc5, s_name)

        self.click(self.loc6)
        self.click(self.loc7)

        self.send(self.loc8, "212")
        self.click(self.loc9)


    def is_add_student_success(self, text):
        #判断text“学生名称”在列表里 包含 00:43
        #“学生名称”在当前页
        #t = self.driver.page_source #获取当前页整个html源码， 方法1
        body = ("tag name", "body") #获取当前页所有tag的名字
        t2 = self.find(body).text
        #print(t2)
        return text in t2

    def is_add_success(self,s_id):
        #第二种判断 学号，判断方法是多种多样的
        t = self.get_text(self.loc_r)
        print("获取的学号：%s" %t)
        return s_id == t #此时可以看下网页代码，如果不是纯文本，包含空格和其他时，可以用包含

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get("http://47.104.190.48:8000/login")
    a = Login(driver)
    a.login()  #先登录
    b = AddStudentInfo(driver) #到添加学生页面
    b.gengduo()
    b.add_student("20000008", "zzzsss")

    result = b.is_add_student_success("zzzsss")
    print("结果: %s"%result)

    t3 = b.is_add_success("20000008")
    print(t3)