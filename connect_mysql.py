import pymysql

db = None

try:
    # pymysql.connect() 함수를 사용하면 DB 서버에 접속할 수 있습니다. connect() 함수의 인자는 다음과 같습니다.
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

except Exception as e:
    # DB 연결 실패 시 오류 내용 출력
    print(e)

finally:
    # DB 가 연결된 경우에만 접속 닫기 시도
    if db is not None:

        # 데이터베이스 서버 닫기
        db.close()
        print("DB 연결 닫기 성공")