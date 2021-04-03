# filestore 관련 모두 지워줌

from exception import DuplicateException, RecordNotFoundException
from db_store import PRStore
from domain import Entity
# 같은 클래스 내에서는 객체 생성 없이 참조할 수 있다. (ex) 같은 클래스에선 '객체'로 가능 클래스 외엔 '객체.'으로 가능)

class PRService:
    # AIEntity: 정보를 저장하는 클래스 변수

    db = PRStore()

    # 수강생등록: code 존재여부 체크
    def register(self, entity):
        result = self.is_exist(entity.code)
        if not bool(result):
            PRService.db.insert(entity)
            return result
        else:
            try:
                raise DuplicateException(entity.code)
            except DuplicateException as error:
                return error

    # 수강생 목록
    def get_all_entity(self):
        return PRService.db.select_all()

    # 수강생정보 수정
    def update_entity(self, entity):
        result = self.is_exist(entity.code)
        if bool(result):
            PRService.db.update(entity)
            return entity.code + '의 정보가 수정되었습니다.'
        else:
            try:
                raise RecordNotFoundException(entity.name)
            except RecordNotFoundException as updateError:
                return str(updateError)

    # 수강생정보 삭제
    def delete_entity(self, code):
        result = self.is_exist(code)
        if bool(result):
            PRService.db.delete(code)
            return code + '삭제되었습니다.'
        else:
            try:
                raise RecordNotFoundException(code)
            except RecordNotFoundException as removeError:
                return str(removeError)

    # 수강생 상세 정보
    def get_one_entity(self, code):
        result = self.is_exist(code)
        if bool(result):
            return result
        else:
            return None

    # code 존재여부
    def is_exist(self, code):
        result = PRService.db.select_by_code(code)
        return result

    def close(self):
        PRService.db.close()
        