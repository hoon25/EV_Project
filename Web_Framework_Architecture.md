## 개발 프레임워크 설계

> - 요구사항
>
>   - 기능
>     - 전기차 충전소 위치찾기
>     - 네이버 사용자 인증
>     - DB연동
>     - GPS, 지도, CCTV 연동 등..
>   - 가격
>     - 무료
>   - 개발편의성
>     - 파이썬은 쉽고 간결함, 문법의 일관성, 빠르게 개발할 수 있는 생산성을 가지고 있으며 다양한 기능을 제공해주는 라이브러리, C언어와의 접착성, 콜백함수, 람다 함수, 이터레이터, 제너레이터 등이 있다.
>     - Django는 파이썬의 프레임워크이며 개발을 바로 시작할 수 있도록 프로그래밍 뼈대를 만들어 주고, 웹 프로그래밍에 필요한 파이썬 표준 라이브러리를 활용, 웹 서버/웹 클라이언트를 개발, 어렵게 생각되는 데이터베이스 연동, 어드민 관리 기능이 쉽게 처리 된다.
>
> - 개발환경
>
>   - OS : CentOS v7.9.2009
>   - git : https://github.com/hoon25/EV_Project
>   - 사용할 개발 프레임워크 : Django v.3.1.5
>   - 사용할 언어 : python v3.8.1
>   - 사용할 DB : mysql v8.0.23
>
>   - 개발 Tool : Pycharm Community Edition 2020.3.3, MySQL Workbench 8.0 CE
>
> - <u>**각 기능별 사용할 플랫폼**</u>
>
>   - 로그인 (서은상)
>
>     - 사이트 내 로그인/회원가입
>     - 네이버 로그인
>       - https://developers.naver.com/docs/login/api/
>
>   - DB (김지윤)
>
>     - 데이터소스 구성 
>
>       : 대부분 오픈API의 데이터, 예약 관련 데이터 구성 필요
>
>     - DB쿼리만 기록 할지? 쿼리 결과까지 기록할지?
>
>   - 오픈 API연동 (정은경)
>
>     - 전기차 충전소 운영정보 : https://www.data.go.kr/iim/api/selectAPIAcountView.do
>     -  한국환경공단_전기자동차 충전소 정보 : https://www.data.go.kr/iim/api/selectAPIAcountView.do
>     - 주유소 가격과 고속도로 통행량의 상관성 (통행량) : https://www.data.go.kr/iim/api/selectAPIAcountView.do
>     - 고속도로 휴게소 정보 (주유소) : https://www.data.go.kr/iim/api/selectAPIAcountView.do
>     - 네이버 로그인 : https://developers.naver.com/docs/login/api/
>     - 네이버지도 : https://www.ncloud.com/product/applicationService/maps
>     - CCTV : 1. http://openapi.its.go.kr/portal/dev/dev6.do, 
>       2. https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=100&sortColumn=&sortDirection=&infId=VIPK0N53968Q7DV5TT2312643570&infSeq=3&order=
>
>   - API 활용하여 전기차 중전소 연동 (서은상)
>
>     - 한국환경공단_전기자동차 충전소 정보 : https://www.data.go.kr/iim/api/selectAPIAcountView.do
>
>   - GPS 기반 가까운 충전소 찾기 (정은경)
>
>     - 위도,경도 활용한 좌표간의 거리 구하는 법 : https://action713.tistory.com/entry/mysql-%EC%9C%84%EB%8F%84-%EA%B2%BD%EB%8F%84-%ED%99%9C%EC%9A%A9%ED%95%9C-%EC%A2%8C%ED%91%9C%EA%B0%84%EC%9D%98-%EA%B1%B0%EB%A6%AC-%EA%B5%AC%ED%95%98%EB%8A%94%EB%B2%95-lng-lat-%EA%B0%80%EC%A7%80%EA%B3%A0-%EC%A2%8C%ED%91%9C-%EA%B7%BC%EB%B0%A9-%EC%9C%84%EC%B9%98-%EA%B5%AC%ED%95%98%EA%B8%B0
>     - GPS 기반 반경 2km 내 가까운 충전소 찾기
>
>   - API 활용하여 지도 연동 (최창훈) 
>
>     - 한국환경공단_전기자동차 충전소 정보 : https://www.data.go.kr/iim/api/selectAPIAcountView.do
>
>   - ~~API 활용하여 CCTV 연동 (김지윤)~~ 
>
>   - 별점 및 리뷰 (최창훈)
>
>     - 충전소 별점 및 리뷰 등록
>     - 마이페이지-리뷰관리 조회, 수정, 삭제 가능
>
>   - 충전소 근처 음식점/놀거리 컨텐츠 추천 (김보라)
>
>     - 위도,경도 활용한 좌표간의 거리 구하는 법 : https://action713.tistory.com/entry/mysql-%EC%9C%84%EB%8F%84-%EA%B2%BD%EB%8F%84-%ED%99%9C%EC%9A%A9%ED%95%9C-%EC%A2%8C%ED%91%9C%EA%B0%84%EC%9D%98-%EA%B1%B0%EB%A6%AC-%EA%B5%AC%ED%95%98%EB%8A%94%EB%B2%95-lng-lat-%EA%B0%80%EC%A7%80%EA%B3%A0-%EC%A2%8C%ED%91%9C-%EA%B7%BC%EB%B0%A9-%EC%9C%84%EC%B9%98-%EA%B5%AC%ED%95%98%EA%B8%B0
>     - GPS기반 반경 2km 내 음식점/놀거리 컨텐츠 추천
>
>   - 충전소 대기자 조회 (김보라)
>
>     - 충전소 상세 내역 테이블에 대기자 수 디스플레이
>
>   - 충전소 예약 서비스 (정은경)
>
>     - 충전소 상세 내역 테이블에 예약 버튼 추가하여 마이페이지-예약내역에서 조회 
>     - (+추가옵션) 더미데이터 몇 개 구성하여 연동할 수도 있음 
>
>   - 충전소 사용 혼잡도 (김지윤)
>
>     - 충전소의 충전기 80% 사용 시 : 빨간색
>     - 충전소의 충전기 50 이상 ~ 80% 미만 사용 시 : 노란색
>     - 충전소의 충전기 50% 미만 사용 시 : 초록색 
>
> - 로그 설계 
>
>   - 로그 포맷 
>
>   - 로그 어떻게 분리할지 
>
>     - timing : 기능 개발시 로깅도
>
>     - purpose : 기능의 목표에 맞춰서 가설확인, 지표측정
>
>     - attribute : 필요한 항목을 정함
>
>       예시1) 개인을 식별할 수 있는 정보 : 가입전-후 / 로그인 전-후
>
>       예시2) 정책 변경에 따라 개인 식별 정보가 바뀔 수 있음에 대비 : ISMS 인증을 위한 개인 정보보호 적용, 탈퇴자 처리 정책 변경
>
>       예시3) 식별 목적 외에도 segmentation 성격의 정보가 추가로 필요 : 차종에 따른 충전기 커넥터 정보 (분석 편의를 위한 경우)
>
>       예시4) 시간
>
>       예시5) 페이지 영역별 naming (이전 영역 정보가 필요할 수 있으므로)
>
>     - sample : 원하는 output을 시나리오별로 작성
>
>   - 로그 주기
>
>     - 얼마나 자주 남길것인지? (대상 이벤트 수준을 잘 정의해야 함)
>     - 얼마나 자세히 남길 것인지?
>     - DB정보를 통해 join으로 확인할 수 있는 정보는 가급적 제외

