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
        url = 'https://m.blog.naver.com/PostList.naver?blogId={}&categoryNo=0&listStyle=card&tab=1'.format(self.__blogId)
        driver = webdriver.Chrome()
        print('네이버 포스팅 스크래핑 시도 : {}'.format(url))
        driver.get(url)
        time.sleep(2)

        #print(driver.page_source)
#/html/body/div[1]/div[5]/div[2]/div[2]/div/div[2]/ul/li[1]
#/html/body/div[1]/div[5]//*[@id='contentslist_block']//*div[2]/div/div[2]/ul/li
        lis = driver.find_elements(By.XPATH, "/html/body/div[1]/div[5]//*[@id='contentslist_block']//*[@class='list_block__XlpUJ']/div/div[2]/ul/li")
        rs = []
        for li in lis:
            col1 = {}
            col2 = {}
            try:
                #idx = i+1
                #print(idx)
                #test1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[4]/div[2]/div/div[2]/ul/li[{}]/div[1]/div[2]/div[2]/a/strong/span".format(idx))
                #test2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[4]/div[2]/div/div[2]/ul/li[{}]/div[1]/div[2]/div[2]/a".format(idx))
                col1_txt =  li.find_element(By.XPATH, './div[1]/div[2]/div[2]/a/strong/span')
                col1_a = li.find_element(By.XPATH, './div[1]/div[2]/div[2]/a')
                title = col1_txt.text
                link = col1_a.get_attribute(name="href")
                #print("{} | {}".format(title, link))
                col1['title'] = title
                #또는 새폴더 불용 특수문자만 넣기
                import re
                titleregex = re.sub(r'[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','', title)
                titleregex = re.sub(r'[\/:*?"><|]','', titleregex)
                col1['titleregex'] = titleregex
                col1['link'] = link
                rs.append(col1)

                col2_txt =  li.find_element(By.XPATH, './div[2]/div[2]/div[2]/a/strong/span')
                col2_a = li.find_element(By.XPATH, './div[2]/div[2]/div[2]/a')
                title = col2_txt.text
                link = col2_a.get_attribute(name="href")
                #print("{} | {}".format(title, link))
                col2['title'] = title
                #또는 새폴더 불용 특수문자만 넣기
                import re
                titleregex = re.sub(r'[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','', title)
                titleregex = re.sub(r'[\/:*?"><|]','', titleregex)
                col2['titleregex'] = titleregex
                col2['link'] = link
                rs.append(col2)
            except Exception as e:
                print('Error....')
                #print(e)
        print('네이버 포스팅 스크래핑 완료 : {}개'.format(len(rs)))
        driver.quit()
        return rs


# 댓글 관련 모듈 작성
class NaverComment:
    def __init__(self):
        print('init Comment')
        super().__init__()

