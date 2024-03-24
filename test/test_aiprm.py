# Deprecated
# 일단 이건 안됨!...[2024.03.20 CJH]

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
print('경로 : {}'.format(current_dir))
extension_relative_path = '\selenium_module\chrome_extension_AIPRM.crx'
extension_path = os.path.join(current_dir, extension_relative_path)
extension_path = 'D:/2.Private/job/td_company/auto_posting/selenium_module/chrome_extension_AIPRM.crx'
print('경로 : {}'.format(extension_path))

# 크롬 옵션 설정 (확장 프로그램 로드)
chrome_options = Options()
chrome_options.add_extension(extension_path)

print('hiroo')
# 크롬 브라우저 시작
driver = webdriver.Chrome(options=chrome_options)

# 웹 페이지 열기 (예시)
driver.get('https://chat.openai.com/')
handles = driver.window_handles
# 두 번째 탭으로 전환
driver.switch_to.window(handles[0])

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
wait = WebDriverWait(driver, 3)
loginElm = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/div/button[1]')))
loginElm.click()

def captcha_check(driver, delay=5):
    time.sleep(delay)
    content = driver.find_element(By.TAG_NAME, "iframe")
    print('step1')
    driver.switch_to.frame(content)
    print('step2')
    #captcha = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/label/input')))
    captcha = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/label/input')
    print(captcha.text)
    captcha.click()
    time.sleep(delay)
    driver.switch_to.default_content
    

captcha_check(driver, delay=8)

time.sleep(120)