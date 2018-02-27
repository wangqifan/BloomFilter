class SimpleHash(object):
    def __init__(self, length, seed):
        self.length = length
        self.seed = seed

    def hash(self, value):
        ret = 0
        for i in range(len(value)):
            ret += self.seed * ret + ord(value[i])
        return (self.length - 1) & ret
class bloomfilter():
    """
    server redis服务
    key  bitmap的key
    """
    def __init__( self , server , key="bloomfilter" ) :
        self.key = key
        self.length = 2 ** 31 - 1
        self.server= server
        self.seeds = [ 1 , 3 , 5 , 13 , 27 , 59 , 61 , 99 ]
        self.hashfunc = []
        for seed in self.seeds:
            self.hashfunc.append(SimpleHash(self.length , seed))
    """
       插入一个str_input
       如果str_input已经存在于bitmap中返回False
       如果上str_input不存在，返回True,并写入bitmap
    """
    def insert(self,str_input):
        if not str_input:
            return False
        res=False
        for f in self.hashfunc:
            loc = f.hash(str_input)
            if self.server.getbit(self.key, loc)==0:
                res=True
                self.server.setbit(self.key , loc , 1)
        return res




