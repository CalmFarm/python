def get_sum(a, b):
    result = a+b
    return result
    # return result

n1 = get_sum(10,20)
print(f'10과 20의 합={n1}')

n2 = get_sum(100,200)
print(f'100과 200의 합={n2}') # return이 없으면 None 출력됨

def get_minus(a, b):
    return a-b

print(get_minus(100,50))