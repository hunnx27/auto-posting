
arg_targetPostId = 'chummilmil99'

from redislib import RedisLib
rlib = RedisLib()
keys = rlib.search_hashkeys(arg_targetPostId)
print('{} 블로그 저장 데이터 조회'.format(arg_targetPostId))
for (idx, key) in enumerate(keys):
    store_hashdata = rlib.get_store_hashdata(key)
    isWrite = 'Y' if store_hashdata.get(b'isWrite') != None and store_hashdata.get(b'isWrite').decode() == 'True' else 'N'
    isError = 'Y' if store_hashdata.get(b'isError')!= None and store_hashdata.get(b'isError').decode() == 'True' else 'N'
    isErrorByte = store_hashdata.get(b'isError')
    titleByte = store_hashdata.get(b'title')
    textByte = store_hashdata.get(b'text')
    savedImagesByte = store_hashdata.get(b'savedImages')
    print("[{}] {} | 작성: {} | 에러: {} | {}".format(idx, titleByte.decode()[0:10], isWrite, isError, key.decode()))

print("## 총 갯수 : {}".format(len(keys)))



