from bs4 import BeautifulSoup
import requests
import os
from imagelib import ImageLib

class ExtractPost:

    def __init__(self, target_url, post_name="블로그", platform="t", savedir="D:/2.Private/job/td_company/data", savefolder='saved'):
        print("~~~~~~~~~~~~init~~~~~~~~~~~~~~~~~~")
        self._idx = 0
        self._target_url = target_url
        self._post_name = post_name
        self._platform = platform
        self._savedir = savedir
        self._savedImageDir = ''
        self._saveFolder =savefolder
        self._text = ''
        self._images = []


    def getSavedImages(self):
        return self._images
    
    def getTitle(self):
        return self._post_name
    
    def getText(self):
        return self._text
    
    # 폴더 체크 및 폴더 생성 함수
    def __checkOrDirs(self, file_path):
        if not os.path.exists(file_path):
            try:
                os.makedirs(file_path)
                return True
            except OSError:
                print('Error: Creating ')
                return False
        else:
            return True

    # HTML 파서
    def __html_parser(self, tag):
        if tag.name == 'img':
            # 이미지 처리
            # img tag 가져오기
            self._idx = self._idx+1
            url = tag.attrs['src']
            if 'data-lazy-src' in tag.attrs:
                url = tag.attrs['data-lazy-src']
            saved_folder_dir = self._savedir + "/" + self._saveFolder  + "/images"
            self._savedImageDir = saved_folder_dir
            saved_file_name =  str(self._idx) + '.png'
            ilib = ImageLib()
            savedFilePath = ''
            if self.__checkOrDirs(saved_folder_dir) :
                savedFilePath = saved_folder_dir + "/" + saved_file_name
                ilib.draw_watermark(url).save(savedFilePath)
                self._images.append(savedFilePath)
                
            #print('pass')
            return '\n[이미지 삽입 위치 {}]\n'.format(str(self._idx))
        if tag.get_text().strip() == '':
            return ''
        elif tag.name == 'p':
            # p tag 가져오기
            return tag.get_text().strip()
        elif tag.name == 'h1' or tag.name == 'h2' or tag.name == 'h3':
            # h1,h2,h3 tag 가져오기
            return '\n\n'+tag.get_text().strip()
        else:
            return '[ELSE][' + tag.name + ']' + tag.get_text().strip() + ";"
        
    def __html_parser2(self, tag):
        if tag.name == 'img':
            # 이미지 처리
            # img tag 가져오기
            self._idx = self._idx+1
            url = tag.attrs['src']
            if 'data-lazy-src' in tag.attrs:
                url = tag.attrs['data-lazy-src']
            saved_folder_dir = self._savedir + "/" + self._saveFolder  + "/images"
            self._savedImageDir = saved_folder_dir
            saved_file_name =  str(self._idx) + '.png'
            print(saved_folder_dir)
            ilib = ImageLib()
            savedFilePath = ''
            if self.__checkOrDirs(saved_folder_dir) :
                savedFilePath = saved_folder_dir + "/" + saved_file_name
                ilib.draw_watermark(url).save(savedFilePath)
                self._images.append(savedFilePath)
            #print('pass')
            return ('image', savedFilePath)
        if tag.get_text().strip() == '':
            return ('text', '')
        elif tag.name == 'p':
            # p tag 가져오기
            return ('text', tag.get_text().strip())
        elif tag.name == 'h1' or tag.name == 'h2' or tag.name == 'h3':
            # h1,h2,h3 tag 가져오기
            return ('text', '\n\n'+tag.get_text().strip())
        else:
            return

    # 블로그 포스팅 가져오기
    def __get_content(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
        req = requests.get(self._target_url)
        content = req.content
        #print(req.content.decode('utf-8'))

        soup = BeautifulSoup(content, 'html.parser')

        # 특정 태그 제거
        for tag in soup.select('.og-title,.og-desc,.og-host'): # 제외할 태그 목록
            print('[EXTRACT]' + tag.get_text())
            tag.extract()

        # 콘텐츠 선택
        contents = []
        if self._platform == 't':
            print('#############티스토리#########')
            contents = soup.select_one('div.blogview_content')
        else:
            print('#############네이버#########')
            contents = soup.select_one('div.se-main-container')

        result = list(map(self.__html_parser, contents.find_all(['img', 'p', 'h3', 'h2', 'h1'])))
        #result = list(map(html_parser, contents.find_all()))

        # 필터링
        for i in range(len(result)):
            text = result[i]
            text = text.replace(u"\xa0", u"")
            text = text.replace(u"\u200b", u"")
            result[i] = text
        result = list(filter(None, result))

        return result

    # 실제 파싱 실행 및 파일 저장
    def parsing_blog(self):
        contents = self.__get_content()
        text = "\n".join(contents)
        #print(text)
        self._text = text
        file_path = self._savedir + "/" + self._saveFolder
        if self.__checkOrDirs(file_path):
            t = open(file_path + '/content.txt', 'w', encoding='utf-8')
            t.write(text)