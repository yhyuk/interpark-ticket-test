from selenium import webdriver
from selenium.webdriver.common.by import By
import time

myId = "인터파크 id"
myPw = "인터파크 pw"

# 웹드라이버 경로 설정 (크롬드라이버를 사용)
driver = webdriver.Chrome()

# 인터파크 티켓 사이트로 이동
driver.get("https://tickets.interpark.com")

# 로그인 페이지로 이동
login_button = driver.find_element(By.LINK_TEXT, "로그인")
login_button.click()

username = driver.find_element(By.ID, "userId")
password = driver.find_element(By.ID, "userPwd")

# id, pw
username.send_keys(myId)
password.send_keys(myPw)

# 로그인 버튼 클릭
login_button = driver.find_element(By.ID, "btn_login")
login_button.click()

# 로그인 후 원하는 공연의 예매 페이지로 이동
driver.get("https://tickets.interpark.com/special/sports/promotion?seq=43")

# 예매하기 버튼 클릭
reserve_button = driver.find_element(By.XPATH, "//span[text()='PO 4차전']/ancestor::li//button[contains(text(), '예매하기')]")
reserve_button.click()


time.sleep(99999999)

# # 좌석 선택 전까지 진행하는 자동화 부분
# .....








# # '예매하기' 버튼 클릭
# reserve_button = driver.find_element(By.ID, "예매버튼의_아이디")
# reserve_button.click()
#
# # 이후의 과정은 좌석 선택 페이지까지 진행 가능
# # 하지만 좌석 선택 부분은 일반적으로 복잡한 JavaScript로 이루어져 있어, 특정 좌석 선택 매크로를 만드는 것은 권장되지 않습니다.
#
# # 마무리 및 브라우저 종료
# time.sleep(5)
# driver.quit()
