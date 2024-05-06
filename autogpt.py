
import pyautogui
import pyperclip
import time
from selenium import webdriver

class AutoGpt:

    def __init__(self, driver='', gpt_url='https://chat.openai.com/'):
        print('init')
        if(driver != ''):
            self._driver = driver
        else:
            self.driver = webdriver.Chrome()

        self._gpt_url = gpt_url

    def searchGPT(self, text):
        time.sleep(1)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.hotkey("enter")
        time.sleep(25)
        pyautogui.hotkey("ctrl", "shift", "c")
        pyautogui.hotkey("alt", "tab")
        paste = pyperclip.paste()
        print(paste)
        return paste
    
    def searchGPT2(self, text):
        print('[GPT ver2]step1')
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        
        driver = self._driver
        ## 최초 알람 체크 및 취소
        from selenium.common.exceptions import NoAlertPresentException
        from selenium.webdriver.common.alert import Alert
        try:
            wait = WebDriverWait(driver, 3)
            alert = wait.until(EC.alert_is_present())
            time.sleep(2)
            alert.dismiss() # 처음 알람이 있는경우 취소처리
        except NoAlertPresentException:
            print('알람이 없습니다.')
        except Exception as e:
            print('알람 에러 - {}'.format(e))

        print('[GPT ver2]step2')
        driver.get("about:blank")
        driver.implicitly_wait(10)
        driver.get(self._gpt_url)
        time.sleep(2)
        # 티스토리 글쓰기
        

        time.sleep(1)


        pyautogui.hotkey("alt", "tab")
        wait = WebDriverWait(driver, 10)
        time.sleep(3)
        pyperclip.copy(text)
        prompt = driver.find_element(By.CSS_SELECTOR, '#prompt-textarea')
        prompt.click()
        pyautogui.hotkey("ctrl", "v")
        print('paste!')
        time.sleep(1)
        pyautogui.hotkey("enter")
        print('enter!')
        print('gpt 응답중.....')
        time.sleep(3)
        gpttxt = ''
        try:
            wait = WebDriverWait(driver, 120)
            #elm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/div[2]/div[2]/form/div/div[2]/div/button")))
            #elm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/div[2]/div[2]//*/button")))
            elm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body//*/textarea[@id='prompt-textarea']/following-sibling::button[@disabled]")))
            print(elm.text)
            print('응답완료..5초뒤 복사!')
            time.sleep(3)
            pyautogui.hotkey("ctrl", "shift", "c")
            gpttxt = pyperclip.paste()
            print('paste text : {}'.format(gpttxt))
        except Exception as e:
            print(e)

        print('alt + tab?!')
        pyautogui.hotkey("alt", "tab")
        return gpttxt

