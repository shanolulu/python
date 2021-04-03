# 네이버 로그인 (chrome browser)

from selenium import webdriver
import time

USER = input('네이버 아이디를 입력해주세요 >> ') # 로그인에 사용될 아이디 입력
PASS = input('네이버 비밀번호를 입력해주세요 >> ') # 로그인에 사용될 비밀번호 입력

# chrome brower 실행
driver = webdriver.Chrome('C:/chromedriver.exe') # chromedriver를 사용
driver.set_window_size(1280, 900) # 창의 크기 설정 (x, y)

# 네이버 로그인 화면으로 이동
driver.get('http://nid.naver.com/nidlogin.login') # URL에 접근하는 메소드: get('http://url.com')

# ! 로그인에 자바 스크립트 코드를 이용하는 이유: find_element함수는 네이버에서 막아놓았기 때문..
# 아이디와 비밀번호를 입력 및 로그인 버튼 클릭
driver.execute_script("document.getElementsByName('id')[0].value=\'" + USER + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + PASS + "\'")
# xpath //*[@id='frmNIDLogin']
# //*: 모든 태그의, @id: id속성 중, 'frmNIDLogin': frmNIDLogin 속성값을 가진 태그 선택
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click() # 로그인 버튼을 클릭
time.sleep(3)
driver.get('http://www.naver.com') # 네이버 메인 화면으로 이동
time.sleep(3)
driver.close()

