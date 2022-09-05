def greet(*names):
    for name in names:
        print(f'안녕하세요 {name} 씨')
        print(type(names))

greet('홍길동','양만춘','이순신')
greet('James','Thomas')
greet()