import requests  # 서버접속
from urllib.parse import urlparse    # 한글 처리

#
# url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?"
#
# keyword="query=강동구"
# url_fin = url+keyword
#
#
# # print(keyword)
# # print(url_fin)
# # get()안에 url과 headers를 포함 할 수 있음
# result = requests.get(urlparse(url_fin).geturl(),
#                       headers = {
#                           "X-NCP-APIGW-API-KEY-ID":"djtsnlvpvb",
#                                  "X-NCP-APIGW-API-KEY":"x4YIbhw6ZKQ6SQQ9y74hkqJiqx8pEtlfU99yp0Y9"})
# print(result.json())
# # items를 제외한 4개의 key value 추출
# json_obj = result.json()
# print(json_obj)


def getGeocode(query):
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?"

    keyword = "query=" + query
    url_fin = url + keyword

    result = requests.get(urlparse(url_fin).geturl(),
                          headers={
                              "X-NCP-APIGW-API-KEY-ID": "djtsnlvpvb",
                              "X-NCP-APIGW-API-KEY": "x4YIbhw6ZKQ6SQQ9y74hkqJiqx8pEtlfU99yp0Y9"})
    json_obj = result.json()
    roadAddress = lng = json_obj['addresses'][0]['roadAddress']
    jibunAddress = lng = json_obj['addresses'][0]['jibunAddress']
    lng = json_obj['addresses'][0]["x"]
    lat = json_obj['addresses'][0]["y"]
    list = [roadAddress, jibunAddress, lng, lat]
    print(list)
    return list

data = getGeocode("천호1동")
print(data)



