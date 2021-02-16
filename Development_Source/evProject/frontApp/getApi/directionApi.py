# 네이버 검색 open api 사용 예제 : 블로그 검색
# requests 패키지 사용하여 코드를 좀 더 간단하게 변경

import requests  # 서버접속
from urllib.parse import urlparse    # 한글 처리

#
# url = "https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?"
#
# s_lat = "127.02532990776793"
# s_lng = "37.49734610716973"
# g_lat = "129.04004110841345"
# g_lng = "35.11585353782553"
# start = s_lat+","+s_lng
# goal = g_lat+","+g_lng
#
# keyword="start="+start+"&goal="+goal
# url_fin = url+keyword
#
# print(start)
# print(goal)
# print(keyword)
# print(url_fin)
# # get()안에 url과 headers를 포함 할 수 있음
# result = requests.get(urlparse(url_fin).geturl(),
#                       headers = {
#                           "X-NCP-APIGW-API-KEY-ID":"djtsnlvpvb",
#                                  "X-NCP-APIGW-API-KEY":"x4YIbhw6ZKQ6SQQ9y74hkqJiqx8pEtlfU99yp0Y9"})
# # print(result.json())
# # items를 제외한 4개의 key value 추출
# json_obj = result.json()
# print(json_obj)


def getDirectionApi(start,goal):
    url = "https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?"

    # s_lat = "127.02532990776793"
    # s_lng = "37.49734610716973"
    # g_lat = "129.04004110841345"
    # g_lng = "35.11585353782553"
    # start = s_lat + "," + s_lng
    # goal = g_lat + "," + g_lng

    # start = "127.02532990776793,37.49734610716973"
    # goal = "129.04004110841345,35.11585353782553"

    keyword = "start=" + start + "&goal=" + goal
    url_fin = url + keyword

    result = requests.get(urlparse(url_fin).geturl(),
                          headers={
                              "X-NCP-APIGW-API-KEY-ID": "djtsnlvpvb",
                              "X-NCP-APIGW-API-KEY": "x4YIbhw6ZKQ6SQQ9y74hkqJiqx8pEtlfU99yp0Y9"})
    json_obj = result.json()

    pathlist = json_obj['route']['traoptimal'][0]['path']
    # print(pathlist)
    # print(len(pathlist)) # 4649 너무많다
    if len(pathlist) > 100:

        div = len(pathlist)/100
        div = int(div)
        minimum_pathlist = []
        for i in range(0,len(pathlist),div):
            minimum_pathlist.append(pathlist[i])
        # print(len(minimum_pathlist))
    else:
        minimum_pathlist = pathlist
    print(type(minimum_pathlist))
    return minimum_pathlist
#
# data = getDirectionApi("127.02532990776793,37.49734610716973","129.04004110841345,35.11585353782553")
# print(data)



