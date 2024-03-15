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
        print('신규처리 : {} | {}'.format(title, link))

    # TODO 자동화 포스팅 로직 넣어야함
        print('TODO 티스토리 자동화 포스팅 작업중')
    
    
    