from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 포스팅 관련 모듈
class NaverPost:
     # travelhyuk
    def __init__(self, blogId):
        self.__blogId = blogId
        super().__init__()

    def getNewPost(self):
        url = 'https://m.blog.naver.com/PostList.naver?blogId={}&tab=1'.format(self.__blogId)
        driver = webdriver.Chrome()
        print('네이버 포스팅 스크래핑 시도 : {}'.format(url))
        driver.get(url)
        time.sleep(2)

        #print(driver.page_source)

        lis = driver.find_elements(By.XPATH, '/html/body/div[1]/div[5]/div[4]/div[2]/div/div[2]/ul/li')
        rs = []
        for li in lis:
            obj = {}
            try:
                #idx = i+1
                #print(idx)
                #test1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[4]/div[2]/div/div[2]/ul/li[{}]/div[1]/div[2]/div[2]/a/strong/span".format(idx))
                #test2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[4]/div[2]/div/div[2]/ul/li[{}]/div[1]/div[2]/div[2]/a".format(idx))
                test1 =  li.find_element(By.XPATH, './div[1]/div[2]/div[2]/a/strong/span')
                test2 = li.find_element(By.XPATH, './div[1]/div[2]/div[2]/a')
                title = test1.text
                link = test2.get_attribute(name="href")
                print("{} | {}".format(title, link))
                obj['title'] = title
                obj['link'] = link
                rs.append(obj)
            except Exception as e:
                print('Error....')
                #print(e)
        print('네이버 포스팅 스크래핑 완료 : {}개'.format(len(rs)))

        return rs


# 댓글 관련 모듈 작성
class NaverComment:
    def __init__(self):
        print('init Comment')
        super().__init__()

