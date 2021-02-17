from django.test import TestCase

# Create your tests here.
import requests  # 서버접속
from urllib.parse import urlparse    # 한글 처리
keyword = "맛집"
url = "https://openapi.naver.com/v1/search/blog?query="
url_fin = url+keyword
# get()안에 url과 headers를 포함 할 수 있음
result = requests.get(urlparse(url_fin).geturl(),
                      headers = {
                          "X-Naver-Client-Id":"F19oLmyXd7Olfjv_Ur8U",
                                 "x-Naver-Client-Secret":"6TQR__hlH9"})
# print(result.json())
# items 출력(검색 결과)
json_obj = result.json()
print(json_obj)