from common.Base import Base

login_url = "http://47.104.190.48:8000/login"

class Login(Base):
    loc1 = ("id", "id_username")
    loc2 = ("id", "id_password")
    loc3 = ("xpath", ".//*[@value='确定']")
    login_xpath = ("xpath", "//*[@id='top-nav']/div[2]/ul/li[2]/a/strong")

    def login(self, user='veratest1', psw='123456'):
        self.send(self.loc1, user)
        self.send(self.loc2, psw)
        self.click(self.loc3)

    def is_login_success(self, text):
        body = ("xpath", "//body")
        body_text = self.get_text(body)
        return text in body_text


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get(login_url)

    loginpage = Login(driver)
    loginpage.login()
