list1 = [10,20,30,40,50]

for ix,n in enumerate(list1):
    list1[ix] = n*10          

print(list1)

list1=[n*10 for n in list1]
print(list1)