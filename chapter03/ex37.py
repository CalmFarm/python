
numbers = [10,20,30,40,50]

s=0
for n in numbers:
    s = s+n
print('리스트 항목 값의 합:',s)

# 리스트의 길이 구하기
size = len(numbers)
print('리스트 항목 값의 평균 :',s/size)

name = 'Garret'
print(len(name))

for ch in 'Hello':
    print(ch,end=' ')