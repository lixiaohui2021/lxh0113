from selenium import webdriver
import time
import unittest
from ddt import ddt,data,unpack
class Email(unittest.TestCase):
    def setUp(self):
        self.mail = webdriver.Firefox()
        self.mail.get("http://mail.qq.com")
        time.sleep(3)
    def tearDown(self):
        self.mail.close()
        self.mail.quit()
    def test_mail(self):
        self.mail.switch_to.frame("login_frame")
        # self.mail.find_element_by_id("switcher_plogin").click()
        self.mail.find_element_by_id("u").send_keys("1013907030")
        self.mail.find_element_by_id("p").send_keys("lixiaohui2020")
        self.mail.find_element_by_css_selector("#login_button").click()
        self.mail.switch_to.default_content()
        time.sleep(3)
        self.mail.find_element_by_xpath("//*[@id='composebtn']").click()
        time.sleep(3)
        self.mail.find_element_by_xpath("/html/body").send_keys("作业做完了")
        self.mail.switch_to.frame("mainFrame")
        self.mail.find_element_by_xpath("/html/body/form[2]/div[2]/div[3]/div[2]/table[2]/tbody/tr/td[2]/div[1]/div[2]/input").send_keys("370801466@qq.com")
        self.mail.find_element_by_xpath("//*[@id='subject']").send_keys("作业")
        self.mail.find_element_by_xpath("/html/body/form[2]/div[3]/div/a[1]").click()
        self.mail.switch_to.default_content()
        time.sleep(5)
if __name__ == '__main__':
    unittest.main()
