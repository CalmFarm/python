n = int(input('합계를 구할 수를 입력 하세요 : '))
total = 0

for i in range(n+1) :
    total += i

print(f'1부터 {n}까지의 합은 {total}')