from copyreg import pickle
from dataclasses import dataclass
import os
from os import path
from unicodedata import category

base = 'images'
def get_category_images1(base):
    images = {}

    for dir in os.listdir(base):
        # dir의 경로가 필요
        dir_path = path.join(base, dir)
        # print(dir,dir_path)

        # dir이 키가 됨
        images[dir] = os.listdir(dir_path)

    return images


import pickle

def save(fpath, data):
    try:
        with open(fpath, 'wb') as file :
            pickle.dump(data, file)
    except Exception as e:
        print(f'{fpath} 파일 쓰기에  실패했습니다.')
        print(e)

def load(fpath):
    try:
        with open(fpath,'rb') as file:
            data= pickle.load(file)
            return data
    except:
        print(f'{fpath} 파일 읽기에 실패했습니다.')


category_images = get_category_images1(base)
save('category.dat', category_images)

data = load('category.dat')
print(data)

# for dir, fnames in category_images.items():
#     for fname in fnames:
#         print(dir, fname)
#         file_path = path.join(base,dir,fname)
#         print(file_path)

for dir, fnames in category_images.items():
    for ix, fname in enumerate(fnames, 1):
        src_path=path.join(base,dir ,fname)
        dst_path=path.join(base,dir,f'{ix:04}.jpg')
        print(f'{src_path} => {dst_path}')
        os.rename(src_path, dst_path)

# 파일의 확장자 분리
# path.splittext ('images/dog/aaa.jpg')
#  -> ('images/dog/aaaa','.png')
