import unittest
import requests
class JiekouTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_phone01(self):
        self.url="https://api.yonyoucloud.com/apis/dst/checkPhoneIfNullByMobiles/getPhoneIfNullByMobiles"
        self.header={
            "apicode":"6957e82f93a34c398776dc1f04ffe302",
            "Content-Type":"application/json"
        }
        self.data={"Content-Type":"application/json","mobiles":"18235468125"}
        result=requests.post(url=self.url,headers=self.header,json=self.data)
        # print(result.text)
        self.assertIn("errcode:300004",result.text,msg='错误码不一致')
if __name__ == '__main__':
    unittest.main()