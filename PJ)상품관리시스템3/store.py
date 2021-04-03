import pymysql.cursors
from domain import AIEntity

# CREATE TABLE ai_list (
#     name  varchar(20) NOT NULL,
#     age   int(3),
#     email   varchar(50),
#     major   varchar(20) NOT NULL,
#     PRIMARY KEY (email)
# )

class AIStore:
    # connection Pool 사용자: method 단위로 connection/close
    connection=None # 현재는 connection을 global 상태로 해두었지만 제대로 사용할 때는
    # module마다 connection을 열고 닫아줘야 한다.
        
    # db연결 (url, user, passwd 정보를 줘야함)
    def __init__(self):
        # Connetion Pool 객체 얻기
        AIStore.connection = pymysql.connect(
            host = 'localhost',
            port = 3306, # 충돌 시 3000번으로
            user = 'aiadmin',
            passwd = 'password',
            db = 'aidb',
            charset = 'utf8',
            cursorclass = pymysql.cursors.DictCursor # db을 가져올 때 타입 지정. 미지정 시 튜플형태로 가져온다.
        )

    # db연결종료
    def close(self): # 사용 후 반납 (commit, fetch)
        AIStore.connection.close()

    # service.py 의 기능들 (is_exist는 select로 부르면 되고, save, read는 사용하지 않으니 필요없다.)
    def insert(self, ai_entity): # register
        try:
            with AIStore.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `member` (`name`, `age`, `email`, `major`) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (ai_entity.name, ai_entity.age, ai_entity.email, ai_entity.major))
                AIStore.connection.commit()
        finally:
            pass
            # connection.close()

    def select_all(self): # get_all_entity_controller
        try:
            with AIStore.connection.cursor() as cursor:
                sql="SELECT * FROM `member`"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def update(self, ai_entity): # entity_update
        try:
            with AIStore.connection.cursor() as cursor:
                # Create a new record
                sql = "UPDATE `member` set `name`=%s, `age`=%s, `major`=%s WHERE `email`=%s"
                cursor.execute(sql, (ai_entity.name, ai_entity.age, ai_entity.major, ai_entity.email)) # 매개변수 순서 잘 맞출 것
                AIStore.connection.commit()
        finally:
            pass

    def delete(self, email): # entity_remove
        try:
            with AIStore.connection.cursor() as cursor:
                # Create a new record
                sql = "DELETE FROM `member` WHERE `email`=%s"
                cursor.execute(sql, (email))
                AIStore.connection.commit() # db에 반영
        finally:
            pass
    
    def select_by_email(self, email): # get_ai_entity
        try:
            with AIStore.connection.cursor() as cursor:
                sql = "SELECT * FROM `member` where `email`=%s"
                cursor.execute(sql, (email))
                result = cursor.fetchone()
        finally:
            pass
        return result

# test=AIStore()
# # test.insert(AIEntity('강1', 24, '@naver.com', 'infosec')) # AIEntity는 domain.py에 있으므로 import 해줘야함
# # test.insert(AIEntity('강2', 24, '@daum.com', 'infosec')) # AIEntity는 domain.py에 있으므로 import 해줘야함
# # test.insert(AIEntity('강3', 24, '@gmail.com', 'infosec')) # AIEntity는 domain.py에 있으므로 import 해줘야함

# # result = test.select_all()
# # test.update(AIEntity('강', 23, '@naver.com', 'AI'))
# # result = test.select_by_email('@naver.com')
# test.delete('@naver.com')
# result= test.select_all()
# print(result)