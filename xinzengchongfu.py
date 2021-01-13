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
    def test_02xinzeng(self):  # 新增产品产品编号重复验证
        self.sy.find_element(By.XPATH, "/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
        self.sy.find_element(By.XPATH, "/html/body/section/aside/div/ul/li[1]/ul/li[1]/a").click()
        self.sy.find_element(By.NAME, "pro_name").send_keys("新疆葡萄干")
        self.sy.find_element(By.NAME, "cpbh").send_keys("12345")
        self.sy.find_element(By.NAME, "cptxm").send_keys("111")
        self.sy.find_element(By.XPATH,"/html/body/section/section/section/div/div/section/div/form/div[8]/div/div/div[2]/iframe").send_keys("大又干，很完美哦")
        try:
            self.sy.find_element(By.XPATH,"/html/body/section/section/section/div/div/section/div/form/div[9]/div/button").click()
            time.sleep(3)
            newyuqi =self.sy.find_element(By.CSS_SELECTOR, ".layui-layer-content").text
            self.assertEqual(newyuqi, "产品编号有重复!", msg="产品码错误")
        except Exception as e:
            print(e)
if __name__ == '__main__':
    unittest.main()