from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import sys
#sys.path.append('..')

class Tistory:

    def __init__(self, url, id='', pw='', driver='', max_ad_size=3, ad_map=None):
        self._url = url
        self._id = id
        self._pw = pw
        self._max_ad_size = max_ad_size
        self._ad_map = ad_map
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

    def exportImageLinkAndMergeTextAndGetText(self, savedimages, gptText, maxImageLen=999):
        text = gptText
        imgArr = self.__getImageTags(savedimages=savedimages)
        ad_location_idx_list = list(range(min(len(imgArr), maxImageLen)))
        ad_location_idx_list.remove(0)
        import random
        random.shuffle(ad_location_idx_list)
        ad_location_idx_list = ad_location_idx_list[0:self._max_ad_size-1]
        ad_location_idx_list.insert(0, 0)
        for (idx, imgtag) in enumerate(imgArr):
            #if len(imgArr) == idx+1:
            #    break
            
            if(idx+1<= maxImageLen):
                try:
                    imgtag = self.__imageLinkInsert(imgtag=imgtag)
                except Exception as e:
                    print('__imageLinkInsert err : {}'.format(e))
            else:
                imgtag = ''

            if idx in ad_location_idx_list:
                #광고 랜덤 삽입
                imgtag = '{}{}'.format(imgtag, self.__get_ad_script())

            findtxt = '[이미지 삽입 위치 {}]'.format(idx+1)
            notfoundlist = []
            if text.find(findtxt) != -1:
                text = text.replace(findtxt, imgtag)
            else:
                text = text + '\n' + imgtag
            
            #print('#text2 : {}'.format(text))

        # 남은 [이미지 삽입 위치 ~] 있는 경우 제거
        filtered_test = self.__remove_empty_image_lines(text)
        time.sleep(1)
        return filtered_test

    def __remove_empty_image_lines(self, text):
            lines = text.split('\n')  # 줄 단위로 분할
            #filtered_lines = [line for line in lines if not '[이미지 삽입 위치' in line]  # 이미지 삽입 위치를 포함하지 않는 줄 선택
            filtered_lines = [line for line in lines if not '[이미지' in line]  # 이미지 삽입 위치를 포함하지 않는 줄 선택
            return '\n'.join(filtered_lines)  # 처리된 줄을 다시 합침

    def __getImageTags(self, savedimages):
        import pyautogui
        
        print('[이미지태그가져오기]step1')
        time.sleep(5)
        pyautogui.hotkey("alt", "tab")
        driver = self._driver
        driver.get("about:blank")
        driver.implicitly_wait(10)
        driver.get("{}{}".format(self._url, '/manage/post'))
        driver.implicitly_wait(10)
        
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        wait = WebDriverWait(driver, 3)
        #writeMoveBtnElm = wait.until(EC.element_to_be_clickable( (By.XPATH, '/html/body/div[2]/div[1]/div/div[3]/div/a[1]')))
        #writeMoveBtnElm = wait.until(EC.element_to_be_clickable( (By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/a[1]')))
        #writeMoveBtnElm = wait.until(EC.element_to_be_clickable( (By.CSS_SELECTOR, '#kakaoHead > div > div.info_tistory > div > a.btn_tistory.btn_log_info')))
        #writeMoveBtnElm.click()

        print('[이미지태그가져오기]step2')
        # 티스토리 글쓰기
        ## 최초 알람 체크 및 취소
        from selenium.common.exceptions import NoAlertPresentException
        from selenium.webdriver.common.alert import Alert
        print('[이미지태그가져오기]step3')
        try:
            alert = wait.until(EC.alert_is_present())
            alert.dismiss() # 처음 알람이 있는경우 취소처리
        except NoAlertPresentException:
            print('알람이 없습니다.')
        except Exception as e:
            print('알람오류 - {}'.format(e))

        # 내용입력
        content = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(content)
        content_write = driver.find_element(By.XPATH, '/html/body')
        content_write.click()

        from imagelib import ImageLib
        import pyautogui
        import pyperclip

        for imgUrl in savedimages:
            try:
                time.sleep(0.3)
                ilib = ImageLib()
                ilib.copy(imgUrl)
                print('image copy')
                pyautogui.hotkey("ctrl", "v")
            except Exception as e:
                print(e)

        driver.switch_to.default_content()

        # HTML 모드 에디터 변경하기
        print('HTML 모드 에디터 변경하기')
        editorModeChangeBtnElm = wait.until(EC.element_to_be_clickable( (By.CSS_SELECTOR, '#editor-mode-layer-btn-open') ))
        editorModeChangeBtnElm.click()
        time.sleep(1)
        markdownModeBtnElm = wait.until(EC.element_to_be_clickable( (By.CSS_SELECTOR, '#editor-mode-html-text') ))
        markdownModeBtnElm.click()
        time.sleep(1)
        try:
            alert = wait.until(EC.alert_is_present())
            alert.accept() # 처음 알람이 있는경우 취소처리
        except NoAlertPresentException:
            print('알람이 없습니다.')
        except Exception as e:
            print('알람오류 - {}'.format(e))

        print('## HTML 에디터 화면 소스 출력 ##')
        time.sleep(3)
        textarea = driver.find_element(By.CSS_SELECTOR, '#html-editor-container > div.mce-edit-area > div > textarea')
        textarea_txt = textarea.get_attribute('innerHTML')
        
        #print(textarea)
        print('# textAREA 파싱!!!!!!!!!')
        print(textarea_txt)
        
        txt = textarea_txt
        imgs = txt.replace('&lt;p&gt;', '').replace('&lt;/p&gt;', '')
        imgsArr = imgs.split(']')
        for (idx, img) in  enumerate(imgsArr):
            imgsArr[idx] = img + ']'

        pyautogui.hotkey("alt", "tab")
        time.sleep(3)
        return imgsArr

    def __imageLinkInsert(self, imgtag):
        DEFAULT_LINK = "https://blog.kakaocdn.net/dn"
        linkarr = imgtag.split('|')
        imgarr = linkarr[1].split('kage@')
        imgpath = imgarr[1]
        link = "{}/{}".format(DEFAULT_LINK, imgpath)
        REPLACE_TXT = '"style":"alignCenter"}_##]'
        #REPLACE_TXT_NEW = '"style":"alignCenter","link":"{}","isLinkNewWindow":true}}_##]'.format(link)
        REPLACE_TXT_NEW = '"style":"alignCenter","link":"{}"}}_##]'.format(link)
        result = imgtag.replace(REPLACE_TXT, REPLACE_TXT_NEW)
        return result
    
    
    def getPostUri(self, title):
        from urllib import parse
        self._url
        post_uri = '{}{}{}'.format(self._url, '/entity/', parse.quote(title))
        return post_uri

    def write(self, title, datas, isSave=False):
        time.sleep(1)
        print('[write]step1')
        driver = self._driver
        driver.get("about:blank")
        driver.implicitly_wait(10)
        driver.get("{}{}".format(self._url, '/manage/post'))
        # /html/body/div[2]/div/div/div/div/div/a[2]

        import pyautogui
        pyautogui.hotkey("alt", "tab")
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        wait = WebDriverWait(driver, 5)
        #writeMoveBtnElm = wait.until(EC.element_to_be_clickable( (By.XPATH, '/html/body/div[2]/div[1]/div/div[3]/div/a[1]')))
        #writeMoveBtnElm.click()
        print('[write]step2')
        # 티스토리 글쓰기
        ## 최초 알람 체크 및 취소
        from selenium.common.exceptions import NoAlertPresentException
        from selenium.webdriver.common.alert import Alert
        print('[write]step3')
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
        #content = driver.find_element(By.TAG_NAME, "iframe")
        #driver.switch_to.frame(content)
        #content_write = driver.find_element(By.XPATH, '/html/body')
       # content_write.click()
        time.sleep(1)
        pyautogui.hotkey("tab")
        time.sleep(0.3)
        pyautogui.hotkey("tab")
        
        from imagelib import ImageLib
        for data in datas:
            time.sleep(1)
            type = data[0]
            context = data[1]
            if type == 'text':
                print('text copy')
                #content_write.send_keys(context)
                pyperclip.copy(context)
                pyautogui.hotkey("ctrl", "v")
            elif type == 'image':
                try:
                    ilib = ImageLib()
                    ilib.copy(context)
                    print('image copy')
                    pyautogui.hotkey("ctrl", "v")
                except Exception as e:
                    pyperclip.copy('')
                    pyautogui.hotkey("ctrl", "v")

        driver.switch_to.default_content()
        time.sleep(3)
        
        if isSave:

            # 완료 버튼
            saveButton = driver.find_element(By.CSS_SELECTOR, "#publish-layer-btn")
            saveButton.click()
            time.sleep(1)

            # 공개 - 라디오박스
            openRadio = driver.find_element(By.CSS_SELECTOR, "#open20")
            openRadio.click()
            time.sleep(0.5)

            # 발행하기 버튼
            publishButton = driver.find_element(By.CSS_SELECTOR, "#publish-btn")
            publishButton.click()
            
            firstContent = wait.until(EC.element_to_be_clickable( (By.XPATH, '/html/body//*//div[@class="wrap_list"]//ul[@class="list_post list_post_type2"]/li[1]/div[2]/strong/a') ))
            urlPublished = firstContent.get_attribute("href")
            print('1. {}'.format(urlPublished))
            uri = urlPublished.split('/entry/')[1]
            print('2. {}'.format(uri))
            urlPublished = '{}{}{}'.format(self._url, '/entry/', uri)
            print('3. {}'.format(urlPublished))
        else:
            # 임시저장
            tempSave = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/span/div/a[1]")
            tempSave.click()
            urlPublished = '#### Warn | Non Published. You should publish First!'

        time.sleep(1)
        pyautogui.hotkey("alt", "tab")
        time.sleep(2)

        return urlPublished
        

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

    def __get_ad_script(self):
        ad_script = '{}{}'.format('\n', self._ad_map[self._url]) if self._ad_map!=None and self._ad_map[self._url]!=None else ''
        return ad_script