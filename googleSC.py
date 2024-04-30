from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from urllib import parse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
class GoogleSC:
    def __init__(self, blog_url, driver: webdriver.Chrome):
        self._blog_url = blog_url
        self._driver = driver
        
    def indexUri(self, post_uri):
        print('# 색인 프로세스 시작 : {}'.format(post_uri))
        time.sleep(2)
        driver = self._driver
        driver.get("about:blank")
        driver.implicitly_wait(1)
        print('1')
        resource_id = parse.quote(self._blog_url)
        search_console_url = 'https://search.google.com/search-console/inspect?resource_id={}'.format(resource_id)
        driver.get(search_console_url)
        input = post_uri

        time.sleep(2)
        # 660 검색 누르고 하기
        # 661~ 바로 검색하기
        print('2')
        width = 660
        try:
            width = driver.execute_script("return window.innerWidth;")
            print('해상도 체크 - width : {}'.format(width))
        except Exception as e:
            print(e)
        #print('해상도 체크 : {}'.format(width))

        if width <= 660:
            # 검색 클릭
            print('[660px 이하] >> 검색 버튼 클릭')
            urlCheckBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.XPATH, "/html/body/div[1]/div[2]/header/div[2]/div[2]/div[2]/form/button[3]") ))
            urlCheckBtn.click()
            #print('검색버튼 clicked..')

        # 색인 URL 검색
        searchUrlInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.CSS_SELECTOR, "#gb > div.gb_sd.gb_ld.gb_yd div.gb_Fe > form > div > div > div > div > div > div.d1dlne > input.Ax4B8.ZAGvjd") ))
        print(3)                                                                          
        searchUrlInput.send_keys(input)
        time.sleep(1)
        searchUrlInput.send_keys(Keys.ENTER)
        print(4)

        # 색인 URL 페이지 로딩 확인
        isFirst = False
        WebDriverWait(driver, 20).until(EC.presence_of_element_located( (By.CSS_SELECTOR, "#yDmH0d > c-wiz.zQTmif.SSPGKf.eejsDc > div > div.OoO4Vb  div.Jjoxhd > div > div.eJo1Yb > div > span > span > div") ))
        print(5)
        try:
            # 인덱스 시작
            #indexBtn = driver.find_element(By.XPATH, "/html/body/div[7]/c-wiz[3]/div/div[2]/div[2]/div/div/div[1]/span/div[2]/div/c-wiz[2]/div[3]/span/div/span/span/div/span/span[1]")
            #indexBtn = WebDriverWait(driver, 1).until(EC.element_to_be_clickable( (By.XPATH, "/html/body/div[7]/c-wiz[3]/div/div[2]/div[2]/div/div/div[1]/span/div[2]/div/c-wiz[2]/div[3]/span/div/span/span/div/span/span[1]") ))
            indexBtn = WebDriverWait(driver, 1).until(EC.element_to_be_clickable( (By.CSS_SELECTOR, "#yDmH0d div.OoO4Vb > div.shSP > div > div > div.LgQiCc.vOSR6b.FDD67d.qtMyGd > span > div:nth-child(2) > div > c-wiz.FrvLod > div.CerIhf > span > div > span > span > div > span > span.cTsG4") ))

            #yDmH0d div.OoO4Vb > div.shSP > div > div > div.LgQiCc.vOSR6b.FDD67d.qtMyGd > span > div:nth-child(2) > div > c-wiz.FrvLod > div.CerIhf > span > div > span > span > div > span > span.cTsG4
            #yDmH0d div.OoO4Vb > div.shSP > div > div > div.LgQiCc.vOSR6b.FDD67d.qtMyGd > span > div:nth-child(2) > div > c-wiz.FrvLod > div.CerIhf > span > div > span > span > div > span > span.cTsG4
            print('색인 검색 시작')
            isFirst = True
            indexBtn.click()
            time.sleep(1)
            # 색인완료 확인
            #loadingPopup = WebDriverWait(driver, 300).until_not(EC.element_to_be_clickable( (By.XPATH, "/html/body/div[1]/div[6]/div[2]/div/div") ))
            loadingPopup = WebDriverWait(driver, 60 * 10).until(EC.presence_of_element_located( (By.CSS_SELECTOR, "#yDmH0d div[jscontroller='dGzwdb'] div[aria-label='색인 생성 요청됨']") ))
            
            print('색인 검색 완료')
        except Exception as e:
            if isFirst:
                print('색인 안되어 있는데 오류 e : {}'.format(e))
            else:
                print('이미 색인 되어 있음(PASS)')
        
        print('# 색인 프로세스 종료')


