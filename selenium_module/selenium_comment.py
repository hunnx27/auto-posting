from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import sys

naver_id = ''
naver_pw = ''
if len(sys.argv) != 3:
    print("길이 :", len(sys.argv))
    print("ID와 비밀번호를 인자로 입력하세요.")
    sys.exit()
else:
    naver_id = sys.argv[1]
    naver_pw = sys.argv[2]
    print(naver_id, naver_pw, '테스트를 시작합니다.')


def autoComment(url, driver):
    try:
        # 자동화 URL 접속
        driver.get(url)
        time.sleep(2)

        # 메뉴 들어가기
        
        menuElm = driver.find_element(By.CSS_SELECTOR, '#app > div > header > div > div.gnb_r > a')
        menuElm.click()

        # 로그인화면 접속하기
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        wait = WebDriverWait(driver, 10)
        loginBtnElm = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#sideMenuContainer > header > div > div > div > a.nick.join')))
        loginBtnElm.click()
        time.sleep(2)

        # ID, PW입력
        print('id입력!!!!!!!!!!!!')
        wait = WebDriverWait(driver, 10)
        idElm = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#id')))
        idElm.click()
        pwElm = driver.find_element(By.CSS_SELECTOR, '#pw')
        loginBtnElm = driver.find_element(By.CSS_SELECTOR, '#log\.login')
        import pyautogui
        import pyperclip
        pyperclip.copy(naver_id)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pwElm.click()
        pyperclip.copy(naver_pw)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        loginBtnElm.click()

        # 새로운기기등록
        wait = WebDriverWait(driver, 10)
        newDvcBtnElm = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#frmNIDLogin > button.btn_check')))
        print('새로운기기등록!!!')
        newDvcBtnElm.click()
        #time.sleep(3)

        #app > div > div > div.comment_textarea_wrap > div > div > div > div > div
        # 댓글등록
        wait = WebDriverWait(driver, 10)
        textareaElm = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div > div > div.comment_textarea_wrap > div > div.textarea_write')))
        textareaElm.click()
        textareaInputElm = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div.comment_textarea_wrap > div > div.textarea_write > div > div > div')
        textareaInputElm.send_keys("열심히 하겠습니다.\n그렇습니다.")
        time.sleep(2)
        print('last btn load!!!')
        submitBtnElm = driver.find_element(By.CSS_SELECTOR, 'div.CafeCommentWriteFooter button.btn_done')
        #submitBtnElm.click()
        print('버튼 클릭은 주석처리함')
        time.sleep(3)
        print('process 종료')
    except Exception as e:
        print('오류가 발생했습니다.', e)


url = 'https://m.cafe.naver.com/ca-fe/web/cafes/23700418/articles/26837/comments?focus=68544428&fromList=true&menuId=110&tc=cafe_article_list'

from selenium.webdriver.common.by import By
driver1 = webdriver.Chrome()
#driver2 = webdriver.Chrome()
autoComment(url, driver1)
#autoComment(url, driver2)