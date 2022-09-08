import os

file_path = 'ex01.py'

print(os.path.isabs(file_path))

# 상대경로를 절대경로로 변경
file_path = os.path.abspath(file_path)
print(file_path)
print("존재여부 :" ,os.path.exists(file_path))
print("파일여부 :", os.path.isfile(file_path))
print('디렉토리여부 : ',os.path.isdir(file_path))
print('파일 크키:',os.path.getsize(file_path))
