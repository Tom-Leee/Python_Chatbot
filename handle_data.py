import pymysql
import pandas as pd

db = None

try:
    # pymysql.connect() 함수를 사용하면 DB 서버에 접속할 수 있습니다.
    # connect() 함수의 인자는 다음과 같습니다.
    # DB 호스트 정보에 맞게 입력
    db = pymysql.connect(

        # 데이터 베이스 서버가 존재하는 호스트 주소
        host='localhost',

        # 데이터베이스 로그인 유저
        user='root',

        # 데이터베이스 로그인 패스워드
        passwd='joker77&',

        # 데이터베이스 명
        db='k_digital',

        # 데이터베이스에서 사용할 charset 인코딩
        charset='utf8'
    )
    print("DB 연결 성공 ")

    # 데이터 DB에 추가될 항목들 정리 ---①
    users = [
        {'name': '구름', 'age': 23, 'address': 'SEOUL'},
        {'name': '딸기', 'age': 27, 'address': 'DAEJEON'},
        {'name': '사과', 'age': 21, 'address': 'DAEGU'},
        {'name': '에어포트', 'age': 25, 'address': 'INCHEON'},
    ]

    for s in users:
        with db.cursor() as cursor:
            sql = '''
                insert user(name, age, address) values("%s", "%d", "%s")
            '''% (s['name'], s['age'], s['address'])

            cursor.execute(sql)

    # DB호스트에 연결된 객체(db)에 commit()를 통해 수정된 내용을
    # DB에 반영하여 줍니다.
    db.commit()

    # 30대 학생만 조회 ---②
    cond_age = 30
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = '''
        select * from user where age > %d
        ''' % cond_age
        cursor.execute(sql)
        results = cursor.fetchall()
    print(results)  # 가져온 데이터 출력

    cond_name = '에어포트'  # 찾고자 하는 이름
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = '''
        select * from tb_student where name="%s"
        ''' % cond_name
        cursor.execute(sql)
        result = cursor.fetchone()  # select 구문으로 조회한 데이터 중 하나만 불러오는 함수
    print(result['name'], result['age'])

    # pandas 데이터 프레임으로 표현
    df = pd.DataFrame(results)
    print(df)

except Exception as e:
    # DB 연결 실패 시 오류 내용 출력
    print(e)

finally:
    # DB 가 연결된 경우에만 접속 닫기 시도
    if db is not None:
        # 데이터베이스 서버 닫기
        db.close()
        # print('table 생성 완료')
        # print('data 삽입 완료')
        # print('data 수정 완료')
        # print('data 삭제 완료')
        print('data 임의로 DB에 삽입 완료')
        print("DB 연결 닫기 성공")