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

blogURL = 'https://superblo.tistory.com'

from googleSC import GoogleSC
sc = GoogleSC(blog_url=blogURL , driver=driver)

target = 'https://superblo.tistory.com/entry/%ED%95%9C%EC%86%8C%ED%9D%AC-%EC%89%AC%EC%A7%80-%EC%95%8A%EA%B3%A0-%ED%99%9C%EB%B0%9C%ED%95%9C-%EC%86%8C%EC%85%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%ED%99%9C%EB%8F%99-%ED%8C%AC%EB%93%A4%EA%B3%BC-%EC%86%8C%ED%86%B5'
sc.indexUri(target)


