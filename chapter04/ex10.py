from glob import glob


def print_sum():
    global a,b
    a = 100
    b = 200
    result = a + b
    print(f'print_sum() 내부: {a}과 {b}의 합은 {result} 입니다.')

a=10
b=20
print_sum()

print(a,b)