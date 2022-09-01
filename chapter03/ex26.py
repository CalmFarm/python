for i in range(2,10) : # 외부 for 루프
    for j in range(1,10) : # 내부 for 루프
        print(f'{i}*{j}={i*j:2d}',end=' ')
    print()