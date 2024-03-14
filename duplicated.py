import redis

# Redis 연결
r = redis.Redis(host='localhost', port=6379, db=0)
def scrape_and_store_data(title, url):
    if r.get(url):
        print("이미 스크랩된 데이터입니다.")
    else:
        r.set(url, title)
        print("데이터가 성공적으로 스크랩되었습니다.")

# 스크랩 데이터 추가 (예시)
scrape_and_store_data("스크래핑 예제", "http://example.com/scraping")
scrape_and_store_data("또 다른 스크래핑 예제", "http://example.com/another_scraping")
scrape_and_store_data("스크래핑 예제", "http://example.com/scraping")  # 중복 스크랩 시도
