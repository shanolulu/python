# main.py에서 사용될 객체이다.
class Entity():
    def __init__(self, name, price, code, color):
        self.name = name
        self.price = price
        self.code = code
        self.color = color

    def __eq__(self, code): # equal 함수로 내용을 비교할 때 사용
        if self.code == code: # 기존에 존재하던 email과 새로 입력된 email을 비교
            return True
        else:
            return False

    def __str__(self): # interface를 제공하기 위해 사용
        return '상품코드 {}의 상세정보: 상품명:{}, 가격: {}, 색상: {}'.format(self.code, self.name, self.price, self.color)
        