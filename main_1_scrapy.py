import sys
import json
# 인자 입력받기
#if len(sys.argv) != 3:
#    print("길이 :", len(sys.argv))
#    print("ID와 비밀번호를 인자로 입력하세요.")
#    sys.exit()

args_id = '' #sys.argv[1]
args_pw = '' #sys.argv[2]
arg_platform = 'n' # n:naver t:tistory TODO 인자로 받게 수정필요
arg_saveDir = 'C:/tdcompany/data' # TODO 인자로 받게 수정필요
arg_targetPostId = 'chummilmil99'
arg_tistoryWriteUrl = 'https://superblo.tistory.com'
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
                savedir=arg_saveDir,
                savefolder=titleregex
            )
            expost.parsing_blog()

            # redis 저장
            title = expost.getTitle()
            text = expost.getText()
            savedImages = expost.getSavedImages()
            
            rlib.set_store_hashdata(link, 'text', expost.getText())
            rlib.set_store_hashdata(link, 'savedImages', json.dumps(expost.getSavedImages()))

            # 즉시 처리를 위한 리스트 저장
            extractPostlist.append((link, title, text, savedImages))
        except Exception as e:
            print(e)
            rlib.remove_key(link) # 신규등록 과정에서 오류 시 레디스에서 키를 제거해서 다시 수행할 수 있게 함
        

    

    