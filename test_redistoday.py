from redislib import RedisLib
rlib = RedisLib()

from datetime import datetime
today = datetime.today().strftime("%Y-%m-%d")
todayKey = '{}:{}'.format('https://superblo.tistory.com', today)
print(todayKey)
today_store_hashdata = rlib.get_store_hashdata(todayKey)
todayCountByte = today_store_hashdata.get(b'write_count') if today_store_hashdata.get(b'write_count')!=None else b'0'
print(todayCountByte.decode())
rlib.set_store_hashdata(todayKey, 'write_count', int(todayCountByte.decode())+1)
today_store_hashdata = rlib.get_store_hashdata(todayKey)
todayCount = today_store_hashdata.get(b'write_count')
print(todayCount.decode())