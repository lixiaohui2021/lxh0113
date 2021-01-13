from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
class Email(unittest.TestCase):
    def setUp(self):
        self.web=webdriver.Firefox()
        self.web.get("https://www.baidu.com")
        time.sleep(10)
    def tearDown(self):
        self.web.close()
        self.web.quit()
    def test_mail(self):
        self.web.find_element(By.ID,'kw').send_keys("qq邮箱")
        self.web.find_element(By.CSS_SELECTOR,"[value='百度一下']").click()
        time.sleep(3)
        self.web.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div[3]/div[1]/h3/a[1]').click()
        time.sleep(3)
        handles=self.web.window_handles
        print(handles)
        self.web.switch_to.window(handles[-1])
        time.sleep(10)
        self.web.switch_to.frame("login_frame")
        self.web.find_element(By.ID,'switcher_plogin').click()
        self.web.find_element(By.ID,'u').send_keys("1013907030")
        self.web.find_element(By.ID,'p').send_keys("lixiaohui2020")
        self.web.find_element(By.XPATH,'//*[@id="login_button"]').click()
        time.sleep(10)
        self.web.switch_to.default_content()

if __name__ == '__main__':
    unittest.main()