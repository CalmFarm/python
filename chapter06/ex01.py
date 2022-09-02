# 로그인 시스템

# id/pwd

# 1)리스트
#[[id1, pwd1],[id2, pwd2], ...]
# 2)튜플 
# ((id1, pwd1),(id1, pwd2), ...)
# 3)사전
# {id1: pwd1, id2:pwd2, ...}

users = { # 회원 DB
    'hoeg': '1234',
    'kim' : '2345',
    'lee' : 'abcd',
    'park': 'LMNO'
}

for n in range(3):
    id = input('ID :')
    user_pwd = input('PASSWORD :')

    password = users.get(id) # user['hong']

    if not password:
        print('id가 존재하지 않습니다.')
    else:
        if user_pwd == password:
            print('로그인 성공')
            break
        else:
            print('로그인 실패')