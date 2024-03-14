from bs4 import BeautifulSoup as bs
import requests
import os

target_url = 'https://m.blog.naver.com/PostList.naver?blogId=travelhyuk&tab=1'
url = target_url
req = requests.get(url)
content = req.content
print(content)

# //*[@id="contentslist_block"]/div[2]/div/div[2]/ul/li[1]
# //*[@id="contentslist_block"]/div[2]/div/div[2]/ul/li[2]

# 타이틀 html, 링크 가져오기 href
# //*[@id="contentslist_block"]/div[2]/div/div[2]/ul/li[1]/div/a/div[2]/strong/span/span
# //*[@id="contentslist_block"]/div[2]/div/div[2]/ul/li[1]/div/a

# bs4 파싱 연동
soup = bs(content, 'html.parser')

titles = soup.select_one('#contentslist_block > div.list_block__XlpUJ > div > div.list__A6ta5 > ul > li:nth-child(1) > div > a > div.text_area__CmNI4 > strong > span > span')
#links = soup.select('//*[@id="contentslist_block"]/div[2]/div/div[2]/ul/li[1]/div/a')

print(titles)