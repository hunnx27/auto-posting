import sys

# 인자 입력받기
#if len(sys.argv) != 3:
#    print("길이 :", len(sys.argv))
#    print("ID와 비밀번호를 인자로 입력하세요.")
#    sys.exit()

args_id = '' #sys.argv[1]
args_pw = '' #sys.argv[2]
arg_platform = 'n' # n:naver t:tistory TODO 인자로 받게 수정필요
arg_saveDir = 'D:/2.Private/job/td_company/data' # TODO 인자로 받게 수정필요
arg_targetPostId = 'travelhyuk'

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
rlib.clearData() # 주석하기(데이터초기화)
extractPostlist = []
for idx, post in enumerate(postlist):
    # 변수 초기화
    title = post['title']
    link = post['link']
    # 레디스 변수 넣고 처리(true인 경우 신규, false는 기처리라 패쓰)
    if rlib.scrape_and_store_data(title, link):
        try:
            # 새글 스크래핑
            print('신규 포스팅 시작 : {} | {}'.format(title, link))
            from extractPost import ExtractPost
            ## 파싱 블로그 URL(티스토리, 모바일주소로 입력)
            platform = 'n' # t:티스토리 , n:네이버
            expost = ExtractPost(
                target_url = link,
                post_name = title, 
                platform=arg_platform,
                savedir=arg_saveDir
            )
            expost.parsing_blog()
            extractPostlist.append(expost)

            if(idx==1): # 2번만 돌게 제한
                break # TODO 주석처리, 혹은 라인삭제 필요
        except Exception as e:
            print(e)
            rlib.removeKey(link) # 신규등록 과정에서 오류 시 레디스에서 키를 제거해서 다시 수행할 수 있게 함

    # TODO 자동화 포스팅 로직 넣어야함
        print('TODO 티스토리 자동화 포스팅 작업중')


from selenium.webdriver.chrome.options import Options
from selenium import webdriver
option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=option)

from selenium_module.tistory import Tistory
import pdb
#pdb.set_trace()
tistory = Tistory(
            url='https://superblo.tistory.com/manage',
            driver=driver
        )
from autogpt import AutoGpt
gpt = AutoGpt(driver=driver, gpt_url='https://chat.openai.com/?AIPRM_PromptID=1785987336174305280')

for expost in extractPostlist:
    title = expost.getTitle()
    savedimages = expost.getSavedImages()
    text = expost.getText()
    gptText = gpt.searchGPT2(text)
    print(gptText)
    datas = []
    datas.append(('text', gptText))
    for img in savedimages:
        datas.append(('image', img))
        break # TODO 해당 라인 삭제 필수
    tistory.write(title=title, datas=datas) # 일단주석

    print('하나 끝')
    

    