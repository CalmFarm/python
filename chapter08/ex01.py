try:
    a, b = input('두 수를 입력하시오:').split()
    result = int(a)/int(b)
    print(f'{a}/{b}={result}')
except Exception as e:
    print('error:',e)
