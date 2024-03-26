import redis

class RedisLib:

    def __init__(self):
        # Redis 연결
        self.__r = redis.Redis(host='localhost', port=6379, db=0)

    def scrape_and_store_data(self, title, url):
        isSuccess = False
        savedData = self.__r.hget(url, 'title')
        print('savedData : {}'.format(savedData))
        if savedData != None:
            print("이미 스크랩된 데이터입니다.")
        else:
            self.__r.hset(url, 'title', title)
            self.__r.hset(url, 'isWrite', str(False))
            isSuccess = True
            #print("데이터가 성공적으로 스크랩되었습니다.")
        return isSuccess
    
    def remove_key(self, url):
        self.__r.delete(url)
        

    def clear_data(self):
        self.__r.flushall()
    
    def get_store_hashdata(self, url):
        return self.__r.hgetall(url)
    
    def set_store_hashdata(self, url, key, value):
        self.__r.hset(url, key, value)
    