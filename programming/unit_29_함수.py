# problem
x = 10
y = 3
def get_quotient_remainder(a, b):
    c,d = a // b, a % b
    return '몫: {0}, 나머지: {1}'.format(c, d)

# problem2
def get(f):
    b,c = f
    a, s, m, d = b + c, b - c, b * c, b / c   # + - * -> type int   / -> type float   // -> type int
    return '덧셈 : {0}, 뺄셈: {1}, 곱셈 : {2}, 나눗셈{3}'.format(a, s, m, d)



if __name__ == '__main__':
    print(get_quotient_remainder(x,y))
    print(get(map(int, input().split())))   # 10 20