import  pymysql
from chatbot.config.DatabaseConfig import *

db = None

try:
    #더 이상 패스워드를 직접 입력하여 관리하지 않습니다
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )

    sql = '''
        CREATE TABLE IF NOT EXISTS `chatbot_train_data` (
        `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
        `intent` VARCHAR(45) NULL,
        `ner` VARCHAR(1024) NULL,
        `query` TEXT NULL,
        `answer` TEXT NOT NULL,
        `answer_image` VARCHAR(2048) NULL,
        PRIMARY KEY (`id`))
    ENGINE = InnoDB DEFAULT CHARSET = utf8
    '''

    with db.cursor() as cursor:

        # cursor 객체의 execute() 함수로 SQL 구문을 실행합니다
        cursor.execute(sql)

    # DB호스트에 연결된 객체(db)에 commit()를 통해 수정된 내용을
    # DB에 반영하여 줍니다.
    db.commit()

except Exception as e:
    # DB 연결 실패 시 오류 내용 출력
    print(e)

finally:
    # DB 가 연결된 경우에만 접속 닫기 시도
    if db is not None:
        # 데이터베이스 서버 닫기
        db.close()
        print('table 생성 및 컬럼 설정 완료')