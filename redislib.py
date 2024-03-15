import redis

class RedisLib:

    def __init__(self):
        # Redis 연결
        self.__r = redis.Redis(host='localhost', port=6379, db=0)

    
    def scrape_and_store_data(self, title, url):
        isSuccess = False
        if self.__r.get(url):
            print("이미 스크랩된 데이터입니다.")
        else:
            self.__r.set(url, title)
            isSuccess = True
            #print("데이터가 성공적으로 스크랩되었습니다.")
        return isSuccess
    
    def removeKey(self, url):
        self.__r.delete(url)
        

    def clearData(self):
        self.__r.flushall()