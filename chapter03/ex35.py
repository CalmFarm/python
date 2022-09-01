from cgi import print_arguments
import numbers


print(type(numbers))

numbers = [11,22,33,44,55,66]
for n in numbers:
    print(n,end=' ')

print()

summer_fruits = ['수박','참외','체리','포도']

for fruits in summer_fruits:
    print(fruits,end=' ' )

print('-------------------------------')
#index 정보 얻기
for idx,fruits in enumerate(summer_fruits, 100):
    print(idx,fruits)