# 메뉴 출력
def menu():
    print('\n상품관리 시스템입니다.')
    print('1. 제품을 등록합니다.')
    print('2. 제품 리스트를 확인합니다.') # 제품 전체 목록
    print('3. 제품 상세정보를 확인합니다.') # 이름, 가격, 색상
    print('4. 제품 정보를 수정합니다.') # 이름, 가격, 색상
    print('5. 제품 정보를 삭제합니다.') # 제품 목록에서 삭제
    print('0. 시스템을 종료합니다.\n') # 저장하고 상품 리스트 txt파일로 저장

# 메세지 출력
def message(message):
    print(message)

# menu select 정보 입력
def input_menu():
    select_menu = input('메뉴를 선택해주세요 >> ')
    select_menu = is_integer(select_menu)
    return select_menu
def input_code():
    code = input('상품코드를 입력해주세요 >> ')
    return code

# entity 정보 입력
def input_entity():
    name = input('이름을 입력해주세요 >> ')
    price = input('가격을 입력해주세요 >> ')
    price = is_integer(price)
    color = input('상품의 색상을 입력해주세요 >> ')
    return name, price, color

# 숫자 정보 입력시 형식 확인
def is_integer(integer): # 메뉴나 가격에 숫자 값을 입력받았는지 확인하기 위해 사용
    if integer.isdigit() == False:
        while True:
            integer = input('숫자로 입력해주세요 >> ')
            if integer.isdigit() == True:
                break
    return int(integer)

# 상품 리스트 출력
def info_all_entity(product_list):
    for i in product_list:
        print(str(i))

# 상품 상세정보 출력
def info_entity(entity):
    print('상품코드: {}의 상세정보 {}'.format(entity.code, str(entity)))
