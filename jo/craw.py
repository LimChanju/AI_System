from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

# Firefox 드라이버 설정
options = Options()
options.add_argument("--headless")  # 창 없이 실행하려면

# 경로 직접 지정
service = Service(executable_path="/usr/local/bin/geckodriver")  # geckodriver 경로

# Firefox 실행 파일 경로 지정
options.binary_location = "/usr/bin/firefox"  # firefox 경로

# Firefox 드라이버 실행
driver = webdriver.Firefox(service=service, options=options)

# 네이버 지도에서 특정 음식점 검색
search_query = "부산 사하구 음식점"
url = f"https://map.naver.com/v5/search/{search_query}"

driver.get(url)

# 로딩 기다리기
time.sleep(5)

# iframe 전환 (네이버 지도는 iframe 내부에 내용이 있어)
try:
    driver.switch_to.frame("searchIframe")
    time.sleep(2)
except Exception:
    print("iframe 전환 실패")

# 음식점 리스트 가져오기 (CSS Selector는 네이버 구조에 따라 달라질 수 있음)
try:
    places = driver.find_elements(By.CSS_SELECTOR, "li .place_bluelink")
except Exception:
    places = []

for i, place in enumerate(places[:20]):  # 상위 5개만 출력 
    try:
        name = place.text
        print(f"\n[{i+1}] 음식점 이름: {name}")
        
        # 별점 가져오기
        rating_elem = place.find_element(By.CSS_SELECTOR, ".place_section_content .PXMot.LXIwF")
        print(f"별점: {rating_elem.text}")

        # 가격 정보 가져오기 (있으면)
        price_elem = place.find_element(By.CSS_SELECTOR, ".kVcFJ")
        print(f"가격 정보: {price_elem.text}")

        # 리뷰 요약 (없을 수도 있음)
        review_elem = place.find_element(By.CSS_SELECTOR, ".owQmN._15_yK")
        print(f"리뷰 요약: {review_elem.text}")

    except Exception as e:
        print("정보 부족 또는 구조 변경")

driver.quit()