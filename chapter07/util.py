INCH = 2.54

def calcsum(n):
    sum = 0
    for num in range(n+1):
        sum += num
    return sum

print('module name',__name__)

if __name__ == '__main__': # 자체 실행된 경우인가?
    print(calcsum(10))
    print(calcsum(20))
