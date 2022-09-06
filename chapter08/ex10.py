try:
    f = open('hello.txt','rt',encoding='utf-8')
    s = f.read(5)
    print(s)    

    s = f.read(5)
    print(s)
    
    f.close
except Exception as e:
    print(e)