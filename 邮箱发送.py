import unittest
from selenium import webdriver
import time
class email(unittest.TestCase):
    def setUp(self):
        self.mail=webdriver.Firefox()
        self.mail.get("http://mail.qq.com")
        time.sleep(3)
    def tearDown(self):
        self.mail.close()
        self.mail.quit()
    def test_mail(self):
        self.mail.switch_to.frame("login_frame")
        self.mail.find_element_by_partial_link_text("帐号密码登录").click()
        self.mail.find_element_by_id("u").send_keys("1013907030")
        self.mail.find_element_by_id("p").send_keys("lixiaohui2020")
        self.mail.find_element_by_id("login_button").click()
        self.mail.switch_to.default_content()
        time.sleep(3)
        self.mail.find_element_by_partial_link_text("写信").click()
        time.sleep(3)
        self.mail.switch_to.frame("mainFrame")
        self.mail.find_element_by_css_selector("[accesskey:'t']").send_keys("707297993@qq.com")
        self.mail.find_element_by_xpath("//*[@id='subject']").send_keys("王莹子")
        self.mail.switch_to.frame(0)
        self.mail.find_element_by_xpath("/html/body").send_keys("hello")
        time.sleep(2)
        self.mail.switch_to.parent_frame()
        time.sleep(3)
        self.mail.find_element_by_partial_link_text("发送").click()
        self.mail.switch_to.default_content()
        time.sleep(3)
if __name__ == '__main__':
    unittest.main()
