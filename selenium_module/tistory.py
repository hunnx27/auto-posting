from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import sys
#sys.path.append('..')

class Tistory:

    def __init__(self, url, id='', pw='', driver=''):
        self._url = url
        self._id = id
        self._pw = pw
        if driver!='':
            self._driver = driver
        else:
            self._driver = webdriver.Chrome()

    # Deprecated
    def login(self):
        driver = self._driver

        # 로그인 페이지 이동
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        loginbtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.XPATH, "/html/body/div[2]/div/div/div/div/div/a[2]") ))
        loginbtn.click()
        time.sleep(1)
        import pyautogui
        import pyperclip
        from selenium.webdriver.common.keys import Keys

        # ID, PW입력
        wait = WebDriverWait(driver, 3)

        idElm = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginId--1')))
        pwElm = driver.find_element(By.CSS_SELECTOR, '#password--2')
        loginBtnElm = driver.find_element(By.CSS_SELECTOR, '#mainContent > div > div > form > div.confirm_btn > button.btn_g.highlight.submit')
        time.sleep(1)
        idElm.click()
        
        time.sleep(1)
        pyperclip.copy(self._id)
        time.sleep(1)
        idElm.send_keys(Keys.CONTROL, "v")
        #pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pwElm.click()
        pyperclip.copy(self._pw)
        time.sleep(1)
        #pyautogui.hotkey("ctrl", "v")
        pwElm.send_keys(Keys.CONTROL, "v")
        time.sleep(1)
        #self.__captcha_check(driver) # 캡차 체크
        time.sleep(1)
        loginBtnElm.click()
        #self.__captcha_check(driver) # 캡차 체크

    def write(self, title, datas):
        print('step1')
        driver = self._driver
        driver.get("{}".format(self._url))
        # /html/body/div[2]/div/div/div/div/div/a[2]

        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        wait = WebDriverWait(driver, 3)
        writeMoveBtnElm = wait.until(EC.element_to_be_clickable( (By.XPATH, '/html/body/div[2]/div[1]/div/div[3]/div/a[1]')))
        writeMoveBtnElm.click()
        print('step2')
        # 티스토리 글쓰기
        ## 최초 알람 체크 및 취소
        from selenium.common.exceptions import NoAlertPresentException
        from selenium.webdriver.common.alert import Alert
        print('step3')
        try:
            alert = wait.until(EC.alert_is_present())
            alert.dismiss() # 처음 알람이 있는경우 취소처리
        except NoAlertPresentException:
            print('알람이 없습니다.')
        except Exception as e:
            print('알람오류 - {}'.format(e))

        # 마크다운으로 변경하기
        print('마크다운으로 변경하기')
        editorModeChangeBtnElm = wait.until(EC.element_to_be_clickable( (By.CSS_SELECTOR, '#editor-mode-layer-btn-open') ))
        editorModeChangeBtnElm.click()
        time.sleep(1)
        markdownModeBtnElm = wait.until(EC.element_to_be_clickable( (By.CSS_SELECTOR, '#editor-mode-markdown') ))
        markdownModeBtnElm.click()
        time.sleep(1)
        try:
            alert = wait.until(EC.alert_is_present())
            alert.accept() # 처음 알람이 있는경우 취소처리
        except NoAlertPresentException:
            print('알람이 없습니다.')
        except Exception as e:
            print('알람오류 - {}'.format(e))

        # 타이틀 입력
        titleElm = wait.until(EC.element_to_be_clickable( (By.XPATH, '/html/body/div[1]/div/main/div/div[2]/textarea') ))
        titleElm.click()
        import pyautogui
        import pyperclip
        pyperclip.copy(title)
        pyautogui.hotkey("ctrl", "v")

        # 내용입력
        content = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(content)
        content_write = driver.find_element(By.XPATH, '/html/body')
        content_write.click()

        from imagelib import ImageLib
        for data in datas:
            time.sleep(3)
            type = data[0]
            context = data[1]
            if type == 'text':
                print('text copy')
                content_write.send_keys(context)
            elif type == 'image':
                ilib = ImageLib()
                ilib.copy(context)
                print('image copy')
                pyautogui.hotkey("ctrl", "v")

        driver.switch_to.default_content()
        time.sleep(3)
        
        # 임시저장
        import pdb
        #pdb.set_trace()
        tempSave = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/span/div/a[1]")
        tempSave.click()
        time.sleep(2)
        pyautogui.hotkey("alt", "tab")

    # 캡차 체크
    def __captcha_check(self, driver, delay=3):
        try:
            time.sleep(delay)
            content = driver.find_element(By.TAG_NAME, "iframe")
            driver.switch_to.frame(content)
            captcha = driver.find_element(By.ID, "recaptcha-anchor")
            captcha.click()
            time.sleep(delay)
            driver.switch_to.default_content
        except Exception as e:
            print(e)