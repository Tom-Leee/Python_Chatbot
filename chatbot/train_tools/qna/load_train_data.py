import pymysql
import openpyxl

#DB 접속 정보 가져오기
from chatbot.config.DatabaseConfig import *

#기존 학습 데이터 초기화 함수 정의
def all_clear_train_data(db):
    sql = '''
        delete from chatbot_train_data
    '''

    with db.cursor() as cursor:
        cursor.execute(sql)

    #ALTER TABLE - 테이블 변경
    #AUTO_INCREMENT를 1로 초기화(시작할 값 설정)
    sql = '''
        ALTER TABLE chatbot_train_data AUTO_INCREMENT=1
    '''

    with db.cursor() as cursor:
        cursor.execute(sql)

#db에 데이터 저장하는 함수 정의
#INSERT를 통해 전달받은 각 컬럼에 대한 값을 추가한다.
def insert_data(db, xls_row):
    intent, ner, query, answer, answer_img_url = xls_row

    sql = '''
        INSERT chatbot_train_data(intent, ner, query, answer, answer_image)
        values(
            '%s', '%s', '%s', '%s', '%s')
    ''' % (intent.value, ner.value, query.value, answer.value,
           answer_img_url.value)

    #엑셀에서 불러온 cell에 데이터가 없는 경우(None) null로 치환
    sql = sql.replace("'None'", "null")

    #입력된 값들 확인하고 커밋
    with db.cursor() as cursor:
        cursor.execute(sql)
        print('{} 저장'.format(query.value))
        db.commit()

train_file = 'C:/Users/Green/PycharmProjects/pythonProject/' \
             'chatbot/train_tools/qna/train_data.xlsx'

db = None

try:
    db = pymysql.connect(
       host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )

    #기존 학습 데이터 초기화 함수 실행(위에서 생성함)
    all_clear_train_data(db)

    #엑셀파일을 읽어오고 wb에 저장합니다.
    wb = openpyxl.load_workbook(train_file)

    #Sheet1의 값을 sheet로 저장
    sheet = wb['Sheet1']

    # 헤더는 불러오지 않기에 2값
    for row in sheet.iter_rows(min_row=2):

        #엑셀 데이터를 한 줄씩 받아와 DB에 INSERT 합니다.
        insert_data(db, row)

    wb.close() #엑셀 파일 닫기

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
        print('train_data.xlsx 파일 데이터 저장 완료')
