from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class DL():
    sy = webdriver.Firefox()
    def login(self):
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
d=DL()
d.login()
d.logout()