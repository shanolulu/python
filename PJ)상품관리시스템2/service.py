from ai_exception import DuplicateException, RecordNotFoundException
from filestore import save_file, read_data

# 같은 클래스 내에서는 객체 생성 없이 참조할 수 있다. (ex) 같은 클래스에선 '객체'로 가능 클래스 외엔 '객체.'으로 가능)

class AIService:
    # AIEntity: 정보를 저장하는 클래스 변수
    ai_list = [] # static
    def __init__(self):
        pass

    # 수강생등록: email 존재여부 체크
    def register(self, ai_entity):
        index = self.is_exist(ai_entity.email)
        if index < 0:
            AIService.ai_list.append(ai_entity) # 클래스 변수기 때문에 앞에 AIService를 붙여준다.
            return print(ai_entity.name + '님 등록되었습니다.')
        else:
            try:
                raise DuplicateException(ai_entity.name)
            except DuplicateException as error:
                return print(error)

    # 수강생 목록
    def get_all_entity_controller(self):
        return AIService.ai_list

    # 수강생정보 수정
    def entity_update(self, ai_entity):
        index = self.is_exist(ai_entity.email)
        if index > -1:
            ai = AIService.ai_list[index]
            ai.name = ai_entity.name
            ai.age = ai_entity.age
            ai.major = ai_entity.major
            return print(ai_entity.name + '님의 정보가 수정되었습니다.')

        else:
            try:
                raise RecordNotFoundException(ai_entity.name)
            except RecordNotFoundException as updateError:
                return str(updateError)

    # 수강생정보 삭제
    def entity_remove(self, email):
        index = self.is_exist(email)
        if index < -1:
            AIService.ai_list.pop(index)
            return print(email + '삭제되었습니다.')
        else:
            try:
                raise RecordNotFoundException(email)
            except RecordNotFoundException as removeError:
                return str(removeError)

    # 수강생 상세 정보
    def get_ai_entity(self, email):
        index = self.is_exist(email)
        if index > -1:
            return AIService.ai_list[index]
        else:
            return None

    # email 존재여부
    def is_exist(self, email):
        for index, entity in enumerate(AIService.ai_list):
            if entity.email == email:
                return index
        return -1

        
    # file store 저장
    def save_list(self):
        save_file(AIService.ai_list)

    # file store read
    def read_list(self):
        AIService.ai_list =read_data()
        