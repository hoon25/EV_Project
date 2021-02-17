# 제목: 네이버 검색 API 활용하기

# import
import json
import requests
import urllib.request
import urllib
from urllib.parse import quote  # 이 패키지는 한글을 ascii코드로 변환할 때 쓰입니다!!
# import pandas as pd  # return 받은 값들을 나중에는 데이터프레임 형태로 저장할 거에요!


def searchContent(keyword):
    # 애플리케이션 클라이언트 id 및 secret
    client_id = "Nnw848NWewOrG4KOqTKN"
    client_secret = "shhEpnNzy9"

    # 지역 검색 url
    # json 방식 https://openapi.naver.com/v1/search/book.json?query=python&display=3&sort=count
    url = "https://openapi.naver.com/v1/search/local.json"
    query = "?query=" + urllib.parse.quote(keyword)
    option = "&start=1&display=5&sort=comment"
    url_query = url + query + option

    # Open API 검색 요청 개체 설정
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    # 검색 요청 및 처리
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        # print(response_body.decode('UTF-8'))
        return response_body.decode('UTF-8')
    else:
        print("Error code:" + rescode)
        return None


# 프로그램 진입점
def main(keyword):
    # 검색 질의 요청
    res = searchContent(keyword)

    if (res == None):
        print("검색 실패!!!")
        exit()

    # 검색 결과를 json개체로 로딩
    jres = json.loads(res)
    if (jres == None):
        print("json.loads 실패!!!")
        exit()

    # 검색 결과의 items 목록의 각 항목(post)을 출력

    roadAddress = jres['items'][0]['roadAddress']
    print("searchRegion - ")
    print(roadAddress)
    # for i in range(len(jres)):
    #     roadAddress = jres['items'][i]['roadAddress']
    #     roadAddressList = [roadAddress]
    #     print(roadAddressList)
    return roadAddress



# 진입점 함수를 main으로 지정
# if __name__ == '__main__':
#     main()
