def get_ans(ans):
    if ans in ['yes','no']:
        print('정상적인 입력입니다.')
    else:
        raise ValueError('입력을 확인하세요')

while True:
    try:
        ans=input('yes/no 중 하나를 선택하시오')
        get_ans(ans)
        break
    except Exception as e:
        print('error:',e)
