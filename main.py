import sys

# 인자 입력받기
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
for post in postlist:
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
            break # TODO 주석처리, 혹은 라인삭제 필요
        except Exception as e:
            print(e)
            rlib.removeKey(link) # 신규등록 과정에서 오류 시 레디스에서 키를 제거해서 다시 수행할 수 있게 함

    # TODO 자동화 포스팅 로직 넣어야함
        print('TODO 티스토리 자동화 포스팅 작업중')
    
from selenium_module.tistory import Tistory
tistory = Tistory(
            url='',
            id='',
            pw='',
        )
from gptautogui import AutoGpt
gpt = AutoGpt()
for expost in extractPostlist:
    title = expost.getTitle()
    savedimages = expost.getSavedImages()
    text = expost.getText()
    gptText = gpt.searchGPT(text)
    print(gptText)
    tistory.write(title=title, datas=[('txt', text)]) # 일단주석

    print('일단종료')
    sys.exit(0)
    

    