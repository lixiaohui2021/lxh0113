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

    def test_05bianji(self):  # 编辑正例
        try:
            self.sy.find_element(By.XPATH, "/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.sy.find_element(By.XPATH, "/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            self.sy.find_element(By.NAME, "chk[]").click()
            self.sy.find_element(By.XPATH,"/html/body/section/section/section/form/div/div/section/table/tbody/tr[2]/td[8]/a").click()
            time.sleep(2)
            self.sy.find_element(By.NAME, "pro_name").clear()
            self.sy.find_element(By.NAME, "pro_name").send_keys("冰糖葫芦")
            self.sy.find_element(By.NAME, "cpbh").clear()
            self.sy.find_element(By.NAME, "cpbh").send_keys("123")
            time.sleep(2)
            self.sy.find_element(By.XPATH,"/html/body/section/section/section/div[2]/div/section/div/form/div[9]/div/button").click()
            time.sleep(2)
            bianyuqi = self.sy.find_element(By.XPATH, "/html/body/div[3]/div").text
            self.assertEqual(bianyuqi, "产品更新成功！", msg="产品修改失败")
        except Exception as e:
            print(e)
if __name__ == '__main__':
    unittest.main()