from extractPost import ExtractPost
## 파싱 블로그 URL(티스토리, 모바일주소로 입력)
post_name="네이버블로6"
target_url = 'https://m.blog.naver.com/PostView.naver?blogId=yosiki1928&logNo=223387739725&parentCategoryNo=&categoryNo=1&viewDate=&isShowPopularPosts=false&from=postView'
#target_url = 'https://superblo.tistory.com/m/entry/%ED%85%8C%EB%AC%B4-%EC%82%AC%EA%B8%B0-%EB%85%BC%EB%9E%80%EA%B3%BC-%ED%99%98%EB%B6%88-%EC%9D%B4%EC%8A%88-%EC%97%90-%EB%8C%80%ED%95%9C-%EC%B4%9D-%EC%A0%95%EB%A6%AC'
platform = 'n' # t:티스토리 , n:네이버
expost = ExtractPost(
    target_url,
    post_name = post_name, 
    platform=platform,
    #savedir="D:/2.Private/job/td_company/data"
)

expost.parsing_blog()
savedimages = expost.getSavedImages()

