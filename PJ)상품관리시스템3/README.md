# pymysql
> 파이썬을 활용하여 mysql의 db연결

Python & MySQL 
    pip install PyMySQL #package install
    import pymysql #package import
    DB연결
        db = pymysql.connect(
            user='사용자명', 
            passwd='설정한 비밀번호', 
            host='mysql서버',
	    port=port번호, 
            db='데이터베이스명', 
            charset='utf8'
        )
    Cursor설정:연결한 데이터베이스와 통신하기 위한 커서 설정
        cursor = 연결변수_db.cursor(pymysql.cursors.DictCursor)
            DictCursor : Dictionary형태로 결과를 리턴하는 Cursor
            일반적으로 튜플로 리턴
    Query 실행 및 결과처리
        SELECT
            예) sql = "SELECT * FROM `테이블명`;"
                cursor.execute(sql)
                result = cursor.fetchall()
            fetchall() : 모든데이터 리턴
            fetchone() : 한행리턴
            fetchmany(n) : n개행 리턴
            * 데이터 편리하게 처리하기 위한 pandas프레임 사용가능 :
            import pandas as pd
                result = pd.DataFrame(result)
                result
                fechone():result = pd.DataFrame(result, index=[0])
        INSERT
            예)sql="INSERT INTO '테이블명' VALUES(삽입할 데이터)
            cursor.execute(sql)
            db.commit()
        UPDATE
            예)sql="UPDATE '테이블명' 
                    SET 컬럼=변경데이터
                    WHERE 수정할데이터 조건
            cursor.execute(sql)
            db.commit()
        DELETE
            예)sql="DELETE FROM '테이블명' WHERE 삭제할데이터 조건
            cursor.execute(sql)
            db.commit()
    DB종료
    동적 데이터 처리(Placehoder)
        sql - parameter: %s
        excute(sql,datalist 또는 datatuple) #하나의 데이터
        예) data = ('hong', 1)
            # SELECT 
            sql = "SELECT * FROM `customer` WHERE name = %s AND id = %s;"
            cursor.execute(sql, data)

            # DELETE
            sql = "DELETE FROM `customer` WHERE `name` = %s AND `id` = %s;"
            cursor.execute(sql, data)
            db.commit()
        executemany(sql, multiple-data)#댜량의데이터
            data = [['hong', 1], ['lee', 2], ['kim', 3]]
            # INSERT 
            sql = "INSERT INTO `customer`(name, id) VALUES (%s, %s);"
            cursor.executemany(sql, data)
            db.commit()

            # UPDATE 
            sql = "UPDATE `customer` SET `name` = %s WHERE `id` = %s;"
            cursor.executemany(sql, data)
            db.commit()
    참고
        https://pymysql.readthedocs.io/en/latest/index.html
        http://pythonstudy.xyz/python/article/201-Python-DB-API

MYSQL인코딩 확인
    desc information_schema.SCHEMATA
    SELECT default_character_set_name, DEFAULT_COLLATION_NAME FROM information_schema.SCHEMATA  WHERE schema_name = "aidb";

    SELECT CCSA.character_set_name FROM information_schema.`TABLES` T,
       information_schema.`COLLATION_CHARACTER_SET_APPLICABILITY` CCSA
        WHERE CCSA.collation_name = T.table_collation
        AND T.table_schema = "aidb"
        AND T.table_name = "member";    

MYSQL 인코딩 변경
    [Windows]
    my.ini
        [client]
        default-character-set=utf8
        [mysqld]
        character-set-server=utf8
        basedir=C:\\tools\\mysql\\current
        datadir=C:\\ProgramData\\MySQL\\data
    [Linux]
       # /etc/mysql/mysql.conf.d/
       #아래의 4개 파일 추가
       vi client.cnf
            [client]
            default-character-set=utf8

        vi mysqld.cnf
            [mysqld]
            character-set-server=utf8
            collation-server=utf8_general_ci
            init_connect=SET collation_connection=utf8_general_ci
            init_connect=SET NAMES utf8

        vi mysqlddump
            [mysqldump]
            default-character-set=utf8

        vi mysql.cnf
            [mysql]
            default-character-set=utf8

        # service mysql restart

-------------------------------------------------------------
# 읽어보면 좋아여!
    * service.py는 localfile에 대해서 작동하는데 file에서는 처음과 끝에 read와 write를 사용하면 load할 데이터가 많아지게 된다.
    * 하지만 file에서 작동하는 것처럼 사용하면 DB를 사용해 여러명의 사람들이 쓸 때 모든 사람들이 모든 작업이 끝나고
    업데이트(insert, delete, update)를 하게 되면 서로 load되는 데이터에 의해 엉키게 된다.
    엉키지 않기 위해서는 db에 connect된 한 사람이 모든 작업을 끝낸 후 다른 사람이 쓰게 되면 비효율적이기 때문에 method마다 연결해
    서로 공유하면서 이용할 수 있도록 한다.
    * web을 통해 db를 연결할 때는 web과 db 사이에 미리 connect를 만들어두어 필요한 connect를 써내 쓸 수 있도록 한다. 나머지는 db연결과 동일하다.
    초기에 메소드를 몇 개 만들지 pool에서 정하여 미리 connect를 만든다.


    https://pymysql.readthedocs.io/en/latest/index.html : install 방법/순서 등 볼 수 있다.
    * terminal
    pip install PyMySQL # 지원하는 버전 확인!

    # domain에서 저장될 변수들을 DB에 저장해야한다.

    * dbeaver
    use aidb; // aidb를 사용하기 위해 사용

    CREATE TABLE member (
        name  varchar(20) NOT NULL,
        age   int(3),
        email   varchar(50),
        major   varchar(20) NOT NULL,
        PRIMARY KEY (email)
    );

    # select = from member
    # delete from member
    # commit

    * visual/store.py
    # service.py는 file에 대해 실행하는 파일이기 때문에 DB에 실행되는 store.py파일을 작성한다.

    * visual/new_service.py
    * main -> DB
    * ai_controller -> db_ai_controller







