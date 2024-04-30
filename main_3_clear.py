
arg_targetPostId = 'okjoa012'
arg_saveDir = 'C:/tdcompany/data'

from redislib import RedisLib
rlib = RedisLib()

keys = rlib.search_hashkeys(arg_targetPostId)
succlist = []
errlist = []
for key in keys:
    try:
        store_hashdata = rlib.get_store_hashdata(key)
        isWriteByte = store_hashdata.get(b'isWrite')
        titleByte = store_hashdata.get(b'title')
        textByte = store_hashdata.get(b'text')
        savedImagesByte = store_hashdata.get(b'savedImages')
        print("삭제 : {} | {}".format(titleByte.decode(), key))
        rlib.remove_key(key)
        succlist.append(key)
    except Exception as e:
        print(e)
        errlist.append(key)


print("## 삭제처리 - 총 갯수 : {}개, 처리갯수 : {}개, 에러갯수 : {}개".format(len(keys), len(succlist), len(errlist)) )