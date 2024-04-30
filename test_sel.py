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


# 인덱스 시작
print('찾기시작')
indexBtn = WebDriverWait(driver, 1).until(EC.element_to_be_clickable( (By.XPATH, "/html/body/div[7]/c-wiz[3]/div/div[2]/div[2]/div/div/div[1]/span/div[2]/div/c-wiz[2]/div[3]/span/div/span/span/div/span/span[1]") ))                                                 
print('인덱스 시작!')


    
