import db_service
from view import message, info_all_entity, info_entity

class PRController:
    
    # def control_file_read(self):
    #     sv = db_service.PRService()
    #     sv.file_read()

    # def control_file_save(self):
    #     sv = db_service.PRService()
    #     sv.file_save()

    def control_register(self, entity): # register(회원가입): 상품코드가 겹치지 않도록 검사 및 형식 확인
        if entity.code == '' or len(entity.code) == 0:
            message('상품코드 형식을 잘못되었습니다.')
        else:
            sv = db_service.PRService()
            message_info = sv.register(entity)
            # message(message_info)
            message('-------------------')
    
    def control_get_all_entity(self):
        sv = db_service.PRService()
        product_list = sv.get_all_entity()
        return product_list

    def control_get_entity(self, code):
        if code == '' or len(code) == 0:
            message('상품코드 형식이 잘못되었습니다.')
        else:
            sv = db_service.PRService()
            entity = sv.get_one_entity(code)
            if entity['code'] != '' or len(entity['code']) == 0:
                return entity
            else:
                message('존재하지 않습니다.')
                
    def control_update_entity(self, entity):
        if entity.code == '' or len(entity.code) == 0:
            message('상품코드 형식이 잘못되었습니다.')
        else:
            sv = db_service.PRService()
            message_update = sv.update_entity(entity)
            # message(message_update)


    def control_delete_entity(self, code):
        if code == '' or len(code) == 0:
            message('상품코드가 존재하지 않습니다.')
        else:
            sv = db_service.PRService()
            message_delete = sv.delete_entity(code)
            # message(message_delete)

    def close(self):
        bm = db_service.PRService()
        bm.close()
        