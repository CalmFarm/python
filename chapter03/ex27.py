n=7
for i in range(n):
    st = ''
    for j in range(i): #내부 for 루프는 i 번 수행
        st = st + ' '  #공백을 i개 추
    print(st+'#')      #공백 추가 후 # 출력
print('---------------------')
n=7
st = ''
for i in range(n):
    for j in range(i):
        st = st + ' '
    print(st+'#')
print('---------------------')
n = 5
for i in range(n):
    for j in range(n - (i + 1)): # 공백을 출력함
        print(' ', end = '')
    for j in range(2 * i + 1): # '+'를 출력함
        print('+', end = '')
    print()
