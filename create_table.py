import pymysql

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

    # 테이블 삽입 sql 정의 -- ①
    sql = '''
    CREATE TABLE user(
        # 컬럼명 id는 기본 키, 자동 증가, null 일 수 없는 제약 조건을 갖는다.
        id int primary key auto_increment not null,
        
        # 컬럼명 name은 32자 내외의 가변 길이의 문자열을 받는 제약 조건
        name varchar(32),
        
        # 칼럼명 age은 정수를 받는 제약 조건
        age int,
        
        # 칼럼명 address은 32자 내외의 가변 길이의 문자열을 받는 제약 조건
        address varchar(32)
        
        # DB 테이블을 생성할 때 사용되는 기본 설정
        ) ENGINE = InnoDB DEFAULT CHARSET=utf8
        '''

    # 테이블 생성 -- ②
    # 연결한 DB와 상호 작용하려면 cursor 객체가 필요합니다.
    # cursor 객체는 우리가 임의로 생성할 수 없으며 반드시 DB 호스트에 연결된
    # 객체(db)의 cursor() 함수로 cursor 객체를 받아와야 합니다.
    with db.cursor() as cursor:

        # cursor 객체의 execute() 함수로 SQL 구문을 실행합니다.
        # with 구문 내에서 cursor 객체를 사용하기 때문에
        # 사용 후에는 자동으로 메모리에서 해제됩니다.
        cursor.execute(sql)

except Exception as e:
    # DB 연결 실패 시 오류 내용 출력
    print(e)

finally:
    # DB 가 연결된 경우에만 접속 닫기 시도
    if db is not None:

        # 데이터베이스 서버 닫기
        db.close()
        print('table 생성 완료')
        print("DB 연결 닫기 성공")