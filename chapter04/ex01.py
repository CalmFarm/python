from time import process_time_ns


def print_star(): # return 값이 없는 함수
    print('***************')

for i in range(4):
    print_star()

def print_star(n):
    for _ in range(n): # _ : 관례상, 문법상 필요시  
        print('*****************')

print_star(int(input('반복 횟수 설정 : ')))