import sys
import json
import time
import configAd

arg_platform = 'n' # n:naver t:tistory TODO 인자로 받게 수정필요
arg_saveDir = 'C:/tdcompany/data' # TODO 인자로 받게 수정필요
arg_targetPostId = 'okjoa012'
arg_tistoryWriteUrl = 'https://superblo.tistory.com'
arg_gptAiprmUrl = 'https://chat.openai.com'
args_today_max_write_count = 15 # 오늘 최대 포스트 작성 갯수
args_image_max_count = 99

#https://cinema.tddiary.com
#https://policy.tddiary.com
#okjoa012  영화7
#alsk1130  영화
#yosiki1928  이슈눈물의 여왕 촬영지 용두객       
#jobary1


from redislib import RedisLib
rlib = RedisLib()

# 작성수 체크
from datetime import datetime
today = datetime.today().strftime("%Y-%m-%d")
todayKey = '{}:{}'.format(arg_tistoryWriteUrl, today)

def checkTodayPostWrite(todayKey):
    today_store_hashdata = rlib.get_store_hashdata(todayKey)
    todayWriteCountByte = today_store_hashdata.get(b'write_count') if today_store_hashdata.get(b'write_count')!=None else b'0'
    todayWriteCount = int(todayWriteCountByte.decode())
    if todayWriteCount >= args_today_max_write_count:
        print('''
### ALARAM ###
해당 블로그는 오늘 작성할 최고 갯수({}개 까지만 가능)를 모두 작성하여 작성이 불가합니다.
작성을 원하시면 args_today_max_write_count 변수의 갯수를 높이세요.[오늘 작성 포스팅 수 : {}개]
'''.format(args_today_max_write_count, todayWriteCount))
        sys.exit(0)
def todayPostWriteCounting(todayKey):
    today_store_hashdata = rlib.get_store_hashdata(todayKey)
    todayWriteCountByte = today_store_hashdata.get(b'write_count') if today_store_hashdata.get(b'write_count')!=None else b'0'
    todayWriteCount = int(todayWriteCountByte.decode())
    rlib.set_store_hashdata(todayKey, 'write_count', todayWriteCount+1)
checkTodayPostWrite(todayKey)

    # 새글 스크래핑
keys = rlib.search_hashkeys(arg_targetPostId)
extractPostList = []
alreadyWriteList = []
for key in keys:
    store_hashdata = rlib.get_store_hashdata(key)
    isWriteByte = store_hashdata.get(b'isWrite')
    titleByte = store_hashdata.get(b'title')
    textByte = store_hashdata.get(b'text')
    savedImagesByte = store_hashdata.get(b'savedImages')
    try:
        if isWriteByte.decode() == 'True':
            print('수집 후 작성 데이터 : {} | {}'.format(titleByte.decode(), key))
            alreadyWriteList.append(key)
        else:
            print('수집 후 미작성 데이터 : {} | {}'.format(titleByte.decode(), key))
            import json
            extractPostList.append((key.decode(), titleByte.decode(), textByte.decode(), json.loads(savedImagesByte)))
    except Exception as e:
        print(e)
        rlib.set_store_hashdata(key.decode(), 'isError', str(True))

print(len(extractPostList))

print('총수집데이터:{} | 미작성데이터:{} | 작성된데이터:{}'.format(len(keys), len(extractPostList), len(alreadyWriteList)))
if len(extractPostList)==0:
    print('작성할 게시물이 없습니다.')
    sys.exit()

print('자동화 포스팅 시작 2초전!')
time.sleep(2)
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=option)

from selenium_module.tistory import Tistory
tistory = Tistory(
            url='{}'.format(arg_tistoryWriteUrl),
            driver=driver,
            max_ad_size=configAd.args_max_ad_size,
            ad_map=configAd.args_ad_map
        )
from autogpt import AutoGpt
gpt = AutoGpt(driver=driver, gpt_url=arg_gptAiprmUrl)
errcnt = 0
errlist = []
for (idx, expostTuple) in enumerate(extractPostList):
    checkTodayPostWrite(todayKey) # 오늘 최고 작성 카운트 체크

    link = expostTuple[0]
    title = expostTuple[1]
    text = expostTuple[2]
    savedimages = expostTuple[3]

    gptText = text 
    gptText = gpt.searchGPT2(text) # gpt 처리 임시 주석(테스트 시 주석처리)
    firstRow = gptText.split('\n')[0]
    extract_title = firstRow.replace('#', '').strip()
    title = extract_title if extract_title!='' else title
    gptText_withoutTitle = gptText.replace(firstRow + '\n', '')
    #mergedText = tistory.exportImageLinkAndMergeTextAndGetText(savedimages=savedimages[:1], gptText=gptText) #테스트용
    mergedText = tistory.exportImageLinkAndMergeTextAndGetText(savedimages=savedimages, gptText=gptText_withoutTitle, maxImageLen=args_image_max_count)
    
    datas = []
    datas.append(('text', mergedText))
    print(mergedText)
    try:
        # 기본 글쓰기 # todo 임시글이 아닌 실제 글쓰기
        urlPublished = tistory.write(title=title, datas=datas, isSave=True)
        rlib.set_store_hashdata(link, 'isWrite', str(True))
        # 색인 등록
        from googleSC import GoogleSC
        sc = GoogleSC(blog_url=arg_tistoryWriteUrl, driver=driver)
        try:
            #sc.indexUri(tistory.getPostUri(urlPublishTitle))
            sc.indexUri(urlPublished)
        except Exception as e:
            print('# 인덱스 에러 : e:{}'.format(e))
        finally:
            time.sleep(2)

        rlib.set_store_hashdata(link, 'isError', str(False))

        # 오늘 작성 블로그 카운팅
        todayPostWriteCounting(todayKey)

        print('작성 완료 {}/{}'.format(idx+1, len(extractPostList)))
    except Exception as e:
        print(e)
        print('작성 실패 : {} | {}'.format(title, link))
        errcnt = errcnt + 1
        rlib.set_store_hashdata(link, 'isError', str(True))
        errlist.append((title, link))

    #break 테스트용
        
print("에러갯수 : {}/{}".format(errcnt, len(extractPostList)))
for (idx, errTuple) in enumerate(errlist):
    print("에러{} : {} | {}".format(idx, errTuple[0], errTuple[1]))