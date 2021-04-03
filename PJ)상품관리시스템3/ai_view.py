# 메뉴 출력
def menu_display():
    print('---- AI 수강생 관리 프로그램 ----')
    print('1. 수강생 등록')
    print('2. 수강생 목록')
    print('3. 수강생 수정')
    print('4. 수강생 삭제')
    print('5. 수강생 검색')
    print('0. 종료')

# 메세지 출력
def message_display(message):
    print(message)

# 목록 출력
def ai_list_display(ai_list):
    for index, value in enumerate(ai_list):
        print('{}번째 : {}'.format(index, str(value)))

# ai_entity 상세정보 출력
def ai_entity_display(ai_entity):
    print('{} 상세정보 : {}'.format(ai_entity.email, str(ai_entity)))

# 구분선
def line_display():
    print('=' * 15)

# ai_entity 정보 입력
def input_ai_entity():
    name = input('name >> ')
    age = int(input('age >> '))
    major = input('major >> ')
    return name, age, major # 여러 개를 한 번에 return 하면 tuple로 return 됨
    
# email 정보 입력
def input_email():
    email = input('email >> ')
    return email

# menu select 정보 입력
def input_select_menu():
    menu = int(input('menu >> '))
    return menu