class AIEntity:
    # 생성자 정의: member variable (name, email, major 초기화)
    def __init__(self, name, age, email, major):
        self.name = name # 맴버 변수 초기화
        self.age = age
        self.email = email
        self.major = major
    # email 정보가 같은 경우 같은 객체로 재정의
    def __eq__(self, email):
        if self.email == email:
            return True
        else:
            return False
    #
    def __str__(self): # str정보가 
        return '{} : {} : {} : {}'.format(self.name, self.age, self.email, self.major)

# xml 파이을 전송할 때!! (전송할 때는 json형태로 한다.)
# tojson: Entity -> json 변환
# fromjson: json -> Entity 변환