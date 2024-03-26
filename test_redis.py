from redislib import RedisLib
import json

rlib = RedisLib()
key = 'https://m.blog.naver.com/PostView.naver?blogId=yosiki1928&logNo=223395418724&navType=by'
#rlib.set_store_hashdata(key, 'text', 'text~~~~~')
#rlib.set_store_hashdata(key, 'savedImages', json.dumps([1,2,3]))
#rlib.set_store_hashdata(key, 'isWrite', str(True))
hashdata = rlib.get_store_hashdata(key)

#print(hashdata.get(b'text'))
#print(hashdata.get(b'savedImages'))
#print(hashdata.get(b'isWrite'))


#print(hashdata.get(b'text').decode())
print(hashdata.get(b'title').decode())
print(hashdata.get(b'isWrite').decode() == 'True')
#print(json.loads(hashdata.get(b'savedImages')))