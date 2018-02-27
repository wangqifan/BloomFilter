import unittest
from BloomFilter import bloomfilter
import redis
import os
import uuid

REDIS_HOST = os.environ.get('REDIST_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
text=["text1","text2","text3","text4","text5","text6","text7","text8","text9","text10"]
text2=["t124359","wqewr9ehfdc","qweufdbvc"]

class WANGYI(unittest.TestCase):
    def setUp(self):
        server=redis.Redis(REDIS_HOST,REDIS_PORT)
        server.delete("bloomfilter")
        filter=bloomfilter(server=server,key="bloomfilter")
        for item in text:
            filter.insert(item)

    def test01(self):
        server = redis.Redis(REDIS_HOST, REDIS_PORT)
        filter = bloomfilter(server=server, key="bloomfilter")
        for item in text:
            res=filter.insert(item)
            self.assertAlmostEqual(res,False)
        for item in text2:
            res=filter.insert(item)
            self.assertAlmostEqual(res,True)
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()