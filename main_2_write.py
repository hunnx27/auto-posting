import sys
import json
import time
# 인자 입력받기
#if len(sys.argv) != 3:
#    print("길이 :", len(sys.argv))
#    print("ID와 비밀번호를 인자로 입력하세요.")
#    sys.exit()

args_id = '' #sys.argv[1]
args_pw = '' #sys.argv[2]
arg_platform = 'n' # n:naver t:tistory TODO 인자로 받게 수정필요
arg_saveDir = 'C:/tdcompany/data' # TODO 인자로 받게 수정필요
arg_targetPostId = 'yosiki1928'
arg_tistoryWriteUrl = 'https://one.tddiary.com'
#arg_gptAiprmUrl = 'https://chat.openai.com/?AIPRM_PromptID=1784224785543462912'
arg_gptAiprmUrl = 'https://chat.openai.com'

# 새글 가져오기
if arg_platform == 'n':
    # 1. 네이버 포스팅 스크래핑 
    from selenium_module.naver import NaverPost
    post = NaverPost(arg_targetPostId)
    postlist = post.getNewPost()
elif arg_platform == 't':
    # 2. 티스토리 포스팅 스크래핑 TODO 아직 미구현
    sys.exit(0)


# 새글 스크래핑
from redislib import RedisLib
rlib = RedisLib()
#rlib.clearData() # 주석하기(데이터초기화)
extractPostlist = []
for idx, post in enumerate(postlist):
    # 변수 초기화
    title = post['title']
    titleregex = post['titleregex']
    link = post['link']
    # 레디스 변수 넣고 처리(true인 경우 신규, false는 기처리라 패쓰)

    store_hashdata = rlib.get_store_hashdata(link)
    isWriteByte = store_hashdata.get(b'isWrite')
    titleByte = store_hashdata.get(b'title')
    textByte = store_hashdata.get(b'text')
    savedImagesByte = store_hashdata.get(b'savedImages')

    if not(isWriteByte != None and titleByte != None and textByte != None and savedImagesByte != None):
        print('isWriteByte : {}'.format(isWriteByte))
        print('titleByte : {}'.format(titleByte))
        print('textByte : {}'.format(textByte))
        print('savedImagesByte : {}'.format(savedImagesByte))
        continue # None인경우는 패쓰..

    if not (isWriteByte != None and isWriteByte.decode() == 'True') :
        print('수집 후 미작성 데이터 : {}'.format(title))
        titleByte = store_hashdata.get(b'title')
        textByte = store_hashdata.get(b'text')
        savedImagesByte = store_hashdata.get(b'savedImages')
        extractPostlist.append((link, titleByte.decode(), textByte.decode(), json.loads(savedImagesByte)))
        
print('총수집데이터:{} | 미작성데이터:{} | 작성된데이터:{}'.format(len(postlist), len(extractPostlist), len(postlist)-len(extractPostlist)))
if len(extractPostlist)==0:
    print('작성할 게시물이 없습니다.')
    sys.exit()

print('자동화 포스팅 시작 3초전!')
time.sleep(3)
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=option)

from selenium_module.tistory import Tistory

tistory = Tistory(
            url='{}/manage'.format(arg_tistoryWriteUrl),
            driver=driver
        )
from autogpt import AutoGpt
gpt = AutoGpt(driver=driver, gpt_url=arg_gptAiprmUrl)

for (idx, expostTuple) in enumerate(extractPostlist):
    link = expostTuple[0]
    title = expostTuple[1]
    text = expostTuple[2]
    savedimages = expostTuple[3]

    gptText = gpt.searchGPT2(text)
    #gptText = text # FIXME gpt 처리 임시 주석
    print('gptText : {}'.format(gptText))
    #for img in savedimages:
        #datas.append(('image', img))
    
    #mergedText = tistory.exportImageLinkAndMergeTextAndGetText(savedimages=savedimages[:1], gptText=gptText) #테스트용
    mergedText = tistory.exportImageLinkAndMergeTextAndGetText(savedimages=savedimages, gptText=gptText)
    
    datas = []
    datas.append(('text', mergedText))
    print(mergedText)
    tistory.write(title=title, datas=datas)
    rlib.set_store_hashdata(link, 'isWrite', str(True))
    print('작성 완료 {}/{}'.format(idx+1, len(extractPostlist)))

    #break 테스트용