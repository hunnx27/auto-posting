text = '[##_Image|kage@yppb8/btsGBxW9VA3/VD9OktLRgwslhatrKCMYt0/img.png|CDM|1.3|{"originWidth":480,"originHeight":693,"style":"alignCenter"}_##]'

DEFAULT_LINK = "https://blog.kakaocdn.net/dn"
linkarr = text.split('|')
imgarr = linkarr[1].split('kage@')
imgpath = imgarr[1]
link = "{}/{}".format(DEFAULT_LINK, imgpath)
REPLACE_TXT = '"style":"alignCenter"}_##]'
REPLACE_TXT_NEW = '"style":"alignCenter","link":"{}","isLinkNewWindow":true}}_##]'.format(link)
linktxt = text.replace(REPLACE_TXT, REPLACE_TXT_NEW)
print(linktxt)