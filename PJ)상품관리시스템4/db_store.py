import pymysql.cursors
from domain import Entity

class PRStore:
    # connection Pool 사용자: method 단위로 connection/close
    connection=None # 현재는 connection을 global 상태로 해두었지만 제대로 사용할 때는
    # module마다 connection을 열고 닫아줘야 한다.
        
    # db연결 (url, user, passwd 정보를 줘야함)
    def __init__(self):
        # Connetion Pool 객체 얻기
        PRStore.connection = pymysql.connect(
            host = 'localhost',
            port = 3306, # 충돌 시 3000번으로
            user = 'aiadmin',
            passwd = 'password',
            db = 'aidb',
            charset = 'utf8',
            cursorclass = pymysql.cursors.DictCursor # db을 가져올 때 타입 지정. 미지정 시 튜플형태로 가져온다.
        )

    # service.py 의 기능들 (is_exist는 select로 부르면 되고, save, read는 사용하지 않으니 필요없다.)
    def insert(self, entity): # register
        try:
            with PRStore.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `member` (`name`, `price`, `code`, `color`) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (entity.name, entity.price, entity.code, entity.color))
                PRStore.connection.commit()
        finally:
            pass
            # connection.close()
    
    def select_all(self): # get_all_entity_controller
        try:
            with PRStore.connection.cursor() as cursor:
                sql="SELECT * FROM `member`"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def select_by_code(self, code): # get_ai_entity
        try:
            with PRStore.connection.cursor() as cursor:
                sql = "SELECT * FROM `member` where `code`=%s"
                cursor.execute(sql, (code))
                result = cursor.fetchone()
        finally:
            pass
        return result

    def update(self, entity): # entity_update
        try:
            with PRStore.connection.cursor() as cursor:
                # Create a new record
                sql = "UPDATE `member` set `name`=%s, `price`=%s, `color`=%s WHERE `code`=%s"
                cursor.execute(sql, (entity.name, entity.price, entity.color, entity.code)) # 매개변수 순서 잘 맞출 것
                PRStore.connection.commit()
        finally:
            pass

    def delete(self, code): # entity_remove
        try:
            with PRStore.connection.cursor() as cursor:
                # Create a new record
                sql = "DELETE FROM `member` WHERE `code`=%s"
                cursor.execute(sql, (code))
                PRStore.connection.commit() # db에 반영
        finally:
            pass

    # db연결종료
    def close(self): # 사용 후 반납 (commit, fetch)
        PRStore.connection.close()