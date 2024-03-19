# 1. 네이버 포스팅 스크래핑 
from selenium_module.naver import NaverPost
post = NaverPost('travelhyuk')
postlist = post.getNewPost()

# 자동화 포스팅 시작
from redislib import RedisLib
rlib = RedisLib()
for post in postlist:
    # 변수 초기화
    title = post['title']
    link = post['link']
    # 레디스 변수 넣고 처리(true인 경우 신규, false는 기처리라 패쓰)
    if rlib.scrape_and_store_data(title, link):
        try:
            # 포스팅 가져오기
            print('신규 포스팅 시작 : {} | {}'.format(title, link))
            from extractPost import ExtractPost
            ## 파싱 블로그 URL(티스토리, 모바일주소로 입력)
            platform = 'n' # t:티스토리 , n:네이버
            expost = ExtractPost(
                target_url = link,
                post_name = title, 
                platform=platform,
                #savedir="D:/2.Private/job/td_company/data"
            )
            expost.parsing_blog()
            savedimages = expost.getSavedImages()
        except Exception as e:
            print(e)
            rlib.removeKey(link) # 신규등록 과정에서 오류 시 레디스에서 키를 제거해서 다시 수행할 수 있게 함

    # TODO 자동화 포스팅 로직 넣어야함
        print('TODO 티스토리 자동화 포스팅 작업중')
    
    
    