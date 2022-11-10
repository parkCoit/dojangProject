# problem
x = 10
y = 3
def get_quotient_remainder(a, b):
    c,d = a // b, a % b
    return '몫: {0}, 나머지: {1}'.format(c, d)



if __name__ == '__main__':
    print(get_quotient_remainder(x,y))