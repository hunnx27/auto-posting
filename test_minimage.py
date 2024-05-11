maxImageSize = 5
_max_ad_size = 3
imagelist = ['img1','img2','img3','img4','img5','img6','img7','img8', 'img9', 'img10']
ad_location_idx_list = list(range(min(len(imagelist), maxImageSize)))
ad_location_idx_list.remove(0)
import random
random.shuffle(ad_location_idx_list)
ad_location_idx_list = ad_location_idx_list[0:_max_ad_size-1]
ad_location_idx_list.insert(0, 0)
print(ad_location_idx_list)
text = '''
    글1
    [이미지 삽입 위치 1]
    글1
    [이미지 삽입 위치 2]
    글1
    [이미지 삽입 위치 3]
    글1
    [이미지 삽입 위치 4]
    글1
    [이미지 삽입 위치 5]
    글1
    [이미지 삽입 위치 6]
    글1
    [이미지 삽입 위치 7]
    글1
    [이미지 삽입 위치 8]
    글1
'''

for (idx, img) in enumerate(imagelist):
    
    if(idx+1<= maxImageSize):
        imgtag = img
    else:
        imgtag = '-'

    if idx in ad_location_idx_list:
        #광고 랜덤 삽입
        imgtag = '{}{}'.format(imgtag, ' self.__get_ad_script()')

    findtxt = '[이미지 삽입 위치 {}]'.format(idx+1)
    notfoundlist = []
    if text.find(findtxt) != -1:
        text = text.replace(findtxt, imgtag)
    else:
        text = text + '\n' + imgtag

print(text)