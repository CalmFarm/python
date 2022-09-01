
def print_star(n, ch):
    for _ in range(n):
        print(ch*20) # 문자열 k*n => 문자열*문자열...n번 반복

print_star(4, '#')
print_star(2, '$')

# print_star(3) / missing
# print_star(2,'0',9) / takes 2 p.a but 3 were given
# positional arguments / TypeError