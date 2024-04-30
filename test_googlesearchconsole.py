from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from urllib import parse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=option)
driver.get("about:blank")
driver.implicitly_wait(1)
blog_url = 'https://superblo.tistory.com'
resource_id = parse.quote(blog_url)
search_console_url = 'https://search.google.com/search-console/inspect?resource_id={}'.format(resource_id)
driver.get(search_console_url)

target = 'https://superblo.tistory.com/entry/%ED%95%9C%EC%86%8C%ED%9D%AC-%EC%89%AC%EC%A7%80-%EC%95%8A%EA%B3%A0-%ED%99%9C%EB%B0%9C%ED%95%9C-%EC%86%8C%EC%85%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%ED%99%9C%EB%8F%99-%ED%8C%AC%EB%93%A4%EA%B3%BC-%EC%86%8C%ED%86%B5'
page_uri =  '/entry/한소희-쉬지-않고-활발한-소셜-네트워크-활동-팬들과-소통'
page_uri = parse.quote(page_uri)
input = '{}{}'.format(blog_url, page_uri)
print(input)

time.sleep(2)
# 660 검색 누르고 하기
# 661~ 바로 검색하기
width = driver.execute_script("return window.innerWidth;")
print('해상도 체크 : {}'.format(width))

if width <= 660:
    # 검색 클릭
    print('[660px 이하] >> 검색 버튼 클릭')
    urlCheckBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.XPATH, "/html/body/div[1]/div[2]/header/div[2]/div[2]/div[2]/form/button[3]") ))
    urlCheckBtn.click()
    print('검색버튼 clicked..')

# 색인 URL 검색
time.sleep(1)
searchUrlInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.XPATH, "/html/body/div[1]/div[2]/header/div[2]/div[2]/div[2]/form/div/div/div/div/div/div[1]/input[2]") ))
searchUrlInput.send_keys(input)
time.sleep(1)
searchUrlInput.send_keys(Keys.ENTER)

# 색인 URL 페이지 로딩 확인
indexBtn = None # 색인생성요청버튼(최초)
retryIndexBtn = None #색인다시요청(두번째)

WebDriverWait(driver, 10).until(EC.presence_of_element_located( (By.XPATH, "/html/body/div[1]/c-wiz[3]/div/div[2]/div[1]/div/div[1]/div/span/span/div") ))
print('로딩완료')
try:
    # 인덱스 시작
    #indexBtn = WebDriverWait(driver, 1).until(EC.element_to_be_clickable( (By.XPATH, "/html/body/div[7]/c-wiz[3]/div/div[2]/div[2]/div/div/div[1]/span/div[2]/div/c-wiz[2]/div[3]/span/div/span/span/div/span/span[1]") ))
    indexBtn = driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz[3]/div/div[2]/div[2]/div/div/div[1]/span/div[2]/div/c-wiz[2]/div[3]/span/div/span/span/div/span/span[1]')
    print('인덱스 시작!')
    indexBtn.click()
    time.sleep(1)
    # 색인완료 확인
    loadingPopup = WebDriverWait(driver, 300).until_not(EC.element_to_be_clickable( (By.XPATH, "/html/body/div[1]/div[6]/div[2]/div/div") ))
    print('인덱스 완료')
except Exception as e:
    print('이미 인덱스 되어 있음 패쓰..')
    












#driver.get("{}{}".format(self._url, '/manage/post'))
#driver.implicitly_wait(10)