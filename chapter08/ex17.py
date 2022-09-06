
try:
    with open('hello.txt','r',encoding='utf8') as f:
        data = f.read()
        print(data)
except Exception as e:
    print('error : ',e)

print('==================')

from file_util import read_file_lines
data=read_file_lines('hello.txt')
print(data)