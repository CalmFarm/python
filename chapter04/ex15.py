from gettext import find


def func(shape,width=1,height=1,radius=1):
    if shape == 0 :
        return width * height
    
    if shape == 1:
        return 3.14 * radius ** 2

print('rect area=',func(0,width=10,height=2))
print('circle area=',func(1,radius=5))

print('------------------------------------------')

numbers_list=[95,62,83,94,45,18,48,28,58,23,55,78]

odd_list=[]
for i in numbers_list:
    if i % 2 == 1:
        odd_list.append(i)

print(odd_list)

print('-----------------------------------------')

def check(checklist):
    find_list=[]
    for i in checklist:
        if i % 2 == 1:
            find_list.append(i)
            
    return find_list

list_00 = [1,23,1234156,13463,7347,458]

a=check(list_00)
print(a)