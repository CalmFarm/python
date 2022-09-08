import shutil
import os

shutil.copy("live.txt", "live2.txt")

answer = input("live2.txt를 삭제할까요 ? [y],n").lower()

print(answer)

if answer == 'y' or answer == '':
    os.remove('live2.txt')