import time

start_time = time.time() 
print(1+2+3+4+5+6+7+8+9+10)

end_time = time.time() 

gap = end_time - start_time
print('1에서 10까지의 합을 구하고 출력하는 시간 :{:7.4f}초'.format(gap))
