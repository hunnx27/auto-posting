
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time




from selenium.webdriver.chrome.options import Options
#import subprocess
#subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')
option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=option)
url = 'https://superblo.tistory.com/manage/newpost'
driver.get(url)

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 3)
try:
    alert = wait.until(EC.alert_is_present())
    alert.dismiss() # 처음 알람이 있는경우 취소처리
except NoAlertPresentException:
    print('알람이 없습니다.')
except Exception:
    print('timeout')

time.sleep(5)

driver.get('https://chat.openai.com/c/f3ca1d2e-26bb-465f-8183-963ae07e00f0')