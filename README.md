pip install redis
python.exe -m pip install --upgrade pip

# redis 설치
https://github.com/microsoftarchive/redis/releases
Redis-x64-3.0.504.zip
redis-server.exe 실행
# redis aop 설정(로그 백업)
redis.windows.conf파일 > appendonly yes 입력
redis-server.exe redis.windows.conf # 설정값이랑 같이 실행해야함
redis-server.exe --service-install redis.windows.conf # 서비스 등록

*.aof 파일로 백업되서 영구저장됨

# parsing 모듈 설치
pip install bs4


# 크롤링 소스 참조할 소스
https://blog.naver.com/chandong83/221955351945
https://github.com/chandong83/download-naver-blog/blob/master/get_category_list.py