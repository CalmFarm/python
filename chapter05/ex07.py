numbers = [13,24,26,47,56,85,63,62,82,73,84]

# numbers의 데이터에서 홀수를 찾아 새로운 리스트를 만들어라

odd_list = [n for n in numbers if n % 2 != 1] #filter
print(odd_list)

numbers = [25,-67,30,46,-84,13,55]
numbers = [n for n in numbers if n >= 0]
print(numbers)
