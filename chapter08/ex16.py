from file_util import read_file_lines

fname = input('입력할 파일의 이름: ')
f=open(fname,'r')
n=1
l=f.readline()
while l:
    print(f'{n:3d}: {l}',end='')
    n += 1
    l=f.readline()
f.close()
print()
print('=======================')

data = read_file_lines('we_will_rock.txt')

for n, l in enumerate(data, 1):
    print(f'{n:3d}: {l}')