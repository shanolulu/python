# filestore 관련 모두 지워줌

from ai_exception import DuplicateException, RecordNotFoundException
from store import AIStore
from domain import AIEntity
# 같은 클래스 내에서는 객체 생성 없이 참조할 수 있다. (ex) 같은 클래스에선 '객체'로 가능 클래스 외엔 '객체.'으로 가능)

class AIService:
    # AIEntity: 정보를 저장하는 클래스 변수
    # ai_list = [] # static

    db = AIStore()
    # def __init__(self):
    #     pass

    # 수강생등록: email 존재여부 체크
    def register(self, ai_entity):
        result = self.is_exist(ai_entity.email)
        if not bool(result):
            AIService.db.insert(ai_entity)
            return result

        else:
            try:
                raise DuplicateException(ai_entity.name)
            except DuplicateException as error:
                return print(error)

    # 수강생 목록
    def get_all_entity_controller(self):
        return AIService.db.select_all()

    # 수강생정보 수정
    def entity_update(self, ai_entity):
        result = self.is_exist(ai_entity.email)
        if bool(result):
            AIService.db.update(ai_entity)
            return print(ai_entity.name + '님의 정보가 수정되었습니다.')

        else:
            try:
                raise RecordNotFoundException(ai_entity.name)
            except RecordNotFoundException as updateError:
                return str(updateError)

    # 수강생정보 삭제
    def entity_remove(self, email):
        result = self.is_exist(email)
        if bool(result):
            AIService.db.delete(email)
            return print(email + '삭제되었습니다.')
        else:
            try:
                raise RecordNotFoundException(email)
            except RecordNotFoundException as removeError:
                return str(removeError)

    # 수강생 상세 정보
    def get_ai_entity(self, email):
        result = self.is_exist(email)
        if bool(result):
            return AIEntity(result['name'], result['age'], result['email'], result['major'])
        else:
            return None

    # email 존재여부
    def is_exist(self, email):
        result = AIService.db.select_by_email(email)
        return result

    def close(self):
        AIService.db.close()
        