from unittest import result


def sum_nums(*numbers):
    result=0
    for n in numbers:
        result += n
    return result

print(sum_nums(10,20,30))
print(sum_nums(10,20,30,40,50,))

n_list=[1,10,40,35,88]
print(sum_nums(*n_list))

n_list2 = [*n_list,45,85]
print(n_list2)