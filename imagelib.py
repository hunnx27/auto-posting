from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

class ImageLib:

    # 워터마트 박기
    def draw_watermark(self, url):
        print("### DRAW WATERMARK START ###")
        # Image 로드
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))

        # 초기 변수 설정
        text = "JJ TV"
        image = image.convert("RGBA")
        width, height = image.size


        # 워터마크 추가
        ## 텍스트 이미지 만들기(투명마크를 위함)
        txt = Image.new('RGBA', image.size, (255,255,255,0))
        d = ImageDraw.Draw(txt)

        #ttf = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
        ttf = './fonts/LiberationSans-Regular.ttf'
        font = ImageFont.truetype(ttf, 30) # 워터마크에 사용할 폰트 설정
        d = ImageDraw.Draw(txt)

        x_point = width/2 # 글자를 출력할 x 축 Point : 가운데 정렬이므로 나누기 2 함
        y_point = height/2 # 글자를 출력할 y 축 Point : 가운데 정렬로 아래에서 계산 함
        bbox = d.textbbox((0,0),text, font)
        text_position = (x_point-(bbox[2]/2), y_point-(bbox[3]/2)) # 워터마크 위치

        text_color = (255, 0, 0, 20)
        d.text(text_position, text, fill=text_color, font=font)

        # border 그리기
        border_color = 'red'
        border_width = 4
        d.line(((0,-1+(border_width/2)), (width,-1+(border_width/2))), fill=border_color, width=border_width) # top border
        d.line(((0,height-(border_width/2)), (width,height-(border_width/2))), fill=border_color, width=border_width) # bottom border
        d.line(((width-(border_width/2),0), (width-(border_width/2),height)), fill=border_color, width=border_width) # bottom right
        d.line(((-1+(border_width/2),0), (-1+(border_width/2),height)), fill=border_color, width=border_width) # bottom left

        # 합성
        combined = Image.alpha_composite(image, txt)
        print("### DRAW WATERMARK END ###")
        return combined