import redis

class RedisLib:

    def __init__(self):
        # Redis 연결
        self.__r = redis.Redis(host='localhost', port=6379, db=0)

    def scrape_and_store_data(self, title, url):
        isSuccess = False
        savedDataByte = self.__r.hget(url, 'title')
        #print('savedData : {}'.format(savedData))
        isErrorByte = self.__r.hget(url, 'isError')
        if savedDataByte == None: 
            self.__r.hset(url, 'title', title)
            self.__r.hset(url, 'isWrite', str(False))
            self.__r.hset(url, 'isError', str(False))
            isSuccess = True
        elif isErrorByte!= None and isErrorByte.decode() == 'True':
            print("오류 데이터 재수집: {} | {}".format(title, url))
            isSuccess = True
        else:
            print("이미 스크랩된 데이터 : {} | {}".format(title, url))
        
        return isSuccess
    
    def remove_key(self, url):
        self.__r.delete(url)
        

    def clear_data(self):
        self.__r.flushall()
    
    def get_store_hashdata(self, url):
        return self.__r.hgetall(url)
    
    def set_store_hashdata(self, url, key, value):
        self.__r.hset(url, key, value)

    def search_hashkeys(self, targetId):
        return self.__r.keys("*{}*".format(targetId))