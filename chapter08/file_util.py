def read_file_lines(fname):
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            data = f.readlines()
            data = [line.strip() for line in data]
            return data
    except Exception as e:
        print('error',e)
    

if __name__ == '__main__':
    data = read_file_lines('foo.txt')
    print(data)
