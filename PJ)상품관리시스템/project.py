import os

def start():
    print('\n상품관리 시스템입니다.')
    print('1. 제품을 등록합니다.')
    print('2. 제품 리스트 정보를 확인합니다.') # 제품 전체 목록
    print('3. 제품 상세정보를 확인합니다.') # 가격, 번호
    print('4. 제품 정보를 수정합니다.') # 이름, 가격, 번호
    print('5. 제품 정보를 삭제합니다.') # 제품에 대한 설명
    print('6. 시스템을 종료합니다.\n') # 저장하고 상품 리스트 txt파일로 저장


def confirm(name):
    try:
        num = int(input('상품의 {}를 입력해주세요 >>'.format(name)))
    except ValueError:
        while True:
            num = input('!! {}은 숫자로만 입력해주세요 !! >>'.format(name))
            if num.isdigit() == True:
                break
        return num
    else:
        return num

def add_product(dic_product):
    if len(list_product) == 0:
        list_product.append(dic_product)
    else:
        for i in list_product:
            if i['name'] == name:
                print('이미 존재하는 이름입니다.')
                break
            else:
                list_product.append(dic_product)
                return print('성공적으로 정보를 저장하였습니다.') # return과 break의 차이: return은 해당 함수를 종료. break는 반복문의 탈출.


def list_search():
    if len(list_product) == 0:
        return print('등록되어 있는 상품이 존재하지 않습니다.')
    else:
        for i in range(len(list_product)):
            print('{}번 -- 상품이름: {}, 상품의 가격: {}, 상품번호 {} 입니다.'.format(i, list_product[i]['name'], list_product[i]['number'], list_product[i]['price']))

def info_product():
    name = input('확인할 상품의 이름을 입력해주세요 >> ')
    if len(list_product) == 0:
        print('등록된 상품이 없습니다.')
    else:
        for i in list_product:
            if i['name'] == name:
                return print('\'{}\'은 상품번호 : {}, 가격 : {}입니다.'.format(name, i['number'], i['price']))
        print('{}은 등록된 상품이 아닙니다.'.format(name))


def list_update():
    name = input('정보를 수정하려는 상품의 이름를 입력해주세요 >> ')
    if len(list_product) == 0:
        print('등록된 상품이 없습니다.')
    else:
        for i in list_product:
            if i['name'] == name:
                try:
                    check = int(input('수정할 정보를 골라주세요 (1. 이름  2. 상품번호  3. 상품가격) >>'))
                except ValueError:
                    while True:
                        check = input('숫자로만 입력해주세요 >>')
                        if check.isdigit() == True:
                            break
                if check == 1:
                    name = input('상품의 이름을 입력해주세요 >> ')
                    i['name'] = name
                elif check == 2:
                    number = confirm(number_name)
                    i['number'] = number
                elif check == 3:
                    price = confirm(price_name)
                    i['price'] = price
        print('{}은 등록된 상품이 아닙니다.'.format(name))

def del_product():
    name = input('삭제할 상품의 이름을 입력해주세요 >> ')
    if len(list_product) == 0:
        return print('등록되어 있는 상품이 존재하지 않습니다.')
    for i in range(len(list_product)):
        if list_product[i]['name'] == name:
            del list_product[i]
            return
    print('{}은 등록된 상품이 아닙니다.'.format(name))

def open_file():
    if os.path.isfile('./product_management_system.dat'):
        with open('product_management_system.dat', 'r') as file:
            data = file.read().splitlines()
            for i in range(len(data)):
                data2 = data[i].split(',')
                dic_product = {
                    'name':data2[0],
                    'number':data2[1],
                    'price':data2[2]
                }
                list_product.append(dic_product)
                

    
def save_file():
    with open('product_management_system.dat', 'w') as file:
        for i in list_product:
            file.write(i['name'] + ',' + str(i['number']) + ',' + str(i['price']) + '\n')

number_name = '상품번호'
price_name = '가격'
list_product = []
while True:
    open_file()
    start()
    menu = int(input('번호를 선택해주세요 >> '))

    if menu == 1:
        name = input('상품의 이름을 입력해주세요 >> ')
        number = confirm(number_name)
        price = confirm(price_name)

        dic_product = {
            'name' : name,
            'number' : number,
            'price' : price
        }
        add_product(dic_product)
    elif menu == 2:
        list_search()
    elif menu == 3:
        info_product()
    elif menu == 4:
        list_update()
    elif menu == 5:
        del_product()
    elif menu == 6:
        print('프로그램을 종료합니다.')
        save_file()
        break
    else:
        print('1~6번을 눌러주세요.')
