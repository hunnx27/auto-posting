from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import sys
#sys.path.append('..')

class Tistory:

    def __init__(self, url, id, pw):
        self._url = url
        self._id = id
        self._pw = pw

    
    datas = [
        ("text","hiroo\n\n\nhello"),
        ("image","d:/2.Private/job/td_company/data/한소희 류준열 타임라인 정리 환승연애 인스타 블로그 주소/images/1.png"),
        ("text","hiroo\n\n\nhello"),
        ("text","hiroo\n\n\nhello"),
        ("image","d:/2.Private/job/td_company/data/한소희 류준열 타임라인 정리 환승연애 인스타 블로그 주소/images/1.png"),
        ]

    def write(self, title, datas):
        driver = webdriver.Chrome()
        driver.get("{}/manage".format(self._url))
        # /html/body/div[2]/div/div/div/div/div/a[2]

        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        # 로그인 페이지 이동
        loginbtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.XPATH, "/html/body/div[2]/div/div/div/div/div/a[2]") ))
        loginbtn.click()
        time.sleep(1)

        # ID, PW입력
        wait = WebDriverWait(driver, 3)
        idElm = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginId--1')))
        pwElm = driver.find_element(By.CSS_SELECTOR, '#password--2')
        loginBtnElm = driver.find_element(By.XPATH, '/html/body/div/div/div/main/article/div/div/form/div[4]/button[1]')
        time.sleep(1)
        idElm.click()
        import pyautogui
        import pyperclip
        time.sleep(1)
        pyperclip.copy(self._id)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pwElm.click()
        pyperclip.copy(self._pw)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)

        self.__captcha_check(driver) # 캡차 체크

        loginBtnElm.click()

        self.__captcha_check(driver) # 캡차 체크

        writeMoveBtnElm = wait.until(EC.element_to_be_clickable( (By.XPATH, '/html/body/div[2]/div[1]/div/div[3]/div/a[1]')))
        writeMoveBtnElm.click()

        # 티스토리 글쓰기
        ## 최초 알람 체크 및 취소
        from selenium.common.exceptions import NoAlertPresentException
        from selenium.webdriver.common.alert import Alert
        try:
            alert = wait.until(EC.alert_is_present())
            alert.dismiss() # 처음 알람이 있는경우 취소처리
        except NoAlertPresentException:
            print('알람이 없습니다.')

        # 타이틀 입력
        titleElm = wait.until(EC.element_to_be_clickable( (By.XPATH, '/html/body/div[1]/div/main/div/div[2]/textarea') ))
        titleElm.click()
        pyperclip.copy(title)
        pyautogui.hotkey("ctrl", "v")

        # 내용입력
        content = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(content)
        content_write = driver.find_element(By.XPATH, '/html/body')
        content_write.click()

        is_wait = False
        from imagelib import ImageLib

        for data in datas:
            if is_wait: time.sleep(2)
            type = data[0]
            context = data[1]
            if type == 'text':
                content_write.send_keys(context)
            elif type == 'image':
                ilib = ImageLib()
                ilib.copy(context)
                pyautogui.hotkey("ctrl", "v")
                is_wait = True

        driver.switch_to.default_content
        time.sleep(30)

        # 임시저장
        #driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/span/div/a[1]").click()

    # 캡차 체크
    def __captcha_check(self, driver, delay=3):
        try:
            time.sleep(delay)
            content = driver.find_element(By.TAG_NAME, "iframe")
            driver.switch_to.frame(content)
            captcha = driver.find_element(By.ID, "#recaptcha-anchor")
            captcha.click
            time.sleep(delay)
            driver.switch_to.default_content
        except Exception as e:
            print(e)