numbers = [26,13,45,62,66,88,90,54,99]

end=len(numbers)

for i in range(end):
    print(numbers[:i],numbers[i:])

    min_v = min(numbers[i:])
    min_idx=numbers[i:].index(min_v)+i

    numbers[i],numbers[min_idx]=numbers[min_idx],numbers[i]

print(numbers)

# 합계와 평균을 구하는 함수 1개

def calc(list_name):
    size = len(list_name)
    total= sum(list_name)
    avg  = total / size 

    # return print(f'합계: {total}, 평균: {avg:.3f}')
    return total, avg

# calc(numbers)
total, avg= calc(numbers) # unpacking
print(f'sum : {total}, avg : {avg:.2f}')

list1=[1,2,3]
list2=list1 # = : 참조의 복사

list2=list1.copy() # 복사본 필요시 .copy()메서드