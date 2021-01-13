from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
# from test_case.test_login import DL
# dl=DL()
class Xinzeng(unittest.TestCase):
    sy = webdriver.Firefox()
    def setUp(self):
        self.sy.get("http://123.57.140.190/manage/index.php")
        time.sleep(3)
        self.sy.find_element(By.XPATH, "/html/body/div/section/form/div/input[1]").send_keys("admin")
        self.sy.find_element(By.XPATH, "/html/body/div/section/form/div/input[2]").send_keys("admin999")
        time.sleep(3)
        self.sy.find_element(By.XPATH, "/html/body/div/section/form/div/input[3]").click()
        time.sleep(1)
    def logout(self):
        self.sy.close()
        self.sy.quit()
    def tearDown(self):
        self.logout()

    def test_04guanli(self):  # 搜索正例
        try:
            self.sy.find_element(By.CSS_SELECTOR, "a.active > span:nth-child(2)").click()
            self.sy.find_element(By.XPATH, "/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            self.sy.find_element(By.NAME, "pro_name").send_keys("山药")
            self.sy.find_element(By.CLASS_NAME, "btn btn-success").click()
            time.sleep(3)
            guanyuqi = self.sy.find_element(By.XPATH,"/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[4]/a").text
            self.assertEqual(guanyuqi, "山药", msg="搜索错误")
        except Exception as e:
            print(e)
if __name__ == '__main__':
    unittest.main()