from turtle import begin_fill


def calcstep(**args):
    begin = args.get('begin',0)
    end = args.get('end',0)
    step = args.get('step',1)

    total=0
    for num in range(begin,end +1, step):
        total += num

    return total

print("3~5=",calcstep(begin=3,end=5,step=1))
print("3~5=",calcstep(step=1,end=5,begin=3))

print("3~5=",calcstep(step=1,end=5))

even =  {
    'begin' :0,
    'end' : 100,
    'step' : 2
}

print(calcstep(**even))

odd = {
    **even,
    'begin': 1
}

print(odd)

def calcscore(name,*score,**option):
    print(name)
    total = 0
    for s in score:
        total += s
    
    print("총점 :",total)
    if(option['avg']==True):
        print("평균 :",total/len(score))

calcscore("홍길동",88,99,77,avg=True)
calcscore("고길동",99,88,95,85,avg=False)