# 파이썬 설치
파이썬 3.10.4버전 64비트 설치
https://www.python.org/downloads/release/python-3104/
Windows Installer (64-bit) - 27.2mb 다운로드 및 설치

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

# 설치된 라이브러리 백업
pip freeze > requirements.txt
# 최초 설치시
pip install -r requirements.txt



