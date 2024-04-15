'''
1) 이슈 블로그 광고(one.tddiary.com)
<div><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7092537400368094"
     crossorigin="anonymous"></script>
<!-- onetd사이트 광고 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-7092537400368094"
     data-ad-slot="8469311447"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script></div>

1) 영화, 티비 블로그 광고(cinema.tddiary.com)
<div><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7092537400368094"
     crossorigin="anonymous"></script>
<!-- CINEMA 사이트 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-7092537400368094"
     data-ad-slot="8166198730"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script></div>

3) 지훈 사이트 광고(https://superblo.tistory.com)
<div><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7092537400368094"
     crossorigin="anonymous"></script>
<!-- 디스플레이(하단) -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-7092537400368094"
     data-ad-slot="2429257873"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script></div>
'''

# one.tddiary.com
ad1 = '''
<div><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7092537400368094"
     crossorigin="anonymous"></script>
<!-- onetd사이트 광고 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-7092537400368094"
     data-ad-slot="8469311447"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script></div>
'''
# cinema.tddiary.com
ad2 = '''
<div><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7092537400368094"
     crossorigin="anonymous"></script>
<!-- CINEMA 사이트 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-7092537400368094"
     data-ad-slot="8166198730"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script></div>
'''
# https://superblo.tistory.com
ad3 ='''
<div><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7092537400368094"
     crossorigin="anonymous"></script>
<!-- 디스플레이(하단) -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-7092537400368094"
     data-ad-slot="2429257873"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script></div>
'''

ad_map ={
    'one.tddiary.com': ad1,
    'cinema.tddiary.com': ad2,
    'https://superblo.tistory.com': ad3
}

#print(ad_map['one.tddiary.com'])

# 랜덤으로 광고 박는 로직
MAX_AD_SIZE = 3
img1 = '[##_Image|kage@1.img_##]'
img2 = '[##_Image|kage@2.img_##]'
img3 = '[##_Image|kage@3.img_##]'
img4 = '[##_Image|kage@4.img_##]'
img5 = '[##_Image|kage@5.img_##]'
img6 = '[##_Image|kage@6.img_##]'
img7 = '[##_Image|kage@7.img_##]'
img8 = '[##_Image|kage@8.img_##]'
imgArr = [img1, img2, img3, img4, img5, img6, img7, img8]
list = list(range(len(imgArr)))
print(list)
import random
random.shuffle(list)
list = list[0:MAX_AD_SIZE]
print(list)
for (idx, img) in enumerate(imgArr):
    if idx in list:
        print('[{}]{}\n{}'.format(idx, img, ad_map['one.tddiary.com']))
     # 여기는 기존로직 그대로