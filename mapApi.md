- 네이버 API 
  1. NAVER Maps JavaScript API v3 기반으로 구현
     - https://navermaps.github.io/maps.js.ncp/docs/tutorial-2-Getting-Started.html
  2. 현재 내 위치 표시 -> HTML5 Geolocation API 활용
     - https://navermaps.github.io/maps.js.ncp/docs/tutorial-6-map-geolocation.example.html
  3. DB에서 전기차 충전소 위치 데이터 불러오기
     - 전기차 충전소 위치 마커 클러스터링
     - https://navermaps.github.io/maps.js.ncp/docs/tutorial-marker-cluster.example.html
     - 이슈) 클러스터링, 보이는 영역 지도만 마커 표시 이미지 - 오류x
       - home_path / url 
         - https://github.com/navermaps/maps.js/blob/master/docs/img/cluster-marker-1.png
         - https://github.com/navermaps/maps.js/blob/master/docs/img/marker-default.png
         - static 디렉토리에 이미지 파일 존재, load static 완료
       - 참고사이트 
         - https://www.zooo.kr/fxbbs/f_view.php?i_code=program&i_id=220

