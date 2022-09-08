from file_util import read_file_lines
import os
import sys

fname = input('입력할 파일의 이름: ')
if not os.path.exists(fname):
    print(fname,'이 존재하지 않습니다.')
    sys.exit(0)

f=open(fname,'r')

