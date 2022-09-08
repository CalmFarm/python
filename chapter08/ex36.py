import os

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = os.path.join(path, f)
        if os.path.isdir(fullpath):
            print('[%s]'%fullpath)
            dumpdir(fullpath)
        else:
            print('\t'+f)

dumpdir('.')

