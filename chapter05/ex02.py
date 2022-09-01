numbers = [95,62,83,94,45,18,48,28,58,23,55,78]

def find_min(checklist):

    min_index = 0
    min_value = checklist[0]
    
    for ix,n in enumerate(checklist):
        if n < min_value:
            min_value = n
            min_index = ix
    
    return print(min_index,min_value)

print(numbers)
find_min(numbers)