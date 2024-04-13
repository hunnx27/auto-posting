arg_targetPostId = 'chummilmil99'

"""
1. keys 로 yosiki1928이 포함된 redis의 해시키를 조회하기
2. 조회한 hashkey를 반복하면서 글을 썼는지 조회하기
"""

from redislib import RedisLib

rlib = RedisLib()

keys = rlib.search_hashkeys(arg_targetPostId)
extractPostList = []
alreadyWriteList = []
for key in keys:
    store_hashdata = rlib.get_store_hashdata(key)
    isWriteByte = store_hashdata.get(b'isWrite')
    print(isWriteByte.decode())
    """
    if isWriteByte.decode() == 'True':
        alreadyWriteList.append(key)
    else:
        titleByte = store_hashdata.get(b'title')
        textByte = store_hashdata.get(b'text')
        savedImagesByte = store_hashdata.get(b'savedImages')
        import json
        extractPostList.append((key, titleByte.decode(), textByte.decode(), json.loads(savedImagesByte)))
    """

print(len(extractPostList))