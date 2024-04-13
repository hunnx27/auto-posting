
arg_targetPostId = 'chummilmil99'
arg_saveDir = 'C:/tdcompany/data'
arg_deletepost = 'https://m.blog.naver.com/PostView.naver?blogId=chummilmil99&logNo=223414142101&navType=by'

from redislib import RedisLib
rlib = RedisLib()

keys = rlib.search_hashkeys(arg_targetPostId)
succlist = []
errlist = []
for key in keys:
    try:
        store_hashdata = rlib.get_store_hashdata(key)
        titleByte = store_hashdata.get(b'title')
        if arg_deletepost == key.decode():
            print("삭제 : {} | {}".format(titleByte.decode(), key))
            rlib.remove_key(key)
            succlist.append(key)
    except Exception as e:
        print(e)
        errlist.append(key)
else:
    print('처리하려는 블로그가 없습니다. - {}'.format(arg_targetPostId))

print("## 삭제처리 - 처리갯수 : {}개, 에러갯수 : {}개".format(len(succlist), len(errlist)) )