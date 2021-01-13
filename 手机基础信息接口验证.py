import unittest
import requests
import json
class JiekouTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_phone01(self):
        self.url="https://api.yonyoucloud.com/apis/dst/matchIdentityWithMobile/matchIdentityWithMobile"
        self.header={
            "apicode":"4c6cc6697ebe49bcbbb8f36e14f1f90e",
            "Content-Type":"application/json"
        }
        self.data={"phoneNo":"1101101100","idNumber":"610526188712598423","userName":"小花"}
        result=requests.post(url=self.url,headers=self.header,json=self.data)

        print(result.text)

        self.assertIn('errcode:300004',result.text,msg='不一致')
if __name__ == '__main__':
    unittest.main()



